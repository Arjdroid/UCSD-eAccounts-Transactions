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

    # If the table is found, process its contents
    if table:
        # Clear the attributes of the table itself
        table.attrs = {}

        # Remove unwanted attributes from the table's children
        for tag in table.find_all(True):  # Find all tags inside the table
            tag.attrs = {}  # Clear all attributes for each tag

        # Only keep the essential table structure (table, thead, tbody, tr, th, td)
        # Remove unwanted tags like 'tfoot', 'colgroup', 'caption', 'span', and 'div'
        for unwanted_tag in table(['tfoot', 'colgroup', 'caption', 'thead table', 'span', 'div']):
            unwanted_tag.decompose()

        # Convert the simplified table back to HTML string
        simplified_table = str(table)

        # Print the simplified table
        print(simplified_table)
    else:
        print("Table not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 extract_table.py /path/to/file")
        sys.exit(1)

    file_path = sys.argv[1]
    extract_table(file_path)
