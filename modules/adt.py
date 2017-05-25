from ADT.adt_class import *


def main():
    #                       Indicators                         #
    # ---------------------------------------------------------#
    #                   Economy and growth                     #
    # ---------------------------------------------------------#

    gdp = "NY.GDP.MKTP.CD"  # GDP (current US$)
    gdp_per_capita = "NY.GDP.PCAP.CD"  # GDP per capita (current US$)
    gross_savings = "NY.GNS.ICTR.ZS"  # Gross savings (% of GDP)
    inflation_gdp = "NY.GDP.DEFL.KD.ZG"  # Inflation, GDP deflator (annual %)
    imports = "NE.IMP.GNFS.ZS"  # Imports of goods and services (% of GDP)
    inflation_consumer_prices = "FP.CPI.TOTL.ZG"  # Inflation, consumer prices (annual %)
    gni = "NY.GNP.MKTP.PP.CD"  # GNI, PPP (current international $)

    # ---------------------------------------------------------#
    #                  Some other indicators                   #
    # ---------------------------------------------------------#

    total_population = "SP.POP.TOTL" # total population indicator
    life_expectancy = "SP.DYN.LE00.IN"  # Life expectancy at birth, total (years)
    high_tech_exports = "TX.VAL.TECH.CD"  # High-technology exports (current US$)
    science_tech_articles = "IP.JRN.ARTC.SC"  # Scientific and technical journal articles

    indicator1 = indicator_adt(total_population)
    print("Current indicator:", indicator1.indicator_name())
    print("Api URL of the indicator:", indicator1.indicator_api_url())
    print("Iso codes of countries in the indicator:", indicator1.country_codes())
    print(indicator1)

    indicator2 = indicator_adt(life_expectancy)
    print("Current indicator:", indicator2.indicator_name())
    print("Api URL of the indicator:", indicator2.indicator_api_url())
    print("Iso codes of countries in the indicator:", indicator2.country_codes())
    print(indicator2)

    print(type(indicator2.get_array()))

main()
