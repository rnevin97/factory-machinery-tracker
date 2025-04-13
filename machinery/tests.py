from django.test import TestCase
from django.contrib.auth.models import User  # Import the User model
from django.db.utils import IntegrityError  # Import IntegrityError
from .models import Machine, Company, User

class MachineModelTest(TestCase):
    def setUp(self):
        # Create a User instance
        self.user = User.objects.create_user(
            username="testuser",
            password="password123."
        )

        # Create a Company instance associated with the User
        self.company = Company.objects.create(
            name="ACME Corp",
            email="acme@test.com",
            phone="1234567890",
            job_title="Supervisor",
            user=self.user  # Associate the company with the user
        )

        # Create a Machine instance associated with the Company
        self.machine = Machine.objects.create(
            name="Lathe Machine",
            serial_number="LM123",
            company=self.company,
            importance=3,
            status="Working"
        )

    def test_machine_creation(self):
        """Test that a machine is created with the correct attributes."""
        self.assertEqual(self.machine.name, "Lathe Machine")
        self.assertEqual(self.machine.serial_number, "LM123")
        self.assertEqual(self.machine.company, self.company)
        self.assertEqual(self.machine.importance, 3)
        self.assertEqual(self.machine.status, "Working")

    def test_machine_string_representation(self):
        """Test the string representation of the Machine model."""
        self.assertEqual(str(self.machine), "Lathe Machine (LM123)")

    def test_company_association(self):
        """Test that the machine is correctly associated with the company."""
        self.assertEqual(self.machine.company.name, "ACME Corp")
        self.assertEqual(self.machine.company.email, "acme@test.com")

    def test_machine_importance_range(self):
        """Test that the machine importance is within a valid range."""
        self.assertGreaterEqual(self.machine.importance, 1)
        self.assertLessEqual(self.machine.importance, 5)

    def test_machine_status(self):
        """Test that the machine status is valid."""
        valid_statuses = ["Working", "Need Repair"]
        self.assertIn(self.machine.status, valid_statuses)

    def test_machine_missing_required_fields(self):
        """Test that creating a machine without required fields raises an error."""
        with self.assertRaises(IntegrityError):
            Machine.objects.create(
                name=None,  # Missing name
                serial_number="LM124",
                company=self.company,
                importance=3,
                status="Working"
            )
    
    def test_duplicate_serial_number(self):
        """Test that duplicate serial numbers are not allowed."""
        with self.assertRaises(IntegrityError):  
            Machine.objects.create(
                name="Drill Machine",
                serial_number="LM123", # Duplicate serial number
                company=self.company,
                importance=2,
                status="Working"
            )