import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import tkinter as tk
from tkinter import messagebox

# Load the dataset (assume 'iris.csv' is in the same directory)
df = pd.read_csv('iris.csv')

# Preprocess: drop Id, features and target
X = df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
y = df['Species']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f'Model Accuracy: {accuracy * 100:.2f}%')  # Console output for reference

# GUI
def predict_species():
    try:
        sepal_length = float(entry_sepal_length.get())
        sepal_width = float(entry_sepal_width.get())
        petal_length = float(entry_petal_length.get())
        petal_width = float(entry_petal_width.get())
        
        input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
        prediction = model.predict(input_data)[0]
        
        messagebox.showinfo("Prediction", f"The predicted species is: {prediction}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

# Create GUI window
root = tk.Tk()
root.title("Iris Flower Classification")
root.geometry("400x300")
root.configure(bg='#f0f0f0')

# Labels and Entries
tk.Label(root, text="Sepal Length (cm):", bg='#f0f0f0').pack(pady=5)
entry_sepal_length = tk.Entry(root)
entry_sepal_length.pack()

tk.Label(root, text="Sepal Width (cm):", bg='#f0f0f0').pack(pady=5)
entry_sepal_width = tk.Entry(root)
entry_sepal_width.pack()

tk.Label(root, text="Petal Length (cm):", bg='#f0f0f0').pack(pady=5)
entry_petal_length = tk.Entry(root)
entry_petal_length.pack()

tk.Label(root, text="Petal Width (cm):", bg='#f0f0f0').pack(pady=5)
entry_petal_width = tk.Entry(root)
entry_petal_width.pack()

# Predict Button
predict_button = tk.Button(root, text="Predict Species", command=predict_species, bg='#4CAF50', fg='white')
predict_button.pack(pady=20)

# Model accuracy label
tk.Label(root, text=f"Model Accuracy: {accuracy * 100:.2f}%", bg='#f0f0f0', font=('Arial', 12, 'bold')).pack(pady=10)

root.mainloop()