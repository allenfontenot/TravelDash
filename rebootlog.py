#!/usr/bin/env python

from datetime import datetime
import settings
import logging
from sendmail import *


store = settings.NSN

logging.basicConfig(filename = 'debug.log', level = logging.DEBUG)

logging.debug(str(datetime.now()) + " rebooting")
sendmail("rebooting",0,0,store,5)
