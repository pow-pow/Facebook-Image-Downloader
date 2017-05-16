'''
Created on 13 May 2017

@author: pow-pow
'''

from pageaccess import PageAccess

# Page name (found in URL)
PAGE = "CHANGEME"

# Page album from which to download images
ALBUM = "Timeline Photos"

# Directory in which to store images
IMG_DIR = "images"

# Minimum number of likes an image should have
MIN_LIKES = 0

# Facebook app credentials
app_id = "CHANGEME"
app_secret = "CHANGEME"
TOKEN = app_id + "|" + app_secret

p = PageAccess(PAGE, ALBUM, IMG_DIR, MIN_LIKES, TOKEN)
p.start()
