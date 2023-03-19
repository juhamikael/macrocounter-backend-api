from enum import Enum


class BodyType(str, Enum):
    ECTOMORPH = "ectomorph"
    MESOMORPH = "mesomorph"
    ENDOMORPH = "endomorph"


class MacroSplit:
    def __init__(self, daily_calories: int, body_type: str):
        self.daily_calories = daily_calories
        self._body_type = body_type
        self.protein_multiplier = self.multipliers[0]
        self.carbs_multiplier = self.multipliers[1]
        self.fat_multiplier = self.multipliers[2]
        self.base_protein = daily_calories / 4
        self.base_carbs = daily_calories / 4
        self.base_fat = daily_calories / 9

    @property
    def body_type(self):
        return self._body_type

    @property
    def multipliers(self):
        if self._body_type == BodyType.ECTOMORPH:
            self.protein_multiplier = 0.25
            self.carbs_multiplier = 0.55
            self.fat_multiplier = 0.2
        elif self._body_type == BodyType.MESOMORPH:
            self.protein_multiplier = 0.3
            self.carbs_multiplier = 0.4
            self.fat_multiplier = 0.3
        elif self._body_type == BodyType.ENDOMORPH:
            self.protein_multiplier = 0.35
            self.carbs_multiplier = 0.25
            self.fat_multiplier = 0.4
        return [self.protein_multiplier, self.carbs_multiplier, self.fat_multiplier]

    @property
    def protein(self):
        return int(self.base_protein * self.protein_multiplier)

    @property
    def carbs(self):
        return int(self.base_carbs * self.carbs_multiplier)

    @property
    def fat(self):
        return int(self.base_fat * self.fat_multiplier)
