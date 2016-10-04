import os
from pycrunchbase import CrunchBase

API_KEY = os.environ["crunchbaseapi_ACCESS_KEY_ID"]

cb = CrunchBase(API_KEY)

print cb
