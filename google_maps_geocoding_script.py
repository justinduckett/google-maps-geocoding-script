#!/usr/bin/env python
# coding: utf-8

# In[2]:


# import python modules
import csv
import requests
import time

# This function makes a request to the Google Maps Geocoding API and extracts the relevant information. 
# You pass in an address and an API key, and it returns the coordinates.

def geocode_address(address, api_key):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": address,
        "key": api_key
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if data["status"] == "OK":
        location = data["results"][0]["geometry"]["location"]
        return location["lat"], location["lng"]
    else:
        return None, None

# This function processes the entire CSV file, geocoding each address and creating a new file with the results. 
# It handles file I/O, CSV parsing and writing, and integrates with the geocoding function while implementing basic rate limiting.

def process_csv(input_file, output_file, api_key):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Write header
        header = next(reader)
        writer.writerow(header + ['Latitude', 'Longitude'])
        
        for row in reader:
            address = row[0]
            lat, lng = geocode_address(address, api_key)
            writer.writerow(row + [lat, lng])
            time.sleep(0.1)  # To avoid hitting API rate limits

# this section sets up the input and output filenames, defines the API key, and calls the process_csv function. 
# this section only runs when you run the script directly.

if __name__ == "__main__":
    input_file = r"C:\Users\fake_user\python_files\addresses.csv" # Replace with an existing file path of a csv containing addresses
    output_file = r"C:\Users\fake_user\python_files\addresses_geocoded.csv" # Replace with an output file path
    api_key = 'xxxxxxxxxxxxxxxxx'  # Replace with your Google Maps geocoding API key
    
    process_csv(input_file, output_file, api_key)
    print("Geocoding complete. Results written to", output_file)


# In[ ]:




