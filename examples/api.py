#import urllib.request
#import urllib.parse
# import json
# import xml.etree.ElementTree as ET

import wbpy
from pprint import pprint

api = wbpy.IndicatorAPI()

iso_country_codes = ["UA"]
total_population = "SP.POP.TOTL"

dataset = api.get_dataset(total_population, iso_country_codes, date="2010:2017")
print(dataset.as_dict())
