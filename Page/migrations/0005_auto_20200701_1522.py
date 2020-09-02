# Generated by Django 3.0.6 on 2020-07-01 09:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Directory', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Page', '0004_auto_20200530_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='directory',
        ),
        migrations.AddField(
            model_name='page',
            name='directory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='Directory.Directory'),
        ),
        migrations.AlterField(
            model_name='page',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages', to=settings.AUTH_USER_MODEL),
        ),
    ]
