# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20150107_0843'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='addons',
            field=models.TextField(default=b'', null=True, blank=True, validators=[django.core.validators.MaxLengthValidator(1000)]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='armory_link',
            field=models.CharField(default=b'', max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='authenticator',
            field=models.CharField(default=b'', max_length=5, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='char_class',
            field=models.CharField(default=b'', max_length=15, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='char_spec',
            field=models.CharField(default=b'', max_length=15, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='computer_specs',
            field=models.TextField(default=b'', null=True, blank=True, validators=[django.core.validators.MaxLengthValidator(1000)]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='experience',
            field=models.TextField(default=b'', null=True, blank=True, validators=[django.core.validators.MaxLengthValidator(1000)]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='how_did_you_hear',
            field=models.TextField(default=b'', null=True, blank=True, validators=[django.core.validators.MaxLengthValidator(500)]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='main_character',
            field=models.CharField(default=b'', max_length=12, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='over_18',
            field=models.CharField(default=b'', max_length=4, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='previous_guild',
            field=models.TextField(default=b'', null=True, blank=True, validators=[django.core.validators.MaxLengthValidator(500)]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='recent_parses',
            field=models.TextField(default=b'', null=True, blank=True, validators=[django.core.validators.MaxLengthValidator(500)]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='screenshot',
            field=models.TextField(default=b'', max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='submitted_app',
            field=models.NullBooleanField(default=False),
            preserve_default=True,
        ),
    ]
