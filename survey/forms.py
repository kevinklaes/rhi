from django import forms
from django_localflavor_us.forms import USZipCodeField

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from survey.models import *

PAGE_THREE_CHOICE_SET = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7))

class PageOne(forms.ModelForm):
    zipcode = USZipCodeField()

    def __init__(self, *args, **kwargs):
        super(PageOne, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.add_input(Submit('submit', 'Next Page'))

    class Meta:
        model = Survey
        fields = ('age', 'state', 'zipcode', 'sexual_orientation', 'sexual_orientation_other', 'gender_identity', 'gender_identity_other', 'gender_assigned',
                    'ethnicity', 'ethnicity_other',)

class PageTwo(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PageTwo, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.add_input(Submit('submit', 'Next Page'))

    class Meta:
        model = Survey
        fields = ('current_body_shape_shoulders', 'current_body_shape_waist', 'current_body_shape_hips',
                    'ideal_body_shape_shoulders', 'ideal_body_shape_waist', 'ideal_body_shape_hips',)

class PageThree(forms.ModelForm):
    exercise_stay_health = forms.ChoiceField(widget = forms.RadioSelect(), choices=PAGE_THREE_CHOICE_SET)
    exercise_lose_weight = forms.ChoiceField(widget = forms.RadioSelect(), choices=PAGE_THREE_CHOICE_SET)
    exercise_improve_appearance = forms.ChoiceField(widget = forms.RadioSelect(), choices=PAGE_THREE_CHOICE_SET)
    exercise_energize = forms.ChoiceField(widget = forms.RadioSelect(), choices=PAGE_THREE_CHOICE_SET)
    exercise_sport = forms.ChoiceField(widget = forms.RadioSelect(), choices=PAGE_THREE_CHOICE_SET)
    exercise_fun = forms.ChoiceField(widget = forms.RadioSelect(), choices=PAGE_THREE_CHOICE_SET)
    exercise_muscle  = forms.ChoiceField(widget = forms.RadioSelect(), choices=PAGE_THREE_CHOICE_SET)
    exercise_not = forms.ChoiceField(widget = forms.RadioSelect(), choices=PAGE_THREE_CHOICE_SET)
    
    def __init__(self, *args, **kwargs):
        super(PageThree, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.add_input(Submit('submit', 'Next Page'))

    class Meta:
        model = Survey
        fields = ('exercise_stay_health', 'exercise_lose_weight', 'exercise_improve_appearance', 'exercise_energize',
                    'exercise_sport', 'exercise_fun', 'exercise_muscle', 'exercise_not',)

class PageFour(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PageFour, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.add_input(Submit('submit', 'Next Page'))

    class Meta:
        model = Survey
        fields = ('strenuous_activity_type', 'moderate_activity_type', 'strength_activity_type',
                    'strenuous_activity_days', 'moderate_activity_days', 'strength_activity_days',)

class PageFive(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PageFive, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.add_input(Submit('submit', 'Next Page'))

    class Meta:
        model = Survey
        fields = ('self_esteem', 'time_to_exercise', 'exercise_enjoyable', 'exercise_risk_age', 'exercise_poor_health', 'exercise_lack_skills',
                    'exercise_lack_funds', 'exercise_intimidation', 'exercise_get_enough', 'low_self_esteem', 'exercise_lack_access',
                    'exercise_safety_concern', 'exercise_inconvenient', 'exercise_goals', 'exercise_lgbtq_friendly', 'exercise_space_friendly',
                    'improve_lgbtq_spaces',)

