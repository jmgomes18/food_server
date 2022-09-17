from datetime import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer
from sqlalchemy.sql.sqltypes import DateTime
from src.database.db_base import Base
from src.database.entities.clients import Clients
from src.database.entities.companies import Companies


class Orders(Base):
    """    
        - id
        - status
        - client_id
        - company_id
    """
    __tablename__ = "orders"
    __table_args__ = {"schema": "food_server"}

    id = Column("id", Integer, primary_key=True)
    client_id = Column("client_id", ForeignKey(Clients.id))
    company_id = Column("company_id", ForeignKey(Companies.id))
    status = Column("status", Boolean, nullable=False, default=True)
    created_at = Column("created_at", DateTime, default=datetime.now)
    updated_at = Column(
        "updated_at", DateTime, default=datetime.now, onupdate=datetime.now
    )

    def __repr__(self) -> str:
        return f"Client: [client_id={self.client_id}, company_id={self.company_id}, status={self.status}]"

    def __eq__(self, __o: object) -> bool:
        if (
            self.client_id == __o.client_id
            and self.company_id == __o.company_id
            and self.status == __o.status
            and self.password == __o.password
        ):
            return True
        return False
