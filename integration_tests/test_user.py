
import json
import requests
import unittest

global HOST_URL
HOST_URL = 'https://88kv4x9wk1.execute-api.ap-southeast-1.amazonaws.com'


class APIIntegrationTest(unittest.TestCase):
  def test_create_delete_user(self):
    item = {
      'name' : 'clarence',
      'address' : 'batasan',
      'age' : 13
    }

    resp = requests.post(
      HOST_URL + '/dev/user/create',
      headers = {'Content-Type' : 'application/json'},
      data = json.dumps(item)
    )

    userId = json.loads(resp.content)['id']

    self.assertEqual(resp.status_code, 200)

    resp = requests.delete(
      HOST_URL + '/dev/user/delete/' + userId,
      headers = {'Content-Type' : 'application/json'}
    )

    self.assertEqual(resp.status_code, 200)

  def test_view_user(self):
    item = {
      'name' : 'clarence',
      'address' : 'batasan',
      'age' : 13
    }

    resp = requests.post(
      HOST_URL + '/dev/user/create',
      headers = {'Content-Type' : 'application/json'},
      data = json.dumps(item)
    )

    userId = json.loads(resp.content)['id']
    print(userId)

    userData = requests.get(
      HOST_URL + '/dev/user/view/' + userId,
      headers = {'Content-Type' : 'application/json'}
    )

    print(userData.content)

    resp = requests.delete(
      HOST_URL + '/dev/user/delete/' + userId,
      headers = {'Content-Type' : 'application/json'}
    )

    self.assertEqual(resp.status_code, 200)

  def test_update_user(self):
    item = {
      'name' : 'clarence',
      'address' : 'batasan',
      'age' : 13
    }

    resp = requests.post(
      HOST_URL + '/dev/user/create',
      headers = {'Content-Type' : 'application/json'},
      data = json.dumps(item)
    )

    userId = json.loads(resp.content)['id']
    print(userId)

    item = {
      'name' : 'kim',
      'address' : 'cubao',
      'age' : 23
    }

    resp = requests.put(
      HOST_URL + '/dev/user/update/' + userId,
      headers = {'Content-Type' : 'application/json'},
      data = json.dumps(item)
    )

    print(resp)

    resp = requests.delete(
      HOST_URL + '/dev/user/delete/' + userId,
      headers = {'Content-Type' : 'application/json'}
    )

    self.assertEqual(resp.status_code, 200)




