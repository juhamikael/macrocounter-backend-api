from backend.userdataprocess.ActivityLevel import ActivityLevel, ActivityType
import unittest


class TestActivityLevel(unittest.TestCase):
    def test_activity_level_sedentary(self):
        activity_level_sedentary = ActivityLevel(ActivityType.SEDENTARY)
        self.assertEqual(activity_level_sedentary.activity_level, 1.2)
        self.assertEqual(activity_level_sedentary.activity_level_text, ActivityType.SEDENTARY)

    def test_activity_level_light(self):
        activity_level_light = ActivityLevel(ActivityType.LIGHT)
        self.assertEqual(activity_level_light.activity_level, 1.3624)
        self.assertEqual(activity_level_light.activity_level_text, ActivityType.LIGHT)

    def test_activity_level_moderate(self):
        activity_level_moderate = ActivityLevel(ActivityType.MODERATE)
        self.assertEqual(activity_level_moderate.activity_level, 1.55)
        self.assertEqual(activity_level_moderate.activity_level_text, ActivityType.MODERATE)

    def test_activity_level_very_active(self):
        activity_level_active = ActivityLevel(ActivityType.ACTIVE)
        self.assertEqual(activity_level_active.activity_level, 1.709)
        self.assertEqual(activity_level_active.activity_level_text, ActivityType.ACTIVE)

    def test_activity_level_extra_active(self):
        activity_level_very_active = ActivityLevel(ActivityType.VERY_ACTIVE)
        self.assertEqual(activity_level_very_active.activity_level, 1.9)
        self.assertEqual(activity_level_very_active.activity_level_text, ActivityType.VERY_ACTIVE)


if __name__ == '__main__':
    unittest.main()
