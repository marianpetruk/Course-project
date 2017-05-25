import wbpy
from ADT.arrays import *


api = wbpy.IndicatorAPI()
iso_country_codes = ["UA", "PL"]


class indicator_adt(object):
    def __init__(self, name):
        self.array = Array2D(27, 2)
        dataset = api.get_dataset(name, iso_country_codes, date="1990:2017")
        self.url = dataset.api_url
        self.name = dataset.indicator_name
        self.array[(0, 0)] = "UA"
        self.array[(0, 1)] = "PL"
        for i in range(1, 27):
            self.array[(i, 0)] = dataset.as_dict()['UA'][str(i - 1 + 1990)]
            self.array[(i, 1)] = dataset.as_dict()['PL'][str(i - 1 + 1990)]

    def indicator_name(self):
        """
        Returns the name of the indicator.
        :return: name in str format.
        """
        return self.name

    def country_codes(self):
        """
        Returns the iso codes of the countries.
        :return: iso codes in str format.
        """
        return " ".join(iso_country_codes)

    def indicator_api_url(self):
        """
        Returns the url of the api request for the indicator.
        :return: url in str type.
        """
        return self.url

    def get_array(self):
        """
        Returns the array with indicator data.
        :return: 2d array.
        """
        return self.array

    def __str__(self):
        """
        For print() function.
        Converts the ADT into str.
        :return: string to print
        """
        string = "\n\tIndicator " + self.name + "\n"
        for i in range(0, self.array.num_rows()):
            string += str(i - 1 + 1990) + " year: " if i > 0 else ""
            string += "\t\t\t" if i == 0 else ""
            for j in range(0, self.array.num_cols()):
                string += "\t\t\t" if (i == 0 and j == 1) else ""
                string += str(self.array[(i, j)]) + " "
            string += "\n"
        return string[1:]

    def print_year(self, year, country):
        """
        Returns indicator data of the given country for the given year.        """
        country = 1 if country == 'PL' else 0
        try:
            string = "\n" + str(self.array[(year-1990+1, country)])
        except IndexError:
            string = "\nSorry, there is no data for " + str(year) + "."
        return string

    def array_2_list(self, country):
        """
        Returns the list with indicator data of the given country 
        from the array.
        :param country: UA or PL.
        :return: list with data.
        """
        list_data = []
        assert type(country) == str, "Country argument must be 'PL' or 'UA'."
        country_id = 1 if country == "PL" else 0
        for i in range(1, 27):
            list_data.append(self.array[(i, country_id)])
        return list_data