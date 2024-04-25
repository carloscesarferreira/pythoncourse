import pandas as pd

ages = [43, 35, 20, 23, 55, 33, 48, 23, 49, 53, 42, 46, 34, 51, 28, 48, 36, 40, 32, 40, 21, 51, 3, 51, 23, 59, 26, 43, 35, 33, 45, 35, 41, 52, 59, 22, 46, 53, 62, 19, 56, 33, 48, 34, 27, 55, 50, 39, 32, 48, 31, 29, 37, 30, 42, 50, 48, 37, 19, 16, 21, 14, 20, 32, 27, 29, 66, 14, 56, 25, 23, 48, 46, 28, 40, 22, 36, 27, 41, 19, 32, 26, 36, 1, 45, 22, 26, 48, 30, 8, 50, 38, 42, 53, 31, 26, 30, 19, 38, 42]

    # my dataset
df = pd.DataFrame(ages, columns=['Age'])
    # convert list to DataFrame with columns' name 'Age'
description = df.describe()
    # use describe function
print("The description of the dataset is:")
print(description)
    # print the result on the screen
print("\n")

##########################
# Other Pandas' commands #
##########################

print("\n")
print("View the first or last few rows of your DataFrame")
print(df.head())  # displays the first 5 rows by default
print(df.tail())  # displays the last 5 rows by default

print("\n")
print("Get a concise summary of the DataFrame including data types and missing values")
print(df.info())

print("\n")
print("Get the dimensions (number of rows and columns) of the DataFrame.")
print(df.shape)

print("\n")
print("Count the occurrences of unique values in a column (Mode).")
print(df['Age'].value_counts())

print("\n")
print("calculate statistical measures for specific columns")
print("Sum: ",df['Age'].sum())
print("Central Tendency")
print("Mean: ",df['Age'].mean())
print("Median: ",df['Age'].median())
print("Variability")
print("Standard Deviation: ",round(df['Age'].std(),2))






