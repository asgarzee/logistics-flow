# Generated by Django 2.0 on 2017-12-05 08:51

from django.db import migrations, models
import django.db.models.deletion
import django_fsm


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', django_fsm.FSMField(default='CRE', max_length=50, protected=True)),
                ('awb', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Orders',
                'verbose_name': 'Order',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130, verbose_name='State Name')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='State Code')),
            ],
            options={
                'verbose_name_plural': 'States',
            },
        ),
        migrations.CreateModel(
            name='StateTransition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='state_flow_source', to='flow.State')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='state_flow_target', to='flow.State')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='statetransition',
            unique_together={('source', 'target')},
        ),
    ]
