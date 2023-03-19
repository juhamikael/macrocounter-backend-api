from backend.userdataprocess.BMR import BMR, Gender
import unittest


class TestBMR(unittest.TestCase):

    def test_bmr_getters(self):
        weight = 50
        height = 175
        age = 30
        bmi = float(round(weight /
                          ((height / 100) * (height / 100)), 1))
        bmr = BMR(weight, height, age, Gender.MALE)
        self.assertEqual(bmr.gender, "male")
        self.assertEqual(bmr.weight, weight)
        self.assertEqual(bmr.height, height)
        self.assertEqual(bmr.age, age)
        self.assertEqual(bmr.bmi, bmi)

    def test_bmr_gender_type(self):
        bmr = BMR(50, 160, 20, Gender.MALE)
        self.assertIs(type(bmr.gender), Gender)
        bmr = BMR(50, 160, 20, Gender.FEMALE)
        self.assertIs(type(bmr.gender), Gender)

    def test_bmr_value_type(self):
        weight = 150
        height = 175
        age = 25
        bmr = BMR(weight, height, age, Gender.MALE)
        self.assertIs(type(bmr.bmr), int)
        self.assertIs(type(bmr.bmr7), int)

    def test_bmr_calculation_male(self):
        weight = 50
        height = 175
        age = 30
        gender = Gender.MALE
        bmr = BMR(weight, height, age, gender)
        mifflin_st_jeor = (10 * bmr.weight + (6.25 * bmr.height) - (5 * bmr.age) - 5)
        harris_benedict = (88.362 + (13.397 * bmr.weight) + (4.799 * bmr.height) - (5.677 * bmr.age))
        self.assertEqual(bmr.bmr, int((mifflin_st_jeor + harris_benedict) / 2))
