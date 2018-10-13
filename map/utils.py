import re
import urllib2
import webbrowser
from xml.etree import ElementTree
from django.http import HttpResponseRedirect


def validate_areacode(outward_code):
    if isinstance(outward_code, int):
        raise Exception("Please enter a string")

    if len(outward_code) > 4:
        raise Exception("The outward code is too long. Please provide a correct outward code.")

    if len(outward_code) is 0:
        raise Exception("Please provide an outward code.")
    return outward_code


def parse_xml_content(content):
    parsed_xml = ElementTree.fromstring(content)
    return parsed_xml


def response_from_url(url):
    return urllib2.urlopen(url).read()


def display_error_page():
    return HttpResponseRedirect("/map/bad_request")
    # webbrowser.open('/map/bad_request')
