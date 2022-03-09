from .views import LandingTemplateView, LiveStreamLandingTemplateView
from django.urls import include
from django.urls import path

app_name = 'landing'
urlpatterns = [
    # Report Dashboard
    path('', LandingTemplateView.as_view(), name='management'),

    path('live/', LiveStreamLandingTemplateView.as_view(), name='live'),

    # # Report
    # path(
    #     'reports/',
    #     include('apps.pages.report_management.urls', namespace='reports')
    # ),

    # # Products
    # path(
    #     'products/',
    #     include('apps.pages.product_management.urls', namespace='products')
    # ),


    # # Data
    # path(
    #     'data/',
    #     include('apps.pages.data_management.urls', namespace='data')
    # ),


]
