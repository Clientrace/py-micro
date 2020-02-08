
import unittest
from unittest.mock import patch, Mock
from wrappers.aws.dynamodb import Dynamodb


class DynamodbTest(unittest.TestCase):

  def test_dynamodb_init(self):
    # Valid dynamodb init
    awsCred = {
      'aws_id' : 'test id',
      'aws_secret' : 'test secret'
    }

    # tableName not string
    self.assertRaises(ValueError, Dynamodb, 0, '', awsCred)

    # region not string
    self.assertRaises(ValueError, Dynamodb, '', 0, awsCred)

    # awscred not dictionary
    self.assertRaises(ValueError, Dynamodb, '', '', 0)

    # awscred missing keys
    self.assertRaises(ValueError, Dynamodb, '', '', {})


  @patch('wrappers.aws.dynamodb.Dynamodb')
  def test_put_item(self):
    awsCred = {
      'aws_id' : 'test id',
      'aws_secret' : 'test secret'
    }

    dynamodb = Dynamodb(
      'test-table',
      'ap-southeast-1'
    )
    item = {
      'id' : {
        'S' : 'test ID'
      }
    }

    dynamodb.put_item(item)








