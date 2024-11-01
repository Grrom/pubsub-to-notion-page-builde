import base64
import datetime
import json
import os

from dotenv import load_dotenv

from main import create_notion_page


load_dotenv()

test_message = {
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
# when using this test message as a json, make sure you update True to true, as True is only for python

base64_message = base64.b64encode(json.dumps(test_message).encode("utf-8"))

create_notion_page({"data": base64_message}, None)
