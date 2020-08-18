# Generated by Django 3.0.8 on 2020-08-18 13:09

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('openwisp_notifications', '0005_delete_notificationuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObjectNotification',
            fields=[
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ('object_id', models.CharField(max_length=255)),
                ('valid_till', models.DateTimeField(null=True)),
                (
                    'object_content_type',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='contenttypes.ContentType',
                    ),
                ),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                'abstract': False,
                'swappable': 'OPENWISP_NOTIFICATIONS_OBJECTNOTIFICATION_MODEL',
                'ordering': ['valid_till'],
            },
        ),
    ]
