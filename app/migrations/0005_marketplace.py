# Generated by Django 3.1.7 on 2021-03-14 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210313_2301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marketplace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodname', models.CharField(blank=True, max_length=150, null=True)),
                ('quantity', models.FloatField(null=True)),
                ('phonenumber', models.CharField(blank=True, max_length=20, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
                ('image', models.ImageField(upload_to='marketplace/')),
            ],
        ),
    ]
