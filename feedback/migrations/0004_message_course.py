# Generated by Django 3.2.4 on 2021-08-27 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='feedback.course', verbose_name='course'),
        ),
    ]