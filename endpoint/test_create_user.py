
import unittest
from test_obj.aws import aws_event
from endpoint import create_user

class CreateUserTest(unittest.TestCase):

  def test_user_creation(self):
    mockEvent = aws_event.AWSMockEvent(
      ResourcePath = 'user/create',
      HTTPMethod = 'POST',
      RequestBody = {
        'name' : 'clarence',
        'address' : 'batasan',
        'age' : 23
      }
    )

    event = mockEvent.get_event()


    resp = create_user.handler(
      mockEvent.get_event(),
      None
    )




