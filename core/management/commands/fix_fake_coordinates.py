
from django.core.management.base import BaseCommand

from core.models import Incident, EvacuationCenter


PHILIPPINE_LOCATIONS = [
    ("Manila, Philippines", 14.5995, 120.9842),
    ("Quezon City, Philippines", 14.6760, 121.0437),
    ("Calamba, Laguna, Philippines", 14.2117, 121.1655),
    ("Cebu City, Philippines", 10.3157, 123.8854),
    ("Davao City, Philippines", 7.1907, 125.4553),
    ("Baguio City, Philippines", 16.4023, 120.5960),
    ("Legazpi City, Philippines", 13.1391, 123.7438),
    ("Iloilo City, Philippines", 10.7202, 122.5621),
    ("Bacolod City, Philippines", 10.6765, 122.9509),
    ("Cagayan de Oro, Philippines", 8.4542, 124.6319),
    ("Tagaytay City, Philippines", 14.1153, 120.9621),
    ("Puerto Princesa, Philippines", 9.7392, 118.7353),
    ("Tacloban City, Philippines", 11.2543, 125.0000),
    ("Zamboanga City, Philippines", 6.9214, 122.0790),
    ("San Fernando, Pampanga, Philippines", 15.0343, 120.6844),
]


class Command(BaseCommand):
    help = "Correct coordinates of the latest Faker-generated records"

    def handle(self, *args, **options):
        incidents = list(
            Incident.objects.order_by("-pk")[:15]
        )

        centers = list(
            EvacuationCenter.objects.order_by("-pk")[:5]
        )

        if len(incidents) < 15 or len(centers) < 5:
            self.stdout.write(
                self.style.ERROR(
                    "Not enough records found. No records were changed."
                )
            )
            return

        for incident, location in zip(
            incidents,
            PHILIPPINE_LOCATIONS
        ):
            address, latitude, longitude = location

            incident.address = address
            incident.latitude = latitude
            incident.longitude = longitude

            incident.save(
                update_fields=["address", "latitude", "longitude"]
            )

        for center, location in zip(
            centers,
            PHILIPPINE_LOCATIONS[:5]
        ):
            address, latitude, longitude = location

            center.address = address
            center.latitude = latitude
            center.longitude = longitude

            center.save(
                update_fields=["address", "latitude", "longitude"]
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully corrected 15 incidents and 5 evacuation centers."
            )
        )
