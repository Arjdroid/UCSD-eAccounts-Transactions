import csv
import sys
from bs4 import BeautifulSoup
from datetime import datetime

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
        #print(simplified_table)
        print("Operation Successful")
        html_table_to_csv(simplified_table)
    else:
        print("Table not found.")

def html_table_to_csv(simplified_table):
    # Parse the HTML table using BeautifulSoup
    soup = BeautifulSoup(simplified_table, 'html.parser')
    table_rows = soup.find_all('tr')

    # Open a CSV file to write the output
    with open('output.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write the CSV header
        writer.writerow(["Date Time", "Company", "Description", "Amount", "Category", "Payment Method"])

        # Iterate through each row in the table (skip the first row since it's the header)
        for row in table_rows[1:]:
            cells = row.find_all('td')

            if len(cells) < 6:  # Skip any invalid or incomplete rows
                continue

            # Date/Time conversion
            original_date_time = cells[0].text.strip()
            date_obj = datetime.strptime(original_date_time, "%m/%d/%Y %I:%M %p")
            formatted_date_time = date_obj.strftime("%Y-%m-%dT%H:%M:00")

            # Location (split first word for company, and the rest for description)
            location = cells[3].text.strip()
            location_parts = location.split(' ', 1)
            company = location_parts[0]
            description = location_parts[1] if len(location_parts) > 1 else ''

            # Amount (remove parentheses and "USD")
            amount_text = cells[5].text.strip()
            amount = amount_text.replace("(", "").replace(")", "").replace(" USD", "")

            # Transaction Type
            transaction_type = cells[4].text.strip()

            # Convert amount to negative if it's a Credit
            if transaction_type == "Credit":
                amount = f"-{amount}"

            # Payment Method (Account Name)
            payment_method = cells[1].text.strip()

            # Category (same as company)
            category = company

            # Write the row to the CSV
            writer.writerow([formatted_date_time, company, description, amount, category, payment_method])



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 extract_table.py /path/to/file")
        sys.exit(1)

    file_path = sys.argv[1]
    extract_table(file_path)
