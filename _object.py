from abc import ABC, abstractmethod
from typing import List
import enum


class obj(enum.Enum):
    INTEGER_OBJ = "INTEGER"
    BOOLEAN_OBJ = "BOOLEAN"
    NULL_OBJ    = "NULL"
    RETURN_VALUE_OBJ = "RETURN_VALUE"
    ERROR_OBJ = "ERROR"




class Object(ABC):
    @abstractmethod
    def Type(self):
        pass
    def Inspect(self):
        pass

################################################################################

class Integer(Object):
    def __init__(self, Value: int):
        self.Value = Value
    def Inspect(self):
        return f'{self.Value}'
    def Type(self):
        return obj.INTEGER_OBJ
    def __eq__(self, other):
        if type(self) is type(other):
            return self.__dict__ == other.__dict__
        return False
################################################################################

class Boolean(Object):
    def __init__(self, Value: bool):
        self.Value = Value
    def Inspect(self):
        return f'{self.Value}'
    def Type(self):
        return obj.BOOLEAN_OBJ
    def __eq__(self, other):
        if type(self) is type(other):
            return self.__dict__ == other.__dict__
        return False
################################################################################

class Null(Object):
    def __init__(self):
        self.Value = None
    def Inspect(self):
        return 'null'
    def Type(self):
        return obj.NULL_OBJ

#################################################################################

class ReturnValue(Object):
    def __init__(self, Value: Object):
        self.Value = Value
    def Type(self):
        return obj.RETURN_VALUE_OBJ
    def Inspect(self):
        return self.Value.Inspect()

#################################################################################

class Error(Object):
    def __init__(self, Message: str):
        self.Message = Message
    def Type(self):
        return obj.ERROR_OBJ
    def Inspect(self):
        return "ERROR " + self.Message

