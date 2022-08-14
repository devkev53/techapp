# Generated by Django 3.2 on 2022-08-14 01:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_historicaldepartment'),
        ('ubications', '0003_ubication_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalUbication',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminacion')),
                ('code', models.CharField(max_length=6, verbose_name='Código')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Address')),
                ('phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='phone')),
                ('estimated_computers', models.PositiveSmallIntegerField(default=0, verbose_name='Estimated Computers')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('department', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.department', verbose_name='Departamento')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Fiscalía',
                'verbose_name_plural': 'historical Fiscalías',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]