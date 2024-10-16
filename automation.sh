#!/bin/zsh

# Change to the directory containing your HTML files
cd "${HOME}/Downloads/ucsd-transactions-html/html_files"

# Loop over each HTML file matching the pattern
for INPUT_FILE in eAccounts\ Account\ Transactions*.html; do
    echo "Processing file: $INPUT_FILE"

    # Run the Python script on the current HTML file
    python3 txn-html-to-csv.py "$INPUT_FILE"

    # Extract the number from the filename
    N=$(echo "$INPUT_FILE" | grep -o '[0-9]\+')

    # Rename the output CSV file
    mv output.csv "output${N}.csv"
done
