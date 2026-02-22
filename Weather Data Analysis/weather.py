import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector

#connectivity
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ARJUN@2005",
    database="weather_db"
)

query = "SELECT * FROM weather_data"
df = pd.read_sql(query, conn)
print(df)

#calculate
print("Temperature Statistics")
print("Minimum:", np.min(df["temperature"]))
print("Maximum:", np.max(df["temperature"]))
print("Average:", np.mean(df["temperature"]))

print("\nHumidity Statistics")
print("Minimum:", np.min(df["humidity"]))
print("Maximum:", np.max(df["humidity"]))
print("Average:", np.mean(df["humidity"]))

#Line Plot
plt.figure()
plt.plot(df["date"], df["temperature"])
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Trend Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Correlation
plt.figure()
correlation = df[["temperature", "humidity"]].corr()
sns.heatmap(correlation, annot=True)
plt.title("Weather Data Correlation Heatmap")
plt.show()

