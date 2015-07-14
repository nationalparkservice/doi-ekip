from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from .views import (
    learn, student_pass, educator_passes, pass_exchange, educator_vouchers, 
    EducatorFormPreview)

from .forms import EducatorForm

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(
        template_name="main_landing.html"), name="main_landing"),

    # GET YOUR PASS
    url(r'get-your-pass/fourth-grader', student_pass, name="student_pass"),
    url(r'get-your-pass/educator/vouchers/', educator_vouchers, name="educator_vouchers"),
    url(r'get-your-pass/educator', EducatorFormPreview(EducatorForm), name="educator_passes"),
    url(r'get-your-pass/', TemplateView.as_view(
        template_name="get_your_pass.html"), name="get_your_pass"),

    # PLAN YOUR TRIP
    url(r'plan-your-trip/pass-exchange/', pass_exchange, name="pass_exchange"),
    url(r'plan-your-trip/', TemplateView.as_view(
        template_name="plan_your_trip.html"), name="plan_your_trip"),

    # LEARN
    url(r'learn/', learn, name="learn"),
)
