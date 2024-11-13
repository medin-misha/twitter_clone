from typing import Any, Dict


def error(msg: str, err_type: str) -> dict[str, bool | str]:
    """
    Функция принимающая которая возвращает сообщение об ошибке:
        msg в качестве сообщения
        err_type в качестве типа ошибки (statuscode)
    Возвращает понятный для фронтенда dict который будет выводиться конечному пользователю.
    """
    response = {
        "result": False,
        "error_message": f"{msg}",
        "error_type": f"{err_type}"
    }
    return response


def frontend_response(resp: dict[Any]) -> dict[bool, Any]:
    """
    Функция задача которой возвращать ответы фронтенду.
    Пока что она очень простая и просто добавляет к ответу result = True.
    Принимает ответ сервера resp
    """
    response = {"result": True}
    response.update(resp)
    return response
