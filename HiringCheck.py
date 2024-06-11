from bs4 import BeautifulSoup
import pandas as pd
import requests

# Function to perform a Google search and check for indications of software engineer hiring
def check_hiring(company_name):
    query = f"{company_name} software engineer jobs"
    url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Analyze search results
    for item in soup.select('div'):
        text = item.get_text().lower()
        if " " in text or "software developer" in text or "developer" in text:
            return True
    return False 

# Load the IT industries DataFrame
it_industries_df = pd.read_csv('./data/file/it_industries.csv')

# Apply the check_hiring function and add the results to a new column
it_industries_df['hiring_software_engineers'] = it_industries_df['Security'].apply(check_hiring)

# Save the updated DataFrame back to CSV
it_industries_df.to_csv('./data/file/it_industries.csv', index=False)

refined_sp_500_df = pd.read_csv('./data/file/refined_s&p_500.csv')
it_industries_df = pd.read_csv('./data/file/it_industries.csv')
non_it_industries_df = pd.read_csv('./data/file/non_it_industries.csv')

for company in it_industries_df['Security']:
    hiring_status = check_hiring(company)
    print(f"{company}: {hiring_status}")


# Get all the companies where the field hiring_software_engineers is True.