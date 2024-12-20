# Generated by Django 5.1.2 on 2024-11-11 13:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Subject Name')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Order')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
            options={
                'verbose_name': 'Subject',
                'verbose_name_plural': 'Subjects',
                'ordering': ['order', 'created_at'],
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(verbose_name='Question')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tests.subject', verbose_name='Subject')),
            ],
            options={
                'verbose_name': 'Test',
                'verbose_name_plural': 'Tests',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='TestQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField(verbose_name='Answer')),
                ('is_correct', models.BooleanField(default=False, verbose_name='Is Correct')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='tests.test', verbose_name='Test')),
            ],
            options={
                'verbose_name': 'Test Question',
                'verbose_name_plural': 'Test Questions',
            },
        ),
    ]
