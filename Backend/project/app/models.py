from django.db import models
from django.contrib.auth.models import User
# settings.py
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


class React(models.Model):
    employee = models.AutoField(primary_key=True)
    department = models.CharField(max_length=40)
    def __str__(self):
        return self.employee


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    house_number = models.CharField(max_length=100)
    road = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=100)
    road_namw = models.CharField(max_length=100)
    state_address = models.CharField(max_length=100)
    district_address = models.CharField(max_length=100)

    def __str__(self):
        return self.address_id


class User(models.Model):
    user_id = models.AutoField(primary_key=True, default='0000000')
    ROLES = (
        ("Admin", "Admin"),
        ("Collector", "Collector"),
        ("Manager", "Manager"),
        ("End_user", "Contributer"),
        ("Region_head", "Region Head"),
        ("Recycle_facility", "Recycle_facility"),
    )
    aadhar = models.CharField(max_length=255, default='000000000000')
    f_name = models.CharField(max_length=255, default='000000000000')
    l_name = models.CharField(max_length=255, default='000000000000')
    role = models.CharField(max_length=20, choices=ROLES, default='000000000000')
    contact_number = models.CharField(max_length=15, default='000000000')
    gst_number = models.CharField(max_length=100, default='000000000')
    age = models.CharField(max_length=100, default='000000000000')
    email = models.CharField(max_length=100, default='000000000000')
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE, default='000000000000')
    device_data = models.CharField(max_length=25, default='000000000000')
    city = models.CharField(max_length=25, default='000000000000')

    def __str__(self):
        return self.user_id


class Collectors_data(models.Model):
    order_id = models.AutoField(primary_key=True)
    cus_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collector_customer')
    collector_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collector_collector')
    regional_head_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='collected_by_regional_heads')
    Feedback = models.TextField()
    collection_schedule = models.DateTimeField()
    weight = models.PositiveIntegerField()

    def __str__(self):
        return self.order_id


class GarbageType(models.Model):
    garbage_serial_number = models.AutoField(primary_key=True, default='00000000')
    order_id = models.ForeignKey(Collectors_data, on_delete=models.CASCADE)
    Plastic = models.FloatField()
    Paper = models.FloatField()
    Metal = models.FloatField()
    Electronics = models.FloatField()
    Wood = models.FloatField()
    Glass = models.FloatField()
    def __str__(self):
        return self.collection_id  


class RecycleFacility(models.Model):
    recycleFacility_Id = models.AutoField(primary_key=True)
    collection_id = models.ForeignKey(Collectors_data, on_delete=models.CASCADE)
    govornor = models.ForeignKey(User, on_delete=models.CASCADE)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    def __str__(self):
        return self.recycleFacility_Id


# class CollectionRoute(models.Model):
#     name = models.CharField(max_length=255)
#     start_point = models.ForeignKey(
#         CollectionPoint, related_name="start_routes", on_delete=models.CASCADE
#     )
#     end_point = models.ForeignKey(
#         CollectionPoint, related_name="end_routes", on_delete=models.CASCADE
#     )
#     assigned_collector = models.ForeignKey(User, on_delete=models.CASCADE)
#     schedule = models.CharField(max_length=255)


# class WasteCollectionRecord(models.Model):
#     collector = models.ForeignKey(User, on_delete=models.CASCADE)
#     bin = models.ForeignKey(WasteBin, on_delete=models.CASCADE)
#     collection_datetime = models.DateTimeField()
#     collected_amount = models.PositiveIntegerField()
#     notes = models.TextField()


# class WasteDisposalSite(models.Model):
#     name = models.CharField(max_length=255)
#     location = models.CharField(max_length=255)
#     capacity = models.PositiveIntegerField()
#     description = models.TextField()


# class DisposalRecord(models.Model):
#     collector = models.ForeignKey(User, on_delete=models.CASCADE)
#     bin = models.ForeignKey(WasteBin, on_delete=models.CASCADE)
#     disposal_site = models.ForeignKey(WasteDisposalSite, on_delete=models.CASCADE)
#     disposal_datetime = models.DateTimeField()
#     disposed_amount = models.PositiveIntegerField()
#     notes = models.TextField()


# class Report(models.Model):
#     report_type = models.CharField(max_length=50)
#     date_generated = models.DateTimeField()
#     parameters = models.JSONField()
#     data = models.JSONField()


# You can extend the User model to include additional fields like Role, Contact Number, and Address
# Or you can create a UserProfile model that's linked to the User model
