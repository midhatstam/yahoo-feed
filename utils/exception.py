class Error(Exception):
    code = -1
    description = None

    def __init__(self, description=None):
        self.description = description or self.description
        super().__init__(self.description)


# PROJECT RELATED EXCEPTIONS #
class ProjectError(Error):
    pass


class FeedNotAvailableError(ProjectError):
    description = 'Feed not available'
