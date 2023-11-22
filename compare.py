import json
import os
import hashlib

# Get the current working directory
directory = os.getcwd()

# To store the content of the JSON files
json_contents = dict()

# Iterate through every file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        filepath = os.path.join(directory, filename)
        
        # Read the JSON file
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = json.load(file)
                
                # Create a hash of the content for efficient comparison
                content_hash = hashlib.sha256(json.dumps(content, sort_keys=True).encode()).hexdigest()
                
                if content_hash in json_contents:
                    json_contents[content_hash].append(filename)
                else:
                    json_contents[content_hash] = [filename]
                    
        except json.JSONDecodeError:
            print(f"Error decoding JSON in file: {filename}")
        except UnicodeDecodeError:
            print(f"Error with character encoding in file: {filename}")

# Print groups of identical non-unique JSON files
for content_hash, filenames in json_contents.items():
    if len(filenames) > 1:  # If there are duplicates
        print(", ".join(filenames))
