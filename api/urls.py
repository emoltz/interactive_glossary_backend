from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import GetTermsAndDefinitions, GetTerms

urlpatterns = [
    # TODO figure out how to text this from angular frontend
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # other api paths...
    path('all_terms_by_grade_level/', GetTermsAndDefinitions.as_view(), name='all_terms_by_grade_level'),
    path('get_terms/', GetTerms.as_view(), name='get_terms')

]
