# Generated by Django 2.0.3 on 2018-03-16 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schedules', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('task_to_day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedules.Days')),
            ],
        ),
    ]