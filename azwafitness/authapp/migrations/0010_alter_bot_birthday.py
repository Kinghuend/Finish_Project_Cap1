# Generated by Django 4.1.7 on 2023-04-26 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0009_rename_body_type_bot_physical_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot',
            name='birthday',
            field=models.CharField(max_length=20),
        ),
    ]
