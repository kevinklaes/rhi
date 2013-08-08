from django.contrib import admin
from survey.models import *

class EthnicityAdmin(admin.ModelAdmin):
    pass

class SurveyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Ethnicity, EthnicityAdmin)
admin.site.register(Survey, SurveyAdmin)
