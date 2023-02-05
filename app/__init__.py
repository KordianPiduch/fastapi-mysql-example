import logging

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)
LOG_FORMATTER = logging.Formatter("%(name)s :: %(levelname)s :: %(message)s")
CONSOLE_HANDLER = logging.StreamHandler()
CONSOLE_HANDLER.setFormatter(LOG_FORMATTER)
LOGGER.addHandler(CONSOLE_HANDLER)

logging.getLogger("mysql.connector.authentication").setLevel(logging.ERROR)