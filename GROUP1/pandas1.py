# Creating dataframes
import pandas as pd
import numpy as np
# Creating a DataFrame from a dictionary
data = {
    'Name': np.array(['Alice', 'Bob', 'Charlie']),
    'Age': np.array([24, 27, 22]),
    'City': np.array(['New York', 'Los Angeles', 'Chicago'])
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)




# Reading data from files in python 
# Reading a CSV file
# df = pd.read_csv('data.csv')
# print("Data from CSV:\n", df)

# Reading an Excel file
# df_excel = pd.read_excel('data.xlsx')
# print("Data from Excel:\n", df_excel)




#Dataframe Operations
# Selecting a single column
ages = df['Age']
print("Ages:\n", ages)

# Filtering data
filtered_df = df[df['Age'] > 25]
print("Filtered DataFrame:\n", filtered_df)

# Adding a new column
df['Salary'] = [50000, 60000, 55000]
print("DataFrame with new column:\n", df)




# Handling missing data 
data_with_nan = {
    'Name': ['Alice', 'Bob', None],
    'Age': [24, None, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df_nan = pd.DataFrame(data_with_nan)
print("DataFrame with NaN:\n", df_nan)

# Filling missing values
df_filled = df_nan.fillna({'Name': 'Unknown', 'Age': 0})
print("Filled DataFrame:\n", df_filled)

# Dropping rows with missing values
df_dropped = df_nan.dropna()
print("Dropped NaN DataFrame:\n", df_dropped)





# Grouping Data
data = {
    'Department': ['Sales', 'Sales', 'HR', 'HR', 'IT'],
    'Employee': ['John', 'Alice', 'Bob', 'Charlie', 'David'],
    'Salary': [70000, 80000, 50000, 60000, 90000]
}
df = pd.DataFrame(data)

# Grouping by Department and summing salaries
group_by_dept = df.groupby('Department')['Salary'].sum()
print("Grouped by Department:\n", group_by_dept)






