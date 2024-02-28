import os
import json

# Specify the directory containing the JSON files, use '.' for the current directory
directory = '.'

# Iterate through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.json'):  # Check if the file is a JSON file
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as file:
            data = json.load(file)
            
            # Modify the image URL by removing '/tree'
            if 'image' in data and '/tree' in data['image']:
                data['image'] = data['image'].replace('/tree', '')
                
                # Save the modified data back to the same file
                with open(filepath, 'w') as file:
                    json.dump(data, file, indent=4)

print("Completed modifying the image links in JSON files.")
