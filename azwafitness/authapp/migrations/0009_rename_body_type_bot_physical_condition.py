# Generated by Django 4.1.7 on 2023-04-26 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0008_alter_bot_birthday'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bot',
            old_name='body_type',
            new_name='physical_Condition',
        ),
    ]