import wbpy
from ADT.adt_class import Array2D


api = wbpy.IndicatorAPI()
iso_country_codes = ["UA", "PL"]


class Indicator(object):
    """A class representation of the indicator."""
    def __init__(self, indicator):
        self.indicator = indicator
        dataset = api.get_dataset(self.indicator, iso_country_codes, date="1990:2017")
        array = Array2D(27, 2)
        array[(0, 0)] = "UA"
        array[(0, 1)] = "PL"
        for i in range(1, 27):
            array[(i, 0)] = dataset.as_dict()['UA'][str(i-1+1990)]
            array[(i, 1)] = dataset.as_dict()['PL'][str(i-1+1990)]
        self.array = array

    def print_year(self, year, country):
        """
        Print indicator data of the given country for the given year.
        """
        country = 1 if country == 'PL' else 0
        try:
            string = "\n" + str(self.array[(year-1990+1, country)])
        except IndexError:
            string = "\nSorry, there is no data for " + str(year) + "."
        return string


def create_indicators():
    """
    Creates instances for the indicators.

    :return: a dict with names of the indicators as keys and their Indicator instances.
    """
    #                       Indicators                         #
    # ---------------------------------------------------------#
    #                   Economy and growth                     #
    # ---------------------------------------------------------#

    gdp = Indicator("NY.GDP.MKTP.CD")  # GDP (current US$)
    gdp_per_capita = Indicator("NY.GDP.PCAP.CD")  # GDP per capita (current US$)
    gross_savings = Indicator("NY.GNS.ICTR.ZS")  # Gross savings (% of GDP)
    inflation_gdp = Indicator("NY.GDP.DEFL.KD.ZG")  # Inflation, GDP deflator (annual %)
    imports = Indicator("NE.IMP.GNFS.ZS")  # Imports of goods and services (% of GDP)
    inflation_consumer_prices = Indicator("FP.CPI.TOTL.ZG")  # Inflation, consumer prices (annual %)
    gni = Indicator("NY.GNP.MKTP.PP.CD")  # GNI, PPP (current international $)

    # ---------------------------------------------------------#
    #                  Some other indicators                   #
    # ---------------------------------------------------------#

    total_population = Indicator("SP.POP.TOTL")  # total population indicator
    life_expectancy = Indicator("SP.DYN.LE00.IN")  # Life expectancy at birth, total (years)
    high_tech_exports = Indicator("TX.VAL.TECH.CD")  # High-technology exports (current US$)
    science_tech_articles = Indicator("IP.JRN.ARTC.SC")  # Scientific and technical journal articles

    return {'gdp': gdp, 'gdp_per_capita': gdp_per_capita, 'gross_savings': gross_savings,
            'inflation_gdp': inflation_gdp, 'imports': imports, 'inflation_consumer_prices': inflation_consumer_prices,
            'gni': gni, 'total_population': total_population, 'life_expectancy': life_expectancy,
            'high_tech_exports': high_tech_exports, 'science_tech_articles': science_tech_articles}


def main():
    indicators = create_indicators()
    print("-----Available indicators-----")
    for i in indicators:
        print("-", i)

    indicator = input("\nChoose the indicator: ")
    assert indicator in indicators.keys(), "Sorry, there is no such indicator."

    year = int(input("\nChoose the year (1990-2017): "))
    assert 1990 <= year <= 2017, "Year must be only in range from 1990 to 2017."

    country = input("\nEnter the country (UA, PL): ")
    assert country in ['UA', 'PL'], "Only PL or UA countries."

    print(indicators[indicator].print_year(year, country))


main()

