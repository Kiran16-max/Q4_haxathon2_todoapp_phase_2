from datetime import datetime
from typing import Any
import json


def convert_datetime_to_string(obj: Any) -> Any:
    """
    Recursively convert datetime objects to ISO format strings in a data structure.
    """
    if isinstance(obj, dict):
        return {key: convert_datetime_to_string(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [convert_datetime_to_string(item) for item in obj]
    elif isinstance(obj, datetime):
        return obj.isoformat()
    else:
        return obj


def jsonable_encoder_with_datetime(obj: Any) -> Any:
    """
    Convert an object to a JSON-serializable format, handling datetime objects.
    """
    converted_obj = convert_datetime_to_string(obj)
    return converted_obj