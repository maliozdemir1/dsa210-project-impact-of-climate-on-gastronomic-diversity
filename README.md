# 🍽️ Impact of Climate and Weather Conditions on Regional Gastronomic Diversity in Turkey

This project explores the relationship between Turkey’s diverse climatic conditions and its regional food culture using data-driven methods.

## 1. Project Overview  
This study investigates whether and how regional climate conditions influence the caloric intensity and category distribution (meat-based vs vegetable-based, etc.) of traditional cuisine across Turkish provinces.  
The underlying hypothesis is that climate acts as an environmental driver, shaping culinary patterns, which in turn reflect in the caloric profile of regional diets.

---

## 2. Research Questions  
- **RQ1:** Do provinces with colder and/or more humid climates tend to have more calorie-dense (meat-based, pastry-heavy) traditional cuisines compared to warmer regions?  
- **RQ2:** How strongly are climatic indicators (average temperature, annual precipitation) correlated with the “Caloric Gastronomic Index” of a region?  

---

## 3. Hypotheses  

**Null Hypothesis 1 (H₀₁):** Regional climate conditions (average temperature, precipitation) do not have a significant impact on the caloric intensity of traditional cuisines.  
**Alternative Hypothesis 1 (H₁₁):** Colder or more humid regions have significantly higher caloric intensity in their traditional cuisines compared to warmer regions.  

**Null Hypothesis 2 (H₀₂):** The type distribution of regional cuisines (meat-based, vegetable-based, pastry, dessert, etc.) is independent of regional climate conditions.  
**Alternative Hypothesis 2 (H₁₂):** Climate conditions significantly influence the type distribution of traditional foods (e.g., colder regions exhibit more meat-based and pastry-heavy cuisines). 

---

## 4. Datasets & Sources  

In order to maintain this analysis, we will use these datasets and sources:
| **Traditional Food Data** | List of regional traditional foods by province, categorized by type (meat, pastry, vegetable, dessert, soup, drink) | [Turkish Patent and Trademark Office – Geographical Indications Database](https://ci.turkpatent.gov.tr/) |
| **Climate Data** | Provincial average annual climate indicators (average temperature °C, annual precipitation mm) | Turkish State Meteorological Service (MGM) / [Open-Meteo API](https://open-meteo.com/) |
| **Food Composition Data** | Average energy values (kcal/100 g) by food category to compute the Caloric Gastronomic Index | [TURKOMP](https://www.turkomp.gov.tr/) & [USDA FoodData Central](https://fdc.nal.usda.gov/) |
| **Control Variables** | Provincial data such as urbanization rate, tourism density, population density | [Turkish Statistical Institute (TÜİK)](https://data.tuik.gov.tr/) |
