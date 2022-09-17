from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.sqltypes import DateTime
from datetime import datetime

from src.database.db_base import Base
from sqlalchemy.orm import relationship

class Companies(Base):
    """    
        - id
        - email
        - password
        - corporate_name
        - active
    """
    __tablename__ = "companies"
    __table_args__ = {"schema": "food_server"}

    id = Column("id", Integer, primary_key=True)
    email = Column("email", String(30), unique=True, nullable=False)
    corporate_name = Column("corporate_name", String(100), nullable=False)
    password = Column("password", String(50), nullable=False)
    active = Column("active", Boolean, nullable=False, default=True)
    created_at = Column("created_at", DateTime, default=datetime.now)
    updated_at = Column(
        "updated_at", DateTime, default=datetime.now, onupdate=datetime.now
    )

    orders = relationship("Orders")

    def __repr__(self) -> str:
        return f"Company: [corporate_name={self.corporate_name}, email={self.email}, active={self.active}]"

    def __eq__(self, __o: object) -> bool:
        if (
            self.corporate_name == __o.corporate_name
            and self.email == __o.email
            and self.active == __o.active
            and self.password == __o.password
        ):
            return True
        return False