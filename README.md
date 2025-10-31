# 🍽️ Impact of Climate and Weather Conditions on Regional Gastronomic Diversity in Turkey

This project explores the relationship between Turkey’s diverse climatic conditions and its regional food culture using data-driven methods.

## 1. Project Overview  
This study investigates whether and how regional climate conditions influence the caloric intensity and category distribution (meat-based vs vegetable-based, etc.) of traditional cuisine across Turkish provinces.  
The underlying hypothesis is that climate acts as an environmental driver, shaping culinary patterns, which in turn reflect in the caloric profile of regional diets.

---
## 3. Motivation  

As a student who is coming from a gastronomically rich city -Afyonkarahisar-, I’ve always been fascinated by how geography and environment shape what people eat. For example, in Afyon the main dietary plans are based on calorie-densed dishes like Bükme, Katmer or Lokul classified as pastry and bakery. Compared to Afyon, my second home city -İzmir- prefers lighter and low-calorie meals like vegetable dishes more often. Then, I realized throughout the travels between Afyon and İzmir that there might correlations between caloric intensity of the foods and geographical features of the regions in our country.

This observation led me to wonder whether these gastronomic differences are random cultural choices or if they have deeper environmental roots — specifically, whether climate conditions such as temperature and humidity have influenced the evolution of regional cuisines in Turkey.  

By analyzing this relationship, I aim to explore how environmental factors can shape long-term dietary patterns, while also strengthening my skills in data preprocessing, visualization, and regression modeling using real-world open datasets. 

Note: I want to use these analysis while I'm going to open my dream restaurant in the future as a student who is crazy about food.

---
## 3. Research Questions  
- **RQ1:** Do provinces with colder and/or more humid climates tend to have more calorie-dense -meat-based, pastry-heavy- traditional cuisines compared to warmer regions?  
- **RQ2:** How strongly are climatic indicators like average temperature, annual precipitation correlated with the “Caloric Gastronomic Index” of a region?  

---

## 4. Hypotheses  

**Null Hypothesis 1 (H₀₁):** Regional climate conditions do not have a significant impact on the caloric intensity of traditional cuisines.  
**Alternative Hypothesis 1 (H₁₁):** Colder or more humid regions have significantly higher caloric intensity in their traditional cuisines compared to warmer regions.  

**Null Hypothesis 2 (H₀₂):** The type distribution of regional cuisines such as meat-based, vegetable-based, pastry, dessert, etc. is independent of regional climate conditions.  
**Alternative Hypothesis 2 (H₁₂):** Climate conditions significantly influence the type distribution of traditional foods. 

---

## 5. Datasets & Sources  

In order to maintain this analysis, we will use these datasets and sources:

 **Traditional Food Data**: List of regional traditional foods by province, categorized by type  [Turkish Patent and Trademark Office – Geographical Indications Database](https://ci.turkpatent.gov.tr/) 
 
 **Climate Data**: Provincial average annual climate indicators taken from Turkish State Meteorological Service (MGM) / [Open-Meteo API](https://open-meteo.com/) 
 
 **Food Composition Data**: Average energy values (kcal/100 g) by food category to compute the Caloric Gastronomic Index [TURKOMP](https://www.turkomp.gov.tr/), [USDA FoodData Central](https://fdc.nal.usda.gov/), [MyFitnessPal](https://www.myfitnesspal.com/), [FatSecret](https://www.fatsecret.com/)
 
---

## 6. Planned Analysis  

Once I collect and clean the data, I’ll explore how regional climate indicators — such as average temperature and precipitation — are related to the caloric intensity and food-type composition of traditional cuisines across Turkey.  

Here’s how I plan to approach the analysis:  
 

- **1. Categorization & Index Calculation:**  
  Traditional foods will be categorized into main groups (meat-based, vegetable-based, pastry, dessert, soup), and each province’s *Caloric Gastronomic Index (CGI)* will be computed to represent its average caloric intensity.  

- **2. Climate Integration & Statistical Testing:**  
  Climate indicators (temperature, precipitation) will be merged with provincial CGI data. Statistical tests (Pearson/Spearman correlations) will determine whether colder or more humid regions have significantly higher caloric cuisines.

- **3. Exploratory Data Analysis (EDA):**  
  I will begin by examining the distributions of climate variables and caloric data, looking for general patterns. Correlation matrices, scatter plots, and choropleth maps will help visualize potential climate–cuisine relationships across provinces.

- **4. Cluster Analysis (Regional Profiling):**  
  Using K-Means or Hierarchical Clustering, I’ll group provinces based on their climate–gastronomy profiles to see whether distinct culinary clusters emerge (e.g., “Cold–High Calorie,” “Warm–Light Cuisine”).  

- **5. Regression Modeling (ML-based analysis):**  
  A multiple linear regression model will be developed to quantify how much of the variation in CGI can be explained by climate factors. Additional models (like Random Forest Regressor or Ridge Regression) may be tested to check robustness and capture non-linear effects.  

- **6. Interpretation & Visualization:**  
  Finally, results will be visualized through interactive maps, correlation heatmaps, and regression plots to communicate insights clearly.  

This approach will not only test the main hypothesis but also help reveal broader patterns about how environmental conditions might shape gastronomic diversity across cities. Depending on data quality, future work could extend the model to include nutritional balance or sustainability dimensions.
