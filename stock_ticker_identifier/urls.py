"""stock_ticker_identifier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls.static import static

from graphene_django.views import GraphQLView

from rest_framework.routers import DefaultRouter

from publicly_traded_companies.views import ExchangesView, ExchangeView, CompaniesView, CompanyView, IndustriesView, \
    IndustryView, SectorsView, SectorView
from publicly_traded_companies.schema import schema

router = DefaultRouter()

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^exchanges/$', ExchangesView.as_view(), name='exchanges_list'),
    url(r'^exchanges/(?P<pk>[0-9]+)$', ExchangeView.as_view(), name='exchange_detail'),

    url(r'^industries/$', IndustriesView.as_view(), name='industries_list'),
    url(r'^industry/(?P<pk>[0-9]+)$', IndustryView.as_view(), name='industry_detail'),

    url(r'^sectors/$', SectorsView.as_view(), name='sectors_list'),
    url(r'^sector/(?P<pk>[0-9]+)$', SectorView.as_view(), name='sector_detail'),

    url(r'^companies/$', CompaniesView.as_view(), name='companies_list'),
    url(r'^companies/(?P<pk>[0-9]+)$', CompanyView.as_view(), name='company_detail'),

    url(r'^graphql', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema)))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
