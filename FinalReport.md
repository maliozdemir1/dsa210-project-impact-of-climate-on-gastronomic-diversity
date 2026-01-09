# Impact of Climate and Weather Conditions on Regional Gastronomic Diversity in Turkey
## Final Report - Mehmet Ali Özdemir 34357

---

## Abstract

This project investigates whether provincial climate conditions in Türkiye—captured by annual mean temperature and annual total precipitation—are associated with the caloric density of Turkish Geographical Indication (GI) foods. Using a food-level dataset (≈1500 items) mapped to provinces and climate normals (1991–2020), we conduct exploratory analysis, hypothesis tests, and predictive modeling. Province-level analyses show no meaningful relationship between climate and average provincial calorie values (Pearson r ≈ −0.04, p ≈ 0.72; t-test cold vs hot p ≈ 0.73). However, food-level modeling reveals that product category is the dominant driver of caloric density (R² ≈ 0.60), while climate variables alone fail to predict calories (R² ≈ 0 or negative). A chi-square test indicates that climate bins and product group distributions are statistically dependent (p ≪ 0.001), but effect size is weak (Cramér’s V ≈ 0.146), suggesting climate may influence what types of foods appear, not their calories per 100g. Overall, caloric density appears primarily shaped by food composition and category rather than provincial climate.

---

## 1. Introduction

Turkish GI foods reflect local culture, ingredients, and production traditions. A natural hypothesis is that climate could shape local food characteristics by influencing agriculture, ingredient availability, and preservation practices. This study evaluates whether climate variables (temperature and precipitation) explain variation in caloric density.

**Research question:**  
Do provincial climate conditions relate to the caloric density of GI foods?

**Main hypothesis (H1):**  
Climate (temperature/precipitation) is associated with higher or lower kcal values.

**Null hypothesis (H0):**  
There is no meaningful relationship between climate and caloric density.

---

## 2. Data and Methodology

### 2.1 Data Sources

- **GI foods dataset:** Food name, province, product group/category, and kcal per 100g values (from a cleaned & standardized manual dataset).
- **Climate dataset (MGM, 1991–2020 normals):** Annual mean temperature (`temp_annual_mean`) and annual total precipitation (`prec_annual_total`) by province.

### 2.2 Data Cleaning and Integration

A key processing step was aligning province names across datasets. Provinces were normalized by:

- uppercasing,
- mapping Turkish characters to ASCII-like equivalents (Ş→S, Ç→C, etc.),
- removing punctuation and extra spaces,
- constructing a stable province key (`prov_key`) for robust merging.

Food records were merged with climate values using the normalized `prov_key`. This ensured consistent province-level linking and avoided mismatches due to spelling or encoding differences.

### 2.3 Analysis Strategy

We analyze the climate–calorie relationship at two levels:

**Province-level aggregation**  
For each province, mean and median kcal values and the number of foods (`n_foods`) were computed. Climate correlations with provincial mean calories were then tested.

**Food-level modeling**  
Each food’s `kcal_100g` value was predicted using:
- climate features (temperature and precipitation),
- product group (category), encoded using one-hot encoding.

This two-level approach is important because province-level averages can hide strong category effects present at the food level.

---

## 3. Exploratory Data Analysis (EDA)

### 3.1 Dataset Structure

- Food-level dataset size: ~1500 rows  
- Provinces covered after merge: ~79  
- Product groups (categories): ~14  

### 3.2 Key Observations

- Caloric density varies widely across food items, consistent with differences in composition (e.g., desserts vs soups vs meats).
- The distribution of foods across product groups is not uniform; some categories dominate the dataset.
- At the province level, mean kcal values exhibit large within-province variance due to the coexistence of many different food types.

EDA suggested that if climate has an effect on caloric density, it is likely subtle and potentially confounded by the distribution of food categories across provinces.

---

## 4. Hypothesis Testing

### 4.1 Correlation Tests (Province-level)

We tested whether temperature or precipitation is correlated with province mean calorie values.

**Temperature vs mean_kcal**
- Pearson r ≈ −0.041, p ≈ 0.717  
- Spearman ρ ≈ −0.063, p ≈ 0.578  

**Precipitation vs mean_kcal**
- Pearson r ≈ −0.016, p ≈ 0.887  
- Spearman ρ ≈ −0.028, p ≈ 0.808  

**Interpretation:**  
All p-values are far above 0.05, and therefore the null hypothesis cannot be rejected. There is no statistically significant linear or monotonic relationship between climate variables and province-level average caloric density.

---

### 4.2 Group Difference Test: Cold vs Hot Provinces

Provinces were binned into climate groups, and “cold” and “hot” provinces were compared in terms of mean calorie values.

