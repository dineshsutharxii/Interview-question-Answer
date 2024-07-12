import logging


class Logging:
    def __init__(self):
        self.file_formatter = None
        self.console_formatter = None
        self.logger = None
        self.file_handler = None
        self.console_handler = None

    def custom_logger(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.console_handler = logging.StreamHandler()  # Handler for console
        self.console_handler.setLevel(logging.DEBUG)  # setLevel to handler
        self.file_handler = logging.FileHandler(r'C:\Users\dines\Learn And Interview\Interview_question_answer\Project\Logs\logs.txt')  # Handler for file
        self.file_handler.setLevel(logging.DEBUG)  # setLevel to handler
        self.console_formatter = logging.Formatter(fmt='%(filename)s - %(asctime)s - %(message)s',
                                                   datefmt='%d-%m-%Y %H:%M:%S')
        self.file_formatter = logging.Formatter(fmt='%(filename)s - %(asctime)s - %(message)s',
                                                datefmt='%d-%m-%Y %H:%M:%S')
        self.console_handler.setFormatter(self.console_formatter)  # add Formatter to handler
        self.file_handler.setFormatter(self.file_formatter)  # add Formatter to handler
        self.logger.addHandler(self.console_handler)  # added handler to logger
        self.logger.addHandler(self.file_handler)  # added handler to logger
        return self.logger
