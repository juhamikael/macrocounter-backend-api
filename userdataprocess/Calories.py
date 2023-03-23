from enum import Enum


class DietStyle(str, Enum):
    HEAVY_BULKING = "heavy_bulking"
    NORMAL_BULKING = "bulking"
    MILD_BULKING = "mild_bulking"
    MAINTAIN_WEIGHT = "maintain_weight"
    MILD_WEIGHT_LOSS = "mild_weight_loss"
    WEIGHT_LOSS = "weight_loss"
    EXTREME_WEIGHT_LOSS = "extreme_weight_loss"


class CaloriesIntake:
    def __init__(self, bmr: int, activity_level: int, diet_style: str, age: int):
        self._diet_style = diet_style
        self.bmr = bmr
        self.activity_level = activity_level
        self.age = age
        self._weight_loss_multiplier = None
        self._age_multiplier = None
        self._calories_daily = None
        self._calories_weekly = None

    @property
    def age_multiplier(self):
        if self.age < 30:
            self._age_multiplier = 1
        elif 30 <= self.age < 50:
            self._age_multiplier = 0.95
        elif 50 <= self.age < 70:
            self._age_multiplier = 0.9
        else:
            self._age_multiplier = 0.85
        return self._age_multiplier

    @property
    def weight_loss_multiplier(self):
        # Different weight loss styles, using Enum for this
        if self._diet_style == DietStyle.HEAVY_BULKING:
            self._weight_loss_multiplier = 1.2
        elif self._diet_style == DietStyle.NORMAL_BULKING:
            self._weight_loss_multiplier = 1.1
        elif self._diet_style == DietStyle.MILD_BULKING:
            self._weight_loss_multiplier = 1.05
        elif self._diet_style == DietStyle.MAINTAIN_WEIGHT:
            self._weight_loss_multiplier = 1
        elif self._diet_style == DietStyle.MILD_WEIGHT_LOSS:
            self._weight_loss_multiplier = 0.9224
        elif self._diet_style == DietStyle.WEIGHT_LOSS:
            self._weight_loss_multiplier = 0.8445
        elif self._diet_style == DietStyle.EXTREME_WEIGHT_LOSS:
            self._weight_loss_multiplier = 0.689
        # Each have different multiplier, we need this to count daily calories intake
        return self._weight_loss_multiplier

    @property
    def calories_daily(self):
        return int(self.bmr * self.weight_loss_multiplier * self.activity_level * self.age_multiplier)

    @property
    def calories_weekly(self):
        return int(self.bmr * self.weight_loss_multiplier * self.activity_level * self.age_multiplier * 7)
