
import json

# Create User Use Case

class CreateUser:

  def __init__(self, repo, requestParams, requestBody):
    self.repo = repo
    self.requestParams = requestParams
    self.requestBody = requestBody

  def execute(self):
    resp = self.repo.CreateUser(self.requestBody)
    return {
      'statusCode' : 200,
      'body' : json.dumps(resp)
    }

