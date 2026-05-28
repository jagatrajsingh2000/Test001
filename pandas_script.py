import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'Salary': [50000, 60000, 75000, 65000, 70000]
}

df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)
print("\n")

# Calculate average salary
average_salary = df['Salary'].mean()
print(f"Average Salary: ${average_salary:,.2f}")
print("\n")

# Filter employees with salary > 60000
high_earners = df[df['Salary'] > 60000]
print("High Earners (Salary > $60,000):")
print(high_earners)
print("\n")

# Sort by age
df_sorted = df.sort_values('Age')
print("Employees sorted by Age:")
print(df_sorted)
