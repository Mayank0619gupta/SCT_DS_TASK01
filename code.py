import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

age_groups = ['0 to 20 Years', '21 to 64 Years', '65+ Years']
population_mn = [5, 57, 0.98]  # Population in millions
population_percent = [5/142 * 100, 57/142 * 100, 0.98/142 * 100]  

data = pd.DataFrame({
    'Age Group': age_groups,
    'Population (Mn)': population_mn,
    'Percentage (%)': population_percent
})

sns.set_style('darkgrid') 

# Bar Chart
plt.figure(figsize=(10, 6))
plt.bar(data['Age Group'], data['Population (Mn)'], color=['#FFD700', '#1E90FF', '#FF69B4'])
plt.title('India Population Distribution by Age in 2022', fontsize=14)
plt.xlabel('Age Group', fontsize=12)
plt.ylabel('Population (Millions)', fontsize=12)
plt.xticks(rotation=45)
for i, v in enumerate(population_mn):
    plt.text(i, v + 0.5, str(v), ha='center', fontsize=10)
plt.tight_layout()
plt.show()

# Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(data['Percentage (%)'], labels=data['Age Group'], colors=['#FFD700', '#1E90FF', '#FF69B4'], autopct='%1.1f%%', startangle=90)
plt.title('India Population Distribution by Age (Percentage) in 2022', fontsize=14)
plt.axis('equal')
plt.tight_layout()
plt.show()

# Line Chart (to show a hypothetical trend over time, assuming data for multiple year)
years = [2020, 2021, 2022]
pop_0_20 = [6, 5.5, 5]
pop_21_64 = [55, 56, 57]
pop_65_plus = [0.9, 0.94, 0.98]

plt.figure(figsize=(10, 6))
plt.plot(years, pop_0_20, marker='o', label='0-20 Years', color='#FFD700')
plt.plot(years, pop_21_64, marker='o', label='21-64 Years', color='#1E90FF')
plt.plot(years, pop_65_plus, marker='o', label='65+ Years', color='#FF69B4')
plt.title('Hypothetical Trend of India Population by Age (2020-2022)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Population (Millions)', fontsize=12)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
