import pandas as pd
import os # Used to interact with the operating system, such as creating folders and file paths.

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)
output_path = 'output.csv'

# # Adding new row to df for V2
new_row_loc = {'Name': 'GF1', 'Age': 20, 'City': 'City1'}
df.loc[len(df.index)] = new_row_loc

# # Adding new row to df for V3
new_row_loc2 = {'Name': 'GF2', 'Age': 30, 'City': 'City2'}
df.loc[len(df.index)] = new_row_loc2

# Ensure that the directory exists at root level
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True) # if directory/folder exists then it will not make it again

# Define the full path
full_path = os.path.join(data_dir, 'sample_data.csv')

# Save the DataFrame to a CSV file including column names
df.to_csv(full_path, index=False) # index=False : Prevents the row index (0,1,2…) from being written to the file.

print(f"DataFrame saved to {full_path}")