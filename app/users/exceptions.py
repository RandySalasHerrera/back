from rest_framework.exceptions import APIException

# TODO: Refactorizar

class BaseAPIException(APIException):
    def response(self):
        return {"code_transaction": self.default_code, "message": self.default_detail}


class NotFoundData(BaseAPIException):
    status_code = 404
    default_detail = "No existen datos para la consulta"
    default_code = "DATA_DOES_NOT_EXIST"

class UserAlreadyRegister(BaseAPIException):
    status_code = 403
    default_detail = "Ya se encuentra registrada un usuario con el mismo nombre"
    default_code = "SESSION_ALREADY_REGISTER"
