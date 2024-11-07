import json
import math
import random

class Pokemon:

    def  __init__(self,data, level:int):
        self.klass = data ['klass']
        self.id = data['id']
        self.dbSymbol = data['dbSymbol']
        self.forms = data ['forms']
        self.evolutions = data ['evolutions']
        self.type = self.get_types()
        self.baseHp = self.forms[0]['baseHp']
        self.baseAtk = self.forms[0]['baseAtk']
        self.baseDfe = self.forms[0]['baseDfe']
        self.baseSpd = self.forms[0]['baseSpd']
        self.baseAts = self.forms[0]['baseAts']
        self.baseDfs = self.forms[0]['baseDfs']
        self.evHp = self.forms[0]['evHp']