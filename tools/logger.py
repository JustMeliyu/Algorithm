# -*-coding:utf-8-*- 

"""
Author: Road36
Date: 19-5-8
"""

import logging
from logging.handlers import TimedRotatingFileHandler
from logging import Formatter

numeric_level = getattr(logging, "INFO", None)
if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level:%s' % "LOG_LEVEL")

formatter = Formatter('%(asctime)s|%(levelname)s|%(module)s|%(process)d|system|%(funcName)s||success||%(message)s|',
                      '%Y-%m-%d %H:%M:%S')
logging.basicConfig(level=numeric_level)
logger = logging.getLogger("Algorithm")
timeRotatingHandler = TimedRotatingFileHandler('../%s.log' % "Algorithm", when='midnight')
timeRotatingHandler.setFormatter(formatter)
timeRotatingHandler.suffix = "_%Y%m%d.log"
logger.addHandler(timeRotatingHandler)
