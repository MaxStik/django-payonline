from django.urls import path
from .views import PayView, CallbackView, FailView, SuccessView


urlpatterns = [
    path('', PayView.as_view(), name='payonline_pay'),
    path('callback/', CallbackView.as_view(), name='payonline_callback'),
    path('fail/', FailView.as_view(), name='payonline_fail'),
    path('success/', SuccessView.as_view(), name='payonline_success'),
]
