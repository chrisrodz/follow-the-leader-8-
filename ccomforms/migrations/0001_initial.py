# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'T02'
        db.create_table(u'ccomforms_t02', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_filled', self.gf('django.db.models.fields.DateField')()),
            ('professor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('Ano_Fiscal', self.gf('django.db.models.fields.IntegerField')()),
            ('Num_Referencia', self.gf('django.db.models.fields.IntegerField')()),
            ('Transaccion', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('f1', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('f2', self.gf('django.db.models.fields.IntegerField')(max_length=9)),
            ('f3', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('f5', self.gf('django.db.models.fields.FloatField')()),
            ('f6', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('f8', self.gf('django.db.models.fields.DateField')()),
            ('f9', self.gf('django.db.models.fields.DateField')()),
            ('f10', self.gf('dbarray.CharArrayField')(max_length=50)),
            ('f11', self.gf('dbarray.CharArrayField')(max_length=50)),
            ('f12', self.gf('dbarray.CharArrayField')(max_length=50)),
            ('f13', self.gf('dbarray.CharArrayField')(max_length=50)),
            ('f14', self.gf('dbarray.CharArrayField')(max_length=50)),
            ('f15', self.gf('dbarray.CharArrayField')(max_length=50)),
            ('f16', self.gf('dbarray.CharArrayField')(max_length=50)),
            ('f17', self.gf('dbarray.CharArrayField')(max_length=50)),
            ('f18', self.gf('dbarray.CharArrayField')(max_length=50)),
            ('f19', self.gf('dbarray.IntegerArrayField')()),
            ('f20', self.gf('dbarray.FloatArrayField')()),
            ('f21', self.gf('dbarray.CharArrayField')(max_length=50)),
            ('f22', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('f23', self.gf('dbarray.CharArrayField')(max_length=50)),
            ('f24', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('f25', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('f26', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('f27', self.gf('dbarray.CharArrayField')(max_length=50)),
            ('f30', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'ccomforms', ['T02'])


    def backwards(self, orm):
        # Deleting model 'T02'
        db.delete_table(u'ccomforms_t02')


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