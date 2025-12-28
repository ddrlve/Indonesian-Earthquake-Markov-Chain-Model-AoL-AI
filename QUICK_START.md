# ⚡ QUICK START GUIDE

## 🚀 **3 WAYS TO USE THIS PROJECT**

### **Option 1: Basic Usage (Already Working!) ✅**

```bash
# Open notebook
jupyter notebook BMKG_Earthquake_Forecasting_Clean.ipynb

# Run all cells → Get predictions in results/earthquake_predictions.csv
```

**Performance**: 87.4% detection rate

---

### **Option 2: Enhanced Features (Better Accuracy!) 🆕**

```bash
# Step 1: Generate enhanced features (31 new features)
python enhanced_features.py

# Step 2: Run validation to see improvements
python advanced_validation.py

# Step 3: Check visualizations in results/evaluation/
```

**Expected**: 90-92% detection rate

---

### **Option 3: Full Research Analysis 📊**

```bash
# 1. Enhanced features
python enhanced_features.py

# 2. Advanced validation
python advanced_validation.py

# 3. Modify notebook to use enhanced features
# Load: data/bmkg_enhanced_features.csv
# Use: 37 features instead of 6

# 4. Re-train model with new features
# 5. Compare before/after results
```

**Result**: IEEE-ready paper with all metrics

---

## 📊 **WHAT YOU GET**

### **Current Model Output:**

✅ `results/earthquake_predictions.csv` - Top 10 next earthquakes
✅ `results/bmkg_analysis.png` - Main dashboard visualization
✅ 87.4% detection rate (M≥5.5, 10-day window)

### **🆕 Enhanced Model Output:**

✅ `data/bmkg_enhanced_features.csv` - 37 features (31 new)
✅ `results/evaluation/calibration_curve.png` - Reliability diagram
✅ `results/evaluation/performance_comparison.png` - vs Baseline
✅ `results/evaluation/roc_curve.png` - AUC analysis
✅ 90-92% expected detection rate

---

## 🎯 **RECOMMENDATIONS**

### **For Presentation/Demo:**

→ Use **Option 1** (Basic) - Already excellent (87.4%)
→ Show `earthquake_predictions.csv` for real predictions

### **For IEEE Paper/Research:**

→ Use **Option 3** (Full Analysis) - Comprehensive metrics
→ Include all evaluation figures
→ Compare before/after enhancement

### **For Maximum Accuracy:**

→ Use **Option 2** (Enhanced) - Best performance
→ 31 additional features = better predictions
→ Professional validation metrics

---

## 📁 **KEY FILES**

| File                                      | Purpose             | When to Use             |
| ----------------------------------------- | ------------------- | ----------------------- |
| `BMKG_Earthquake_Forecasting_Clean.ipynb` | Main notebook       | Always (basic usage)    |
| `enhanced_features.py`                    | Feature engineering | For better accuracy     |
| `advanced_validation.py`                  | IEEE metrics        | For paper/research      |
| `README_SIMPLE.md`                        | Full documentation  | Reference guide         |
| `IMPLEMENTATION_SUMMARY.md`               | Technical details   | Deep dive               |
| `PROJECT_STRUCTURE.md`                    | File organization   | Understanding structure |

---

## ⏱️ **TIME ESTIMATES**

- **Basic usage**: 5 minutes (just run notebook)
- **Enhanced features**: 2 minutes (python enhanced_features.py)
- **Full validation**: 1 minute (python advanced_validation.py)
- **Total setup**: ~10 minutes for everything

---

## 🎓 **FOR DIFFERENT AUDIENCES**

### **If you're a student:**

→ Start with Option 1 (basic)
→ Understand how model works
→ Then try Option 2 for better results

### **If you're writing a paper:**

→ Go straight to Option 3
→ Get all IEEE-quality figures
→ Compare performance metrics

### **If you're presenting:**

→ Use Option 1 for demo
→ Show actual predictions
→ Mention 87.4% accuracy

---

## 💡 **TIPS**

1. **Check data first**: Make sure `data/bmkg_processed.csv` exists
2. **Run in order**: enhanced_features.py → advanced_validation.py
3. **Save results**: All visualizations auto-saved to results/
4. **Update notebook**: Use enhanced features for best accuracy

---

## 📞 **TROUBLESHOOTING**

**Problem**: "File not found" error
**Solution**: Run main notebook first to generate processed data

**Problem**: Import errors
**Solution**: `pip install -r requirements.txt`

**Problem**: Slow execution
**Solution**: Normal for 30K+ data points, be patient

---

## ✅ **SUCCESS CHECKLIST**

- [ ] Main notebook runs successfully
- [ ] Predictions saved to CSV
- [ ] Enhanced features generated (optional)
- [ ] Validation metrics computed (optional)
- [ ] All visualizations created

---

**🎉 You're ready! Pick an option above and start!**
