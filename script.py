import requests

# Notion API credentials
NOTION_TOKEN = "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"
DB_MAIL_ID = "17d9fa5e9b43803f80f7e3fedbb6960d"

# API endpoint and headers
URL = "https://api.notion.com/v1/databases/" + DB_MAIL_ID + "/query"
HEADERS = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

# Function to fetch data
def fetch_notion_data():
    # Send POST request to Notion API
    response = requests.post(URL, headers=HEADERS)

    # Check if the response is successful
    if response.status_code == 200:
        # Convert response body to Python dictionary
        data = response.json()

        # Check if 'results' exists in the response
        if "results" in data:
            results = data["results"]  # Get the list of database entries
        else:
            results = []  # Default to an empty list if 'results' is not found

        # Loop through each result in the database
        for result in results:
            # Get the properties of the current entry
            props = result["properties"]

            # Extract the Title
            if "Title" in props:
                title_data = props["Title"]
                if "rich_text" in title_data and len(title_data["rich_text"]) > 0:
                    title = title_data["rich_text"][0]["text"]["content"]
                else:
                    title = "No Title"
            else:
                title = "No Title"

            # Extract the URL
            if "URL" in props:
                url_data = props["URL"]
                if "title" in url_data and len(url_data["title"]) > 0:
                    url = url_data["title"][0]["text"]["content"]
                else:
                    url = "No URL"
            else:
                url = "No URL"

            # Print the Title and URL
            print("Title:", title)
            print("URL:", url)
    else:
        # If the request failed, print the error code
        print("Failed to fetch data. Status code:", response.status_code)
        print("Error message:", response.text)

# Run the function
fetch_notion_data()