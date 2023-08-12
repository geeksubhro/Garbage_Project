from django.db import models
from django.contrib.auth.models import User

class React (models.Model):
    employee = models.CharField(max_length=30)
    department = models.CharField(max_length=40)
    
    
class Address(models.Model):
  address_id= models.AutoField(primary_key=True)
  house_number = models.CharField(max_length=100)
  road = models.CharField(max_length=100)
  pin_code = models.CharField(max_length=100)
  road_namw= models.CharField(max_length=100)
  state_address = models.CharField(max_length=100)
  district_address = models.CharField(max_length=100)
  def __str__(self):
    return self.address_id      
      
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    ROLES = (
        ('Admin', 'Admin'),
        ('Collector', 'Collector'),
        ('Manager', 'Manager'),
        ('End_user', 'Contributer'),
        ('Region_head', 'Region Head'),
        ('Recycle_facility', 'Recycle_facility'),
        )
    aadhar= models.CharField(max_length=255)
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLES)
    contact_number = models.CharField(max_length=15)
    gst_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    device_data = models.CharField(max_length=25)
    def __str__(self):
      return self.user_id
     
       

        

   
class Collectors_data(models.Model):
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    def __str__(self):
      return self.user_id 

    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)  # You can also use PointField for coordinates
    description = models.TextField()
    collection_schedule = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    supervisor = models.ForeignKey(User, on_delete=models.CASCADE)
    


class WasteBin(models.Model):
    point = models.ForeignKey(CollectionPoint, on_delete=models.CASCADE)
    capacity = models.PositiveIntegerField()
    current_fill_level = models.PositiveIntegerField()
    last_emptied_date = models.DateTimeField()
    status = models.CharField(max_length=20)
    type = models.CharField(max_length=20)

class CollectionRoute(models.Model):
    name = models.CharField(max_length=255)
    start_point = models.ForeignKey(CollectionPoint, related_name='start_routes', on_delete=models.CASCADE)
    end_point = models.ForeignKey(CollectionPoint, related_name='end_routes', on_delete=models.CASCADE)
    assigned_collector = models.ForeignKey(User, on_delete=models.CASCADE)
    schedule = models.CharField(max_length=255)

class WasteCollectionRecord(models.Model):
    collector = models.ForeignKey(User, on_delete=models.CASCADE)
    bin = models.ForeignKey(WasteBin, on_delete=models.CASCADE)
    collection_datetime = models.DateTimeField()
    collected_amount = models.PositiveIntegerField()
    notes = models.TextField()

class WasteDisposalSite(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    description = models.TextField()

class DisposalRecord(models.Model):
    collector = models.ForeignKey(User, on_delete=models.CASCADE)
    bin = models.ForeignKey(WasteBin, on_delete=models.CASCADE)
    disposal_site = models.ForeignKey(WasteDisposalSite, on_delete=models.CASCADE)
    disposal_datetime = models.DateTimeField()
    disposed_amount = models.PositiveIntegerField()
    notes = models.TextField()

class Report(models.Model):
    report_type = models.CharField(max_length=50)
    date_generated = models.DateTimeField()
    parameters = models.JSONField()
    data = models.JSONField()

# You can extend the User model to include additional fields like Role, Contact Number, and Address
# Or you can create a UserProfile model that's linked to the User model
