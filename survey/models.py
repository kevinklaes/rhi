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
PAGE_THREE_CHOICE_SET = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'))
PAGE_FOUR_CHOICE_SET_EXERCISE_TYPE = (('None', 'None'),
                                        ('1', 'Less than 1/2 an hour'),
                                        ('2', '1/2 - 2 hours'),
                                        ('3', '2 1/5 - 4 hours'),
                                        ('4', '4 1/2 - 6 hours'),
                                        ('5', '6 1/2 hours or more'),)
PAGE_FOUR_CHOICE_SET_DAYS = (('0', '0 days'), ('1', '1 day'), ('2', '2 days'), ('3', '3 days'), ('4', '4 days'), ('5', '5 days'), ('6', '6 days'), ('7', '7 days'))
PAGE_FIVE_CHOICE_SET = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'))
PAGE_FIVE_CHOICE_SET_YNNS = (('Yes', 'Yes'), ('No', 'No'), ('Dont\' know / Not sure', 'Don\'t know / Not sure'))

class Ethnicity(models.Model):
    name = models.CharField('Ethnicity', max_length=40)

    def __unicode__(self):
        return self.name

class Survey(models.Model):
    # Page 1
    age = models.IntegerField('How old are you?', max_length=3)
    state = USStateField('What state do you live in?')
    zipcode = models.CharField('In which zip code do you live?', max_length=10)
    sexual_orientation = models.CharField('What best describes your sexual orientation?', max_length=30, choices=SEXUAL_ORIENTATION_CHOICES)
    sexual_orientation_other = models.CharField('If you chose other for your sexual orientation, please provide it here', max_length=30, blank=True, null=True)
    gender_identity = models.CharField('What is your current gender identity?', max_length=40, choices=GENDER_CHOICES)
    gender_identity_other = models.CharField('If you selected other for your gender identity, please provide it here.', max_length=40, blank=True, null=True)
    gender_assigned = models.CharField('What sex were you assigned at birth, meaning on your original birth certificate?', max_length=20, choices=GENDER_CHOICES_ASSIGNED)
    ethnicity = models.ManyToManyField(Ethnicity)
    #ethnicity = models.CharField('What best describes your racial/ethnic background?', help_text='(please check all that apply)', max_length=40, choices=ETHNICITY_CHOICES)
    ethnicity_other = models.CharField('If you selected other for ethnicity, please provide it here.', max_length=40, blank=True, null=True)
    
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

    exercise_other_reasons = models.TextField('If you have any other reasons for exercising, please list them below:', null=True, blank=True)

    # Page 4
    strenuous_activity_type = models.CharField('Strenuous activity (heart beats rapidly)', help_text=' Ex: biking fast, aerobics, running, basketball, swimming laps, rollerblading', max_length=4, choices=PAGE_FOUR_CHOICE_SET_EXERCISE_TYPE)
    moderate_activity_type = models.CharField('Moderate exercise (not exhausting)', help_text='Ex: walking quickly, easy biking, volleyball, yoga', max_length=4, choices=PAGE_FOUR_CHOICE_SET_EXERCISE_TYPE)
    strength_activity_type = models.CharField('Exercise to Strengthen or tone your muscles.', help_text='Ex: push-ups, sit-ups, weight lifting / training', max_length=4, choices=PAGE_FOUR_CHOICE_SET_EXERCISE_TYPE)

    strenuous_activity_days = models.CharField('Strenuous activity (heart beats rapidly)', help_text='Ex: biking fast, aerobics, running, basketball, swimming laps, rollerblading', max_length=1, choices=PAGE_FOUR_CHOICE_SET_DAYS)
    moderate_activity_days = models.CharField('Moderate exercise (not exhausting)', help_text='Ex: walking quickly, easy biking, volleyball, yoga', max_length=1, choices=PAGE_FOUR_CHOICE_SET_DAYS)
    strength_activity_days = models.CharField('Exercise to Strengthen or tone your muscles.', help_text='Ex: push-ups, sit-ups, weight lifting / training', max_length=1, choices=PAGE_FOUR_CHOICE_SET_DAYS)

    # Page 5
    self_esteem = models.CharField('Overall, I have high self-esteem.', max_length=1, choices=PAGE_FIVE_CHOICE_SET)
    time_to_exercise = models.CharField('I do not have enough time to exercise.', max_length=1, choices=PAGE_FIVE_CHOICE_SET)
    exercise_enjoyable = models.CharField('I do not find exercise enjoyable.', max_length=1, choices=PAGE_FIVE_CHOICE_SET)
    exercise_risk_age = models.CharField('I\'m getting older so exercise can be risky.', max_length=1, choices=PAGE_FIVE_CHOICE_SET)
    exercise_poor_health = models.CharField('I have poor health so exercise can be risky.', max_length=1, choices=PAGE_FIVE_CHOICE_SET)
    exercise_lack_skills = models.CharField('I do not get enough exercise because I have never learned the skills for any sport.', max_length=1, choices=PAGE_FIVE_CHOICE_SET)
    exercise_lack_funds = models.CharField('I think it\'s too expensive to include physical activity in my life. You have to take a class or join a club or buy the right equipment.', max_length=1, choices=PAGE_FIVE_CHOICE_SET)
    exercise_intimidation = models.CharField('I feel intimidated about going to a gym or fitness club. I worry I won\'t know what I\'m doing and/or that others will judge me.', max_length=1, choices=PAGE_FIVE_CHOICE_SET)
    exercise_encouragement = models.CharField('I feel I don\'t have enough encouragement, companionship, or support from friends and family to exercise.', max_length=1, choices=PAGE_FIVE_CHOICE_SET)
    exercise_get_enough = models.CharField('I feel that I do get enough exercise.', max_length=1, choices=PAGE_FIVE_CHOICE_SET)
    low_self_esteem = models.CharField('Overall, I have low self-esteem.', max_length=1, choices=PAGE_FIVE_CHOICE_SET)
    exercise_lack_access = models.CharField('I do not have access to places to exercise.', max_length=1, choices=PAGE_FIVE_CHOICE_SET)
    exercise_safety_concern = models.CharField('I do not feel safe or comfortable in the fitness spaces available to me.', max_length=1, choices=PAGE_FIVE_CHOICE_SET)
    exercise_inconvenient = models.CharField('I find it inconvenient to exercise.', max_length=1, choices=PAGE_FIVE_CHOICE_SET)
    exercise_goals = models.CharField('I have difficulty setting exercise goals, monitoring progress, and rewarding my own progress towards those goals.', max_length=1, choices=PAGE_FIVE_CHOICE_SET)
    exercise_lgbtq_friendly = models.CharField('Do you feel like you have access to an LGBTQ-friendly exercise environment? This could be a fitness center, classes, a park, a sports team, etc.', max_length=25, choices=PAGE_FIVE_CHOICE_SET_YNNS)
    exercise_space_friendly = models.TextField('How do you know if an exercise space is LGBTQ friendly? For example, do you notice signage, staff, or other people exercising?', max_length=400, blank=True, null=True)
    improve_lgbtq_spaces = models.TextField('What could spaces or activities do to become more friendly and welcoming to the LGBTQ community?', max_length=400, blank=True, null=True)
