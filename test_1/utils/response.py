# 状态码
class ReturnCode:
    BROKEN_AUTHORIZED_DATA = -501
    RESOURUCES_NOT_EXISTS = None
    RESOURUCES_NOT_FOUND = -102
    SUCCESS = 0
    FAILED = -100
    UNAUTHORIZED = -500
    WRONG_PARMAS = -101

    @classmethod
    def message(cls, code):
        if code == cls.SUCCESS:
            return 'success'
        elif code == cls.FAILED:
            return 'failed'
        elif code == cls.UNAUTHORIZED:
            return 'unauthorizwd'
        elif code == cls.WRONG_PARMAS:
            return 'wrong params'
        elif code == cls.RESOURUCES_NOT_FOUND:
            return 'resources not found'


def wrap_json_response(data=None, code=None, message=None):
    response = {}
    if not code:
        code = ReturnCode.SUCCESS
    if not message:
        message = ReturnCode.message(code)
    if data is not None:
        response['data'] = data
    response['result_code'] = code
    response['message'] = message
    return response


class CommonResponseMixin(object):
    @classmethod
    def wrap_json_response(cls,data=None, code=None, message=None):
        response = {}
        if not code:
            code = ReturnCode.SUCCESS
        if not message:
            message = ReturnCode.message(code)
        if data is not None:
            response['data'] = data
        response['result_code'] = code
        response['message'] = message
        return response