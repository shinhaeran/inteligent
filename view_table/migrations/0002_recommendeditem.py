# Generated by Django 2.2.5 on 2019-11-13 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('view_table', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecommendedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=45)),
                ('product', models.CharField(max_length=45)),
                ('frequency', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'recommended_item',
                'managed': False,
            },
        ),
    ]