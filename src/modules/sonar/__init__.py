import urllib
import urllib2
import logging
import json
import sonar.rest

class Rule(object):

    def __init__(self, data):
        self.data = data

    @property
    def name(self):
        '''Returns a one sentence name of the problem.
        '''
        return self.data['name']

class Resource(object):

    def __init__(self, data):
        self.data = data

    @property
    def key(self):
        return self.data['key']

    @property
    def name(self):
        '''
        Example value: ComponentProfilerStubImpl
        '''

        return self.data['name']

class Violation(object):

    def __init__(self, data):
        self.data = data

    @property
    def id(self):
        return self.data['id']

    @property
    def rule(self):
        return Rule(self.data['rule'])

    @property
    def message(self):
        '''Returns a detailed message of the problem.
        '''
        return self.data['message']

    @property
    def resource(self):
        return Resource(self.data['resource'])

    @property
    def line(self):
        return self.data['line']

def getApiServiceUrl(apiBaseUrl, service, params = {}):
    return rest.buildUrl(apiBaseUrl + '/' + urllib.quote(service), list(params.iteritems()))

class Api(object):
    '''python API for the sonar webservices.

    The sonar REST API is documented below http://docs.codehaus.org/display/SONAR/Web+Service+API.
    '''

    def __init__(self, apiBaseUrl, urlopen = urllib.urlopen):
        '''TODO

        @apiBaseUrl Should be someting like
        http://localhost/sonar/api
        '''

        self.apiBaseUrl = apiBaseUrl
        self.urlopen = urlopen

    def getViolations(self, resource, priorities, depth = -1):
        '''Returns the sonar violations.

        Example URL http://my.sonar.host/sonar/api/violations?resource=my:resource&depth=-1&priorities=BLOCKER,CRITICAL
        '''

        url = getApiServiceUrl(self.apiBaseUrl, 'violations', {'resource': resource, 'priorities': ','.join(priorities), 'depth': depth})
        
        logging.debug('Calling sonar service %s', url)

        return [Violation(data) for data in json.load(self.urlopen(url))]
