from django.contrib.formtools.wizard.views import SessionWizardView
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from survey.models import *

class SurveyWizard(SessionWizardView):
    instance = None

    def get_form_instance(self, step):
        if self.instance is None:
            self.instance = Survey()
        return self.instance

    def done(self, form_list, **kwargs):
        self.instance.save()
        return HttpResponseRedirect(reverse('thanks'))

class Thanks(TemplateView):
    template_name = 'thanks.html'
