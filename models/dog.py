from databases.db import db
from flask import jsonify

class Dog(db.Model):
    __tablename__ = 'dogs'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    breed = db.Column(db.String(50), nullable = False)
    age = db.Column(db.String(50), nullable = False)
    weight = db.Column(db.Numeric(5,2), nullable = False)
    id_daycare = db.Column(db.Integer)


    def __init__(self, nombre:str, raza:str, peso:float, edad: int ):
        self.nombre = nombre
        self.raza = raza
        self.peso = peso
        self.edad = edad

    #Metodos 
    def get_list_dogs():
        list_dogs = Dog.query.all()
        return list_dogs

    #Get and set 
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, value:str) -> None:
        if isinstance(value, str):
            self.__nombre = value
        else:
            raise ValueError('Expected str')
        
    @property
    def raza(self) -> str:
        return self.__raza
    
    @raza.setter
    def raza(self, value:str) -> None:
        if isinstance(value, str):
            self.__raza = value
        else:
            raise ValueError('Expected str')
        
    @property
    def peso(self) -> float:
        return self.__peso
    
    @peso.setter
    def peso(self, value:float) -> None:
        if isinstance(value, float):
            self.__peso = value
        else:
            raise ValueError('Expected float')
    
    @property
    def edad(self) -> int:
        return self.__edad
    
    @edad.setter
    def edad(self, value:int) -> None:
        if isinstance(value, int):
            self.__edad = value
        else:
            raise ValueError('Expected int')