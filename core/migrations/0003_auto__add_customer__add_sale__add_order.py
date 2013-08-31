# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Customer'
        db.create_table(u'core_customer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=105)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=105)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('mobile_platform', self.gf('django.db.models.fields.CharField')(default='android', max_length=15)),
            ('phone_no', self.gf('django.db.models.fields.CharField')(unique=True, max_length=15)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=105)),
            ('date_registered', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Customer'])

        # Adding model 'Sale'
        db.create_table(u'core_sale', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='Sales!!!', max_length=105)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(related_name='product_on_sale', to=orm['core.Product'])),
            ('sale_start_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('sale_end_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('regular_price', self.gf('django.db.models.fields.FloatField')()),
            ('sale_price', self.gf('django.db.models.fields.FloatField')()),
            ('conditions', self.gf('django.db.models.fields.TextField')()),
            ('sale_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Sale'])

        # Adding model 'Order'
        db.create_table(u'core_order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(related_name='product_ordered', to=orm['core.Product'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('is_wishlist_bool', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ordered_by', to=orm['core.Customer'])),
            ('order_platform', self.gf('django.db.models.fields.CharField')(max_length=55)),
            ('mobile_coord_upon_order', self.gf('django.db.models.fields.CharField')(max_length=105, null=True, blank=True)),
            ('order_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Order'])


    def backwards(self, orm):
        # Deleting model 'Customer'
        db.delete_table(u'core_customer')

        # Deleting model 'Sale'
        db.delete_table(u'core_sale')

        # Deleting model 'Order'
        db.delete_table(u'core_order')


    models = {
        u'core.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '105'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '105'})
        },
        u'core.customer': {
            'Meta': {'object_name': 'Customer'},
            'date_registered': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '105'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '105'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '105'}),
            'mobile_platform': ('django.db.models.fields.CharField', [], {'default': "'android'", 'max_length': '15'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'phone_no': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'core.designer': {
            'Meta': {'object_name': 'Designer'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '105'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '105'})
        },
        u'core.order': {
            'Meta': {'object_name': 'Order'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ordered_by'", 'to': u"orm['core.Customer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_wishlist_bool': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mobile_coord_upon_order': ('django.db.models.fields.CharField', [], {'max_length': '105', 'null': 'True', 'blank': 'True'}),
            'order_platform': ('django.db.models.fields.CharField', [], {'max_length': '55'}),
            'order_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'product_ordered'", 'to': u"orm['core.Product']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {})
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
        },
        u'core.sale': {
            'Meta': {'object_name': 'Sale'},
            'conditions': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Sales!!!'", 'max_length': '105'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'product_on_sale'", 'to': u"orm['core.Product']"}),
            'regular_price': ('django.db.models.fields.FloatField', [], {}),
            'sale_end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'sale_price': ('django.db.models.fields.FloatField', [], {}),
            'sale_start_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'sale_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']