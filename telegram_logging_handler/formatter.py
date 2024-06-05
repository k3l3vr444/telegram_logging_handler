import logging


class TelegramFormatter(logging.Formatter):
    def __init__(self, fmt=None, datefmt=None, style='%', app_name: str = "MyApp"):
        super().__init__(fmt, datefmt, style)
        self.app_name = app_name

    def format(self, record):
        record.app_name = self.app_name
        return super().format(record)
