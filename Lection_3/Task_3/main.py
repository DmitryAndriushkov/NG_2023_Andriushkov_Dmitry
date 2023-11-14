import json

def findValue(data, key):
    if isinstance(data, dict):
        for item1, item2 in data.items():
            if item1 == key:
                return item2
            result = findValue(item2, key)
            if result is not None:
                return result
            
    elif isinstance(data, list):
        for item in data:
            result = findValue(item, key)
            if result is not None:
                return result

print("\nHi! This program can read your JSON file and display the value for the key that you want.\n")
userFileInput = input("Enter the path to the file: ")

try:
    with open(userFileInput, encoding='utf-8') as file:
        data = json.load(file)

        print("Your JSON file:")
        print(json.dumps(data, indent=4))

        key = input("Enter the key: ")

        value = findValue(data, key)
        if value is not None:
            print(f"Value for {key}: {value}")
        else:
            print(f"Key '{key}' not found in the file.")

except FileNotFoundError:
    print(f"File at the path '{userFileInput}' not found.")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}. Make sure the JSON file is valid.")
except Exception as e:
    print(f"An error occurred: {e}")