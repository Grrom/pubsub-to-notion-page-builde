import json
import os

from requests import Request

from dotenv import load_dotenv

from main import create_notion_page


load_dotenv()

test_body = {
    "organization": os.getenv("TEST_NOTION_ORGANIZATION"),
    "database-id": os.getenv("TEST_NOTION_DATABASE_ID"),
    "view-id": os.getenv("TEST_NOTION_VIEW_ID"),
    "properties": [
        {
            "key": "Name",
            "value": "test doc",
        },
    ],
    "children": [
        {
            "type": "text",
            "content": "This is a test document",
        },
    ],
}

request = Request(
    method="POST",
    url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    headers={
        "Content-Type": "application/json",
    },
    data=json.dumps(test_body),
)

create_notion_page(request)
