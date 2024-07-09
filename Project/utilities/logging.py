import logging

class Logging:
    def logger(self):
        #create logger
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        # Create handler (Console or file handler)
        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler('..\Project\Logs\logs.log')
        # formater
        console_formatter = logging.Formatter('%(filename)s - %(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S,uuu')
        file_formatter = logging.Formatter('%(filename)s : %(asctime)s : %(message)s')
        #add handler to logger
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
        #
        logging.debug('Debug level - This message should go to the log file')
        logging.info('Info : So should this')
        logging.warning('Warning : And this, too')
        logging.error('Error : And non-ASCII stuff, too, like Øresund and Malmö')

