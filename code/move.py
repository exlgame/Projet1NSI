import json


class Move:
    """
    Move class to manage the moves
    """
    def __init__(self, move_data):
        """
        Initialize the move
        :param move_data:
        """
        self.id = move_data.get('id')
        self.dbSymbol = move_data.get('dbSymbol')
        self.klass = move_data.get('klass')
        self.mapUse = move_data.get('mapUse')
        self.type = move_data.get('type')
        self.power = move_data.get('power')
        self.accuracy = move_data.get('accuracy')
        self.maxpp = move_data.get('pp')
        self.category = move_data.get('category')
        self.movecriticalRate = move_data.get('movecriticalRate')
        self.battleEngineMethod = move_data.get('battleEngineMethod')
        self.priority = move_data.get('priority')
        self.isDirect = move_data.get('isDirect')
        self.isCharge = move_data.get('isCharge')
        self.isRecharge = move_data.get('isRecharge')
        self.isBlocable = move_data.get('isBlocable')
        self.isSnatchable = move_data.get('isSnatchable')
        self.isMirrorMove = move_data.get('isMirrorMove')
        self.isPunch = move_data.get('isPunch')
        self.isGravity = move_data.get('isGravity')
        self.isMagicCoatAffected = move_data.get('isMagicCoatAffected')
        self.isUnfreeze = move_data.get('isUnfreeze')
        self.isSoundAttack = move_data.get('isSoundAttack')
        self.isDistance = move_data.get('isDistance')
        self.isHeal = move_data.get('isHeal')
        self.isAuthentic = move_data.get('isAuthentic')
        self.isBite = move_data.get('isBite')
        self.isPulse = move_data.get('isPulse')
        self.isBallistics = move_data.get('isBallistics')
        self.isMental = move_data.get('isMental')
        self.isNonSkyBattle = move_data.get('isNonSkyBattle')
        self.isDance = move_data.get('isDance')
        self.isKingRockUtility = move_data.get('isKingRockUtility')
        self.isPowder = move_data.get('isPowder')
        self.effectChance = move_data.get('effectChance')
        self.battleEngineAimedTarget = move_data.get('battleEngineAimedTarget')
        self.battleStageMod: list[dict] = move_data.get('battleStageMod')
        self.moveStatus = move_data.get('moveStatus')

        self.pp = self.maxpp

    @staticmethod
    def createMove(name: str) -> "Move":
        """
        Create a move from the name
        :param name:
        :return:
        """
        return Move(json.load(open(f"../assets/json/moves/{name.lower()}.json")))

    def to_dict(self):
        """
        Convertir l'objet Move en dictionnaire sérialisable.
        :return: dict
        """
        return {
            'id': self.id,
            'dbSymbol': self.dbSymbol,
            'klass': self.klass,
            'mapUse': self.mapUse,
            'type': self.type,
            'power': self.power,
            'accuracy': self.accuracy,
            'maxpp': self.maxpp,
            'pp': self.pp,
            'category': self.category,
            'movecriticalRate': self.movecriticalRate,
            'battleEngineMethod': self.battleEngineMethod,
            'priority': self.priority,
            'isDirect': self.isDirect,
            'isCharge': self.isCharge,
            'isRecharge': self.isRecharge,
            'isBlocable': self.isBlocable,
            'isSnatchable': self.isSnatchable,
            'isMirrorMove': self.isMirrorMove,
            'isPunch': self.isPunch,
            'isGravity': self.isGravity,
            'isMagicCoatAffected': self.isMagicCoatAffected,
            'isUnfreeze': self.isUnfreeze,
            'isSoundAttack': self.isSoundAttack,
            'isDistance': self.isDistance,
            'isHeal': self.isHeal,
            'isAuthentic': self.isAuthentic,
            'isBite': self.isBite,
            'isPulse': self.isPulse,
            'isBallistics': self.isBallistics,
            'isMental': self.isMental,
            'isNonSkyBattle': self.isNonSkyBattle,
            'isDance': self.isDance,
            'isKingRockUtility': self.isKingRockUtility,
            'isPowder': self.isPowder,
            'effectChance': self.effectChance,
            'battleEngineAimedTarget': self.battleEngineAimedTarget,
            'battleStageMod': self.battleStageMod,
            'moveStatus': self.moveStatus
        }

    @staticmethod
    def from_dict(data: dict) -> "Move":
        """
        Recréer un Move à partir d'un dictionnaire.
        :param data: dict
        :return: Move
        """
        move = Move.__new__(Move)
        move.__dict__.update(data)
        return move
