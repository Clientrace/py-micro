
import boto3


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
    pass













