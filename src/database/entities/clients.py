from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from src.database.db_base import Base

class Clients(Base):
    """    
        - email
        - password
        - name
        - active
    """
    __tablename__ = "clients"
    __table_args__ = {"schema": "food_server"}

    id = Column("id", Integer, primary_key=True)
    email = Column("email", String(30), unique=True, nullable=False)
    name = Column("name", String(100), nullable=False)
    password = Column("password", String(50), nullable=False)
    active = Column("active", Boolean, nullable=False, default=True)
    created_at = Column("created_at", DateTime, default=datetime.now)
    updated_at = Column(
        "updated_at", DateTime, default=datetime.now, onupdate=datetime.now
    )

    orders = relationship("Orders")

    def __repr__(self) -> str:
        return f"Client: [name={self.name}, email={self.email}, active={self.active}]"

    def __eq__(self, __o: object) -> bool:
        if (
            self.name == __o.name
            and self.email == __o.email
            and self.active == __o.active
            and self.password == __o.password
        ):
            return True
        return False