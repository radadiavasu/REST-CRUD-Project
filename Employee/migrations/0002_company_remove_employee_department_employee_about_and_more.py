# Generated by Django 4.2 on 2023-09-17 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=250)),
                ('about', models.TextField()),
                ('type', models.CharField(choices=[('I.T', 'I.T'), ('Non IT', 'Non IT'), ('Electronics', 'Electronics'), ('Corporate Services', 'Corporate Services'), ('Ecommerce Service Providers', 'Ecommerce Service Providers'), ('Game Development', 'Game Development')], max_length=100)),
                ('added_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='department',
        ),
        migrations.AddField(
            model_name='employee',
            name='about',
            field=models.TextField(default='No information provided'),
        ),
        migrations.AddField(
            model_name='employee',
            name='address',
            field=models.CharField(default='No address provided', max_length=200),
        ),
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.CharField(default='example@example.com', max_length=50),
        ),
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=models.CharField(default='0000000000', max_length=10),
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.CharField(choices=[('Manager', 'Manager'), ('Software Developer', 'Software Developer'), ('Project Leader', 'Project Leader')], default='Manager', max_length=50),
        ),
        migrations.AddField(
            model_name='employee',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Employee.company'),
        ),
    ]