import unittest
from backend.userdataprocess.MacroSplit import BodyType, MacroSplit


class TestMacroSplit(unittest.TestCase):
    daily_calories = 2000
    endomorph = BodyType.ENDOMORPH
    mesomorph = BodyType.MESOMORPH
    ectomorph = BodyType.ECTOMORPH

    def test_protein(self):
        self.assertEqual(MacroSplit(self.daily_calories, self.ectomorph).protein, 125)
        self.assertEqual(MacroSplit(self.daily_calories, self.mesomorph).protein, 150)
        self.assertEqual(MacroSplit(self.daily_calories, self.endomorph).protein, 175)

    def test_carbs(self):
        self.assertEqual(MacroSplit(self.daily_calories, self.ectomorph).carbs, 275)
        self.assertEqual(MacroSplit(self.daily_calories, self.mesomorph).carbs, 200)
        self.assertEqual(MacroSplit(self.daily_calories, self.endomorph).carbs, 125)

    def test_fat(self):
        self.assertEqual(MacroSplit(self.daily_calories, self.ectomorph).fat, 44)
        self.assertEqual(MacroSplit(self.daily_calories, self.mesomorph).fat, 66)
        self.assertEqual(MacroSplit(self.daily_calories, self.endomorph).fat, 88)

    def test_macro_split_body_type(self):
        self.assertEqual(MacroSplit(self.daily_calories, self.ectomorph).body_type, self.ectomorph)
        self.assertEqual(MacroSplit(self.daily_calories, "mesomorph").body_type, self.mesomorph)

    def test_macro_multipliers_with_enum(self):
        self.assertEqual(MacroSplit(self.daily_calories, self.ectomorph).multipliers, [0.25, 0.55, 0.2])
        self.assertEqual(MacroSplit(self.daily_calories, self.mesomorph).multipliers, [0.3, 0.4, 0.3])
        self.assertEqual(MacroSplit(self.daily_calories, self.endomorph).multipliers, [0.35, 0.25, 0.4])

    def test_macro_multipliers_with_str(self):
        self.assertEqual(MacroSplit(self.daily_calories, "ectomorph").multipliers, [0.25, 0.55, 0.2])
        self.assertEqual(MacroSplit(self.daily_calories, "mesomorph").multipliers, [0.3, 0.4, 0.3])
        self.assertEqual(MacroSplit(self.daily_calories, "endomorph").multipliers, [0.35, 0.25, 0.4])

    def test_protein_multiplier(self):
        self.assertEqual(MacroSplit(self.daily_calories, self.ectomorph).protein_multiplier, 0.25)
        self.assertEqual(MacroSplit(self.daily_calories, self.mesomorph).protein_multiplier, 0.3)
        self.assertEqual(MacroSplit(self.daily_calories, self.endomorph).protein_multiplier, 0.35)

    def test_carbs_multiplier(self):
        self.assertEqual(MacroSplit(self.daily_calories, self.ectomorph).carbs_multiplier, 0.55)
        self.assertEqual(MacroSplit(self.daily_calories, self.mesomorph).carbs_multiplier, 0.4)
        self.assertEqual(MacroSplit(self.daily_calories, self.endomorph).carbs_multiplier, 0.25)

    def test_fat_multiplier(self):
        self.assertEqual(MacroSplit(self.daily_calories, self.ectomorph).fat_multiplier, 0.2)
        self.assertEqual(MacroSplit(self.daily_calories, self.mesomorph).fat_multiplier, 0.3)
        self.assertEqual(MacroSplit(self.daily_calories, self.endomorph).fat_multiplier, 0.4)

    def test_ectomorph_multipliers(self):
        self.assertEqual(MacroSplit(self.daily_calories, self.ectomorph).protein_multiplier, 0.25)
        self.assertEqual(MacroSplit(self.daily_calories, self.ectomorph).carbs_multiplier, 0.55)
        self.assertEqual(MacroSplit(self.daily_calories, self.ectomorph).fat_multiplier, 0.2)

    def test_mesomorph_multipliers(self):
        self.assertEqual(MacroSplit(self.daily_calories, self.mesomorph).protein_multiplier, 0.3)
        self.assertEqual(MacroSplit(self.daily_calories, self.mesomorph).carbs_multiplier, 0.4)
        self.assertEqual(MacroSplit(self.daily_calories, self.mesomorph).fat_multiplier, 0.3)

    def test_endomorph_multipliers(self):
        self.assertEqual(MacroSplit(self.daily_calories, self.endomorph).protein_multiplier, 0.35)
        self.assertEqual(MacroSplit(self.daily_calories, self.endomorph).carbs_multiplier, 0.25)
        self.assertEqual(MacroSplit(self.daily_calories, self.endomorph).fat_multiplier, 0.4)


if __name__ == '__main__':
    unittest.main()
