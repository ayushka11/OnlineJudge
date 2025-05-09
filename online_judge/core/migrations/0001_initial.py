# Generated by Django 5.2 on 2025-04-08 07:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('description', models.TextField()),
                ('sample_input', models.TextField()),
                ('sample_output', models.TextField()),
                ('hidden_inputs', models.JSONField()),
                ('hidden_outputs', models.JSONField()),
                ('tags', models.CharField(max_length=225)),
                ('rating', models.IntegerField(default=0)),
                ('total_submissions', models.IntegerField(default=0)),
                ('correct_submissions', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('time_limit', models.IntegerField(default=1)),
                ('memory_limit', models.IntegerField(default=128)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('cpp', 'C++'), ('java', 'Java'), ('python', 'Python'), ('c', 'C')], max_length=10)),
                ('code', models.TextField()),
                ('compiled_code', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('ACCEPTED', 'Accepted'), ('TLE', 'Time Limit Exceeded'), ('WA', 'Wrong Answer'), ('RTE', 'Runtime Error'), ('CE', 'Compilation Error')], default='PENDING', max_length=20)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('submission_time', models.IntegerField(default=0)),
                ('submission_memory', models.IntegerField(default=0)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.problem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
