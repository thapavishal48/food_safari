# Generated by Django 2.2.3 on 2019-08-06 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resturants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_example', models.CharField(choices=[('A', 'aa'), ('B', 'bb'), ('C', 'cc')], max_length=20)),
            ],
        ),
    ]