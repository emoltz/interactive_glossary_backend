from django.db import models
from enum import Enum

class Languages(Enum):
    ENGLISH = "english"
    SPANISH = "spanish"
    FRENCH = "french"
    GERMAN = "german"
    ITALIAN = "italian"
    PORTUGUESE = "portuguese"

class ReadingLevels(Enum):
    FIRST_GRADE = 1
    SECOND_GRADE = 2
    THIRD_GRADE = 3
    FOURTH_GRADE = 4
    FIFTH_GRADE = 5
    SIXTH_GRADE = 6
    SEVENTH_GRADE = 7
    EIGHTH_GRADE = 8
    NINTH_GRADE = 9
    TENTH_GRADE = 10
    ELEVENTH_GRADE = 11
    TWELFTH_GRADE = 12
    COLLEGE = 13
    ADULT = 14

class Terms(models.Model):
    term = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.term

class Definitions(models.Model):
    related_term = models.ForeignKey(Terms, on_delete=models.CASCADE, related_name='definitions')
    definition = models.TextField()
    language = models.CharField(max_length=20, choices=[(language.value, language.name) for language in Languages])
    reading_level = models.IntegerField(choices=[(level.value, level.name) for level in ReadingLevels])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.definition

class ChatLog(models.Model):
    user_id = models.CharField(max_length=200)
    session_id = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    related_term = models.ForeignKey(Terms, on_delete=models.CASCADE, related_name='chat_logs')

    def __str__(self):
        return f"{self.user_id} -- {self.session_id} -- {self.message}"
