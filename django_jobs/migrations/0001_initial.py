# Generated by Django 2.0 on 2018-07-07 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False, verbose_name='created at')),
                ('modified', models.DateTimeField(editable=False, verbose_name='modified at')),
                ('object_id', models.PositiveIntegerField()),
                ('handler_id', models.IntegerField(blank=True, null=True, verbose_name='handler id')),
                ('is_enabled', models.BooleanField(default=True, verbose_name='is enabled')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'CREATED'), (1, 'SCHEDULED'), (2, 'STARTED'), (3, 'STOPPED'), (4, 'RESTARTED'), (5, 'CANCELED'), (6, 'ERROR'), (7, 'DONE')], db_index=True, default=0, verbose_name='status')),
                ('extra_status', models.PositiveSmallIntegerField(blank=True, choices=[(0, 'TO_RESTART'), (1, 'TO_CANCEL')], db_index=True, null=True, verbose_name='extra status')),
                ('error_message', models.TextField(blank=True, verbose_name='error message')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name_plural': 'jobs',
                'verbose_name': 'job',
            },
        ),
    ]
