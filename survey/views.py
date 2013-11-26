from django.contrib.formtools.wizard.views import SessionWizardView
from django.views.generic import TemplateView, ListView
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core.exceptions import PermissionDenied
from survey.models import *

class SurveyWizard(SessionWizardView):
    instance = None

    def get_form_instance(self, step):
        if self.instance is None:
            self.instance = Survey()
        return self.instance

    def done(self, form_list, **kwargs):
        self.instance.save()
        return HttpResponseRedirect('http://www.rainbowhealth.org/survey/thanks/')#reverse('thanks'))

class Thanks(TemplateView):
    template_name = 'thanks.html'

class CSVModelExportResponseMixin(object):
    """
    Mixin that constructs a CSV response file from a Django model based on the requested
    list of objects.
    """
    model = None

    def render_to_response(self, context, **response_kwargs):
        # If `?export=csv` is in the GET variables.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=%s.csv' % (self.model.__name__)
        writer = csv.writer(response)
        headers = [field.name for field in self.model._meta.fields]
        writer.writerow(headers)
        # Double list comprehension, I'm a jerk, I know.
        # The inner comprehension loops over the fields in headers and the outer
        # comprehension loops over the objects in the queryset for the view.
        [writer.writerow([getattr(obj, field) for field in headers]) for obj in self.get_queryset()]
        return response

class Results(CSVModelExportResponseMixin, ListView):
    model = Survey
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied
        return super(Results, self).dispatch(request, *args, **kwargs)
