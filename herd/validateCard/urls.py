from django.urls import path
from validateCard import views

urlpatterns = [
    path('validate-card/',views.ValidateCardView.as_view()),
]