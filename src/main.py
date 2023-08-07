from fastapi import FastAPI
from .managers import TextSearchManager
from fastapi.responses import JSONResponse


app = FastAPI()


@app.get("/api/textsearch/{word}")
def get_data_by_text_search(word: str = None):
    """
    get method to send query to db through models and get response or error

    Args:
        word (str, optional): a key-word for making a search in db. Defaults to None.
    """
    data = TextSearchManager().fetch(word)
    return [query.to_response for query in data]
