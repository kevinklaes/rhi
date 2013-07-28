from django.contrib.formtools.wizard.views import SessionWizardView
from django.http import HttpResponse

from survey.models import *

class SurveyWizard(SessionWizardView):
    instance = None

    def get_form_instance(self, step):
        if self.instance is None:
            self.instance = Survey()
        return self.instance

    def done(self, form_list, **kwargs):
        self.instance.save()
        return HttpResponse('Thanks')
