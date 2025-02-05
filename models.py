from config import session
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Text

Base = declarative_base()


# Medical Rule Model
class MedicalRule(Base):
    __tablename__ = 'rules'
    id = Column(Integer, primary_key = True)
    conditions = Column(Text, nullable = False) 
    priority = Column(String(50), nullable = False) 
    message = Column(String(255), nullable = False) 


if __name__ == '__main__':
    try:
        Base.metadata.create_all(session.bind)
        print('Tables created successfully!')
    except Exception as e:
        print(f'An error occured: {e}')
