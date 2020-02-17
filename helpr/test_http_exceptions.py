
import sys
import logging
import unittest
from helpr.http_exceptions import HTTPExceptions, BadRequest, InternalServerError, MethodNotAllowed


class HttpExceptionTest(unittest.TestCase):

  def test_badrequest_init(self):
    # Assert code if integer
    self.assertRaises(ValueError, BadRequest, '', '', '', '')

    # Assert msg if string
    self.assertRaises(ValueError, BadRequest, 0, 0, 0, 0)

    # Assert endpoint if string
    self.assertRaises(ValueError, BadRequest, 0, '', 0, 0)

    # Assert fieldError if string
    self.assertRaises(ValueError, BadRequest, 0, '', '', 0)

  def test_internal_server_error_init(self):
    # Assert code if integer
    self.assertRaises(ValueError, InternalServerError, '', '', '')

    # Assert msg if string
    self.assertRaises(ValueError, InternalServerError, 0, 0, 0)

    # Assert endpoint if string
    self.assertRaises(ValueError, InternalServerError, 0, '', 0)

  def test_method_not_allowed(self):
    # Assert code if integer
    self.assertRaises(ValueError, MethodNotAllowed, '', '', '')

    # Assert msg if string
    self.assertRaises(ValueError, MethodNotAllowed, 0, 0, 0)

    # Assert endpoint if string
    self.assertRaises(ValueError, MethodNotAllowed, 0, '', 0)

  def test_bad_request_exception(self):
    with self.assertRaises(Exception) as context:
      HTTPExceptions.raise_exception( HTTPExceptions.BAD_REQUEST,
        '/testendpoint/badrequest',
        'field'
      )


    self.assertEqual(context.exception.code, HTTPExceptions.BAD_REQUEST)
    self.assertEqual(context.exception.msg, 'Bad Request')
    self.assertEqual(context.exception.endpoint, '/testendpoint/badrequest')


  def test_internal_server_error_exception(self):
    with self.assertRaises(Exception) as context:
      HTTPExceptions.raise_exception(
        HTTPExceptions.INTERNAL_SERVER_ERROR,
        '/testendpoint/internalservererror'
      )


    self.assertEqual(context.exception.code, HTTPExceptions.INTERNAL_SERVER_ERROR)
    self.assertEqual(context.exception.msg, 'Internal Server Error')
    self.assertEqual(context.exception.endpoint, '/testendpoint/internalservererror')

  def test_method_not_allowed_exception(self):
    with self.assertRaises(Exception) as context:
      HTTPExceptions.raise_exception(
        HTTPExceptions.METHOD_NOT_ALLOWED,
        '/testendpoint/methodnotallowed'
      )


    self.assertEqual(context.exception.code, HTTPExceptions.METHOD_NOT_ALLOWED)
    self.assertEqual(context.exception.msg, 'Method not Allowed')
    self.assertEqual(context.exception.endpoint, '/testendpoint/methodnotallowed')




