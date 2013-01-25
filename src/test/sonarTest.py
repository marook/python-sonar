import sonar
import unittest

class GetApiServiceUrlTest(unittest.TestCase):

    def testBuildUrlWithoutParams(self):
        self.assertEqual(sonar.getApiServiceUrl('http://host/api', 'service'), 'http://host/api/service')

    def testBuildUrlWithOneParam(self):
        self.assertEqual(sonar.getApiServiceUrl('http://host/api', 'service', {'key': 'value'}), 'http://host/api/service?key=value')

    def testBuildUrlWithEscapedParamValue(self):
        self.assertEqual(sonar.getApiServiceUrl('http://host/api', 'service', {'key': 'hello world'}), 'http://host/api/service?key=hello%20world')

    def testBuildUrlWithTwoParams(self):
        self.assertEqual(sonar.getApiServiceUrl('http://host/api', 'service', {'k1': 'v1', 'k2': 'v2'}), 'http://host/api/service?k2=v2&k1=v1')

if __name__ == '__main__':
    unittest.main()
