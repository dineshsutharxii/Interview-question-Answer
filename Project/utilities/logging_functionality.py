import logging


class Logging:
    def logging_log(self, level = logging.DEBUG):
        # logger = logging.getLogger(__name__)
        # logger.setLevel(level)
        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler('..\Logs\logs.txt')

        logging.basicConfig(level=level,
                            format="%(asctime)s - %(levelname)s %(name)s: " + "Line: " + "%(lineno)d - %(message)s",
                            handlers=[console_handler, file_handler], datefmt="%Y-%m-%d %H:%M:%S")

        # logger.setLevel(level=logging.DEBUG)
        # Create handler (Console or file handler)
        # formater
        # console_formatter = logging.Formatter('%(filename)s - %(asctime)s - %(message)s',
        #                                       datefmt='%Y-%m-%d %H:%M:%S,uuu')
        file_formatter = logging.Formatter('%(filename)s : %(asctime)s : %(message)s')
        #setFormatter
        # console_handler.setFormatter(console_formatter)
        file_handler.setFormatter(file_formatter)
        # add handler to logger
        # logger.addHandler(console_handler)
        # logger.addHandler(file_handler)
        #
        logging.debug('Debug level - This message should go to the log file')
        logging.info('Info : So should this')
        logging.warning('Warning : And this, too')
        logging.error('Error : And non-ASCII stuff, too, like Øresund and Malmö')
        logging.critical("Critical: its critical error")


test_log = Logging()
test_log.logging_log()
