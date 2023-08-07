from dataclasses import dataclass

@dataclass(frozen=True)
class TextSearch:
    """
    _summary_

    Returns:
        _type_: _description_
    """
    id: int
    first_name: str
    last_name: str
    email: str

    @property
    def to_response(self) -> dict:
        """
        _summary_

        Returns:
            dict: _description_
        """        
        return self.__dict__