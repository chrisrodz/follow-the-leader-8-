# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'A125.payments_paid'
        db.alter_column(u'ccomforms_a125', 'payments_paid', self.gf('djorm_pgarray.fields.ArrayField')(dbtype='text', null=True))

        # Changing field 'A125.sponsored_accounts'
        db.alter_column(u'ccomforms_a125', 'sponsored_accounts', self.gf('djorm_pgarray.fields.ArrayField')(dbtype='text', null=True))

        # Changing field 'A125.cost_sharing'
        db.alter_column(u'ccomforms_a125', 'cost_sharing', self.gf('djorm_pgarray.fields.ArrayField')(dbtype='text', null=True))

        # Changing field 'A125.total_compensation'
        db.alter_column(u'ccomforms_a125', 'total_compensation', self.gf('djorm_pgarray.fields.ArrayField')(dbtype='text', null=True))

        # Changing field 'A125.university_funds'
        db.alter_column(u'ccomforms_a125', 'university_funds', self.gf('djorm_pgarray.fields.ArrayField')(dbtype='text', null=True))

    def backwards(self, orm):

        # Changing field 'A125.payments_paid'
        db.alter_column(u'ccomforms_a125', 'payments_paid', self.gf('dbarray.CharArrayField')(max_length=50, null=True))

        # Changing field 'A125.sponsored_accounts'
        db.alter_column(u'ccomforms_a125', 'sponsored_accounts', self.gf('dbarray.CharArrayField')(max_length=50, null=True))

        # Changing field 'A125.cost_sharing'
        db.alter_column(u'ccomforms_a125', 'cost_sharing', self.gf('dbarray.CharArrayField')(max_length=50, null=True))

        # Changing field 'A125.total_compensation'
        db.alter_column(u'ccomforms_a125', 'total_compensation', self.gf('dbarray.CharArrayField')(max_length=50, null=True))

        # Changing field 'A125.university_funds'
        db.alter_column(u'ccomforms_a125', 'university_funds', self.gf('dbarray.CharArrayField')(max_length=50, null=True))

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
            'cost_sharing': ('djorm_pgarray.fields.ArrayField', [], {'default': 'None', 'dbtype': "'text'", 'null': 'True', 'blank': 'True'}),
            'date_filled': ('django.db.models.fields.DateField', [], {}),
            'effective_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'multi_campus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'payments_paid': ('djorm_pgarray.fields.ArrayField', [], {'default': 'None', 'dbtype': "'text'", 'null': 'True', 'blank': 'True'}),
            'period': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            'professor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'sponsored_accounts': ('djorm_pgarray.fields.ArrayField', [], {'default': 'None', 'dbtype': "'text'", 'null': 'True', 'blank': 'True'}),
            'ssn': ('django.db.models.fields.IntegerField', [], {'max_length': '9', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            'total_compensation': ('djorm_pgarray.fields.ArrayField', [], {'default': 'None', 'dbtype': "'text'", 'null': 'True', 'blank': 'True'}),
            'university_funds': ('djorm_pgarray.fields.ArrayField', [], {'default': 'None', 'dbtype': "'text'", 'null': 'True', 'blank': 'True'})
        },
        u'ccomforms.t02': {
            'Ano_Fiscal': ('django.db.models.fields.IntegerField', [], {}),
            'Meta': {'object_name': 'T02'},
            'Num_Referencia': ('django.db.models.fields.IntegerField', [], {}),
            'Transaccion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'date_filled': ('django.db.models.fields.DateField', [], {}),
            'f1': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'f10': ('djorm_pgarray.fields.ArrayField', [], {'default': 'None', 'dbtype': "'text'", 'null': 'True', 'blank': 'True'}),
            'f11': ('djorm_pgarray.fields.ArrayField', [], {'default': 'None', 'dbtype': "'text'", 'null': 'True', 'blank': 'True'}),
            'f12': ('djorm_pgarray.fields.ArrayField', [], {'default': 'None', 'dbtype': "'text'", 'null': 'True', 'blank': 'True'}),
            'f13': ('djorm_pgarray.fields.ArrayField', [], {'default': 'None', 'dbtype': "'text'", 'null': 'True', 'blank': 'True'}),
            'f14': ('djorm_pgarray.fields.ArrayField', [], {'default': 'None', 'dbtype': "'text'", 'null': 'True', 'blank': 'True'}),
            'f15': ('djorm_pgarray.fields.ArrayField', [], {'default': 'None', 'dbtype': "'text'", 'null': 'True', 'blank': 'True'}),
            'f16': ('djorm_pgarray.fields.ArrayField', [], {'default': 'None', 'dbtype': "'text'", 'null': 'True', 'blank': 'True'}),
            'f17': ('djorm_pgarray.fields.ArrayField', [], {'default': 'None', 'dbtype': "'text'", 'null': 'True', 'blank': 'True'}),
            'f18': ('djorm_pgarray.fields.ArrayField', [], {'default': 'None', 'dbtype': "'text'", 'null': 'True', 'blank': 'True'}),
            'f19': ('djorm_pgarray.fields.ArrayField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'f2': ('django.db.models.fields.IntegerField', [], {'max_length': '9'}),
            'f20': ('djorm_pgarray.fields.ArrayField', [], {'default': 'None', 'dbtype': "'real'", 'null': 'True', 'blank': 'True'}),
            'f21': ('djorm_pgarray.fields.ArrayField', [], {'default': 'None', 'dbtype': "'text'", 'null': 'True', 'blank': 'True'}),
            'f22': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'f23': ('djorm_pgarray.fields.ArrayField', [], {'default': 'None', 'dbtype': "'text'", 'null': 'True', 'blank': 'True'}),
            'f24': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'f25': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'f26': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'f27': ('djorm_pgarray.fields.ArrayField', [], {'default': 'None', 'dbtype': "'text'", 'null': 'True', 'blank': 'True'}),
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