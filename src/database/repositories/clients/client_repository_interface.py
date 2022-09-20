from abc import ABC, abstractmethod

class ClientRepositoryInterface(ABC):
    @abstractmethod
    def insert(data):
        raise NotImplementedError
    
    @abstractmethod
    def select():
        raise NotImplementedError

    @abstractmethod
    def delete(id):
        raise NotImplementedError
    
    @abstractmethod
    def select_by_id(id):
        raise NotImplementedError