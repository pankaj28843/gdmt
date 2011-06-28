from sqlalchemy import *

engine = create_engine('sqlite:///db.sqlite', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
