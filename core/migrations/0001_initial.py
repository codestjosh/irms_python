# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'core_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=105)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=105)),
        ))
        db.send_create_signal(u'core', ['Category'])

        # Adding model 'Designer'
        db.create_table(u'core_designer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=105)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=105)),
        ))
        db.send_create_signal(u'core', ['Designer'])

        # Adding model 'Products'
        db.create_table(u'core_products', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=105)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='product_category', to=orm['core.Category'])),
            ('designer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='product_designer', to=orm['core.Designer'])),
            ('colour', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('price', self.gf('django.db.models.fields.FloatField')()),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=105)),
            ('last_stocked_timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('on_sales_bool', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('entry_by', self.gf('django.db.models.fields.CharField')(max_length=105)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Products'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'core_category')

        # Deleting model 'Designer'
        db.delete_table(u'core_designer')

        # Deleting model 'Products'
        db.delete_table(u'core_products')


    models = {
        u'core.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '105'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '105'})
        },
        u'core.designer': {
            'Meta': {'object_name': 'Designer'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '105'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '105'})
        },
        u'core.products': {
            'Meta': {'object_name': 'Products'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'product_category'", 'to': u"orm['core.Category']"}),
            'colour': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '105'}),
            'designer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'product_designer'", 'to': u"orm['core.Designer']"}),
            'entry_by': ('django.db.models.fields.CharField', [], {'max_length': '105'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'last_stocked_timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '105'}),
            'on_sales_bool': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'quantity': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['core']