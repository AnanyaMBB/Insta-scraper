import requests
import json 
import os

directory = os.getcwd()

# parsed_files = [f"{jsonFile.split('-')[0]}.json" for jsonFile in os.listdir(directory + '/dataset/json_files') if jsonFile.endswith(".json") and jsonFile.split('-')[1].split('.')[0] == '10']
parsed_files_max = max([int(jsonFile.split('-')[0]) for jsonFile in os.listdir(directory + '/dataset/json_files') if jsonFile.endswith(".json") and jsonFile.split('-')[1].split('.')[0] == '10'], default=-1)
# print(parsed_files_max)
json_list = [jsonFile for jsonFile in os.listdir(directory + './dataset/unparsed_json') if jsonFile.endswith(".json") and int(jsonFile.split('.')[0]) > parsed_files_max] # and jsonFile not in parsed_files] # and int(jsonFile.split('.')[0]) > parsed_files_max]
json_list.sort(key=lambda x: int(x.split('.')[0]))

for json_file in json_list: 
    try:
        
        file_name_start = json_file.split('.')[0]
        with open(f'./dataset/unparsed_json/{json_file}', 'r', encoding='utf-8') as file:
            file = json.loads(file.read())
            nodes = file['data']['xdt_api__v1__clips__home__connection_v2']['edges']
            count = 0
            for node in nodes:
                video_url = node['node']['media']['video_versions'][0]['url']
                # print(f"Video URL: {video_url}")
                r = requests.get(video_url, allow_redirects=True)
                open(f'./dataset/video_files/{file_name_start}-{count}.mp4', 'wb').write(r.content)
                with open(f'./dataset/json_files/{file_name_start}-{count}.json', 'w', encoding='utf-8') as file:
                    file.write(json.dumps(node['node'], indent=4, ensure_ascii=False))
                count += 1
    except Exception:
        pass