- Welch t-test: t ≈ 0.347, p ≈ 0.729  
- Mann–Whitney U test: U ≈ 817, p ≈ 0.720  

**Interpretation:**  
No statistically significant difference was found between the calorie distributions of cold and hot climate groups. This further supports the conclusion that climate does not directly influence caloric density.

---

### 4.3 Chi-square Test: Climate Bin × Product Group

Climate bins were created using quantiles:

- `temp_bin`: Cold / Mild / Hot  
- `precip_bin`: Dry / Normal / Wet  
- `climate_bin` = `temp_bin` + "_" + `precip_bin`  

The dependence between `climate_bin` and product group was tested using a chi-square independence test.

- χ² ≈ 246.10  
- Degrees of freedom = 72  
- p ≈ 6.96e−21  
- Effect size (Cramér’s V) ≈ 0.146  

**Interpretation:**  
The extremely small p-value indicates a statistically detectable association between climate bins and product group distribution. However, the effect size is weak, as indicated by the low Cramér’s V value.

**Meaning:**  
Climate may slightly influence which types of food categories are more common in certain regions, but this influence is too weak to imply a direct effect on caloric density.

---

## 5. Machine Learning Results

### 5.1 Province-level Prediction (mean_kcal)

Models were trained to predict province-level mean caloric values using temperature, precipitation, and the number of foods.

- **Ridge Regression:** RMSE ≈ 45.16, R² ≈ −0.173  
- **Random Forest:** RMSE ≈ 47.98, R² ≈ −0.378  

**Interpretation:**  
Negative R² values indicate that both models perform worse than a simple mean baseline. Province-level mean caloric density cannot be reliably predicted from climate variables and food counts.

---

### 5.2 Food-level Prediction (kcal_100g)

Food-level models were trained using:
- `temp_annual_mean`,
- `prec_annual_total`,
- `product_group_en` (one-hot encoded).

Results from 5-fold cross-validation:

- **Food-level Ridge Regression:** RMSE ≈ 97.18, R² ≈ 0.603  
- **Food-level Random Forest:** RMSE ≈ 102.84, R² ≈ 0.555  

**Interpretation:**  
Food-level prediction performs well only when product group information is included. This confirms that caloric density is primarily explained by food category and composition rather than climate.

---

### 5.3 Feature Ablation Study (What Matters?)

A feature ablation study compared different input combinations:

- TEMP only / PRECIP only / TEMP + PRECIP: R² ≈ 0 or negative  
- GROUP only: R² ≈ 0.604  
- GROUP + TEMP / GROUP + PRECIP / GROUP + TEMP + PRECIP: R² remains ≈ 0.603–0.604  

**Interpretation:**
- Climate variables alone are essentially non-informative for predicting kcal per 100g.
- Product group alone explains approximately 60% of the variance.
- Adding climate variables to product group provides negligible improvement.

**Core takeaway:**  
Calories per 100g are primarily determined by food category and composition, not by provincial climate.

---

## 6. Discussion

Across hypothesis testing and machine learning analyses, results consistently indicate that climate variables do not directly explain caloric density. Correlation tests and group comparisons show no significant climate–calorie relationship at the province level, and province-level machine learning models fail to generalize. Food-level machine learning models succeed only because they capture category-level effects, while climate variables contribute little additional explanatory power.

Nevertheless, chi-square results suggest a weak but statistically detectable association between climate and product group distribution. This implies an indirect pathway: climate may influence local agriculture and food traditions, thereby shaping which categories of foods are produced in a region, but the caloric density of those foods is governed primarily by recipe composition and food type.

---

## 7. Conclusion

This project found no strong evidence that provincial climate conditions (temperature and precipitation) directly affect the caloric density of Turkish GI foods. Province-level analyses consistently show weak or nonexistent relationships. In contrast, food category emerges as the dominant predictor of caloric density, explaining roughly 60% of variability at the food level. Climate shows a statistically significant but weak association with product group distributions, suggesting that climate may shape what foods are made rather than how caloric they are.

---

## 8. Limitations

- GI food calorie values may vary with preparation methods; reported kcal values represent typical or approximate values.
- Climate data are aggregated at the province level and do not capture microclimates or seasonal variation.
- Product group categories are broad, leading to substantial within-category variance.
- Province-level averaging may obscure patterns due to heterogeneous food distributions within provinces.

---

## 9. Future Work

- Incorporate richer features such as ingredient types (animal-based vs plant-based), sugar and fat proxies, cooking methods, and preservation techniques.
- Apply count models or robust regression approaches to better handle heavy-tailed calorie distributions.
- Expand climate descriptors to include seasonality, temperature extremes, and growing degree days.
- Compare GI foods with non-GI foods to assess whether GI designation modifies climate sensitivity patterns.

