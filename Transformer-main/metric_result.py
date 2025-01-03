import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np

# Örnek veri: Tahmin uzunluklarına ve metriklere göre sonuçlar
data = {
    "Metric": [
        "MSE", "MAE", "RMSE", "MAPE", "MSPE", "R2",
        "MSE", "MAE", "RMSE", "MAPE", "MSPE", "R2",
        "MSE", "MAE", "RMSE", "MAPE", "MSPE", "R2",
        "MSE", "MAE", "RMSE", "MAPE", "MSPE", "R2"
    ],
    "Length": [
        "24", "24", "24", "24", "24", "24",
        "48", "48", "48", "48", "48", "48",
        "72", "72", "72", "72", "72", "72",
        "96", "96", "96", "96", "96", "96"
    ],
    "Autoformer": [
        0.111, 0.254, 0.334, 0.974, 385.553, 0.647,
        0.196, 0.338, 0.443, 0.979, 126.008, 0.378,
        0.228, 0.373, 0.477, 1.156, 172.438, 0.272,
        0.247, 0.394, 0.497, 1.127, 295.359, 0.205
    ],
    "Reformer": [
        0.121, 0.289, 0.348, 0.783, 211.751, 0.616,
        0.198, 0.374, 0.445, 1.01, 248.478, 0.372,
        0.251, 0.421, 0.501, 1.042, 215.633, 0.198,
        0.437, 0.574, 0.661, 1.097, 157.362, -0.41
    ],
    "Informer": [
        0.067, 0.206, 0.259, 0.795, 328.618, 0.787,
        0.118, 0.279, 0.343, 1.03, 549.888, 0.626,
        0.191, 0.356, 0.437, 0.955, 232.806, 0.389,
        0.233, 0.402, 0.482, 1.032, 234.146, 0.250
    ],
    "Vanilla": [
        0.06, 0.193, 0.245, 0.778, 281.595, 0.810,
        0.124, 0.279, 0.353, 1.102, 515.877, 0.606,
        0.157, 0.317, 0.396, 0.898, 180.353, 0.499,
        0.145, 0.293, 0.380, 1.048, 228.118, 0.534
    ]
}

# Pandas veri çerçevesi oluştur
length_df = pd.DataFrame(data)

# Tablonun her uzunluk için ayrı ayrı görselleştirilmesi
lengths = ["24", "48", "72", "96"]

def save_table(df, title, filename, figsize=(6, 4), fontsize=10):
    # Tablonun görselleştirilmesi
    plt.figure(figsize=figsize)
    sns.set_theme(style="whitegrid")

    # Renklendirme için her satırdaki veriyi normalize et
    cell_colors = []
    cmap = plt.cm.Blues
    for row in df.itertuples(index=False):
        # İlk iki sütun dışındaki veriler üzerinde işlem yap
        row_values = np.array(row[2:], dtype=float)
        norm = plt.Normalize(row_values.min() - 0.1, row_values.max() + 0.1)
        row_colors = ['white', 'white'] + [cmap(norm(value), alpha=0.6) for value in row_values]
        cell_colors.append(row_colors)

    # Tablonun çizilmesi
    table = plt.table(
        cellText=df.values,
        colLabels=df.columns,
        cellLoc='center',
        loc='center',
        rowLoc='center',
        colLoc='center',
        cellColours=cell_colors
    )

    # Tablo ayarları
    table.auto_set_font_size(False)
    table.set_fontsize(fontsize)
    table.auto_set_column_width(col=list(range(len(df.columns))))

    # Başlık ekleme
    plt.title(title, fontsize=fontsize + 2, fontweight='bold', pad=20)

    # Eksenleri kaldır
    plt.axis('off')

    # Dosyayı masaüstüne kaydet
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    output_path = os.path.join(desktop, filename)
    plt.savefig(output_path, bbox_inches='tight', dpi=300)
    plt.close()

    print(f"{title} başarıyla {output_path} konumuna kaydedildi!")

# Uzunluk bazlı tabloları kaydet
for length in lengths:
    subset = length_df[length_df["Length"] == length]
    save_table(subset, f"Length {length} Metrics Table", f"model_metrics_table_{length}.png")
