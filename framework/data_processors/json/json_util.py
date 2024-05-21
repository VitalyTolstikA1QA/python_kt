import json


def get_value(response: json, field: str) -> str:
    return response.get(field)
