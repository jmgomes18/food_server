import logging
from sqlalchemy.exc import InvalidRequestError
from src.database.entities import Clients
from src.database.config import DBConnectionHandler

logger = logging.getLogger(__name__)

class ClientsRepository:
    @classmethod
    def insert(cls, data):
        with DBConnectionHandler as conn:
            try:
                values = Clients(**data)

                logger.info('inserting data')
                conn.session.add(values)
                conn.session.commit()

                return Clients(
                    id=values.id, 
                    email=values.email, 
                    password=values.password, 
                    name=values.name, 
                    active=values.active
                )
            except InvalidRequestError as e:
                logger.error('crashed inserting data')
                conn.session.rollback()
                raise
            finally:
                conn.session.close()

    @classmethod
    def select():
        pass

    @classmethod
    def delete(id):
        pass
    
    @classmethod
    def select_by_id(id):
        pass