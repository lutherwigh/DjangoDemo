import leancloud
import logging

APP_ID = ''
APP_KEY = ''

leancloud.init(APP_ID,APP_KEY)
logging.basicConfig(level=logging.DEBUG)

ping "API_BASE_URL"