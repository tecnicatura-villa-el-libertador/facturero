# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('precio_compra', models.DecimalField(max_digits=6, decimal_places=2)),
                ('precio_venta', models.DecimalField(max_digits=6, decimal_places=2)),
                ('cantidad_por_bulto', models.IntegerField()),
                ('codigo_barra', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('condicion', models.CharField(max_length=50, choices=[('responsable', 'Responsable Inscripto'), ('montributo', 'Monotributista')])),
                ('cuit', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField()),
                ('total', models.DecimalField(max_digits=6, decimal_places=2)),
                ('cliente', models.ForeignKey(to='factura.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Renglon',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('total', models.DecimalField(max_digits=6, decimal_places=2)),
                ('articulo', models.ForeignKey(to='factura.Articulo')),
                ('factura', models.ForeignKey(to='factura.Factura')),
            ],
        ),
    ]
