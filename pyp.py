import matplotlib
matplotlib.use('Agg')

import pandas as pd 
import matplotlib.pyplot as plt

data_path = 'Sheet1.csv'
data = pd.read_csv(data_path)

data['Date'] = pd.to_datetime(data['Date'])
data['Year'] = data['Date'].dt.year
data['Month'] = data['Date'].dt.strftime('%Y-%m')
data['Day'] = data['Date'].dt.date

daily_sales = data.groupby('Day')['Total'].sum()
monthly_sales = data.groupby('Month') ['Total'].sum()
yearly_sales = data.groupby('Year')['Total'].sum()

plt.figure(figsize=(10, 6))
daily_sales.plot (kind='line', marker='o')
plt.title('Дневные продажи')
plt.xlabel('Дата')
plt.ylabel('Объем продаж')
plt.xticks (rotation=45)
plt.tight_layout()
plt.savefig('dally_sales.png')
plt.close()


plt.figure(figsize=(10, 6))
monthly_sales.plot (kind='bar')
plt.title('Месячные продажи')
plt.xlabel('Месяц')
plt.ylabel('Объем продаж')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('monthly_sales.png')
plt.close()


plt.figure(figsize=(10, 6))
yearly_sales.plot (kind='bar')
plt.title('Годовые продажи')
plt.xlabel('Год')
plt.ylabel('Объем продаж')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('yearly_sales.png')
plt.close()