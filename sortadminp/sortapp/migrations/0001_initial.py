# Generated by Django 4.2 on 2023-05-15 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analyser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('analyser_name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sma_id', models.PositiveIntegerField(unique=True)),
                ('analisys_name', models.CharField(max_length=50, unique=True)),
                ('host_code', models.CharField(max_length=10, unique=True)),
                ('dead_volume', models.PositiveSmallIntegerField()),
                ('test_volume', models.PositiveSmallIntegerField()),
                ('lih_flag', models.BooleanField()),
                ('description', models.CharField(max_length=50)),
                ('analyzer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sortapp.analyser')),
            ],
        ),
        migrations.CreateModel(
            name='ContainerType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('container_type', models.CharField(max_length=20, unique=True)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=20, unique=True)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('routine_name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=50)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sortapp.location')),
            ],
        ),
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workflow', models.CharField(max_length=30, unique=True)),
                ('description', models.CharField(max_length=50)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sortapp.location')),
            ],
        ),
        migrations.CreateModel(
            name='SortArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_area', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=50)),
                ('routine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sortapp.routine')),
            ],
        ),
        migrations.CreateModel(
            name='AnalysisRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('analysis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sortapp.analysis')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sortapp.location')),
                ('sort_area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sortapp.sortarea')),
                ('workflow', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sortapp.workflow')),
            ],
        ),
        migrations.AddField(
            model_name='analysis',
            name='container_type_main',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='main', to='sortapp.containertype'),
        ),
        migrations.AddField(
            model_name='analysis',
            name='container_type_tr',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transport', to='sortapp.containertype'),
        ),
    ]
