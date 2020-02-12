
import uuid
from wrappers.aws.dynamodb import Dynamodb


class DynamoDBRepo:

  def __init__(self, tableName, region, credentials=None):
    self.dynamodb = Dynamodb(tableName, region, credentials)

  def create_user(self, item):
    item['id'] = uuid.uuid4().hex
    resp = self.dynamodb.put_item(item)
    return {'id' : item['id']}





