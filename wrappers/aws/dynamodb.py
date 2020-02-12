
import sys
import boto3
import logging


class Dynamodb:

  def __init__(self, tableName, region, awsCred=None):
    """
    Initialize Dynamodb Table
    :param tableName: AWS Dynamodb Tablename
    :param region: AWS region
    :param awsCred: AWS Credentials (id and secret token)
    :type tableName: string
    :type region: string
    :type awsCred: Dictionary {'aws_id': '<aws ID>', 'aws_secret' : '<aws secret token'}
    """

    if type(tableName) != str:
      raise ValueError('Parameter tableName: Type Error (It should be string)')

    if type(region) != str:
      raise ValueError('Parameter tableName: Type Error (It should be string)')


    self.tableName = tableName

    if awsCred != None:
      if type(awsCred) != dict:
        raise ValueError('Parameter awsCred: Type Error (It should be dictionary)')

      if 'aws_id' not in awsCred and 'aws_secret' not in awsCred:
        raise ValueError('Parameter awsCred: Type Error (It should be dictionary)')

      self.DYNAMODB_c = boto3.client(
        'dynamodb',
        aws_access_key_id = awsCred['aws_id'],
        aws_secret_access_key = awsCred['aws_secret'],
        region_name = region
      )

      self.DYNAMODB_r = boto3.resource(
        'dynamodb',
        aws_access_key_id = awsCred['aws_id'],
        aws_secret_access_key = awsCred['aws_secret'],
        region_name = region
      )

    else:
      self.DYNAMODB_c = boto3.client(
        'dynamodb',
        region_name = 'ap-southeast-1'
      )
      self.DYNAMODB_r = boto3.resource(
        'dynamodb',
        region_name = 'ap-southeast-1'
      )


  def put_item(self, item):
    """
    Dynamodb Add record
    :param item: Dynamodb Item
    :type item: json (dictionary)
    :returns: Dynamodb Response object
    :rtype: json (dictionary)
    """
    table = self.DYNAMODB_r.Table(self.tableName)
    resp = table.put_item(
      Item = item,
      ReturnConsumedCapacity = 'TOTAL'
    )
    return resp

  def update_item(self, key, item):
    """
    Dynamodb update item attribute
    :param key: Item key
    :param item: Dynamodb Item
    :type key: json (dictionary)
    :type item: json (dictionary)
    :returns: Dynamodb Response object
    :rtype: json (dictionary)
    """

    resp = self.DYNAMODB_c.update_item(
      TableName = self.tableName,
      Key = key,
      AttributeUpdates = item
    )
    return resp

  def increment(self, key, attribute):
    """
    Atomic Number increment
    :param key: Item Key
    :param attribute: Attrib to increment
    """

    resp = self.DYNAMODB_c.update_item(
      TableName = self.tableName,
      Key = key,
      UpdateExpression = 'ADD #'+attribute+' :inc',
      ExpressionAttributeValues = {
        ':inc' : {
          'N' : '1'
        }
      },
      ExpressionAttributeNames = {
        '#'+attribute : attribute
      },
      ReturnValues='UPDATED_NEW'
    )
    return resp

  def get_item(self, key):
    """
    Retrieve Dynamodb Record
    :param key: Item key
    :type key: json (dictionary)
    :returns: Dynamodb Response object
    :rtype: json (dicionary)
    """
    table = self.DYNAMODB_r.Table(self.tableName)
    resp = table.get_item(
      Key = key,
      ReturnConsumedCapacity = 'TOTAL'
    )
    return resp

  def delete_item(self, key):
    """
    Delete dynamodb item
    :param key: table key
    :type key: dictionary
    :returns:
    """

    table = self.DYNAMODB_r.Table(self.tableName)
    resp = table.delete_item(
      Key = key,
      ReturnConsumedCapacity = 'TOTAL'
    )
    return resp

  def batch_delete(self, items):
    """
    Dynamodb batch delete items
    :param item: Dynamodb Items to be deleted
    :type item: json (dictionary)
    """

    table = self.DYNAMODB_r.Table(self.tableName)

    with table.batch_writer() as batch:
      for item in items:
        batch.delete_item(Key=item)

  def batch_put(self, items):
    """
    Dynamodb batch insert items
    :param item: Dynamodb Items to be inserted
    :type item: json (dictionary)
    """

    table = self.DYNAMODB_r.Table(self.tableName)
    
    with table.batch_writer() as batch:
      for item in items:
        batch.put_item(Item=item)

  def query(self, keyExpression):
    """
    Dynamodb query
    :param keyExpression: Dynamodb KeyConditionExpression
    :type keyExpression: Key (boto3.key)
    :returns: Dynamodb Response object
    :rtype: json (dicionary)
    """

    table = self.DYNAMODB_r.Table(self.tableName)

    resp = table.query(KeyConditionExpression=keyExpression)
    return resp['Items']    

  


 








