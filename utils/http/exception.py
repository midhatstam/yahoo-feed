from utils.exception import ProjectError, Error


class HttpError(ProjectError):
    # http errors starts with 2
    code = 20000
    http_code = None
    description = "Base HTTP Exception"

    def __init__(self, response=None):
        self.response = response
        super().__init__(self.__get_message(response))

    @classmethod
    def __get_message(cls, response):
        return f"{response.status_code}: {response.content}"


class UniqueConstraintFailed(Error):
    code = 20401
    http_code = 400
