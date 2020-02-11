
import json

from helpr.aws_service_handler import AWSServiceHandler
from ms.services.create_user import CreateUser
from ms import dynamodb_repo

def handler(event, context):

  # Initialize Request Handler for Request Validation
  svh = AWSServiceHandler(
    event,
    Service = CreateUser,
    Repo=dynamodb_repo.Dynamodb(
      'users_table',
      'ap-southeast-1'
    ),
    ReqQueryparams={
      'name' : AWSServiceHandler.STRING,
      'address' : AWSServiceHandler.STRING,
      'age' : AWSServiceHandler.INTEGER
    }
  )

  try:
    return svh.execute()
  except Exception as e:
    print(e.args)
    return {
      'statusCode' : 500,
      'body' : str(e)
    }


