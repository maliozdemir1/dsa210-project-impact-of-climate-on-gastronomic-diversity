import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

def tum_kategorilerle_analiz():
    print("🚀 Analiz Başlatılıyor... Filtreler Kaldırıldı, TÜM VERİ Kullanılıyor...\n")


    try:
        df_food = pd.read_excel("kaloriler manual.xlsx")
        df_food.columns = df_food.columns.str.strip()
        
        cal_col = 'Kalori' if 'Kalori' in df_food.columns else 'Enerji (kcal)'
        df_food[cal_col] = pd.to_numeric(df_food[cal_col], errors='coerce')
        df_food = df_food.dropna(subset=[cal_col])
        print(f"✅ Gıda Verisi Okundu: {len(df_food)} ürün")

        df_climate = pd.read_excel("iklimverisi.xlsx")
        df_climate = df_climate.iloc[:, :3]
        df_climate.columns = ['İl', 'Ort_Sicaklik', 'Yagis_Miktari']
        df_climate = df_climate.dropna()
        print(f"✅ İklim Verisi Okundu: {len(df_climate)} il.")

    except Exception as e:
        print(f"❌ Dosya Hatası: {e}")
        return


    df_food['İl'] = df_food['İl'].astype(str).str.strip().str.title()
    df_climate['İl'] = df_climate['İl'].astype(str).str.strip().str.title()

    df_final = pd.merge(df_food, df_climate, on='İl', how='inner')
    print(f"🔗 Final Veri Boyutu: {len(df_final)} satır.\n")

    print("📦 En popüler kategoriler:")
    print(df_final['Ürün Grubu'].value_counts().head(10))


    print("\n📊 --- OLS REGRESYON SONUCU ---")
    try:
        X = sm.add_constant(df_final['Ort_Sicaklik'])
        y = df_final[cal_col]
        model = sm.OLS(y, X).fit()
        print(model.summary())
    except:
        print("OLS çalıştırılırken hata oluştu.")


    sns.set_theme(style="whitegrid")



    print("\n📈 Grafik 1: Regresyon Plot")
    g = sns.jointplot(
        x="Ort_Sicaklik", y=cal_col, data=df_final, kind="reg",
        height=8, scatter_kws={'alpha': 0.3}, line_kws={'color': 'red'}
    )
    g.fig.suptitle("H1: Tüm Ürünlerde Sıcaklık - Kalori İlişkisi", y=1.02)
    plt.show()



    print("🎻 Grafik 2: En Popüler 8 Kategorinin İklim Dağılımı")
    plt.figure(figsize=(16, 8))
    top_cats = df_final['Ürün Grubu'].value_counts().head(8).index
    df_top = df_final[df_final['Ürün Grubu'].isin(top_cats)]
    order = df_top.groupby("Ürün Grubu")["Ort_Sicaklik"].median().sort_values().index
    sns.violinplot(x="Ürün Grubu", y="Ort_Sicaklik", data=df_top, order=order, palette="coolwarm")
    plt.xticks(rotation=30)
    plt.show()



    print("📊 Grafik 3: İklim Bölgelerine Göre Ortalama Kalori")
    plt.figure(figsize=(10, 6))
    df_final['Sicaklik_Grubu'] = pd.cut(
        df_final['Ort_Sicaklik'], bins=[-10, 10, 15, 50],
        labels=['Soğuk (<10)', 'Ilıman (10-15)', 'Sıcak (>15)']
    )
    ax = sns.barplot(x='Sicaklik_Grubu', y=cal_col, data=df_final, palette='coolwarm')
    plt.show()



    print("🔥 Grafik 4: Kategori - Bölgesel Kalori Heatmap")
    plt.figure(figsize=(12, 8))
    pivot = df_final[df_final['Ürün Grubu'].isin(top_cats)].pivot_table(
        index='Ürün Grubu', columns='Sicaklik_Grubu',
        values=cal_col, aggfunc='mean'
    )
    sns.heatmap(pivot, annot=True, fmt=".0f", cmap="YlOrRd")
    plt.show()



    print("🌡 Grafik 5: Sıcaklık - Kalori Bubble Chart")
    plt.figure(figsize=(12, 6))
    sns.scatterplot(
        data=df_final,
        x="Ort_Sicaklik",
        y=cal_col,
        hue="Ürün Grubu",
        size=cal_col,
        alpha=0.5
    )
    plt.title("Sıcaklık - Kalori Bubble Chart")
    plt.show()


 
    print("📍 Grafik 6: İl Bazlı Kalori Barplot")
    df_il = df_final.groupby("İl")[cal_col].mean().sort_values()
    plt.figure(figsize=(10, 20))
    sns.barplot(x=df_il.values, y=df_il.index, palette="magma")
    plt.title("İllere Göre Ortalama Kalori")
    plt.show()


   
    print("🧊 Grafik 7: Pairplot Korelasyon")
    sns.pairplot(df_final[["Kalori", "Ort_Sicaklik", "Yagis_Miktari"]], kind="reg")
    plt.show()

    print("\n✅ Analiz Tamamlandı! 🇹🇷 (Harita çıkarıldı)")

if __name__ == "__main__":
    tum_kategorilerle_analiz()
