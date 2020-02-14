
import uuid
from wrappers.aws.dynamodb import Dynamodb
from ms.repository import Repository


class DynamoDBRepo(Repository):

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

    resp = self.dynamodb.get_item({'id' : id})
    user = resp['Item']
    user['age'] = int(user['age'])
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


  def update_user(self, id, update_val):
    itemKey = {
      'id' : {
        'S' : id
      }
    }

    updateExp = {}

    for key in update_val.keys():
      if type(update_val[key]) == str:
        updateExp[key] = {
          'Value' : {
            'S' : update_val[key]
          }
        }

      if type(update_val[key]) == int:
        updateExp[key] = {
          'Value' : {
            'N' : str(update_val[key])
          }
        }

    self.dynamodb.update_item(itemKey, updateExp)
    return {}


