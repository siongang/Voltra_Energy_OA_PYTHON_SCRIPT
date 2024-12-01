import os
import json
import read_json
import gpt_api_handler
import google_api_handler
import sys
sys.stdout.reconfigure(encoding='utf-8')  # Set the standard output encoding to UTF-8
import csv

CSV_PATH = 'results.csv'



"""
Main Function. Reads data from Export.json and writes domain data onto the csv file
"""
def main():
    dataset = []
    csv_header = ["Company Name", "EV Charger Location", "Domain"]
 

    try:
        with open('export.json', 'r') as file:

            previous_data = {"address" : None}

            # loop counter for TESTING 
            counter = 0


            # Iterate through each line in the export.json file
            for line in file:

                # Turn the line to a dictionary
                data = json.loads(line) 
                find_company_name = read_file_to_string("find_company_name.txt")
                find_domain = read_file_to_string("find_domain.txt")
                # Make sure the address and location is different. THIS ASSUMES THAT THE LIST IS ALREADY SORTED!!!
                if data["address"] != previous_data["address"]:   
                     
                    ''' FIRST METHOD : CHROME WEBSEARCH AND CHATGPT '''
                    # Create the address of the location
                    # Search the address with Google Search API
                    # Inquire ChatGPT and determine owner based on websearch results
                    # Search {owner} + Official Website with Google Search API
                    # Inquire ChatGPT and determine company domain
                
                    if data.get('city','NA') != 'NA':
                        address = f"{data['city']} {data.get('address', 'Unknown Address')}"
                    else:
                        address = f"{data.get('address', 'Unknown Address')}"

                    google_search_results = google_api_handler.google_search(address,6)
                    owner = gpt_api_handler.chat_with_gpt(find_company_name, google_search_results)

                    if (owner.lower() != "unknown"):
                        query = f"{owner} {data.get('city', data.get('postalcode', '')) if data.get('city', '') != 'NA' else data.get('postalcode', '')} Official Website"
                        google_search_results = google_api_handler.google_search(query, 6)
                        domain = gpt_api_handler.chat_with_gpt(find_domain, google_search_results)
                        
                        line = {"Company Name":owner, "Address": address, "Domain": domain}
                        dataset.append(line)
                     
                    # Saving the current dictionary that holds data to previous data. 
                    previous_data = data
                

                # USED FOR TESTING
                counter += 1
                print(f"{counter} domain")
                # if counter > 5: break

            
            # WRITING ONTO RESULTS.CSV
            write_dict_to_csv(CSV_PATH, dataset)



            # USED FOR TESTING Printing Owner
            for data in dataset:
                print(data)
                print()

                    

    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Invalid JSON format.")



def read_file_to_string(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

# Write the list of dictionaries to the CSV file
def write_dict_to_csv(path, data):

    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    with open(path, mode='w', newline='') as file:
        # Get the fieldnames from the first dictionary
        fieldnames = data[0].keys()        
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    main()