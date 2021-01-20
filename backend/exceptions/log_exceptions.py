class LogNotFoundException(Exception):
    def __init__(self):
        super().__init__('The Log was not found.')
