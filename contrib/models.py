from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy import UUID
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from uuid import uuid4


class Basemodel(DeclarativeBase):
    pass
    
    