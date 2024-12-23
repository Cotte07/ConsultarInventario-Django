# Generated by Django 5.1.2 on 2024-10-13 23:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultarInv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_compra', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='Proveedor',
            new_name='proveedor',
        ),
        migrations.AlterModelTable(
            name='producto',
            table=None,
        ),
        migrations.AddField(
            model_name='producto',
            name='id_categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='consultarInv.categoria'),
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_Rotacion', models.DateField(blank=True, null=True)),
                ('estado', models.CharField(blank=True, max_length=20)),
                ('id_Producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='consultarInv.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Lote_Historial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=9)),
                ('unidad_medida', models.CharField(max_length=20)),
                ('precio_compra', models.DecimalField(decimal_places=2, max_digits=9)),
                ('id_historial', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='consultarInv.historial')),
                ('id_lote', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='consultarInv.lote')),
            ],
        ),
    ]
