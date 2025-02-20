# Apple Keychain to Bitwarden Converter

This project provides a Python script that converts an Apple Keychain CSV file to a Bitwarden-compatible JSON format. The script processes your CSV export by grouping entries that share the same username and password, merging related website URLs, and standardizing the entry titles.

## How It Works

- **CSV Parsing and Data Extraction**  
  The script reads your Apple Keychain CSV file using Python’s CSV library. It expects columns like "Title", "URL", "Username", and "Password". Rows missing any of these fields are skipped.

- **Title Cleaning**  
  It uses the `clean_title()` function to remove any extra email information in parentheses from the title, ensuring a cleaner display name.

- **Domain Extraction with tldextract**  
  The `extract_site_name()` function employs the `tldextract` library to parse the URL and extract the core domain (ignoring subdomains and suffixes). The resulting domain is capitalized, offering a consistent naming format for your entries.

- **Merging Logins**  
  By using a grouping mechanism keyed on `(username, password)`, the script consolidates multiple entries into one when the same credentials are detected. All relevant URLs are combined into a single list, so each Bitwarden entry includes all associated websites.

- **Conversion to Bitwarden Format**  
  After processing, the script builds a JSON structure that matches Bitwarden’s import format. Each item contains the entry name, login details (username, password, and list of URIs), and a type field set to `1` (representing a standard login).

## Prerequisites

- Python 3.x
- The `tldextract` library

You can install `tldextract` via pip:

    pip install tldextract

## Installation

1. Clone or download this repository.
2. Ensure that Python 3 and the `tldextract` library are installed on your system.

## Usage

1. Place your Apple Keychain CSV file (e.g., `apple_keychain.csv`) in the same directory as the script.
2. Run the script using Python:

       python convert_keychain_to_bitwarden_json.py

   By default, the script expects:
   - Input file: `apple_keychain.csv`
   - Output file: `bitwarden_import.json`

3. The output JSON file will be created and can be imported directly into Bitwarden.

## Example Command

    python convert_keychain_to_bitwarden_json.py apple_keychain.csv bitwarden_import.json

*(If you modify the script to accept command-line arguments, update the usage instructions accordingly.)*

## Error Handling

- **File Not Found:** The script will raise an error if the input CSV file is not found.
- **Badly Formatted CSV:** Rows without the necessary fields (URL, username, password) are automatically skipped.
- Other exceptions are caught and printed to help troubleshoot issues.

## License

This project is licensed under the MIT License.

## Contributing

Feel free to fork the repository and submit pull requests. Please ensure any contributions maintain the clarity and usability of the project.
