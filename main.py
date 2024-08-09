import logging
import random


# https://docs.python.org/3/library/logging.html#logrecord-attributes
FORMAT = '%(name)s:%(levelname)s:%(asctime)s:%(message)s'

logging.basicConfig(
    level=logging.CRITICAL,
    filename="prod.log",
    filemode="a",
    format=FORMAT
)

logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)

handler = logging.FileHandler("staging.log", mode="a")
handler.setLevel(logging.CRITICAL)

formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.critical("Your CRITICAL message")  # 50
logger.error("Your ERROR message")  # 40
logger.warning("Your WARNING message")  # 30
logger.info("Your INFO message")  # 20
logger.debug("Your DEBUG message")  # 10
# NOTSET - 10

core_logger = logging.getLogger("core")
templatetags_logger = logging.getLogger("core.templatetags")
main_logger = logging.getLogger(__name__)

#####

FORMAT = "%(levelname)s - %(message)s C => DEBUG - 20 C"

logger = logging.getLogger()

handler = logging.FileHandler("battery_temperature.log", mode="a")
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)

logger.addHandler(handler)

#
temp = random.randint(20, 40)

for minute in range(60):
    if temp < 20:
        logger.DEBUG(temp)
    elif temp >= 30 and temp <= 35:
        logger.WARNING(temp)
    elif temp > 35:
        logger.CRITICAL(temp)
