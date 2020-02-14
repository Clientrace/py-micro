
from abc import ABCMeta, abstractmethod


# Repository SucperClass
class Repository(metaclass=ABCMeta):

  @abstractmethod
  def create_user(self):
    return None

  @abstractmethod
  def get_user(self):
    return None

  @abstractmethod
  def delete_user(self):
    return None

  @abstractmethod
  def update_user(self):
    return None


