import pytest
from src.tasks.tasks import get_data, get_updated_data


def test_request_for_data():
    data = get_updated_data()
    assert data is not False
    assert len(data) > 0
    assert "fields" in data

@pytest.mark.parametrize("data", [({},), ("skjbgss",), (124141,), ({"Error": 404})])
def test_listing_data_and_inserting_to_db(data):
    get_data(data)


if __name__ == "__main__":
    test_listing_data_and_inserting_to_db()
