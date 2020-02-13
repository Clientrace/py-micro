
import json


class UpdateUser:

  def __init__(self, repo, requestParams, requestBody, pathParams):
    self.repo = repo
    self.requestParams = requestParams
    self.requestBody = requestBody
    self.pathParams = pathParams

  def execute(self):
    resp = self.repo.update_user(
      self.pathParams['id'],
      self.requestBody
    )

    return {
      'statusCode' : 200,
      'body' : json.dumps(resp)
    }


