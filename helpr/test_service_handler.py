
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
      '', '', None, None 
    )
    self.assertRaises(
      ValueError,
      ServiceHandler,
      '', '', {}, None 
    )

  def test_qparam_validator(self):
    serviceHandler = ServiceHandler(
      '/testendpoint/badrequest',
      'get',
      {
        'param1' : 'value1'
      },
      ['param1', 'param2']
    )

    with self.assertRaises(BadRequest) as context:
      serviceHandler._validate_request_params()

    self.assertEqual(context.exception.code, HTTPExceptions.BAD_REQUEST)
    self.assertEqual(context.exception.msg, 'Bad Request')
    self.assertEqual(context.exception.endpoint, '/testendpoint/badrequest')













