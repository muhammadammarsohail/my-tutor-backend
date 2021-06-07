# Generated by Django 3.2.4 on 2021-06-07 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0003_auto_20210606_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='is_graduate',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='is_master',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='speaks_english',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='transactionMethod',
        ),
        migrations.AddField(
            model_name='teacher',
            name='education',
            field=models.CharField(default='abc', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='intro',
            field=models.CharField(default='abc', max_length=300),
            preserve_default=False,
        ),
    ]