# Generated by Django 3.1.4 on 2020-12-21 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('title', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=512, null=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='matcher_app.candidate')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='matcher_app.job')),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='matcher_app.skill'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='skills',
            field=models.ManyToManyField(blank=True, related_name='candidates', to='matcher_app.Skill'),
        ),
    ]
