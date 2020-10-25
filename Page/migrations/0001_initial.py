# Generated by Django 3.1.2 on 2020-10-25 10:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Directory', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300)),
                ('comments', models.CharField(blank=True, max_length=1000)),
                ('link', models.URLField()),
                ('directory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='Directory.directory')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
