# backend/src/utils/api_responses.py
from typing import Any, Dict
from fastapi import HTTPException
from fastapi.responses import JSONResponse

def success_response(data: Any = None, message: str = "Success", status_code: int = 200) -> JSONResponse:
    """
    Standardized success response
    """
    response_data = {
        "success": True,
        "message": message,
        "data": data
    }
    return JSONResponse(content=response_data, status_code=status_code)

def error_response(error: str, message: str = "Error occurred", status_code: int = 400) -> JSONResponse:
    """
    Standardized error response
    """
    response_data = {
        "success": False,
        "error": error,
        "message": message
    }
    return JSONResponse(content=response_data, status_code=status_code)

def not_found_response(item: str = "Item") -> HTTPException:
    """
    Standardized not found response
    """
    return HTTPException(
        status_code=404,
        detail=f"{item} not found"
    )

def unauthorized_response(message: str = "Unauthorized") -> HTTPException:
    """
    Standardized unauthorized response
    """
    return HTTPException(
        status_code=401,
        detail=message
    )

def forbidden_response(message: str = "Forbidden") -> HTTPException:
    """
    Standardized forbidden response
    """
    return HTTPException(
        status_code=403,
        detail=message
    )