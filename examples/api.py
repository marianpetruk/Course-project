import wbpy
from pprint import pprint


api = wbpy.IndicatorAPI()

iso_country_codes = ["GB", "FR", "JP"]
total_population = "SP.POP.TOTL"
dataset = api.get_dataset(total_population, iso_country_codes, date="2010:2012")

print(dataset, end='\n\n')
print(dataset.as_dict(), end='\n\n')

print(dataset.api_url, end='\n\n')

print(dataset.indicator_name, end='\n\n')
print(dataset.indicator_topics, end='\n\n')

print(dataset.countries, end='\n\n')


population_indicators = api.get_indicators(search="population")
print("There are now only " + str(len(population_indicators)) + " indicators to, browse!", end='\n\n')


health_topic_id = 8
health_indicators = api.get_indicators(search="population", topic=health_topic_id)
print("We've narrowed it down to " + str(len(health_indicators)) + " indicators!", end='\n\n')
print(health_indicators[list(health_indicators)[1]], end='\n\n')


countries = api.get_countries(search="united")
print(api.print_codes(countries), end='\n\n')

all_regions = api.get_regions()
all_sources = api.get_sources()
print("There are " + str(len(all_regions)) + " regions and " + str(len(all_sources)) + " sources.", end='\n\n')

pprint(api.search_results("debt", all_sources))
narrow_matches = api.get_topics(search="poverty")
wide_matches = api.get_topics(search="poverty", search_full=True)
print(str(len(narrow_matches)) + " topic(s) match(es) 'poverty' in the title field, and " + str(len(wide_matches)) + " topics match 'poverty' in all fields.", end='\n\n')

print(api.print_codes(api.NON_STANDARD_REGIONS), end='\n\n')

c_api = wbpy.ClimateAPI()

print(c_api.ARG_DEFINITIONS["instrumental_types"], end='\n\n')

print(c_api.ARG_DEFINITIONS["instrumental_intervals"], end='\n\n')

print(c_api.ARG_DEFINITIONS["modelled_types"], end='\n\n')

print(c_api.ARG_DEFINITIONS["modelled_intervals"], end='\n\n')

