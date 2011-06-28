import platform
from PyQt.QtCore import *
from PyQt.QtGui import *
from sqlalchemy import (Table, Column, Integer, String, Text, Float, MetaData,
        ForeignKey)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class HealthCenterType(Base):
    __tablename__ = 'health_center_types'

    id = Column('id', Integer, primery_key=True)
    name = Column('name', String(100))
    description = Column('description', Text, nullable=True)

    def __init__(self, name, description=''):
        self.name = name
        self.description = description

    def __unicode__(self):
        self.name

class HealthCenter(Base):
    __tablename__ = 'health_centers'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(100))
    type_id = Column('type', ForeignKey('health_center_types.id'))
    latitude = Column('latitude', Float)
    longitude = Column('longitude', Float)
    description = Column('description', Text, nullable=True)

    type = relationship(HealthCenterType, backref('health_centers', order_by=id))

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

class RatingCriteria(Base):
    __tablename__ = 'rating_criterias'

    id = Column('id', Integer, primary_key=true)
    name = Column('name', String(100))
    min_value = Column('min_value', Float)
    max_value = Column('max_value', Float)
    description = Column('description', Teaxt, nullable=True)

    def __init__(self, name, description=''):
        self.name = name
        self.description = description

    def __unicode__(self):
        self.name

class Rating(Base):
    __tablename__ = 'ratings'

    id = Column('id', Integer, primary_key=true)
    value = Column('value', Float)
    health_center_id = Column('health_center', ForeignKey('health_centers.id'))
    criteria_id = Column('criteria', ForeignKey('rating_crierias.id'))
    date = Column('date', Date)
    description = Column('description', Text, nullable=True)

    criteria = relationship(RatingCriteria, backref('ratings', order_by=id))
    health_center = relationship(HealthCenter, backref('ratings', order_by=id))

    def __init__(self, value, health_center_id, criteria, date, description=''):
        self.value = value
        self.health_center = health_center
        self.criteria = criteria
        self.date = date
        self.description = description

    def __unicode__(self):
        return 'Value:%f, Criteria:%s, Health Center:%s' % (self.value,
                self.criteria, self.health_center)
