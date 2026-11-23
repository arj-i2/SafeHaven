import random

from faker import Faker
from django.core.management.base import BaseCommand

from core.models import (
    Resident,
    DisasterType,
    Incident,
    EvacuationCenter,
    RescueTeam,
    Response,
    Resource,
)


fake = Faker("en_PH")

PHILIPPINE_LOCATIONS = [
    ("Manila", 14.5995, 120.9842),
    ("Quezon City", 14.6760, 121.0437),
    ("Calamba, Laguna", 14.2117, 121.1655),
    ("Cebu City", 10.3157, 123.8854),
    ("Davao City", 7.1907, 125.4553),
    ("Baguio City", 16.4023, 120.5960),
    ("Legazpi City", 13.1391, 123.7438),
    ("Iloilo City", 10.7202, 122.5621),
    ("Bacolod City", 10.6765, 122.9509),
    ("Cagayan de Oro", 8.4542, 124.6319),
    ("Tagaytay City", 14.1153, 120.9621),
    ("Puerto Princesa", 9.7392, 118.7353),
    ("Tacloban City", 11.2543, 125.0000),
    ("Zamboanga City", 6.9214, 122.0790),
    ("San Fernando, Pampanga", 15.0343, 120.6844),
]


class Command(BaseCommand):
    help = "Generate realistic sample data for SafeHaven"

    def handle(self, *args, **options):

        self.stdout.write("Generating SafeHaven sample data...")

        # 1. Create residents
        residents = []

        for _ in range(20):
            resident = Resident.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                contact_number=f"09{random.randint(100000000, 999999999)}",
                address=f"{fake.street_address()}, {fake.city()}, Philippines",
                birth_date=fake.date_of_birth(
                    minimum_age=18,
                    maximum_age=85
                ),
            )
            residents.append(resident)

        self.stdout.write(
            self.style.SUCCESS("20 residents created.")
        )

        # 2. Create disaster types
        disaster_names = [
            "Typhoon",
            "Flood",
            "Earthquake",
            "Landslide",
            "Volcanic Eruption",
        ]

        disaster_types = []

        for name in disaster_names:
            disaster_type, created = DisasterType.objects.get_or_create(
                name=name,
                defaults={
                    "description": f"Emergency incidents involving {name.lower()}."
                }
            )
            disaster_types.append(disaster_type)

        self.stdout.write(
            self.style.SUCCESS("Disaster types created or reused.")
        )

        # 3. Create incidents
        incidents = []

        incident_statuses = [
            "Pending",
            "In Progress",
            "Resolved",
        ]

        for _ in range(15):
            location, latitude, longitude = random.choice(
                PHILIPPINE_LOCATIONS
            )

            incident = Incident.objects.create(
                resident=random.choice(residents),
                disaster_type=random.choice(disaster_types),
                title=f"{random.choice(disaster_names)} Incident",
                description=fake.sentence(nb_words=12),
                address=f"{fake.street_address()}, {location}, Philippines",
                latitude=latitude,
                longitude=longitude,
                status=random.choice(incident_statuses),
            )
            incidents.append(incident)

        self.stdout.write(
            self.style.SUCCESS("15 incidents created.")
        )

        # 4. Create evacuation centers
        centers = []

        for _ in range(5):
            capacity = random.randint(100, 500)

            location, latitude, longitude = random.choice(
                PHILIPPINE_LOCATIONS
            )

            center = EvacuationCenter.objects.create(
                name=f"{location} Evacuation Center",
                address=f"{fake.street_address()}, {location}, Philippines",
                capacity=capacity,
                current_occupants=random.randint(0, capacity),
                latitude=latitude,
                longitude=longitude,
                contact_person=fake.name(),
                contact_number=f"09{random.randint(100000000, 999999999)}",
                is_active=random.choice([True, True, True, False]),
            )
            centers.append(center)

        self.stdout.write(
            self.style.SUCCESS("5 evacuation centers created.")
        )

        # 5. Create rescue teams
        teams = []

        team_statuses = [
            "Available",
            "On Duty",
            "Unavailable",
        ]

        for number in range(1, 6):
            team = RescueTeam.objects.create(
                team_name=f"Rescue Team {number}",
                team_leader=fake.name(),
                contact_number=f"09{random.randint(100000000, 999999999)}",
                members_count=random.randint(4, 12),
                status=random.choice(team_statuses),
            )
            teams.append(team)

        self.stdout.write(
            self.style.SUCCESS("5 rescue teams created.")
        )

        # 6. Create responses
        response_statuses = [
            "Assigned",
            "Responding",
            "Completed",
        ]

        for _ in range(10):
            Response.objects.create(
                incident=random.choice(incidents),
                rescue_team=random.choice(teams),
                status=random.choice(response_statuses),
                remarks=fake.sentence(nb_words=10),
            )

        self.stdout.write(
            self.style.SUCCESS("10 responses created.")
        )

        # 7. Create resources
        resource_items = [
            ("Drinking Water", "Food", "bottles"),
            ("Rice", "Food", "kilograms"),
            ("Canned Goods", "Food", "cans"),
            ("First Aid Kit", "Medicine", "kits"),
            ("Paracetamol", "Medicine", "boxes"),
            ("Medical Supplies", "Medicine", "packs"),
            ("Flashlight", "Equipment", "pieces"),
            ("Emergency Radio", "Equipment", "units"),
            ("Rescue Rope", "Equipment", "meters"),
            ("Blankets", "Clothing", "pieces"),
            ("Raincoats", "Clothing", "pieces"),
            ("Emergency Clothing", "Clothing", "sets"),
            ("Batteries", "Other", "packs"),
            ("Hygiene Kits", "Other", "kits"),
            ("Sleeping Mats", "Other", "pieces"),
        ]

        for name, category, unit in resource_items:
            Resource.objects.create(
                name=name,
                category=category,
                quantity=random.randint(20, 200),
                unit=unit,
                description=fake.sentence(nb_words=8),
            )

        self.stdout.write(
            self.style.SUCCESS("15 resources created.")
        )

        self.stdout.write(
            self.style.SUCCESS(
                "\nSafeHaven fake data generation completed successfully!"
            )
        )
