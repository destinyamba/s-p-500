import pandas as pd

# Load the CSV file
df = pd.read_csv('./data/file/it_industries.csv')

# Filter the rows where hiring_software_engineers is True
filtered_df = df[df['hiring_software_engineers'] == True]


# Print the filtered dataframe
print(filtered_df)
# Write the filtered dataframe to a CSV file
filtered_df.to_csv('./data/file/currentopenings.csv', index=False)