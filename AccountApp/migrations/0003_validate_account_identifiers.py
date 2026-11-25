import django.core.validators
from django.db import migrations, models

import AccountApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('AccountApp', '0002_doctor_specialities'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='licence_number',
            new_name='license_number',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='license_number',
            field=models.CharField(
                max_length=6,
                unique=True,
                validators=[django.core.validators.MinLengthValidator(6)],
            ),
        ),
        migrations.AlterField(
            model_name='patient',
            name='national_id',
            field=models.CharField(
                max_length=8,
                unique=True,
                validators=[django.core.validators.RegexValidator(r'^\d{8}$')],
            ),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.CharField(
                max_length=8,
                validators=[django.core.validators.RegexValidator(r'^\d{8}$')],
            ),
        ),
        migrations.AlterField(
            model_name='patient',
            name='birth_date',
            field=models.DateField(validators=[AccountApp.models.validate_past_date]),
        ),
    ]
