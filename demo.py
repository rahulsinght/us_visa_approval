from us_visa.logger import logging
from us_visa.exception import Usvisaexception
import sys

logging.info('shows some info at logging file')

try:
    a = 10 / '2'
except Exception as e:
    raise Usvisaexception(e, sys) from e