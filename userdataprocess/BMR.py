from enum import Enum


class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"


class BMR:
    def __init__(self, weight: int, height: int, age: int, gender: str):
        self._weight = weight
        self._height = height
        self._age = age
        self._gender = gender
        mifflin_st_jeor = (10 * self._weight + (6.25 * self._height) - (5 * self._age))
        if self._gender == "male":
            mifflin_st_jeor -= 5
            harris_benedict = (
                    88.362 + (13.397 * self._weight) + (4.799 * self._height) - (5.677 * self._age))
        elif self._gender == "female":
            mifflin_st_jeor -= 161
            harris_benedict = (
                    447.593 + (9.247 * self._weight) + (3.098 * self._height) - (4.330 * self._age))
        else:
            mifflin_st_jeor = 0
            harris_benedict = 0

        self._bmr = int((mifflin_st_jeor + harris_benedict) / 2)
        self._bmi = float(round(self._weight /
                                ((self._height / 100) * (self._height / 100)), 1))

    @property
    def weight(self):
        return self._weight

    @property
    def height(self):
        return self._height

    @property
    def age(self):
        return self._age

    def set_gender(self):
        if self._gender == "male":
            self._gender = Gender.MALE
        elif self._gender == "female":
            self._gender = Gender.FEMALE

    @property
    def gender(self):
        return self._gender

    @property
    def bmr(self):
        return self._bmr

    @property
    def bmr7(self):
        return self._bmr * 7

    @property
    def bmi(self):
        return self._bmi
