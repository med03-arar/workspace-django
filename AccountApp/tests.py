from datetime import timedelta

from django.core.exceptions import ValidationError
from django.test import SimpleTestCase
from django.utils import timezone

from .models import Doctor, Patient, Specialty, validate_past_date


class AccountFieldValidationTests(SimpleTestCase):
    def test_license_number_must_be_six_characters(self):
        field = Doctor._meta.get_field("license_number")

        with self.assertRaises(ValidationError):
            field.clean("12345", None)
        with self.assertRaises(ValidationError):
            field.clean("1234567", None)
        self.assertEqual(field.clean("123456", None), "123456")

    def test_patient_identifiers_must_contain_eight_digits(self):
        for field_name in ("national_id", "phone"):
            field = Patient._meta.get_field(field_name)
            with self.subTest(field=field_name):
                with self.assertRaises(ValidationError):
                    field.clean("1234AB78", None)
                self.assertEqual(field.clean("12345678", None), "12345678")

    def test_birth_date_must_be_before_today(self):
        today = timezone.localdate()

        with self.assertRaises(ValidationError):
            validate_past_date(today)
        with self.assertRaises(ValidationError):
            validate_past_date(today + timedelta(days=1))
        validate_past_date(today - timedelta(days=1))


class SpecialtyModelTests(SimpleTestCase):
    def test_specialty_has_only_the_amen_business_field(self):
        fields = [
            field.name
            for field in Specialty._meta.fields
            if not field.auto_created
        ]

        self.assertEqual(fields, ["amen"])

    def test_doctor_has_a_direct_many_to_many_to_specialty(self):
        field = Doctor._meta.get_field("specialties")

        self.assertIs(field.remote_field.model, Specialty)
        self.assertTrue(field.remote_field.through._meta.auto_created)
