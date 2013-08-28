from django import forms
from django_localflavor_us.forms import USZipCodeField

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder
from crispy_forms.bootstrap import InlineRadios

from survey.models import *

class PageOne(forms.ModelForm):
    zipcode = USZipCodeField()
    #sexual_orientation = forms.ChoiceField(widget = forms.RadioSelect(), choices = SEXUAL_ORIENTATION_CHOICES)
    #gender_identity = forms.ChoiceField(widget = forms.RadioSelect(), choices = GENDER_CHOICES)
    #gender_assigned = forms.ChoiceField(widget = forms.RadioSelect(), choices = GENDER_CHOICES_ASSIGNED)
    #ethnicity = forms.ModelMultipleChoiceField(queryset = Ethnicity.objects.all(), widget=forms.CheckboxSelectMultiple)

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
    current_body_shape_shoulders = forms.CharField(widget = forms.HiddenInput())
    current_body_shape_waist = forms.CharField(widget = forms.HiddenInput())
    current_body_shape_hips = forms.CharField(widget = forms.HiddenInput())
    ideal_body_shape_shoulders = forms.CharField(widget = forms.HiddenInput())
    ideal_body_shape_waist = forms.CharField(widget = forms.HiddenInput())
    ideal_body_shape_hips = forms.CharField(widget = forms.HiddenInput())
    
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
        self.helper.layout = Layout('',
                                    InlineRadios('exercise_stay_health'),
                                    InlineRadios('exercise_lose_weight'),
                                    InlineRadios('exercise_improve_appearance'),
                                    InlineRadios('exercise_energize'),
                                    InlineRadios('exercise_sport'),
                                    InlineRadios('exercise_fun'),
                                    InlineRadios('exercise_muscle'),
                                    InlineRadios('exercise_not'),)

    class Meta:
        model = Survey
        fields = ('exercise_stay_health', 'exercise_lose_weight', 'exercise_improve_appearance', 'exercise_energize',
                    'exercise_sport', 'exercise_fun', 'exercise_muscle', 'exercise_not',)

class PageFour(forms.ModelForm):
    strenuous_activity_type = forms.ChoiceField(widget = forms.RadioSelect(), choices=PAGE_FOUR_CHOICE_SET_EXERCISE_TYPE)
    moderate_activity_type = forms.ChoiceField(widget = forms.RadioSelect(), choices=PAGE_FOUR_CHOICE_SET_EXERCISE_TYPE)
    strength_activity_type = forms.ChoiceField(widget = forms.RadioSelect(), choices=PAGE_FOUR_CHOICE_SET_EXERCISE_TYPE)
    strenuous_activity_days = forms.ChoiceField(widget = forms.RadioSelect(), choices=PAGE_FOUR_CHOICE_SET_DAYS)
    moderate_activity_days = forms.ChoiceField(widget = forms.RadioSelect(), choices=PAGE_FOUR_CHOICE_SET_DAYS)
    strength_activity_days = forms.ChoiceField(widget = forms.RadioSelect(), choices=PAGE_FOUR_CHOICE_SET_DAYS)

    def __init__(self, *args, **kwargs):
        super(PageFour, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.add_input(Submit('submit', 'Next Page'))
        self.helper.layout = Layout('',
                                InlineRadios('strenuous_activity_type'),
                                InlineRadios('moderate_activity_type'),
                                InlineRadios('strength_activity_type'),
                                InlineRadios('strenuous_activity_days'),
                                InlineRadios('moderate_activity_days'),
                                InlineRadios('strength_activity_days'),)

    class Meta:
        model = Survey
        fields = ('strenuous_activity_type', 'moderate_activity_type', 'strength_activity_type',
                    'strenuous_activity_days', 'moderate_activity_days', 'strength_activity_days',)

class PageFive(forms.ModelForm):
    self_esteem = forms.ChoiceField(widget = forms.RadioSelect(), choices=PAGE_FIVE_CHOICE_SET)
    time_to_exercise = forms.ChoiceField(widget = forms.RadioSelect(), choices=PAGE_FIVE_CHOICE_SET)
    exercise_enjoyable = forms.ChoiceField(widget = forms.RadioSelect(), choices=PAGE_FIVE_CHOICE_SET)
    exercise_risk_age = forms.ChoiceField(widget = forms.RadioSelect(), choices=PAGE_FIVE_CHOICE_SET)
    exercise_poor_health = forms.ChoiceField(widget = forms.RadioSelect(), choices=PAGE_FIVE_CHOICE_SET)
    exercise_lack_skills = forms.ChoiceField(widget = forms.RadioSelect(), choices=PAGE_FIVE_CHOICE_SET)
    exercise_lack_funds = forms.ChoiceField(widget = forms.RadioSelect(), choices=PAGE_FIVE_CHOICE_SET)
    exercise_intimidation = forms.ChoiceField(widget = forms.RadioSelect(), choices=PAGE_FIVE_CHOICE_SET)
    exercise_lack_access = forms.ChoiceField(widget = forms.RadioSelect(), choices=PAGE_FIVE_CHOICE_SET)
    exercise_get_enough = forms.ChoiceField(widget = forms.RadioSelect(), choices=PAGE_FIVE_CHOICE_SET)
    low_self_esteem = forms.ChoiceField(widget = forms.RadioSelect(), choices=PAGE_FIVE_CHOICE_SET)
    exercise_safety_concern = forms.ChoiceField(widget = forms.RadioSelect(), choices=PAGE_FIVE_CHOICE_SET)
    exercise_inconvenient = forms.ChoiceField(widget = forms.RadioSelect(), choices=PAGE_FIVE_CHOICE_SET)
    exercise_goals  = forms.ChoiceField(widget = forms.RadioSelect(), choices=PAGE_FIVE_CHOICE_SET)

    def __init__(self, *args, **kwargs):
        super(PageFive, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.add_input(Submit('submit', 'Next Page'))
        self.helper.layout = Layout('',
                                    InlineRadios('self_esteem'),
                                    InlineRadios('time_to_exercise'),
                                    InlineRadios('exercise_enjoyable'),
                                    InlineRadios('exercise_risk_age'),
                                    InlineRadios('exercise_poor_health'),
                                    InlineRadios('exercise_lack_skills'),
                                    InlineRadios('exercise_lack_funds'),
                                    InlineRadios('exercise_intimidation'),
                                    InlineRadios('exercise_get_enough'),
                                    InlineRadios('low_self_esteem'),
                                    InlineRadios('exercise_lack_access'),
                                    InlineRadios('exercise_safety_concern'),
                                    InlineRadios('exercise_inconvenient'),
                                    InlineRadios('exercise_goals'),)

    class Meta:
        model = Survey
        fields = ('self_esteem', 'time_to_exercise', 'exercise_enjoyable', 'exercise_risk_age', 'exercise_poor_health', 'exercise_lack_skills',
                    'exercise_lack_funds', 'exercise_intimidation', 'exercise_get_enough', 'low_self_esteem', 'exercise_lack_access',
                    'exercise_safety_concern', 'exercise_inconvenient', 'exercise_goals', 'exercise_lgbtq_friendly', 'exercise_space_friendly',
                    'improve_lgbtq_spaces',)

