# Generated by Django 5.1.3 on 2024-12-11 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0016_alter_job_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bookmarkjob',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='job',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
