from typing import Any, Dict


def error_response(msg: str, err_type: int) -> dict[str, bool | str]:
    response = {"result": False, "error_message": f"{msg}", "error_type": f"{err_type}"}
    return response


def ok_response(resp: dict[Any]) -> dict[bool, Any]:
    response = {"result": True}
    response.update(resp)
    return response
