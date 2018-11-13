import datetime

from sqlalchemy import Column, Integer, String, Text, ForeignKey, Date
from .core import Base


class Client(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))

    def __init__(self, name: str):
        self.name = name


class ProductArea(Base):
    __tablename__ = 'product_area'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))

    def __init__(self, name: str):
        self.name = name


class FeatureRequest(Base):
    __tablename__ = 'feature_request'
    id = Column(Integer, primary_key=True)
    title = Column(String(256))
    description = Column(Text())
    client_id = Column(Integer, ForeignKey('client.id'))
    client_priority = Column(Integer)

    target_date = Column(Date)

    product_area_id = Column(Integer, ForeignKey('product_area.id'))

    def __init__(self, title: str, description: str, client_id: int,
                 client_priority: int, target_date: datetime.date, product_area_id: int):
        self.title = title
        self.description = description
        self.client_id = client_id
        self.client_priority = client_priority
        self.target_date = target_date
        self.product_area_id = product_area_id

    def __repr__(self) -> str:
        return f'<FeatureRequest {self.title} - #{self.client_priority}>'

    def to_camel_case_dict(self) -> dict:
        return {
            'id': self.id,
            'title': self.title,
            'date': self.target_date.strftime("%Y-%m-%d"),
            'client': Client.query.get(self.client_id).name,
            'clientPriority': self.client_priority,
            'productArea': ProductArea.query.get(self.product_area_id).name,
            'description': self.description
        }
