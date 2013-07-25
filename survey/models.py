from django.db import models
from django_localflavor_us.models import USStateField
SEXUAL_ORIENTATION_CHOICES  = (('Lesbian', 'Lesbian'),
                                ('Gay', 'Gay'),
                                ('Bisexual', 'Bisexual'),
                                ('Queer', 'Queer'),
                                ('Straight/Heterosexual', 'Straight/Heterosexual'),
                                ('Other', 'Other'))
GENDER_CHOICES = (('Male', 'Male'), 
                  ('Female', 'Female'), 
                  ('Trans male / Trans man', 'Trans male / Trans man'), 
                  ('Trans female / Trans woman', 'Trans female / Trans woman'), 
                  ('Genderqueer / Gender Non-conforming', 'Genderqueer / Gender Non-conforming'), 
                  ('Other', 'Other'),)
GENDER_CHOICES_ASSIGNED = (('Male', 'Male'),
                            ('Female', 'Female'),
                            ('Interex', 'Interex'),)
ETHNICITY_CHOICES = (('Black / African American', 'Black / African American'), 
                    ('African-born', 'African-born'),
                    ('Non-Hispanic White / Caucasian', 'Non-Hispanic White / Caucasian'),
                    ('Hispanic / Latino', 'Hispanic / Latino'),
                    ('American Indian / Native American', 'American Indian / Native American'),
                    ('Native Hawaiian / Pacific Islander', 'Native Hawaiian / Pacific Islander'),  
                    ('Hmong', 'Hmong'),
                    ('Asian Indian', 'Asian Indian'),
                    ('Chinese', 'Chinese'),
                    ('Japanese', 'Japanese'),
                    ('Vietnamese', 'Vietnamese'),
                    ('Korean', 'Korean'),
                    ('Filipino', 'Filipino'),
                    ('Laotian', 'Laotian'),
                    ('Cambodian', 'Cambodian'),
                    ('Other', 'Other'),)
PAGE_THREE_CHOICE_SET = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7))
PAGE_FOUR_CHOICE_SET_EXERCISE_TYPE = ((0, 'None'),
                                        (1, 'Less than 1/2 an hour'),
                                        (2, '1/2 - 2 hours'),
                                        (3, '2 1/5 - 4 hours'),
                                        (4, '4 1/2 - 6 hours'),
                                        (5, '6 1/2 hours or more'),)
PAGE_FOUR_CHOICE_SET_DAYS = ((1, '1 day'), (2, '2 days'), (3, '3 days'), (4, '4 days'), (5, '5 days'), (6, '6 days'), (7, '7 days'))
PAGE_FIVE_CHOICE_SET = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7))
PAGE_FIVE_CHOICE_SET_YNNS = (('Yes', 'Yes'), ('No', 'No'), ('Dont\' know / Not sure', 'Don\'t know / Not sure'))

