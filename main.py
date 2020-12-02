
#Imports
from notion.client import NotionClient
import random
import smtplib
import requests

#Create array of entries
all_entries = []

#Set up notion client
#replace your_token with a valid notion v2 token - can be found in cookies
client = NotionClient(token_v2="your_token")

#Get table from notion
#replace your_page_url with the url of a notion page containing a table
cv = client.get_collection_view("your_page_url")

#Add text of each row to entries array
for row in cv.collection.get_rows():
  all_entries.append(row.title)

#Display random sample of 3 entries for testing
random_sample = random.sample(all_entries, 3)
test = ""
for entry in random_sample:
  test = test + entry + "\n" + "\n"
print(test)

#Send to Readwise
#Replace XXX with your Readwise token
token = "Token XXX"

for entry in all_entries:
  data = {
        "highlights": [{
            "text": entry,
            "title": "Thoughts",
            "author": "Me",
            "source_type": "book",
           
        }]
    }
  requests.post(
    url="https://readwise.io/api/v2/highlights/",
    headers={"Authorization": token},
    json= data
)

  
  




