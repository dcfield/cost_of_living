# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from mock import MagicMock
from map.models.CalculationModel import CalculationModel
from map.models.DistanceCalculatorModel import DistanceCalculatorModel
from map import API_KEY


class CalculationModelTests(TestCase):

    # format_request_url()
    def test_formatRequestUrl_withString_returnUrl(self):
        postcode = "e14"

        correct_url = "http://api.zoopla.co.uk/api/v1/property_listings.xml?" \
                      + "postcode=" + postcode + "&listing_status=rent&api_key=" + API_KEY

        self.assertEqual(CalculationModel().format_request_url(postcode), correct_url)

    def test_formatRequestUrl_withInteger_returnUrl(self):
        postcode = 123

        correct_url = "http://api.zoopla.co.uk/api/v1/property_listings.xml?" \
                      + "postcode=" + str(postcode) + "&listing_status=rent&api_key=" + API_KEY

        self.assertEqual(CalculationModel().format_request_url(postcode), correct_url)

    def test_formatRequestUrl_withEmptyString_throwException(self):
        self.assertRaises(Exception, CalculationModel().format_request_url, "")

    # get_average_from_list()
    def test_getAverageFromList_withListOfIntegers_returnAverage(self):
        # GIVEN
        list_of_integers = [1, 2, 6, 7654, 35]

        # WHEN
        call_average = CalculationModel().get_average_from_list(list_of_integers)

        # THEN
        self.assertEqual(call_average, 1539.6)

    def test_getAverageFromList_withListOfFloats_returnAverage(self):
        # GIVEN
        list_of_floats = [1.0, 2.1, 6.23, 7654.004, 35.90]

        # WHEN
        call_average = CalculationModel().get_average_from_list(list_of_floats)

        # THEN
        self.assertEqual(call_average, 1539.8468)

    def test_getAverageFromList_withListOfValidStrings_returnAverage(self):
        # GIVEN
        list_of_strings = ["1.0", "56", "234"]

        # WHEN
        call_average = CalculationModel().get_average_from_list(list_of_strings)

        # THEN
        self.assertEqual(call_average, 97.0)

    def test_getAverageFromList_withListContainingInvalidString_throwValueError(self):
        # GIVEN
        list_of_strings = ['5', '1', 'number']

        # THEN
        self.assertRaises(ValueError,

                          # WHEN
                          CalculationModel().get_average_from_list,
                          list_of_strings
                          )


    def test_getAverageFromList_withListOfMixed_throwValueError(self):
        # GIVEN
        list_of_mixed = [234, 1, 'number']

        # THEN
        self.assertRaises(ValueError,

                          # WHEN
                          CalculationModel().get_average_from_list,
                          list_of_mixed
                          )

    def test_getAverageFromList_withEmptyList_returnZero(self):
        # GIVEN
        empty_list = []

        # WHEN
        call_average = CalculationModel().get_average_from_list(empty_list)

        # THEN
        self.assertEqual(call_average, 0)

    def test_convertXmlListToString_withEmptyList_returnEmptyList(self):
        # GIVEN
        empty_list = []

        # WHEN
        convert_to_string_list = CalculationModel().convert_xml_list_to_string(empty_list)

        # THEN
        self.assertFalse(convert_to_string_list)

    # format_double_with_separators
    def test_formatNumWithSeparators_withEmptyString_returnError(self):
        # GIVEN
        empty_string = ""

        # THEN
        self.assertRaises(ValueError,

                          # WHEN
                          CalculationModel().format_num_with_separators,
                          empty_string
                          )


    def test_formatNumWithSeparators_withDouble_returnStringWithCommas(self):
        # GIVEN
        test_double = 12345.678

        # WHEN
        formatted_double = CalculationModel().format_num_with_separators(test_double)

        # THEN
        self.assertEqual(formatted_double, "12,345.678")

    def test_formatNumWithSeparators_withInteger_returnStringWithCommas(self):
        # GIVEN
        test_int = 12345678

        # WHEN
        formatted_int = CalculationModel().format_num_with_separators(test_int)

        # THEN
        self.assertEqual(formatted_int, "12,345,678")


# class HomeToWorkCalculatorTests(TestCase):

    # calcaulate distance between 2 area codes
    # def test_getDistanceBetweenTwoPoints_withTwoValidPostcodes_returnDouble(self):
    #     # GIVEN
    #     postcode1 = 'EC1A 1BB'
    #     postcode2 = 'W1A 0AX'

    #     # WHEN
    #     DistCalcModel = DistanceCalculatorModel()
    #     DistCalcModel.get_distance_between_two_points = MagicMock(return_value = 5)
    #     distance = DistanceCalculatorModel().get_distance_between_two_points(postcode1, postcode2)

    #     # THEN
    #     self.assertEqual(distance, 5)

    # convert distance to cost of petrol

