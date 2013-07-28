# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Survey.excercise_lose_weight'
        db.delete_column(u'survey_survey', 'excercise_lose_weight')

        # Adding field 'Survey.exercise_lose_weight'
        db.add_column(u'survey_survey', 'exercise_lose_weight',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=1),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Survey.excercise_lose_weight'
        raise RuntimeError("Cannot reverse this migration. 'Survey.excercise_lose_weight' and its values cannot be restored.")
        # Deleting field 'Survey.exercise_lose_weight'
        db.delete_column(u'survey_survey', 'exercise_lose_weight')


    models = {
        u'survey.survey': {
            'Meta': {'object_name': 'Survey'},
            'age': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'current_body_shape_hips': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'current_body_shape_shoulders': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'current_body_shape_waist': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'ethnicity': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'ethnicity_other': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'exercise_encouragement': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'exercise_energize': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'exercise_enjoyable': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'exercise_fun': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'exercise_get_enough': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'exercise_goals': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'exercise_improve_appearance': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'exercise_inconvenient': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'exercise_intimidation': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'exercise_lack_access': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'exercise_lack_funds': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'exercise_lack_skills': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'exercise_lgbtq_friendly': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'exercise_lose_weight': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'exercise_muscle': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'exercise_not': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'exercise_poor_health': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'exercise_risk_age': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'exercise_safety_concern': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'exercise_space_friendly': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'exercise_sport': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'exercise_stay_health': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'gender_assigned': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'gender_identity': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'gender_identity_other': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ideal_body_shape_hips': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'ideal_body_shape_shoulders': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'ideal_body_shape_waist': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'improve_lgbtq_spaces': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'low_self_esteem': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'moderate_activity_days': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'moderate_activity_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'other_reasons': ('django.db.models.fields.TextField', [], {}),
            'self_esteem': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'sexual_orientation': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'sexual_orientation_other': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'state': ('django_localflavor_us.models.USStateField', [], {'max_length': '2'}),
            'strength_activity_days': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'strength_activity_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'strenuous_activity_days': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'strenuous_activity_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'time_to_exercise': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['survey']