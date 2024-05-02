from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError
from openai import OpenAIError
from ...models import Terms, Definitions, Languages, ReadingLevels

class Command(BaseCommand):
    help="creates terms and definitions for the glossary"
    num_of_items = 10

    def handle(self, *args, **options):
        pass