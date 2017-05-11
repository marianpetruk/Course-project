import wbpy
from modules.ADT.adt_class import Array2D

api = wbpy.IndicatorAPI()
iso_country_codes = ["UA", "PL"]


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

    dataset = api.get_dataset(total_population, iso_country_codes, date="1990:2017")
    # print(dataset, end='\n\n')
    print(dataset.as_dict(), end='\n\n')
    # print(dataset.api_url, end='\n\n')
    # print(dataset.indicator_name, end='\n\n')

    # GDP using 2D_Array ADT
    gdp_2d_array = Array2D(27, 2)
    gdp_2d_array[(0, 0)] = "UA"
    gdp_2d_array[(0, 1)] = "PL"
    print("Num of rows in the gdp_2d_array =", gdp_2d_array.num_rows())
    print("Num of columns in the gdp_2d_array =", gdp_2d_array.num_cols())
    for i in range(1, 27):
        gdp_2d_array[(i, 0)] = dataset.as_dict()['UA'][str(i-1+1990)]
        gdp_2d_array[(i, 1)] = dataset.as_dict()['PL'][str(i-1+1990)]
    print(gdp_2d_array)


main()
