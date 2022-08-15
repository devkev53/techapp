# Generated by Django 3.2 on 2022-08-14 06:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0001_initial'),
        ('users', '0002_alter_employee_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('maintenances', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('cpu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cpu', to='equipments.equipement', verbose_name='CPU')),
                ('figer_printer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='finger_printer', to='equipments.equipement', verbose_name='Lector de Huellas')),
                ('hard_disk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hard_disk', to='equipments.equipement', verbose_name='Disco Duro')),
                ('keyboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='keyboard', to='equipments.equipement', verbose_name='Teclado')),
                ('monitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monitor', to='equipments.equipement', verbose_name='Monitor')),
                ('mouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mouse', to='equipments.equipement', verbose_name='Mouse')),
                ('phone_ip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phone_ip', to='equipments.equipement', verbose_name='Telefono IP')),
                ('printer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='printer', to='equipments.equipement', verbose_name='Impresora')),
                ('scanner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scanner', to='equipments.equipement', verbose_name='Escanér')),
                ('speakers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='speakers', to='equipments.equipement', verbose_name='Bocinas')),
                ('technical', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Técnico')),
                ('ups', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ups', to='equipments.equipement', verbose_name='Bateria UPS')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.employee', verbose_name='Usuario Responsable')),
                ('webcam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='webcam', to='equipments.equipement', verbose_name='Camára Web')),
            ],
            options={
                'verbose_name': 'Mantenimiento',
                'verbose_name_plural': 'Mantenimientos',
            },
        ),
    ]