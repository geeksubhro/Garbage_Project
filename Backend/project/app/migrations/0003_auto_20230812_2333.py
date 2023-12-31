# Generated by Django 3.2.20 on 2023-08-12 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_collectionpoint_report_user_wastebin_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('house_number', models.CharField(max_length=100)),
                ('road', models.CharField(max_length=100)),
                ('pin_code', models.CharField(max_length=100)),
                ('road_namw', models.CharField(max_length=100)),
                ('state_address', models.CharField(max_length=100)),
                ('district_address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Collectors_data',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('Feedback', models.TextField()),
                ('collection_schedule', models.DateTimeField()),
                ('weight', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GarbageType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Plastic', models.FloatField()),
                ('Paper', models.FloatField()),
                ('Metal', models.FloatField()),
                ('Electronics', models.FloatField()),
                ('Wood', models.FloatField()),
                ('Glass', models.FloatField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.collectors_data')),
            ],
        ),
        migrations.CreateModel(
            name='RecycleFacility',
            fields=[
                ('recycleFacility_Id', models.AutoField(primary_key=True, serialize=False)),
                ('address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.address')),
                ('collection_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.collectors_data')),
            ],
        ),
        migrations.RemoveField(
            model_name='collectionpoint',
            name='supervisor',
        ),
        migrations.RemoveField(
            model_name='collectionroute',
            name='assigned_collector',
        ),
        migrations.RemoveField(
            model_name='collectionroute',
            name='end_point',
        ),
        migrations.RemoveField(
            model_name='collectionroute',
            name='start_point',
        ),
        migrations.RemoveField(
            model_name='disposalrecord',
            name='bin',
        ),
        migrations.RemoveField(
            model_name='disposalrecord',
            name='collector',
        ),
        migrations.RemoveField(
            model_name='disposalrecord',
            name='disposal_site',
        ),
        migrations.DeleteModel(
            name='Report',
        ),
        migrations.RemoveField(
            model_name='wastebin',
            name='point',
        ),
        migrations.RemoveField(
            model_name='wastecollectionrecord',
            name='bin',
        ),
        migrations.RemoveField(
            model_name='wastecollectionrecord',
            name='collector',
        ),
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='aadhar',
            field=models.CharField(default='000000000000', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.CharField(default='000000000000', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default='000000000000', max_length=25),
        ),
        migrations.AddField(
            model_name='user',
            name='device_data',
            field=models.CharField(default='000000000000', max_length=25),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='000000000000', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='f_name',
            field=models.CharField(default='000000000000', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='gst_number',
            field=models.CharField(default='000000000', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='l_name',
            field=models.CharField(default='000000000000', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.AutoField(default='0000000', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='contact_number',
            field=models.CharField(default='000000000', max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Collector', 'Collector'), ('Manager', 'Manager'), ('End_user', 'Contributer'), ('Region_head', 'Region Head'), ('Recycle_facility', 'Recycle_facility')], default='000000000000', max_length=20),
        ),
        migrations.DeleteModel(
            name='CollectionPoint',
        ),
        migrations.DeleteModel(
            name='CollectionRoute',
        ),
        migrations.DeleteModel(
            name='DisposalRecord',
        ),
        migrations.DeleteModel(
            name='WasteBin',
        ),
        migrations.DeleteModel(
            name='WasteCollectionRecord',
        ),
        migrations.DeleteModel(
            name='WasteDisposalSite',
        ),
        migrations.AddField(
            model_name='recyclefacility',
            name='govornor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user'),
        ),
        migrations.AddField(
            model_name='collectors_data',
            name='collector_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collector_collector', to='app.user'),
        ),
        migrations.AddField(
            model_name='collectors_data',
            name='cus_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.address'),
        ),
        migrations.AddField(
            model_name='collectors_data',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collector_customer', to='app.user'),
        ),
        migrations.AddField(
            model_name='collectors_data',
            name='regional_head_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collected_by_regional_heads', to='app.user'),
        ),
        migrations.AddField(
            model_name='user',
            name='address_id',
            field=models.ForeignKey(default='000000000000', on_delete=django.db.models.deletion.CASCADE, to='app.address'),
        ),
    ]
