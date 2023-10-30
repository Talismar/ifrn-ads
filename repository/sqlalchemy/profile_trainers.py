from sqlalchemy.orm import Session
from domain.data.sqlalchemy_models import Profile_Trainers


class ProfileTrainersRepository():
    def __init__(self, session: Session):
        self.__session: Session = session

    def insert(self, data: dict):
        try:
            new_data = Profile_Trainers(**data)
            self.__session.add(new_data)
            self.__session.commit()
        except Exception as e:
            return False 
        return True
    
    def get_all(self):
        return self.__session.query(Profile_Trainers).all() 

    def get_by_id(self, id: int):
        return self.__session.query(Profile_Trainers).filter(Profile_Trainers.id == id).one_or_none()
    
    def partial_update(self, id:int, details: dict) -> bool: 
       try:
            self.__session.query(Profile_Trainers).filter(Profile_Trainers.id == id).update(details)     
            self.__session.commit() 
       except: 
           return False 
       return True
   
    def delete(self, id:int) -> bool: 
        try:
           self.__session.query(Profile_Trainers).filter(Profile_Trainers.id == id).delete()
           self.__session.commit()
          
        except Exception as e: 
            return False 
        
        return True
    

