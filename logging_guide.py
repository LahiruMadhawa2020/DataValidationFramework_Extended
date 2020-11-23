import logging

# log_format = "%(asctime)s::%(levelname)s::%(name)s::"\
#              "%(filename)s::%(lineno)d::%(message)s"
log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
# logging.basicConfig(filename='mylogs.log', level='DEBUG', format=log_format)
logging.basicConfig(filename='mylogs.log', filemode='w', level='DEBUG', format=log_format)

# logger = logging.getLogger(__name__)

# To override the default severity of logging
# logger.setLevel('DEBUG')

# Use FileHandler() to log to a file
# file_handler = logging.StreamHandler()
# formatter = logging.Formatter(log_format)
# file_handler.setFormatter(formatter)
#
# # Don't forget to add the file handler
# logger.addHandler(file_handler)
# logger.info("I am a separate Logger")

logging.debug("This is a debug message")
logging.info("This is an informational message")
logging.warning("Careful! Something does not look right")
logging.error("You have encountered an error")
logging.critical("You are in trouble")
