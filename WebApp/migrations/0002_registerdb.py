# Generated by Django 5.1.2 on 2024-10-26 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registerdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Email', models.EmailField(blank=True, max_length=50, null=True)),
                ('Mobile', models.IntegerField(blank=True, null=True)),
                ('Password', models.CharField(blank=True, max_length=50, null=True)),
                ('ConformPassword', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
