# Generated by Django 2.1.3 on 2018-11-25 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BandModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('genre', models.CharField(max_length=50)),
                ('history', models.CharField(blank=True, max_length=255, null=True)),
                ('pic', models.FileField(default='static/default.jpg', upload_to='static/')),
            ],
            options={
                'db_table': 'band',
            },
        ),
        migrations.CreateModel(
            name='MemberModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('birthdate', models.DateField()),
                ('deathdate', models.DateField(blank=True, null=True)),
                ('country', models.CharField(max_length=30)),
                ('photo', models.FileField(blank=True, default='static/default.jpg', upload_to='static/')),
            ],
            options={
                'db_table': 'member',
            },
        ),
        migrations.CreateModel(
            name='MembershipModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('function', models.CharField(max_length=50)),
                ('statuss', models.BooleanField(default=1)),
                ('id_band_FK', models.ForeignKey(db_column='id_band_FK', on_delete=django.db.models.deletion.CASCADE, to='MMB.BandModel')),
                ('id_member_FK', models.ForeignKey(db_column='id_member_FK', on_delete=django.db.models.deletion.CASCADE, to='MMB.MemberModel')),
            ],
            options={
                'db_table': 'membership',
            },
        ),
        migrations.AddField(
            model_name='bandmodel',
            name='members',
            field=models.ManyToManyField(blank=True, null=True, through='MMB.MembershipModel', to='MMB.MemberModel'),
        ),
    ]
