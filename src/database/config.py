import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

class DBConnectionHandler:
    """SQLAlchmy database connection"""

    def __init__(self) -> None:
        self.__user = os.environ.get("DB_USER")
        self.__password = os.environ.get("DB_PASSWORD")
        self.__host = os.environ.get("DB_HOST")
        self.__port = os.environ.get("DB_PORT")
        self.__database = os.environ.get("DB_DATABASE")
        self.__connection_string = f"mysql+pymysql://{self.__user}:{self.__password}@{self.__host}:{self.__port}/{self.__database}"  # pylint: disable=max-line-length
        self.__engine = self.__create_database_engine()
        self.session = None

    def get_engine(self):
        """Return connection Engine
        :parram - None
        :return - engine connection to Database
        """
        return self.__engine

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def __enter__(self):
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()  # pylint: disable=no-member
