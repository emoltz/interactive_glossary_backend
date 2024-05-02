from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response

from .models import Terms, Definitions, ChatLog


class GetTerms(APIView):
    @staticmethod
    def get(request):
        """
        get all terms
        """
        try:
            terms = Terms.objects.all()
            response = {
                "terms": [term.term for term in terms]
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
class GetTermsAndDefinitions(APIView):
    @staticmethod
    def post(request):
        """
        get all terms and definitions by grade level
        """
        try:
            grade_level: str = request.data.get("grade_level")
            terms = Terms.objects.all()
            definitions = Definitions.objects.filter(reading_level=grade_level)
            term_definiton_dict = {}
            list_of_terms = [term.term for term in terms]
            for term in list_of_terms:
                # get definitions of each term and add to dictionary
                term_definiton_dict[term] = [definition.definition for definition in definitions if definition.related_term.term == term]


            response = {
                "terms": term_definiton_dict
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)