import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Load datasets (assume files are in the same directory)
df1 = pd.read_csv('Unemployment in India.csv')
df2 = pd.read_csv('Unemployment_Rate_upto_11_2020.csv')

# Clean df1
df1.columns = df1.columns.str.strip()
df1['Date'] = pd.to_datetime(df1['Date'], dayfirst=True)
df1 = df1.dropna()  # Drop empty rows

# Clean df2
df2.columns = df2.columns.str.strip()
df2['Date'] = pd.to_datetime(df2['Date'], dayfirst=True)

# Combine for analysis (focus on common columns like unemployment rate, date, region)
combined_df = pd.concat([df1[['Region', 'Date', 'Estimated Unemployment Rate (%)']],
                         df2[['Region', 'Date', 'Estimated Unemployment Rate (%)']]], ignore_index=True)

# Covid impact: pre-covid (<2020-03), during covid
combined_df['Period'] = 'Pre-Covid'
combined_df.loc[combined_df['Date'] >= '2020-03-01', 'Period'] = 'During Covid'

# GUI
root = tk.Tk()
root.title("Unemployment Analysis")
root.geometry("800x600")
root.configure(bg='#f0f0f0')

# Notebook for tabs
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# Tab 1: Overall Trends
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text='Trends')

fig1, ax1 = plt.subplots(figsize=(6,4))
sns.lineplot(data=combined_df, x='Date', y='Estimated Unemployment Rate (%)', hue='Period', ax=ax1)
ax1.set_title('Unemployment Rate Trends (Pre vs During Covid)')
canvas1 = FigureCanvasTkAgg(fig1, master=tab1)
canvas1.draw()
canvas1.get_tk_widget().pack()

# Tab 2: Regional Analysis
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text='Regional')

fig2, ax2 = plt.subplots(figsize=(6,4))
sns.boxplot(data=combined_df, x='Region', y='Estimated Unemployment Rate (%)', ax=ax2)
ax2.set_title('Unemployment by Region')
ax2.tick_params(axis='x', rotation=90)
canvas2 = FigureCanvasTkAgg(fig2, master=tab2)
canvas2.draw()
canvas2.get_tk_widget().pack()

# Tab 3: Insights
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text='Insights')

insights = """
Key Insights:
- Unemployment spiked during Covid-19 (March 2020 onwards).
- Average pre-Covid rate: {:.2f}%
- Average during Covid rate: {:.2f}%
- Regions like Haryana, Bihar saw higher impacts.
- Seasonal trends: Higher in rural areas during certain months.
""".format(combined_df[combined_df['Period']=='Pre-Covid']['Estimated Unemployment Rate (%)'].mean(),
           combined_df[combined_df['Period']=='During Covid']['Estimated Unemployment Rate (%)'].mean())

tk.Label(tab3, text=insights, justify='left', bg='#f0f0f0').pack(pady=10)

root.mainloop()