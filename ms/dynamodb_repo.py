

from wrappers.aws.dynamodb import Dynamodb


class DynamoDBRepo:

  def __init__(self, tableName, credentials=None):
    self.dynamodb = Dynamodb(tableName, credentials)


  

    


