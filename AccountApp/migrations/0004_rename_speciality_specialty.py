from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AccountApp', '0003_validate_account_identifiers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Speciality',
            new_name='Specialty',
        ),
        migrations.RenameField(
            model_name='specialty',
            old_name='name',
            new_name='amen',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='specialities',
            new_name='specialties',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialties',
            field=models.ManyToManyField(
                blank=True,
                related_name='doctors',
                to='AccountApp.specialty',
            ),
        ),
    ]
