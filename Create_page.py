import requests
from Cred import HEADERS, NOTION_ENDPOINT 


page_id = "17d9fa5e9b43803f80f7e3fedbb6960d"
url = f"https://api.notion.com/v1/databases/{page_id}/query"

#url = f"{NOTION_ENDPOINT}/database/{page_id}/query"

data = {
    'parent': {'page_id' : page_id},
    'properties': {
        'title' : [
            {
                'text':{
                    'content' : 'wasupppppp'
                }
            }
        ]
    }
}

response = requests.post(url, headers=HEADERS,json=data)

# Check the response
if response.status_code == 200:
    print("Page created successfully!")
    print(response.json())
else:
    print("Failed to create page")
    print(f"Status Code: {response.status_code}")
    print(response.json())

print (url)

