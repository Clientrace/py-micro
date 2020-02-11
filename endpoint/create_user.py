
import json

from helpr.aws_service_handler import AWSServiceHandler
from ms.services.create_user import CreateUser
from ms import dynamodb_repo

def handler(event, context):
  # Initialize Request Handler for Request Validation
  svh = AWSServiceHandler(
    event,
    None,
    {
      'name' : AWSServiceHandler.STRING,
      'address' : AWSServiceHandler.STRING,
      'age' : AWSServiceHandler.INTEGER
    }
  )

  try:
      svh.validate_request_params()
  except Exception as e:
    print(e)
    return 

  # DynamoDB Repo 
  db = dynamodb_repo.Dynamodb(
    'members',
    'ap-southeast-1'
  )

  # Create Database Repo
  service = CreateUser(
    db,
    svh.get_request_params(),
    svh.get_request_body()
  )

  return  service.execute()
  




