UCSD-eAccounts-Transactions
---
A python script that gives you spreadsheets of your UCSD Dining Dollars and Triton Cash transactions for personal budget tracking.

## How to use it:
You must have `python3` installed on your system and be able to navigate the command line, whether it be Windows, Linux or macOS Terminal.
1. Download this repository and its python script: `git clone https://github.com/Arjdroid/UCSD-eAccounts-Transactions`
2. Run `pip3 install beautifulsoup4`
3. Go to https://eacct-ucsd-sp.transactcampus.com/eAccounts/AccountSummary.aspx and log in with your UCSD Student SSO
4. Click on 'Account Transactions' and specify the desired 'Transaction Period' before clicking 'Search'
5. Right click on the page and select "Save As..." (on Chrome) or "Save Page As..." (on Firefox) to save the webpage
> You must repeat this for each page of transactions. It gets tedious, I know, but I haven't found an API for this yet so if you do, please let me know.
6. Once you have the `eAccounts Account Transactions.html` file, you can run `txn-html-to-csv.py` with the path to the `.html` file as an argument
> Eg. `txn-html-to-csv.py /path/to/eAccounts Account Transactions.html`
7. Then, you have a file called `output.csv`
8. Import `output.csv` into your desired spreadsheet program of choice

### Importing into Google Sheets
1. Go to https://sheets.google.com
2. Open your current budget tracking spreadsheet OR create a new one if desired
3. Click on 'File' in the top right corner, then 'Import' in the drop-down menu from there
4. Then you may click 'Upload' and 'Browse' to choose your `output.csv`
5. Once you've uploaded 'output.csv', ensure you choose the right 'Import location'
6. Click 'Import location' and select "Insert new sheet(s)", then you may select 'Import Data'
> Repeat this process for each html page. I might add an auto-collation and de-duplication feature to the script later.

> Disclaimer: This project does not claim any official endorsement from UCSD nor Transact Campus. 
> This project also does not offer any guarantees of functionality. 
> However, you are welcome to raise issues for valid bugs or pull requests to add genuine features.
