import sys
import requests

from celery_main import celery_app
from typing import Dict, Any

sys.path.insert(0, "C:\\Users\\steve\\Works Projects\\contact-list-testing\\src")
from managers import ApplicationsManager


def get_updated_data() -> Dict[str, Any]:
    """
    func for getting data for updating

    Returns:
        Dict[str, Any]: json type data
    """
    data = requests.get(
        "https://api.nimble.com/api/v1/contacts/",
        headers={"Authorization": "Bearer NxkA2RlXS3NiR8SKwRdDmroA992jgu"},
    )
    return data.json()


def get_data(
    data: Dict[str, Any] = get_updated_data(),
    make_insert: ApplicationsManager = ApplicationsManager(),
):
    """
    func for getting manipulation with data

    Args:
        data (Dict[str, Any], optional): data from requests to parse. Defaults to get_updated_data().
        make_insert (ApplicationsManager, optional): access to db with data that need to get changed. Defaults to ApplicationsManager().
    """
    fields = [
        dict([j for j in fields["fields"].items() if len(fields["fields"]) > 4])
        for fields in data["resources"]
    ]

    for _id, data in enumerate(fields, start=10):
        if data.get("email") and data.get("first name") and data.get("last name"):
            first_name, last_name, email = (
                data["first name"][0]["value"],
                data["last name"][0]["value"],
                data["email"][0]["value"],
            )
            make_insert.commit(_id, first_name, last_name, email)


@celery_app.task
def make_updates() -> str:
    """
    func for run task

    Returns:
        str: msg about finishing your task!
    """
    print("Taks has started")
    get_data()
    return "Data has been changed!"
