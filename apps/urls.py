from django.urls import path

from apps.views import main, about, service, solution, contact, system_112, error_404_view

urlpatterns = [
    path('', main, name='main'),
    path('/about', about, name='about'),
    path('/services', service, name='service'),
    path('/solutions', solution, name='solution'),
    path('/contact', contact, name='contact'),
    path('/112', system_112, name='system_112'),
    path('404/', error_404_view, name='error_404'),
]