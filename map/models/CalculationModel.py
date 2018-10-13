# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import map.utils
from map import API_KEY


class CalculationModel():

    def get_average_price_of_area(self, postcode):
        rental_prices_per_month = self.list_of_rental_prices_per_month_for_postcode(postcode)
        list_of_rental_prices_per_month = self.convert_xml_list_to_string(rental_prices_per_month)
        average_rent_price = self.get_average_from_list(list_of_rental_prices_per_month)
        # format_average_rent_price = self.format_double_with_separators(average_rent_price)

        return average_rent_price

    def convert_xml_list_to_string(self, xml_list):
        final_list = []
        for element in xml_list:
            final_list.append(element.text)

        return final_list

    def get_average_from_list(self, my_list):
        total = 0

        for l in my_list:
            cast_to_float = float(l)
            total = total + cast_to_float

        if len(my_list) == 0:
            return 0

        average = total / len(my_list)
        return round(average, 4)

    def format_num_with_separators(self, num):
        return "{:,}".format(num)

    # Returns xml object response for given postcode
    def create_xml_object_with_response_from_request(self,postcode):
        url = self.format_request_url(postcode)

        contents =  map.utils.response_from_url(url)

        return map.utils.parse_xml_content(contents)

    # Returns list of all monthly rental prices
    def list_of_rental_prices_per_month_for_postcode(self, postcode):
        xml_object = self.create_xml_object_with_response_from_request(postcode)

        rental_prices_per_month = xml_object.findall(
            'listing/rental_prices/per_month')

        return rental_prices_per_month

    # Formats the URL GET request
    def format_request_url(self, postcode):

        if postcode is "":
            raise Exception('Postcode is empty')

        request_url = "http://api.zoopla.co.uk/api/v1/property_listings.xml?" \
                      + "postcode=" + str(postcode) + "&listing_status=rent&api_key=""" + API_KEY

        return request_url
