# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'A125.name'
        db.add_column(u'ccomforms_a125', 'name',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'A125.ssn'
        db.add_column(u'ccomforms_a125', 'ssn',
                      self.gf('django.db.models.fields.IntegerField')(max_length=9, null=True),
                      keep_default=False)

        # Adding field 'A125.title'
        db.add_column(u'ccomforms_a125', 'title',
                      self.gf('django.db.models.fields.CharField')(max_length=1, null=True),
                      keep_default=False)

        # Adding field 'A125.base_salary'
        db.add_column(u'ccomforms_a125', 'base_salary',
                      self.gf('django.db.models.fields.FloatField')(null=True),
                      keep_default=False)

        # Adding field 'A125.period'
        db.add_column(u'ccomforms_a125', 'period',
                      self.gf('django.db.models.fields.CharField')(max_length=1, null=True),
                      keep_default=False)

        # Adding field 'A125.effective_date'
        db.add_column(u'ccomforms_a125', 'effective_date',
                      self.gf('django.db.models.fields.DateField')(null=True),
                      keep_default=False)

        # Adding field 'A125.multi_campus'
        db.add_column(u'ccomforms_a125', 'multi_campus',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'A125.sponsored_accounts'
        db.add_column(u'ccomforms_a125', 'sponsored_accounts',
                      self.gf('dbarray.CharArrayField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'A125.cost_sharing'
        db.add_column(u'ccomforms_a125', 'cost_sharing',
                      self.gf('dbarray.CharArrayField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'A125.university_funds'
        db.add_column(u'ccomforms_a125', 'university_funds',
                      self.gf('dbarray.CharArrayField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'A125.total_compensation'
        db.add_column(u'ccomforms_a125', 'total_compensation',
                      self.gf('dbarray.CharArrayField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'A125.payments_paid'
        db.add_column(u'ccomforms_a125', 'payments_paid',
                      self.gf('dbarray.CharArrayField')(max_length=50, null=True),
                      keep_default=False)

        # Adding field 'A125.comments'
        db.add_column(u'ccomforms_a125', 'comments',
                      self.gf('django.db.models.fields.TextField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'A125.name'
        db.delete_column(u'ccomforms_a125', 'name')

        # Deleting field 'A125.ssn'
        db.delete_column(u'ccomforms_a125', 'ssn')

        # Deleting field 'A125.title'
        db.delete_column(u'ccomforms_a125', 'title')

        # Deleting field 'A125.base_salary'
        db.delete_column(u'ccomforms_a125', 'base_salary')

        # Deleting field 'A125.period'
        db.delete_column(u'ccomforms_a125', 'period')

        # Deleting field 'A125.effective_date'
        db.delete_column(u'ccomforms_a125', 'effective_date')

        # Deleting field 'A125.multi_campus'
        db.delete_column(u'ccomforms_a125', 'multi_campus')

        # Deleting field 'A125.sponsored_accounts'
        db.delete_column(u'ccomforms_a125', 'sponsored_accounts')

        # Deleting field 'A125.cost_sharing'
        db.delete_column(u'ccomforms_a125', 'cost_sharing')

        # Deleting field 'A125.university_funds'
        db.delete_column(u'ccomforms_a125', 'university_funds')

        # Deleting field 'A125.total_compensation'
        db.delete_column(u'ccomforms_a125', 'total_compensation')

        # Deleting field 'A125.payments_paid'
        db.delete_column(u'ccomforms_a125', 'payments_paid')

        # Deleting field 'A125.comments'
        db.delete_column(u'ccomforms_a125', 'comments')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'ccomforms.a125': {
            'Meta': {'object_name': 'A125'},
            'base_salary': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'cost_sharing': ('dbarray.CharArrayField', [], {'max_length': '50', 'null': 'True'}),
            'date_filled': ('django.db.models.fields.DateField', [], {}),
            'effective_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'multi_campus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'payments_paid': ('dbarray.CharArrayField', [], {'max_length': '50', 'null': 'True'}),
            'period': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            'professor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'sponsored_accounts': ('dbarray.CharArrayField', [], {'max_length': '50', 'null': 'True'}),
            'ssn': ('django.db.models.fields.IntegerField', [], {'max_length': '9', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            'total_compensation': ('dbarray.CharArrayField', [], {'max_length': '50', 'null': 'True'}),
            'university_funds': ('dbarray.CharArrayField', [], {'max_length': '50', 'null': 'True'})
        },
        u'ccomforms.t02': {
            'Ano_Fiscal': ('django.db.models.fields.IntegerField', [], {}),
            'Meta': {'object_name': 'T02'},
            'Num_Referencia': ('django.db.models.fields.IntegerField', [], {}),
            'Transaccion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'date_filled': ('django.db.models.fields.DateField', [], {}),
            'f1': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'f10': ('dbarray.CharArrayField', [], {'max_length': '50'}),
            'f11': ('dbarray.CharArrayField', [], {'max_length': '50'}),
            'f12': ('dbarray.CharArrayField', [], {'max_length': '50'}),
            'f13': ('dbarray.CharArrayField', [], {'max_length': '50'}),
            'f14': ('dbarray.CharArrayField', [], {'max_length': '50'}),
            'f15': ('dbarray.CharArrayField', [], {'max_length': '50'}),
            'f16': ('dbarray.CharArrayField', [], {'max_length': '50'}),
            'f17': ('dbarray.CharArrayField', [], {'max_length': '50'}),
            'f18': ('dbarray.CharArrayField', [], {'max_length': '50'}),
            'f19': ('dbarray.IntegerArrayField', [], {}),
            'f2': ('django.db.models.fields.IntegerField', [], {'max_length': '9'}),
            'f20': ('dbarray.FloatArrayField', [], {}),
            'f21': ('dbarray.CharArrayField', [], {'max_length': '50'}),
            'f22': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'f23': ('dbarray.CharArrayField', [], {'max_length': '50'}),
            'f24': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'f25': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'f26': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'f27': ('dbarray.CharArrayField', [], {'max_length': '50'}),
            'f3': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'f30': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'f5': ('django.db.models.fields.FloatField', [], {}),
            'f6': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'f8': ('django.db.models.fields.DateField', [], {}),
            'f9': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'professor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['ccomforms']