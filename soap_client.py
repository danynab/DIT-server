__author__ = 'mvidalgarcia'

from suds.client import Client

has_permissions = True
c = Client('http://156.35.95.75:8000?wsdl')

print(c.service.get_all_category())
