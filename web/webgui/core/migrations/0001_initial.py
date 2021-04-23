# Generated by Django 3.1.7 on 2021-04-23 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(max_length=255, unique=True)),
                ('comment', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Release',
                'verbose_name_plural': 'Release',
                'db_table': 'Release',
            },
        ),
        migrations.CreateModel(
            name='SFibersStackHitFinderPar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameters', models.TextField()),
                ('valid_from', models.DateTimeField()),
                ('valid_to', models.DateTimeField()),
                ('version', models.IntegerField()),
                ('remarks', models.CharField(blank=True, max_length=255, null=True)),
                ('release', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sfibersstackhitfinderpar_versions', to='core.release')),
            ],
            options={
                'verbose_name': 'SFibersStackHitFinderPar',
                'verbose_name_plural': 'SFibersStackHitFinderPar',
                'db_table': 'SFibersStackHitFinderPar',
            },
        ),
        migrations.CreateModel(
            name='SFibersStackHitFinderFiberPar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameters', models.TextField()),
                ('valid_from', models.DateTimeField()),
                ('valid_to', models.DateTimeField()),
                ('version', models.IntegerField()),
                ('remarks', models.CharField(blank=True, max_length=255, null=True)),
                ('release', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sfibersstackhitfinderfiberpar_versions', to='core.release')),
            ],
            options={
                'verbose_name': 'SFibersStackHitFinderFiberPar',
                'verbose_name_plural': 'SFibersStackHitFinderFiberPar',
                'db_table': 'SFibersStackHitFinderFiberPar',
            },
        ),
        migrations.CreateModel(
            name='SFibersStackGeomPar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameters', models.TextField()),
                ('valid_from', models.DateTimeField()),
                ('valid_to', models.DateTimeField()),
                ('version', models.IntegerField()),
                ('remarks', models.CharField(blank=True, max_length=255, null=True)),
                ('release', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sfibersstackgeompar_versions', to='core.release')),
            ],
            options={
                'verbose_name': 'SFibersStackGeomPar',
                'verbose_name_plural': 'SFibersStackGeomPar',
                'db_table': 'SFibersStackGeomPar',
            },
        ),
        migrations.CreateModel(
            name='SFibersStackDigitizerPar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameters', models.TextField()),
                ('valid_from', models.DateTimeField()),
                ('valid_to', models.DateTimeField()),
                ('version', models.IntegerField()),
                ('remarks', models.CharField(blank=True, max_length=255, null=True)),
                ('release', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sfibersstackdigitizerpar_versions', to='core.release')),
            ],
            options={
                'verbose_name': 'SFibersStackDigitizerPar',
                'verbose_name_plural': 'SFibersStackDigitizerPar',
                'db_table': 'SFibersStackDigitizerPar',
            },
        ),
        migrations.CreateModel(
            name='SFibersStackDDUnpackerPar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameters', models.TextField()),
                ('valid_from', models.DateTimeField()),
                ('valid_to', models.DateTimeField()),
                ('version', models.IntegerField()),
                ('remarks', models.CharField(blank=True, max_length=255, null=True)),
                ('release', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sfibersstackddunpackerpar_versions', to='core.release')),
            ],
            options={
                'verbose_name': 'SFibersStackDDUnpackerPar',
                'verbose_name_plural': 'SFibersStackDDUnpackerPar',
                'db_table': 'SFibersStackDDUnpackerPar',
            },
        ),
        migrations.CreateModel(
            name='SFibersStackDDLookupTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameters', models.TextField()),
                ('valid_from', models.DateTimeField()),
                ('valid_to', models.DateTimeField()),
                ('version', models.IntegerField()),
                ('remarks', models.CharField(blank=True, max_length=255, null=True)),
                ('release', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sfibersstackddlookuptable_versions', to='core.release')),
            ],
            options={
                'verbose_name': 'SFibersStackDDLookupTable',
                'verbose_name_plural': 'SFibersStackDDLookupTable',
                'db_table': 'SFibersStackDDLookupTable',
            },
        ),
        migrations.CreateModel(
            name='SFibersStackCalibratorPar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameters', models.TextField()),
                ('valid_from', models.DateTimeField()),
                ('valid_to', models.DateTimeField()),
                ('version', models.IntegerField()),
                ('remarks', models.CharField(blank=True, max_length=255, null=True)),
                ('release', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sfibersstackcalibratorpar_versions', to='core.release')),
            ],
            options={
                'verbose_name': 'SFibersStackCalibratorPar',
                'verbose_name_plural': 'SFibersStackCalibratorPar',
                'db_table': 'SFibersStackCalibratorPar',
            },
        ),
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=255)),
                ('start_time', models.DateTimeField()),
                ('stop_time', models.DateTimeField()),
                ('remarks', models.CharField(blank=True, max_length=255, null=True)),
                ('run_id', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'files',
                'verbose_name_plural': 'files',
                'db_table': 'files',
                'unique_together': {('run_id', 'start_time', 'stop_time')},
            },
        ),
    ]
