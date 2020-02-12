
import uuid
from wrappers.aws.dynamodb import Dynamodb


class DynamoDBRepo:

  def __init__(self, tableName, region, credentials=None):
    self.dynamodb = Dynamodb(tableName, region, credentials)

  def create_user(self, user):
    """
    Create User
    :param user: user to be created
    :type user: dictionary
    """

    user['id'] = uuid.uuid4().hex
    self.dynamodb.put_item(user)
    return {'id' : user['id']}

  def get_user(self, id):
    """
    Get user
    :param id: user id
    :type id: string
    """

    user = self.dynamodb.get_item({'id' : id})
    return user

  def delete_user(self, id):
    """
    Delete user by ID
    :param id: id of the user to be deleted
    :type id: string
    :returns: empty json
    """

    self.dynamodb.delete_item({'id' : id})
    return {}



