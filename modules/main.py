from ADT.adt_class import *


def create_indicators():
    """
    Creates instances for the indicators.

    :return: a dict with names of the indicators as keys and their Indicator instances.
    """
    #                       Indicators                         #
    # ---------------------------------------------------------#
    #                   Economy and growth                     #
    # ---------------------------------------------------------#

    gdp = indicator_adt("NY.GDP.MKTP.CD")  # GDP (current US$)
    gdp_per_capita = indicator_adt("NY.GDP.PCAP.CD")  # GDP per capita (current US$)
    gross_savings = indicator_adt("NY.GNS.ICTR.ZS")  # Gross savings (% of GDP)
    inflation_gdp = indicator_adt("NY.GDP.DEFL.KD.ZG")  # Inflation, GDP deflator (annual %)
    imports = indicator_adt("NE.IMP.GNFS.ZS")  # Imports of goods and services (% of GDP)
    inflation_consumer_prices = indicator_adt("FP.CPI.TOTL.ZG")  # Inflation, consumer prices (annual %)
    gni = indicator_adt("NY.GNP.MKTP.PP.CD")  # GNI, PPP (current international $)

    # ---------------------------------------------------------#
    #                  Some other indicators                   #
    # ---------------------------------------------------------#

    total_population = indicator_adt("SP.POP.TOTL")  # total population indicator
    life_expectancy = indicator_adt("SP.DYN.LE00.IN")  # Life expectancy at birth, total (years)
    high_tech_exports = indicator_adt("TX.VAL.TECH.CD")  # High-technology exports (current US$)
    science_tech_articles = indicator_adt("IP.JRN.ARTC.SC")  # Scientific and technical journal articles

    return {'gdp': gdp, 'gdp_per_capita': gdp_per_capita, 'gross_savings': gross_savings,
            'inflation_gdp': inflation_gdp, 'imports': imports, 'inflation_consumer_prices': inflation_consumer_prices,
            'gni': gni, 'total_population': total_population, 'life_expectancy': life_expectancy,
            'high_tech_exports': high_tech_exports, 'science_tech_articles': science_tech_articles}


def data_by_year():
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

def plot_graph():
    import matplotlib.pyplot as plt
    import numpy as np

    indicators = create_indicators()

    print("-----Available indicators-----")
    for i in indicators:
        print("-", i)

    indicator = input("\nChoose the indicator: ")
    assert indicator in indicators.keys(), "Sorry, there is no such indicator."

    fig, ax = plt.subplots()
    fig.suptitle(indicators[indicator].indicator_name(), fontsize=14, fontweight='bold')
    line1, = ax.plot(indicators[indicator].array_2_list("UA"), label="Ukraine")
    line2, = ax.plot(indicators[indicator].array_2_list("PL"), label="Poland")
    plt.legend(handles=[line1, line2])
    plt.ylabel('Indicator data')
    plt.xlabel('Years')
    plt.show()



def main():

    print("You have two options:\n- type 1 if you want to plot a graph for an indicator;\n- type 2 if you want to get "
          "data for a particular year.")
    choice = int(input("\nPlease make your decision: "))
    if choice == 1:
        plot_graph()
    elif choice == 2:
        data_by_year()







main()

