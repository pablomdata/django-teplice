# Generated by Django 3.2.9 on 2021-11-09 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_auto_20211109_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='status',
            field=models.CharField(default='Favorite', max_length=200),
            preserve_default=False,
        ),
    ]