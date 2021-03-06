# Generated by Django 2.2.7 on 2019-11-14 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=60)),
                ('options', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(max_length=100)),
                ('required', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='AttributeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RiskType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=60, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RiskAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('raw_value', models.CharField(max_length=60)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', related_query_name='risk_attribute', to='suite.Attribute')),
                ('risk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='suite.Risk')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='risk',
            name='risk_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='risks', related_query_name='risk', to='suite.RiskType'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='attribute_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='suite.AttributeType'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='risk_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='attributes', related_query_name='attribute', to='suite.RiskType'),
        ),
    ]
