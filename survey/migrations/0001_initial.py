# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Survey'
        db.create_table(u'survey_survey', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('age', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('state', self.gf('django_localflavor_us.models.USStateField')(max_length=2)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('sexual_orientation', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('sexual_orientation_other', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('gender_identity', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('gender_identity_other', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('gender_assigned', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('ethnicity', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('ethnicity_other', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('current_body_shape_shoulders', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('current_body_shape_waist', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('current_body_shape_hips', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('ideal_body_shape_shoulders', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('ideal_body_shape_waist', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('ideal_body_shape_hips', self.gf('django.db.models.fields.IntegerField')(max_length=3)),
            ('exercise_stay_health', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('excercise_lose_weight', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('exercise_improve_appearance', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('exercise_energize', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('exercise_sport', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('exercise_fun', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('exercise_muscle', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('exercise_not', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('strenuous_activity_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('moderate_activity_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('strength_activity_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('strenuous_activity_days', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('moderate_activity_days', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('strength_activity_days', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('other_reasons', self.gf('django.db.models.fields.TextField')()),
            ('self_esteem', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('time_to_exercise', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('exercise_enjoyable', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('exercise_risk_age', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('exercise_poor_health', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('exercise_lack_skills', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('exercise_lack_funds', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('exercise_intimidation', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('exercise_encouragement', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('exercise_get_enough', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('low_self_esteem', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('exercise_lack_access', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('exercise_safety_concern', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('exercise_inconvenient', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('exercise_goals', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('exercise_lgbtq_friendly', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('exercise_space_friendly', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('improve_lgbtq_spaces', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'survey', ['Survey'])


    def backwards(self, orm):
        # Deleting model 'Survey'
        db.delete_table(u'survey_survey')


    models = {
        u'survey.survey': {
            'Meta': {'object_name': 'Survey'},
            'age': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'current_body_shape_hips': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'current_body_shape_shoulders': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'current_body_shape_waist': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'ethnicity': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'ethnicity_other': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'excercise_lose_weight': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
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
            'exercise_muscle': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'exercise_not': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'exercise_poor_health': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'exercise_risk_age': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'exercise_safety_concern': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'exercise_space_friendly': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'exercise_sport': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'exercise_stay_health': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'gender_assigned': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
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