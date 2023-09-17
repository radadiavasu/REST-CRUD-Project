# Generated by Django 4.2 on 2023-09-17 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0003_alter_employee_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='about',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='address',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='company',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='email',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='position',
        ),
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.CharField(default='department', max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='code',
            field=models.CharField(default='code', max_length=8),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(default='name', max_length=50),
        ),
        migrations.DeleteModel(
            name='Company',
        ),
    ]