
import json
import requests


HOST_URL = 'https://88kv4x9wk1.execute-api.ap-southeast-1.amazonaws.com'


item = {
  'name' : 'clarence',
  'address' : 'batasan',
  'age' : 13
}

resp = requests.post(
  HOST_URL + '/dev/user/create?test=123',
  headers = {'Content-Type' : 'application/json'},
  data = json.dumps(item)
)

print(resp.status_code)
print(resp.content)


