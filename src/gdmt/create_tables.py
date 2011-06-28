#!/usr/bin/env/python

from utils.config import engine
from gui.library.models import Base

metadata = Base.metadata
metadata.create_all(engine)
