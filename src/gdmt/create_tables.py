#!/usr/bin/env python

from utils.config import engine, session
from gui.library.models import Base, HealthCenterType

metadata = Base.metadata
metadata.create_all(engine)

session.add_all([
    HealthCenterType(name='Primary Health Center', description=''),
    HealthCenterType(name='Sub Center', description='')
    ])
session.commit()
