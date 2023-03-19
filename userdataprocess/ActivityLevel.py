from enum import Enum


class ActivityType(str, Enum):
    SEDENTARY = "sedentary"
    LIGHT = "light"
    ACTIVE = "active"
    MODERATE = "moderate"
    VERY_ACTIVE = "very_active"


class ActivityLevel:
    def __init__(self, activity_type):
        self._activity_type = activity_type
        self._activity_level = self.activity_level
        self._activity_level_text = self._activity_type

    @property
    def activity_type(self):
        return self._activity_type

    @property
    def activity_level(self):
        if self._activity_type == ActivityType.SEDENTARY:
            self._activity_level = 1.2
        elif self._activity_type == ActivityType.LIGHT:
            self._activity_level = 1.3624
        elif self._activity_type == ActivityType.MODERATE:
            self._activity_level = 1.55
        elif self._activity_type == ActivityType.ACTIVE:
            self._activity_level = 1.709
        elif self._activity_type == ActivityType.VERY_ACTIVE:
            self._activity_level = 1.9
        return self._activity_level

    @property
    def activity_level_text(self):
        if self._activity_type == ActivityType.SEDENTARY:
            self._activity_level_text = "sedentary"
        elif self._activity_type == ActivityType.LIGHT:
            self._activity_level_text = "light"
        elif self._activity_type == ActivityType.ACTIVE:
            self._activity_level_text = "active"
        elif self._activity_type == ActivityType.MODERATE:
            self._activity_level_text = "moderate"
        elif self._activity_type == ActivityType.VERY_ACTIVE:
            self._activity_level_text = "very_active"
        return self._activity_level_text
