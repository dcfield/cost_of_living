# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import urllib2

from django.shortcuts import render
from django.shortcuts import redirect
from map.models import CalculationModel


# Create your views here.
def index(request):

    data = {
        'action': 'Enter areacode.'
    }

    return render(request, 'map/index.html', data)


# /map/calculate
def map_calculate(request):
    calculation_model = CalculationModel.CalculationModel()

    # Try 'e14' as postcode to test
    postcode = request.POST.get('postcode', '')

    try:
        average_price_of_area = calculation_model.get_average_price_of_area(postcode)

        data = {
            'result': average_price_of_area,
            'postcode': postcode
        }

        return render(request, 'map/calculate.html', data)

    except urllib2.HTTPError:
        data = {
            'action': 'That was a bad request. Please try again.'
        }

        return render(request, 'map/index.html', data)


# /map/bad_request
def map_bad_request(request):
    calculation_model = CalculationModel.CalculationModel()

    data = {
        'error_message': 'Error 400. Try again with a valid areacode. eg. e14'
    }

    return render(request, 'map/bad_request.html', data)
