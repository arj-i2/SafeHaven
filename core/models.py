from django.db import models


class Resident(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    address = models.TextField()
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class DisasterType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name



class Incident(models.Model):

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    resident = models.ForeignKey(
        Resident,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    disaster_type = models.ForeignKey(
        DisasterType,
        on_delete=models.PROTECT
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    address = models.TextField()

    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    reported_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class EvacuationCenter(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    capacity = models.PositiveIntegerField()
    current_occupants = models.PositiveIntegerField(default=0)

    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    contact_person = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name



class RescueTeam(models.Model):

    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('On Duty', 'On Duty'),
        ('Unavailable', 'Unavailable'),
    ]

    team_name = models.CharField(max_length=150)
    team_leader = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    members_count = models.PositiveIntegerField(default=1)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Available'
    )

    def __str__(self):
        return self.team_name


class Response(models.Model):

    STATUS_CHOICES = [
        ('Assigned', 'Assigned'),
        ('Responding', 'Responding'),
        ('Completed', 'Completed'),
    ]

    incident = models.ForeignKey(
        Incident,
        on_delete=models.CASCADE,
        related_name='responses'
    )

    rescue_team = models.ForeignKey(
        RescueTeam,
        on_delete=models.PROTECT,
        related_name='responses'
    )

    assigned_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Assigned'
    )

    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.rescue_team.team_name} - {self.incident.title}"


class Resource(models.Model):

    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Medicine', 'Medicine'),
        ('Equipment', 'Equipment'),
        ('Clothing', 'Clothing'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=150)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    quantity = models.PositiveIntegerField(default=0)
    unit = models.CharField(max_length=30)

    description = models.TextField(blank=True)

    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
