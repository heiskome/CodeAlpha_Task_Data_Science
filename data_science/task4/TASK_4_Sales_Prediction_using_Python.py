import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import tkinter as tk
from tkinter import messagebox

# Load dataset (assume 'Advertising.csv' is in the same directory)
# Note: The first column is index, skip it
df = pd.read_csv('Advertising.csv', index_col=0)

# Features and target
X = df[['TV', 'Radio', 'Newspaper']]
y = df['Sales']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse:.2f}')  # Console output

# GUI
def predict_sales():
    try:
        tv = float(entry_tv.get())
        radio = float(entry_radio.get())
        newspaper = float(entry_newspaper.get())
        
        input_data = [[tv, radio, newspaper]]
        prediction = model.predict(input_data)[0]
        
        messagebox.showinfo("Prediction", f"The predicted sales are: {prediction:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

# Create GUI window
root = tk.Tk()
root.title("Sales Prediction")
root.geometry("400x250")
root.configure(bg='#f0f0f0')

# Labels and Entries
tk.Label(root, text="TV Advertising Spend:", bg='#f0f0f0').pack(pady=5)
entry_tv = tk.Entry(root)
entry_tv.pack()

tk.Label(root, text="Radio Advertising Spend:", bg='#f0f0f0').pack(pady=5)
entry_radio = tk.Entry(root)
entry_radio.pack()

tk.Label(root, text="Newspaper Advertising Spend:", bg='#f0f0f0').pack(pady=5)
entry_newspaper = tk.Entry(root)
entry_newspaper.pack()

# Predict Button
predict_button = tk.Button(root, text="Predict Sales", command=predict_sales, bg='#4CAF50', fg='white')
predict_button.pack(pady=20)

root.mainloop()