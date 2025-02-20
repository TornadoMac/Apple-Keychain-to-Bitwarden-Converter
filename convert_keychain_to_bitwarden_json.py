import csv
import json
import tldextract
from collections import defaultdict

def clean_title(title):
    """Remove email from the title if it exists in parentheses."""
    if "(" in title:
        return title.split(" (")[0]
    return title

def extract_site_name(url):
    """Extracts the core site name without .com, .net, etc."""
    extracted = tldextract.extract(url)
    return extracted.domain.capitalize()  # Capitalize for a clean look

def process_apple_keychain_csv(input_file, output_file):
    """Convert Apple Keychain CSV to Bitwarden JSON format with merged logins."""
    entries = defaultdict(lambda: {"name": "", "username": "", "password": "", "uris": []})
    
    try:
        with open(input_file, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                title = clean_title(row["Title"])
                url = row["URL"]
                username = row["Username"]
                password = row["Password"]
                
                if not url or not username or not password:
                    continue  # Skip empty entries

                key = (username, password)  # Group by credentials
                
                site_name = extract_site_name(url)
                if not entries[key]["name"]:
                    entries[key]["name"] = site_name  # Set initial title
                entries[key]["uris"].append({"uri": url})  # Add all related URLs
                
                # Prioritize the most common site name
                if site_name not in entries[key]["name"]:
                    entries[key]["name"] = site_name

                entries[key]["username"] = username
                entries[key]["password"] = password

        # Convert to Bitwarden JSON format
        bitwarden_data = {
            "items": [
                {
                    "name": entry["name"],
                    "login": {
                        "username": entry["username"],
                        "password": entry["password"],
                        "uris": entry["uris"] if entry["uris"] else []
                    },
                    "type": 1  # Login type
                }
                for entry in entries.values()
            ]
        }

        with open(output_file, "w", encoding="utf-8") as jsonfile:
            json.dump(bitwarden_data, jsonfile, indent=4)
        print(f"Conversion successful! Output saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage example
if __name__ == "__main__":
    process_apple_keychain_csv("apple_keychain.csv", "bitwarden_import.json")
