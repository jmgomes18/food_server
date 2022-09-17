from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.sql.sqltypes import DateTime
from datetime import datetime

from src.database.db_base import Base

class Menu(Base):
    """    
        - id
        - item
        - description
    """
    __tablename__ = "menu"
    __table_args__ = {"schema": "food_server"}

    id = Column("id", Integer, primary_key=True)
    item = Column("item", String(30), unique=True, nullable=False)
    description = Column("description", Text, nullable=False)
    created_at = Column("created_at", DateTime, default=datetime.now)
    updated_at = Column(
        "updated_at", DateTime, default=datetime.now, onupdate=datetime.now
    )

    def __repr__(self) -> str:
        return f"Client: [description={self.description}, item={self.item}]"

    def __eq__(self, __o: object) -> bool:
        if (
            self.description == __o.description
            and self.item == __o.item
        ):
            return True
        return False