import json
from dataclasses import dataclass
from typing import List

from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError
from openai import OpenAIError
from ...models import Terms, Definitions, Languages, ReadingLevels
from ...open_ai_connect import OpenAIConnect


@dataclass
class Term:
    term: str
    definition: str
    reading_level: int

    def to_json(self):
        """Convert the Term instance into a JSON string."""
        return json.dumps(self.__dict__)


class Command(BaseCommand):
    help = "creates terms and definitions for the glossary"
    num_of_items = 10
    json_format = """
    {
        "term": "your term here",
        "definition": "your definition here",
        "reading_level": 8
    }
    """
    connection = OpenAIConnect(max_tokens=4000, json_format=json_format, timeout=60)
    prompt = f"""
    Please provide a list of {num_of_items} math terms and definitions in json format: {json_format} \n
    Make sure the definitions are at an 8th grade reading level. 
    """

    def handle(self, *args, **options):
        # first generate the terms and definitions
        try:
            response_json = self.connection.get_response(prompt=self.prompt)
        except OpenAIError as e:
            raise CommandError("Error in generatewordlist.py: ", e)

        # parse the response
        response_dict = json.loads(response_json)["terms"]
        # then store them in the database
        for term in response_dict:
            try:
                term_obj = Terms.objects.create(term=term["term"])
                reading_level: int = int(term["reading_level"])
                definition_obj = Definitions.objects.create(related_term=term_obj, definition=term["definition"],
                                                            language=Languages.ENGLISH.value,
                                                            reading_level=reading_level)
                term_obj.save()
                definition_obj.save()
            except IntegrityError as e:
                raise CommandError("Error in generatewordlist.py: ", e)
        self.stdout.write(self.style.SUCCESS(f"Successfully created {len(response_dict)} terms and definitions."))