
import json

# Create User Use Case

class CreateUser:

  def __init__(self, repo, requestParams, requestBody,  pathParams):
    self.repo = repo
    self.requestParams = requestParams
    self.requestBody = requestBody
    self.pathParams = pathParams

  def execute(self):
    resp = self.repo.create_user(self.requestBody)
    return {
      'statusCode' : 200,
      'body' : json.dumps(resp)
    }





