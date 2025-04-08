from django.test import TestCase
from .models import Machine, Company

class MachineModelTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(
            name="ACME Corp",
            email="acme@test.com",
            phone="1234567890",
            job_title="Supervisor"
        )
        self.machine = Machine.objects.create(
            name="Lathe Machine",
            serial_number="LM123",
            company=self.company,
            importance=3,
            status="OK"
        )

    def test_machine_creation(self):
        self.assertEqual(self.machine.name, "Lathe Machine")
        self.assertEqual(self.machine.status, "OK")

    def test_string_representation(self):
        self.assertEqual(str(self.machine), "Lathe Machine (LM123)")
