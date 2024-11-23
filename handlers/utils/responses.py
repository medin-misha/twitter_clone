from typing import Any, Dict


def error_response(msg: str, err_type: int) -> dict[str, bool | str]:
    response = {"result": False, "error_message": f"{msg}", "error_type": f"{err_type}"}
    return response


def ok_response(
    resp: Any, name: str
) -> dict[str, bool | Any]:
    response = {"result": True}
    return response | {f"{name}": resp} if resp is not None else response
