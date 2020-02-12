
import json

from helpr.aws_service_handler import AWSServiceHandler
from ms.services.create_user import CreateUser
from ms import dynamodb_repo

def handler(event, context):
  # Initialize Request Handler for Request Validation
  svh = AWSServiceHandler(
    event,
    Service = CreateUser,
    Repo=dynamodb_repo.DynamoDBRepo(
      'users_table',
      'ap-southeast-1'
    ),
    ReqPathParams={
      'id' : AWSServiceHandler.STRING
    }
  )

  try:
    return svh.execute()
  except Exception as e:
    return {
      'statusCode' : e.args[0],
      'body' : str(e.args)
    }






