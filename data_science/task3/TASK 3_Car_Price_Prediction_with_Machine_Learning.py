import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
import tkinter as tk
from tkinter import messagebox

# Load dataset (assume 'car data.csv' is in the same directory)
df = pd.read_csv('car data.csv')

# Preprocess: features and target
X = df[['Year', 'Present_Price', 'Driven_kms', 'Fuel_Type', 'Selling_type', 'Transmission', 'Owner']]
y = df['Selling_Price']

# Categorical columns
categorical_features = ['Fuel_Type', 'Selling_type', 'Transmission']

# Pipeline
preprocessor = ColumnTransformer(
    transformers=[('cat', OneHotEncoder(), categorical_features)],
    remainder='passthrough'
)

model = Pipeline(steps=[('preprocessor', preprocessor),
                        ('regressor', LinearRegression())])

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse:.2f}')  # Console output

# GUI
def predict_price():
    try:
        year = int(entry_year.get())
        present_price = float(entry_present_price.get())
        driven_kms = int(entry_driven_kms.get())
        fuel_type = entry_fuel_type.get()
        selling_type = entry_selling_type.get()
        transmission = entry_transmission.get()
        owner = int(entry_owner.get())
        
        input_data = pd.DataFrame([[year, present_price, driven_kms, fuel_type, selling_type, transmission, owner]],
                                  columns=['Year', 'Present_Price', 'Driven_kms', 'Fuel_Type', 'Selling_type', 'Transmission', 'Owner'])
        
        prediction = model.predict(input_data)[0]
        
        messagebox.showinfo("Prediction", f"The predicted selling price is: ${prediction:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid values.")

# Create GUI window
root = tk.Tk()
root.title("Car Price Prediction")
root.geometry("400x400")
root.configure(bg='#f0f0f0')

# Labels and Entries
tk.Label(root, text="Year:", bg='#f0f0f0').pack(pady=5)
entry_year = tk.Entry(root)
entry_year.pack()

tk.Label(root, text="Present Price:", bg='#f0f0f0').pack(pady=5)
entry_present_price = tk.Entry(root)
entry_present_price.pack()

tk.Label(root, text="Driven Kms:", bg='#f0f0f0').pack(pady=5)
entry_driven_kms = tk.Entry(root)
entry_driven_kms.pack()

tk.Label(root, text="Fuel Type (Petrol/Diesel/CNG):", bg='#f0f0f0').pack(pady=5)
entry_fuel_type = tk.Entry(root)
entry_fuel_type.pack()

tk.Label(root, text="Selling Type (Dealer/Individual):", bg='#f0f0f0').pack(pady=5)
entry_selling_type = tk.Entry(root)
entry_selling_type.pack()

tk.Label(root, text="Transmission (Manual/Automatic):", bg='#f0f0f0').pack(pady=5)
entry_transmission = tk.Entry(root)
entry_transmission.pack()

tk.Label(root, text="Owner (0/1/2/...):", bg='#f0f0f0').pack(pady=5)
entry_owner = tk.Entry(root)
entry_owner.pack()

# Predict Button
predict_button = tk.Button(root, text="Predict Price", command=predict_price, bg='#4CAF50', fg='white')
predict_button.pack(pady=20)

root.mainloop()