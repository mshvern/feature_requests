from sqlalchemy import Column, Integer, String, Text, ForeignKey, Date
from .database import Base


class FeatureRequest(Base):
    __tablename__ = 'feature_request'
    id = Column(Integer, primary_key=True)
    title = Column(String(256))
    description = Column(Text())
    client_id = Column(Integer, ForeignKey('client.id'))
    client_priority = Column(Integer)

    target_date = Column(Date)

    product_area = Column(Integer, ForeignKey('product_area.id'))

    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description

    def __repr__(self) -> str:
        return f'<FeatureRequest {self.id}>'


class Client(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))


class ProductArea(Base):
    __tablename__ = 'product_area'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
