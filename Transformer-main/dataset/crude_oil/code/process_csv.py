import pandas as pd

# CSV dosyasını yükle
df = pd.read_csv('./dataset//crude_oil//crude_oil_data_with_indicators.csv')

# 'date' sütununu datetime formatına dönüştür ve UTC'ye çevir
df['date'] = pd.to_datetime(df['date'], utc=True)

# Gerekli sütunları seçin (Modelinize uygun veriler)
# Burada sadece örnek olarak gerekli olan sütunları seçiyorum, ihtiyaca göre düzenlenebilir
df = df[['date','Open','High','Low','Close','MACD','MACD_Signal','RSI','Upper_Band','Middle_Band','Lower_Band','EMA_25','EMA_50','EMA_100','EMA_200']]

# Eksik verileri kontrol et (NaN değerleri temizleyebilirsiniz)
df = df.dropna()

# 'date' sütunu haricindeki diğer sütunlardaki verileri noktadan sonra maksimum 2 haneli olacak şekilde yuvarla
df.iloc[:, 1:] = df.iloc[:, 1:].round(4)

# Veriyi uygun şekilde kaydedin
df.to_csv('crude_oil_data_with_indicators2.csv', index=False)

print("CSV dosyası işlenip kaydedildi!")
