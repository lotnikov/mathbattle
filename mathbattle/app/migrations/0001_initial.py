# Generated by Django 4.2 on 2023-04-09 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('DateStart', models.DateField(blank=True, verbose_name='Дата начала')),
                ('DateEnd', models.DateField(blank=True, verbose_name='Дата окончания')),
                ('Address', models.CharField(max_length=255)),
                ('Phone', models.CharField(max_length=30)),
                ('Logo', models.ImageField(blank=True, upload_to='photo/tournaments/%Y/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
