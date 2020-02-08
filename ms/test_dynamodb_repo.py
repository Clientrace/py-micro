
from ms.dynamodb_repo import DynamoDBRepo


class DynamodbRepositoryTest:

  def test_repo_init(self):
    repository = DynamoDBRepo(
      'user-table'
    )



