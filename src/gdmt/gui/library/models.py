import platform
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from sqlalchemy import (Table, Column, Integer, String, Text, Float, MetaData,
        ForeignKey, Date, UniqueConstraint)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from utils.config import session

Base = declarative_base()

class HealthCenterType(Base):
    __tablename__ = 'health_center_types'

    id = Column('id', Integer, primary_key=True)
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
    type_id = Column('type_id', ForeignKey('health_center_types.id'))
    latitude = Column('latitude', String(50))
    longitude = Column('longitude', String(50))
    description = Column('description', Text, nullable=True)
    responsible_person = Column('responsible_person', String(100))
    phone_number = Column('phone_number', String(20))
    email_address = Column('email_address', String(20), nullable=True)

    type = relationship(HealthCenterType,
            backref=backref('health_center_types', order_by=id))

    def __init__(self, name, type_id, latitude, longitude,
            responsible_person, phone_number, email_address='',
            description=''):
        self.name = name
        self.type_id = type_id
        self.latitude = latitude
        self.longitude = longitude
        self.description = description
        self.responsible_person = responsible_person
        self.phone_number = phone_number
        self.email_address = email_address

    def __repr__(self):
        return '<HealthCenter(%s, %s)' % (self.name, self.type)

    def __unicode__(self):
        return self.name

class RatingCriteria(Base):
    __tablename__ = 'rating_criterias'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(100))
    min_value = Column('min_value', String(50))
    max_value = Column('max_value', String(50))
    description = Column('description', Text, nullable=True)

    def __init__(self, name, description=''):
        self.name = name
        self.description = description

    def __unicode__(self):
        self.name

class Rating(Base):
    __tablename__ = 'ratings'

    id = Column('id', Integer, primary_key=True)
    value = Column('value', String(50))
    health_center_id = Column('health_center_id',
            ForeignKey('health_centers.id'))
    criteria_id = Column('criteria_id', ForeignKey('rating_criterias.id'))
    date = Column('date', Date)
    description = Column('description', Text, nullable=True)

    criteria = relationship(RatingCriteria,
            backref=backref('rating_criterias', order_by=id))
    health_center = relationship(HealthCenter,
            backref=backref('health_centers', order_by=id))

    UniqueConstraint('health_center_id', 'criteria_id')

    def __init__(self, value, health_center_id, criteria_id, date,
            description=''):
        self.value = value
        self.health_center_id = health_center_id
        self.criteria_id = criteria_id
        self.date = date
        self.description = description

    def __unicode__(self):
        return 'Value:%f, Criteria:%s, Health Center:%s' % (self.value,
                self.criteria, self.health_center)

