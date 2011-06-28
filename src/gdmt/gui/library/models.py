import platform
from PyQt.QtCore import *
from PyQt.QtGui import *
from sqlalchemy import (Table, Column, Integer, String, Text, Float, MetaData,
        ForeignKey)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class HealthCenterType(Base):
    __tablename__ = 'healthcenter_types'

    id = Column('id', Integer, primery_key=True)
    name = Column('name', String(100))
    description = Column('description', Text, nullable=True)

    def __init__(self, name, description=''):
        self.name = name
        self.description = description

    def __unicode__(self):
        self.name

class HealthCenter(Base):
    __tablename__ = 'healthcenters'

    id = Column('name', String(100))
    type = Column('type', ForeignKey('healthcenter_types.id'))
    latitude = Column('latitude', Float)
    longitude = Column('longitude', Float)
    description = Column('description', Text, nullable=True)

    def __init__(self, name, type, latitude, longitude, description=''):
        self.name = name
        self.type = type
        self.latitude = latitude
        self.longitude = longitude
        self.description = description

    def __repr__(self):
        return '<HealthCenter(%s, %s)' % (self.name, self.type)

    def __unicode__(self):
        return self.name