class Survey(models.Model):
    # Page 1
    age = models.IntegerField('How old are you?', max_length=3)
    state = USStateField('What state do you live in?')
    zipcode = models.CharField('In which zip code do you live?', max_length=10)
    sexual_orientation = models.CharField('What best describes your sexual orientation?', max_length=30, choices=SEXUAL_ORIENTATION_CHOICES)
    sexual_orientation_other = models.CharField(max_length=30, blank=True, null=True)
    gender_identity = models.CharField('What is your current gender identity?', max_length=40, choices=GENDER_CHOICES)
    gender_identity_other = models.CharField(max_length=40, blank=True, null=True)
    gender_assigned = models.CharField('What sex were you assigned at birth, meaning on your original birth certificate?', max_length=20, choices=GENDER_CHOICES_ASSIGNED)
    ethnicity = models.CharField('What best describes your racial/ethnic background?', help_text='(please check all that apply)', max_length=40, choices=ETHNICITY_CHOICES)
    ethnicity_other = models.CharField(max_length=40, blank=True, null=True)
    
    # Page 2 - The device
    current_body_shape_shoulders = models.IntegerField(max_length=3)
    current_body_shape_waist = models.IntegerField(max_length=3)
    current_body_shape_hips = models.IntegerField(max_length=3)
    
    ideal_body_shape_shoulders = models.IntegerField(max_length=3)
    ideal_body_shape_waist = models.IntegerField(max_length=3)
    ideal_body_shape_hips = models.IntegerField(max_length=3)

    # Page 3
    exercise_stay_health = models.CharField('I exercise to stay healthy and prevent health problems.', max_length=1, choices=PAGE_THREE_CHOICE_SET)
    exercise_lose_weight = models.CharField('I exercise to lose weight.', max_length=1, choices=PAGE_THREE_CHOICE_SET)
    exercise_improve_appearance = models.CharField('I exercise to improve my appearance.', max_length=1, choices=PAGE_THREE_CHOICE_SET)
    exercise_energize = models.CharField('I exercise because it energizes me.', max_length=1, choices=PAGE_THREE_CHOICE_SET)
    exercise_sport = models.CharField('I exercise to train for a sport or event.', max_length=1, choices=PAGE_THREE_CHOICE_SET)
    exercise_fun = models.CharField('I exercise because I find it fun.', max_length=1, choices=PAGE_THREE_CHOICE_SET)
    exercise_muscle = models.CharField('I exercise to increase my muscle mass.', max_length=1, choices=PAGE_THREE_CHOICE_SET)
    exercise_not = models.CharField('I do not exercise.', max_length=1, choices=PAGE_THREE_CHOICE_SET)

    # Page 4
    strenuous_activity_type = models.CharField(max_length=1, choices=PAGE_FOUR_CHOICE_SET_EXERCISE_TYPE)
    moderate_activity_type = models.CharField(max_length=1, choices=PAGE_FOUR_CHOICE_SET_EXERCISE_TYPE)
    strength_activity_type = models.CharField(max_length=1, choices=PAGE_FOUR_CHOICE_SET_EXERCISE_TYPE)
    other_reasons = models.TextField()

    strenuous_activity_days = models.CharField(max_length=1, choices=PAGE_FOUR_CHOICE_SET_DAYS)
    moderate_activity_days = models.CharField(max_length=1, choices=PAGE_FOUR_CHOICE_SET_DAYS)
    strength_activity_days = models.CharField(max_length=1, choices=PAGE_FOUR_CHOICE_SET_DAYS)

    other_reasons = models.TextField()

    # Page 5
    self_esteem = models.CharField(max_length=1, choices=PAGE_FIVE_CHOICE_SET)
    time_to_exercise = models.CharField(max_length=1, choices=PAGE_FIVE_CHOICE_SET)
    exercise_enjoyable = models.CharField(max_length=1, choices=PAGE_FIVE_CHOICE_SET)
    exercise_risk_age = models.CharField(max_length=1, choices=PAGE_FIVE_CHOICE_SET)
    exercise_poor_health = models.CharField(max_length=1, choices=PAGE_FIVE_CHOICE_SET)
    exercise_lack_skills = models.CharField(max_length=1, choices=PAGE_FIVE_CHOICE_SET)
    exercise_lack_funds = models.CharField(max_length=1, choices=PAGE_FIVE_CHOICE_SET)
    exercise_intimidation = models.CharField(max_length=1, choices=PAGE_FIVE_CHOICE_SET)
    exercise_encouragement = models.CharField(max_length=1, choices=PAGE_FIVE_CHOICE_SET)
    exercise_get_enough = models.CharField(max_length=1, choices=PAGE_FIVE_CHOICE_SET)
    low_self_esteem = models.CharField(max_length=1, choices=PAGE_FIVE_CHOICE_SET)
    exercise_lack_access = models.CharField(max_length=1, choices=PAGE_FIVE_CHOICE_SET)
    exercise_safety_concern = models.CharField(max_length=1, choices=PAGE_FIVE_CHOICE_SET)
    exercise_inconvenient = models.CharField(max_length=1, choices=PAGE_FIVE_CHOICE_SET)
    exercise_goals = models.CharField(max_length=1, choices=PAGE_FIVE_CHOICE_SET)
    exercise_lgbtq_friendly = models.CharField(max_length=25, choices=PAGE_FIVE_CHOICE_SET_YNNS)
    exercise_space_friendly = models.CharField(max_length=200)
    improve_lgbtq_spaces = models.CharField(max_length=200)
