__author__ = 'Dani'

from suds.client import Client

has_permissions = True
client = Client('http://156.35.95.75:8888?wsdl')

from application.wsservices.category_wsservice import CategoryWSService