# Generated by Django 3.0.8 on 2020-07-03 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200703_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_choice',
            field=models.CharField(choices=[('Boast', 'Boast'), ('Roast', 'Roast')], default='Boast', max_length=6),
        ),
    ]
