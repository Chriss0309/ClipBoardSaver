import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"

def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == "save":
        key = input("Please enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data saved!")
    elif command == "load":
        key = input("Enter a key to load: ")
        if key in data:
            clipboard.copy(data[key])
            print(f"Data for '{key}' copied to clipboard.")
        else:
            print(f"No data found for key '{key}'.")
    elif command == "list":
        if data:
            print("Keys stored:")
            for key in data.keys():
                print(key)
        else:
            print("No data stored.")
    else:
        print("Unknown command")
else:
    print("Please pass exactly one command.")



