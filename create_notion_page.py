import json
import os
from dotenv import load_dotenv
import base64
from notion.client import NotionClient

load_dotenv()

client = NotionClient(os.getenv("TOKEN_V2"))

def create_notion_page(event, _):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
        event (dict): Event payload.
        context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event["data"]).decode("utf-8")
    request_body = json.loads(pubsub_message)

    organization = request_body.get("organization")
    if organization is None:
        raise ValueError("Organization is required")

    database_id = request_body.get("database-id")
    if database_id is None:
        raise ValueError("Database ID is required")

    view_id = request_body.get("view-id")
    if view_id is None:
        raise ValueError("View ID is required")

    cv = client.get_collection_view(
        f"https://www.notion.so/{organization}/{database_id}?v={view_id}"
    )

    properties = request_body.get("properties") or []

    row = cv.collection.add_row()
    for prop in properties:
        row.set_property(prop["key"], prop["value"])
