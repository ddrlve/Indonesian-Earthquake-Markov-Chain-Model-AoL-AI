"""
===================================================================
ENHANCED FEATURE ENGINEERING FOR EARTHQUAKE PREDICTION
Advanced Multi-Dimensional Features for 2nd-Order Markov Chain
===================================================================

This module adds 10+ advanced features to improve prediction accuracy:
- Temporal patterns (time-of-day, seasonal)
- Spatial correlation (distance, clustering)
- Energy dynamics (release patterns, accumulation)
- Statistical indicators (b-value, event rates)

Target: Increase detection rate from 87.4% to 90-92%
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

def calculate_haversine_distance(lat1, lon1, lat2, lon2):
    """Calculate distance between two points on Earth (km)"""
    R = 6371  # Earth radius in km
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    return R * c

def calculate_local_b_value(magnitudes, window=100, min_mag=None):
    """
    Calculate local Gutenberg-Richter b-value
    b-value indicates stress state: lower b = higher stress
    """
    if len(magnitudes) < 10:
        return 1.0  # Default b-value
    
    try:
        if min_mag is None:
            min_mag = magnitudes.quantile(0.1)
        
        mags_above = magnitudes[magnitudes >= min_mag]
        if len(mags_above) < 5:
            return 1.0
        
        # b-value from maximum likelihood estimation
        b = np.log10(np.e) / (mags_above.mean() - min_mag)
        
        # Constrain to reasonable range
        return b if 0.5 < b < 2.0 else 1.0
    except:
        return 1.0

def engineer_enhanced_features(df):
    """
    Add comprehensive features to earthquake dataframe
    
    Parameters:
    -----------
    df : pandas.DataFrame
        Must contain: time, latitude, longitude, depth, magnitude
    
    Returns:
    --------
    df_enhanced : pandas.DataFrame
        Original data + 15+ new features
    """
    print("="*80)
    print("🔬 ENHANCED FEATURE ENGINEERING")
    print("="*80)
    
    df = df.copy()
    df['time'] = pd.to_datetime(df['time'])
    df = df.sort_values('time').reset_index(drop=True)
    
    print(f"\n📊 Input: {len(df):,} earthquakes")
    print(f"   Period: {df['time'].min()} to {df['time'].max()}")
    print(f"   Magnitude range: M{df['magnitude'].min():.1f} - {df['magnitude'].max():.1f}")
    
    # ==========================================
    # 1. TEMPORAL FEATURES
    # ==========================================
    print("\n1️⃣ Temporal features...")
    
    df['year'] = df['time'].dt.year
    df['month'] = df['time'].dt.month
    df['day'] = df['time'].dt.day
    df['hour'] = df['time'].dt.hour
    df['day_of_week'] = df['time'].dt.dayofweek
    df['day_of_year'] = df['time'].dt.dayofyear
    
    # Time of day (4 categories)
    df['time_of_day'] = pd.cut(df['hour'], 
                               bins=[0, 6, 12, 18, 24],
                               labels=['Night', 'Morning', 'Afternoon', 'Evening'],
                               include_lowest=True)
    
    # Season (4 quarters)
    df['season'] = pd.cut(df['month'],
                         bins=[0, 3, 6, 9, 12],
                         labels=['Q1_Jan-Mar', 'Q2_Apr-Jun', 'Q3_Jul-Sep', 'Q4_Oct-Dec'],
                         include_lowest=True)
    
    # Inter-event time (hours and days)
    df['inter_event_hours'] = df['time'].diff().dt.total_seconds() / 3600
    df['inter_event_days'] = df['inter_event_hours'] / 24
    df['inter_event_hours'] = df['inter_event_hours'].fillna(0)
    df['inter_event_days'] = df['inter_event_days'].fillna(0)
    
    print(f"   ✓ Added 10 temporal features")
    
    # ==========================================
    # 2. SPATIAL FEATURES
    # ==========================================
    print("\n2️⃣ Spatial features...")
    
    # Inter-event distance
    distances = [0]  # First event
    for i in range(1, len(df)):
        try:
            dist = calculate_haversine_distance(
                df.iloc[i-1]['latitude'], df.iloc[i-1]['longitude'],
                df.iloc[i]['latitude'], df.iloc[i]['longitude']
            )
            distances.append(dist)
        except:
            distances.append(0)
    df['inter_event_distance_km'] = distances
    
    # Spatial velocity (km/day)
    df['spatial_velocity'] = df['inter_event_distance_km'] / (df['inter_event_days'] + 0.01)
    df['spatial_velocity'] = df['spatial_velocity'].clip(upper=1000)  # Cap outliers
    
    print(f"   ✓ Added 2 spatial features")
    print(f"   ✓ Mean inter-event distance: {df['inter_event_distance_km'].mean():.1f} km")
    
    # ==========================================
    # 3. ENERGY FEATURES
    # ==========================================
    print("\n3️⃣ Energy features...")
    
    # Seismic energy (Joules) - Gutenberg-Richter relation
    df['seismic_energy_joules'] = 10 ** (1.5 * df['magnitude'] + 4.8)
    df['energy_log10'] = np.log10(df['seismic_energy_joules'])
    
    # Energy release rate (rolling windows)
    df['energy_rate_7d'] = df['seismic_energy_joules'].rolling(window=7, min_periods=1).sum() / 7
    df['energy_rate_30d'] = df['seismic_energy_joules'].rolling(window=30, min_periods=1).sum() / 30
    
    # Cumulative energy (stress accumulation indicator)
    df['cumulative_energy'] = df['seismic_energy_joules'].cumsum()
    df['cumulative_energy_normalized'] = df['cumulative_energy'] / df['cumulative_energy'].max()
    
    total_energy = df['seismic_energy_joules'].sum()
    energy_megatons = total_energy / (4.184e15)  # Convert to megatons TNT
    print(f"   ✓ Added 6 energy features")
    print(f"   ✓ Total seismic energy: {energy_megatons:.1f} Megaton TNT")
    
    # ==========================================
    # 4. STATISTICAL INDICATORS
    # ==========================================
    print("\n4️⃣ Statistical indicators...")
    
    # Event rate (earthquakes per day in rolling windows)
    # Use rolling count with fixed window size (number of events, not time-based)
    df['event_count_7d'] = df['magnitude'].rolling(window=7, min_periods=1).count()
    df['event_count_30d'] = df['magnitude'].rolling(window=30, min_periods=1).count()
    df['event_rate_7d'] = df['event_count_7d'] / 7
    df['event_rate_30d'] = df['event_count_30d'] / 30
    
    # Local b-value (rolling window)
    window_size = 100
    b_values = []
    for i in range(len(df)):
        if i < window_size:
            b_values.append(1.0)  # Default
        else:
            mags = df['magnitude'].iloc[i-window_size:i]
            b = calculate_local_b_value(mags, window=window_size)
            b_values.append(b)
    
    df['b_value_local'] = b_values
    
    # Global b-value
    global_b = calculate_local_b_value(df['magnitude'])
    print(f"   ✓ Added 5 statistical features")
    print(f"   ✓ Global b-value: {global_b:.3f}")
    
    # ==========================================
    # 5. MAGNITUDE & DEPTH CATEGORIES
    # ==========================================
    print("\n5️⃣ Enhanced state categories...")
    
    # Fine-grained magnitude states (5 categories)
    df['magnitude_state_fine'] = pd.cut(
        df['magnitude'],
        bins=[4.0, 4.5, 5.0, 5.5, 6.0, 10.0],
        labels=['M4.0-4.5', 'M4.5-5.0', 'M5.0-5.5', 'M5.5-6.0', 'M6.0+']
    )
    
    # Depth categories
    df['depth_category'] = pd.cut(
        df['depth'],
        bins=[0, 70, 300, 1000],
        labels=['Shallow', 'Intermediate', 'Deep']
    )
    
    # Magnitude intensity indicator
    df['is_major'] = (df['magnitude'] >= 6.0).astype(int)
    df['is_significant'] = (df['magnitude'] >= 5.5).astype(int)
    df['is_moderate'] = (df['magnitude'] >= 5.0).astype(int)
    
    print(f"   ✓ Added 5 category features")
    
    # ==========================================
    # 6. CLUSTERING INDICATORS
    # ==========================================
    print("\n6️⃣ Clustering indicators...")
    
    # Recent activity level (events in past 24 hours)
    # Simplified: use inter-event time to estimate activity
    df['events_last_24h'] = (24 / (df['inter_event_hours'] + 0.1)).clip(upper=100)
    
    # Is part of cluster? (>3 events in 24h)
    df['is_cluster'] = (df['events_last_24h'] >= 3).astype(int)
    
    # Time since last major event (M≥6.0)
    major_events = df[df['magnitude'] >= 6.0]['time']
    df['days_since_major'] = np.nan
    for i, t in enumerate(df['time']):
        previous_majors = major_events[major_events < t]
        if len(previous_majors) > 0:
            df.loc[i, 'days_since_major'] = (t - previous_majors.iloc[-1]).total_seconds() / 86400
        else:
            df.loc[i, 'days_since_major'] = 9999  # No previous major
    
    print(f"   ✓ Added 3 clustering features")
    
    # ==========================================
    # SUMMARY
    # ==========================================
    new_features = len(df.columns) - 6  # Subtract original columns
    
    print("\n" + "="*80)
    print("✅ FEATURE ENGINEERING COMPLETE!")
    print("="*80)
    print(f"\n📊 Summary:")
    print(f"   Original features: 6")
    print(f"   New features added: {new_features}")
    print(f"   Total features: {len(df.columns)}")
    print(f"\n📋 Feature categories:")
    print(f"   • Temporal: 10 features")
    print(f"   • Spatial: 2 features")
    print(f"   • Energy: 6 features")
    print(f"   • Statistical: 5 features")
    print(f"   • Categories: 5 features")
    print(f"   • Clustering: 3 features")
    print(f"   TOTAL: {new_features} enhanced features")
    
    # Save feature importance info
    feature_info = {
        'temporal': ['year', 'month', 'day', 'hour', 'day_of_week', 'day_of_year',
                    'time_of_day', 'season', 'inter_event_hours', 'inter_event_days'],
        'spatial': ['inter_event_distance_km', 'spatial_velocity'],
        'energy': ['seismic_energy_joules', 'energy_log10', 'energy_rate_7d', 
                  'energy_rate_30d', 'cumulative_energy', 'cumulative_energy_normalized'],
        'statistical': ['event_count_7d', 'event_count_30d', 'event_rate_7d', 
                       'event_rate_30d', 'b_value_local'],
        'categories': ['magnitude_state_fine', 'depth_category', 'is_major', 
                      'is_significant', 'is_moderate'],
        'clustering': ['events_last_24h', 'is_cluster', 'days_since_major']
    }
    
    return df, feature_info

if __name__ == "__main__":
    print("\n" + "="*80)
    print("🚀 ENHANCED FEATURE ENGINEERING - DEMO")
    print("="*80)
    
    # Test with existing data
    try:
        df = pd.read_csv('data/bmkg_processed.csv')
        print(f"\n✅ Loaded {len(df):,} earthquakes")
        
        # Apply enhanced features
        df_enhanced, features = engineer_enhanced_features(df)
        
        # Save enhanced dataset
        output_file = 'data/bmkg_enhanced_features.csv'
        df_enhanced.to_csv(output_file, index=False)
        print(f"\n💾 Enhanced dataset saved: {output_file}")
        
        # Preview
        print(f"\n🔍 Preview of new features:")
        new_cols = [col for col in df_enhanced.columns if col not in df.columns]
        print(df_enhanced[new_cols].head(10))
        
    except FileNotFoundError:
        print("\n❌ Data file not found: data/bmkg_processed.csv")
        print("   Run the main notebook first to generate processed data")
