import requests
from bs4 import BeautifulSoup
import csv

# URL of the Wikipedia page to scrape
url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the table containing the data
    table = soup.find("table", class_="wikitable")

    # Extract the data from the table
    data = []
    headers = table.find("tr").find_all("th")
    data.append([header.text.strip() for header in headers])
    for row in table.find_all("tr")[1:]:
        cells = row.find_all("td")
        if len(cells) > 0:
            data.append([cell.text.strip() for cell in cells])

    # Write the extracted data into a file
    with open('./file/s&p_500.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
else:
    print("Failed to retrieve data from the Wikipedia page.")