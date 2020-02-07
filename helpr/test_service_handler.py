
import logging
import unittest
from helpr.http_exceptions import *
from helpr.service_handler import ServiceHandler


class ServiceHandlerTest(unittest.TestCase):

  def test_service_handler_init(self):
    self.assertRaises(
      ValueError,
      ServiceHandler,
      0, None, None, None
    )
    self.assertRaises(
      ValueError,
      ServiceHandler,
      '', 0, None, None 
    )
    self.assertRaises(
      ValueError,
      ServiceHandler,
      '', '', 0, None 
    )
    self.assertRaises(
      ValueError,
      ServiceHandler,
      '', '', [], 0
    )

  def test_param_validator_for_get_request(self):
    serviceHandler = ServiceHandler(
      '/testendpoint',
      'GET',
      ['qparam1', 'qparam2', 'qparam3'],
      None
    )

    testQueryParam = {
      'qparam1' : 'testvalue1',
      'qparam2' : 'testvalue2',
      'qparam3' : 'testvalue3'
    }
    
    self.assertEqual(
      serviceHandler._validate_request_params(
        testQueryParam,
      ), 0 
    )

  def test_param_validator_for_get(self):
    serviceHandler = ServiceHandler(
      '/testendpoint',
      'GET',
      ['param1', 'param2', 'param3'],
      None
    )

    testQparams1 = {
      'param1' : 'value1',
      'param2' : 'value2',
      'param3' : 'value3'
    }

    testQparams2  = {
      'param1' : 'value1'
    }

    # Valid request
    self.assertEqual(
      serviceHandler._validate_request_params(
        testQparams1,
      ), 0 
    )

    # Raise BadRequest Exception for Empty Param
    self.assertRaises(
      BadRequest,
      serviceHandler._validate_request_params,
      None,
      None
    )

    # Raise BadRequest Exception for Empty Param
    self.assertRaises(
      BadRequest,
      serviceHandler._validate_request_params,
      testQparams2,
      None
    )

    




  
    





