# Generated by Django 2.0.13 on 2019-12-28 17:50
import datetime

import django.utils.timezone
from django.db import migrations
from django.db import models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [("webauthin", "0002_authdata_sign_count")]

    operations = [
        migrations.AddField(
            model_name="authdata",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True,
                default=datetime.datetime(2019, 12, 28, 17, 50, 48, 20406, tzinfo=utc),
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="authdata",
            name="last_used_on",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
