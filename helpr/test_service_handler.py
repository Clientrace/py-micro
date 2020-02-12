import logging
import unittest
from helpr.service_handler import ServiceHandler
from helpr.http_exceptions import HTTPExceptions, BadRequest, InternalServerError, MethodNotAllowed


class ServiceHandlerTest(unittest.TestCase):

  def test_service_handler_init(self):
    self.assertRaises(
      ValueError,
      ServiceHandler,
      0, None, None, None, None
    )
    self.assertRaises(
      ValueError,
      ServiceHandler,
      '', 0, None, None, None
    )
    self.assertRaises(
      ValueError,
      ServiceHandler,
      '', '', 0, None, None
    )
    self.assertRaises(
      ValueError,
      ServiceHandler,
      '', '', {}, 0,None
    )
    self.assertRaises(
      ValueError,
      ServiceHandler,
      '', '', {}, {}, 0
    )

  def test_param_validator_for_get_request(self):
    serviceHandler = ServiceHandler(
      endpoint = '/testendpoint',
      method = 'GET',
      rqparams = {
        'qparam1' : ServiceHandler.STRING,
        'qparam2' : ServiceHandler.STRING,
        'qparam3' : ServiceHandler.STRING
      }
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

  def test_validate_req_types(self):
    serviceHandler = ServiceHandler(
      endpoint='/testendpoint',
      method='GET'
    )

    self.assertRaises(
      ValueError,
      serviceHandler._validate_request_params,
      0,
      {}
    )

    self.assertRaises(
      ValueError,
      serviceHandler._validate_request_params,
      {},
      0
    )


  def test_param_validator_for_get(self):
    serviceHandler = ServiceHandler(
      endpoint = '/testendpoint',
      method = 'GET',
      rqparams={
        'param1' : ServiceHandler.STRING,
        'param2' : ServiceHandler.STRING,
        'param3' : ServiceHandler.STRING
      }
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

    # Raise BadRequest Exception for Incomplete Param
    self.assertRaises(
      BadRequest,
      serviceHandler._validate_request_params,
      testQparams2,
      None
    )

  def test_param_validator_for_post(self):
    serviceHandler = ServiceHandler(
      endpoint='/testendpoint',
      method='post',
      rqparams={
        'param1' : ServiceHandler.STRING,
        'param2' : ServiceHandler.STRING,
        'param3' : ServiceHandler.STRING
      },
      rbparams={
        'field1' : ServiceHandler.STRING,
        'field2' : ServiceHandler.STRING,
        'field3' : ServiceHandler.STRING
      }
    )

    testQParams = {
      'param1' : 'value1',
      'param2' : 'value2',
      'param3' : 'value3'
    }

    testReqBody = {
      'field1' : 'value1',
      'field2' : 'value2',
      'field3' : 'value3'
    }

    testQParams2 = {
      'param1' : 'value1',
      'param2' : 'value2'
    }

    testReqBody2 = {
      'field1' : 'value1',
      'field2' : 'value2'
    }

    # Valid Post Request
    self.assertEqual(
      serviceHandler._validate_request_params(
        testQParams,
        testReqBody
      ), 0
    )

    # Raise BadRequest Exception for Empty query param and request body param
    self.assertRaises(
      BadRequest,
      serviceHandler._validate_request_params,
      None,
      None
    )

    # Raise BadRequest Exception for incomplete qparams
    self.assertRaises(
      BadRequest,
      serviceHandler._validate_request_params,
      testQParams2,
      testReqBody
    )

    # Raise BadRequest Exception for incomplete reqbody
    self.assertRaises(
      BadRequest,
      serviceHandler._validate_request_params,
      testQParams,
      testReqBody2
    )

    # No QParam required
    serviceHandler = ServiceHandler(
      endpoint='/testendpoint',
      method='post',
      rbparams={
        'field1' : ServiceHandler.STRING,
        'field2' : ServiceHandler.STRING,
        'field3' : ServiceHandler.STRING
      }
    )

    # Valid Post Request
    self.assertEqual(
      serviceHandler._validate_request_params(
        None,
        testReqBody
      ), 0
    )

    # Raise BadRequest Exception for Empty Request Body Param
    self.assertRaises(
      BadRequest,
      serviceHandler._validate_request_params,
      None,
      None
    )

    # Raise BadRequest Exception for Empty Request Body Param
    self.assertRaises(
      BadRequest,
      serviceHandler._validate_request_params,
      None,
      testReqBody2
    )



  def test_type_check(self):
    serviceHandler = ServiceHandler(
      endpoint='/testendpoint',
      method='post',
      rqparams={
        'param1' : ServiceHandler.STRING,
        'param2' : ServiceHandler.STRING,
        'param3' : ServiceHandler.STRING
      },
      rbparams={
        'field1' : ServiceHandler.STRING,
        'field2' : ServiceHandler.STRING,
        'field3' : {
          'f1' : ServiceHandler.INTEGER,
          'f2' : ServiceHandler.INTEGER
        }
      }
    )

    # Raise BadRequest Exception for invalid type
    self.assertRaises(
      BadRequest,
      serviceHandler._validate_request_params,
      {
        'param1' : '',
        'param2' : '',
        'param3' : ''
      },
      {
        'field1' : '',
        'field2' : '',
        'field3' : {
          'f1' : 0,
          'f2': ''
        }
      }
    )
   






