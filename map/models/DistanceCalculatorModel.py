# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
import urllib2


class DistanceCalculatorModel():

    def get_distance_between_two_points(self, postcode1, postcode2):
        url = 'http://router.project-osrm.org/route/v1/driving/13.388860,52.517037;13.397634,52.529407;13.428555,52.523219?overview=false'
        response = urllib2.urlopen(url)
        html = response.read()
        print html

        return False

DistanceCalculatorModel().get_distance_between_two_points('EC1A 1BB', 'W1A 0AX')