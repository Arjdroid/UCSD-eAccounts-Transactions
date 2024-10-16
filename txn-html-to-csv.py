import sys
from bs4 import BeautifulSoup

def extract_table(file_path):
    # Open and read the HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')

    # Find the table with the specific class and ID
    table = soup.find('table', {'class': 'rgMasterTable RadGrid_BorderOverride', 'id': 'ctl00_MainContent_ResultRadGrid_ctl00'})
    
    # If the table is found, print its contents
    if table:
        print(table.prettify())
    else:
        print("Table not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 extract_table.py /path/to/file")
        sys.exit(1)

    file_path = sys.argv[1]
    extract_table(file_path)
