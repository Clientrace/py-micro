
import logging
import unittest
from helpr.http_exceptions import HTTPExceptions
from helpr.http_exceptions import BadRequest
from helpr.http_exceptions import InternalServerError

class HttpException(unittest.TestCase):

  def test_badrequest_init(self):
    # Code Type Error
    self.assertRaises(ValueError, BadRequest, '', '', '')
    self.assertRaises(ValueError, BadRequest, 0, 0, 0)
    self.assertRaises(ValueError, BadRequest, 0, '', 0)

  def test_internal_server_error_init(self):
    # Code Type Error
    self.assertRaises(ValueError, InternalServerError, '', '', '')
    self.assertRaises(ValueError, InternalServerError, 0, 0, 0)
    self.assertRaises(ValueError, InternalServerError, 0, '', 0)

  def test_raise_exception(self):
    with self.assertRaises(Exception) as context:
      HTTPExceptions.raise_exception( HTTPExceptions.BAD_REQUEST,
        '/testendpoint/badrequest'
      )

    logging.getLogger('show').info(context.exception)

    self.assertEqual(context.exception.code, HTTPExceptions.BAD_REQUEST)
    self.assertEqual(context.exception.msg, 'Bad Request')
    self.assertEqual(context.exception.endpoint, '/testendpoint/badrequest')


  def test_raise_exception_2(self):
    with self.assertRaises(Exception) as context:
      HTTPExceptions.raise_exception(
        HTTPExceptions.INTERNAL_SERVER_ERROR,
        '/testendpoint/internalservererror'
      )

    logging.getLogger('show').info(context.exception)

    self.assertEqual(context.exception.code, HTTPExceptions.INTERNAL_SERVER_ERROR)
    self.assertEqual(context.exception.msg, 'Internal Server Error')
    self.assertEqual(context.exception.endpoint, '/testendpoint/internalservererror')





