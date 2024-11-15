from typing import Any, Dict


def error_response(msg: str, err_type: int) -> dict[str, bool | str]:
    response = {"result": False, "error_message": f"{msg}", "error_type": f"{err_type}"}
    return response


def ok_response(
    resp: dict[Any] | list, name: str
) -> dict[str, bool | dict[Any] | list]:
    response = {"result": True}
    return response | {f"{name}": resp}
