import datetime
import json
import os
from dotenv import load_dotenv
from notion.client import NotionClient

load_dotenv()

client = NotionClient(os.getenv("TOKEN_V2"))


def create_notion_page(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_body = json.loads(request.data)

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
    children = request_body.get("children") or []

    row = cv.collection.add_row()

    for child in children:
        row.children.add_new(child["type"], title=child["content"])

    for property in properties:
        property_row = next(
            (prop for prop in row.schema if prop["name"] == property["key"]), None
        )
        if property_row is None:
            raise ValueError(f"Property {property['key']} not found")

        if property_row["type"] == "date":
            row.set_property(
                property["key"],
                datetime.datetime.strptime(property["value"], "%m-%d-%Y"),
            )
            continue

        if property_row["type"] == "number":
            row.set_property(property["key"], float(property["value"].replace(",", "")))
            continue

        row.set_property(property["key"], property["value"])

    return "Success"
