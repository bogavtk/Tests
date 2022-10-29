# Generated by Django 4.1.2 on 2022-10-29 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calc_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('val1', models.IntegerField()),
                ('val2', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('result', models.CharField(blank=True, max_length=100, null=True)),
                ('operator', models.CharField(max_length=100)),
            ],
        ),
    ]