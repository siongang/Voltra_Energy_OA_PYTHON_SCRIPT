import json


def get_file():
    try:
        with open('export.json', 'r') as file:
            
            for line in file:
                dataset = json.loads(line)    
                print(dataset)
        
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Invalid JSON format.")