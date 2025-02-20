# Apple Keychain to Bitwarden Converter

This script converts Apple Keychain CSV files to Bitwarden JSON format, merging logins with the same credentials.

## Requirements

- Python 3.x
- `tldextract` library

Install the required library using pip:

    pip install tldextract

## Usage

1. Place your Apple Keychain CSV file in the same directory as this script.
2. Run the script with the input and output file names:

    python convert_keychain_to_bitwarden_json.py

By default, the script will look for `apple_keychain.csv` and output to `bitwarden_import.json`.

## Example

    python convert_keychain_to_bitwarden_json.py apple_keychain.csv bitwarden_import.json

## Error Handling

The script includes basic error handling for scenarios such as:
- File not found errors.
- Improperly formatted CSV entries.

Ensure your input file exists and is correctly formatted before running the script.

## License

This project is licensed under the MIT License.
