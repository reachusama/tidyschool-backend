# Generated by Django 3.2.12 on 2022-03-26 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0002_ai_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='account.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='account.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='SupplyInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher', models.ManyToManyField(to='account.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalPlanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher', models.ManyToManyField(to='account.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.ManyToManyField(to='teacher.School')),
            ],
        ),
    ]
