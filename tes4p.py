#-*- coding:utf8 -*-
import log4p
logger = log4p.GetLogger(__name__)
log = logger.logger
log.debug("debug information")
log.info("nfo text")
log.error("Error Message")
log.warning("Warning Message")