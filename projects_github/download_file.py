import requests
url="URLHERE.Txt"

response=requests.get(url)

if response.status_code == 200:
    file_content=response.text
    local_file_path="input.txt"

    with open(local_file_path,"w",encoding="utf-8") as local_file:
        local_file.write(file_content)

    print(f"File saved as {local_file_path}")
else:
    print(f"Failed to download file. Status code: {response.status_code}")