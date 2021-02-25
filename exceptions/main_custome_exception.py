


class VkaptureError(Exception):
    ''' This is custome vkapture error If you found this then All the best '''

    def __init__(self, message="", status_code= 400) -> None:
        self.message = message
        self.status_code = status_code