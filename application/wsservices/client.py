from suds.client import Client

__author__ = 'Dani'

has_permissions = True


def get_client():
    return Client('http://156.35.95.75:8888?wsdl')
