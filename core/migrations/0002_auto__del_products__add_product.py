# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Products'
        db.delete_table(u'core_products')

        # Adding model 'Product'
        db.create_table(u'core_product', (
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
        db.send_create_signal(u'core', ['Product'])


    def backwards(self, orm):
        # Adding model 'Products'
        db.create_table(u'core_products', (
            ('designer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='product_designer', to=orm['core.Designer'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=105)),
            ('on_sales_bool', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('price', self.gf('django.db.models.fields.FloatField')()),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('entry_by', self.gf('django.db.models.fields.CharField')(max_length=105)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='product_category', to=orm['core.Category'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=105)),
            ('colour', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('last_stocked_timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'core', ['Products'])

        # Deleting model 'Product'
        db.delete_table(u'core_product')


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
        u'core.product': {
            'Meta': {'object_name': 'Product'},
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