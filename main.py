### Normalized
# import pandas as pd

# # Define a function to normalize phone numbers by removing non-numeric characters
# def normalize_phone_number(phone):
#     return ''.join(filter(str.isdigit, str(phone)))

# # Load the CSV files into DataFrames
# df1 = pd.read_csv('iphone.csv')
# df2 = pd.read_csv('google.csv')

# # Assuming the phone numbers are in a column named 'phone'
# # Normalize the phone numbers in both DataFrames
# df1['normalized_phone'] = df1['Phone 1 - Value'].apply(normalize_phone_number)
# df2['normalized_phone'] = df2['Phone 1 - Value'].apply(normalize_phone_number)

# # Combine the DataFrames
# combined_df = pd.concat([df1, df2])

# # Find duplicates based on the normalized phone number
# duplicates = combined_df.duplicated(subset=['normalized_phone'], keep=False)

# # Filter out the duplicates
# non_duplicates = combined_df[~duplicates]

# # Drop the normalized_phone column if you don't need it in the output
# non_duplicates.drop(columns=['normalized_phone'], inplace=True)

# # Print or save the result
# print(non_duplicates)

# # If you want to save the result to a new CSV file
# non_duplicates.to_csv('non_duplicates.csv', index=False)


### Not Normalized
import pandas as pd

# Load the CSV files into DataFrames
df1 = pd.read_csv('google.csv')
df2 = pd.read_csv('iphone.csv')

# Concatenate the DataFrames
combined_df = pd.concat([df1, df2])

# Find duplicates based on all columns (consider all columns to identify duplicates)
duplicates = combined_df.duplicated(subset=['Name'], keep=False)

# Filter out the duplicates
non_duplicates = combined_df[~duplicates]

# Print or save the result
print(non_duplicates)

# If you want to save the result to a new CSV file
non_duplicates.to_csv('non_duplicates.csv', index=False)

