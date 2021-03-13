# Generated by Django 3.1.7 on 2021-03-13 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_warehouse'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransportItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(null=True)),
                ('time_created', models.DateField(auto_now_add=True)),
                ('dispatchtime', models.DateTimeField()),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
                ('Location', models.CharField(blank=True, max_length=100, null=True)),
                ('drive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver_name', to='app.driver')),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.aadhar')),
            ],
        ),
    ]