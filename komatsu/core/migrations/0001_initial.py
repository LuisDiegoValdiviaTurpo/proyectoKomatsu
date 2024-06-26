# Generated by Django 5.0.4 on 2024-04-05 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('TODO', 'To-Do'), ('IN_PROCESS', 'In-Process'), ('DONE', 'Done')], default='TODO', max_length=20)),
                ('nombre', models.CharField(max_length=100)),
                ('atributo_1', models.CharField(max_length=100)),
                ('atributo_2', models.CharField(max_length=100)),
                ('estado_trabajo', models.CharField(choices=[('ARMADO', 'Armado'), ('DESARME', 'Desarme')], default='DESARME', max_length=20)),
            ],
        ),
    ]
