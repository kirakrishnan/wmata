from django.db import models

# Create your models here.


class StationInfo(models.Model):
 car_db = models.IntegerField()
 destination_db = models.CharField(max_length = 20)
 destinationCode_db = models.CharField(max_length = 5)
 destinationName_db = models.CharField(max_length = 30)
 group_db = models.IntegerField()
 line_db = models.CharField(max_length = 10)
 locationCode_db = models.CharField(max_length = 5, default = 'D05')
 locationName_db = models.CharField(max_length = 30, default = 'Capitol South')
 min_db = models.IntegerField()
 def __str__(self):
  return self.locationCode_db


    # {'Car': '6',
    #  'Destination': 'Wiehle',
    #  'DestinationCode': 'N06',
    #  'DestinationName': 'Wiehle-Reston East',
    #  'Group': '2',
    #  'Line': 'SV',
    #  'LocationCode': 'D05',
    #  'LocationName': 'Capitol South',
    #  'Min': '1'}

    # {'Car': '8',
    #  'Destination': 'Largo',
    #  'DestinationCode': 'G05',
    #  'DestinationName': 'Largo Town Center',
    #  'Group': '1',
    #  'Line': 'BL',
    #  'LocationCode': 'C04',
    #  'LocationName': 'Foggy Bottom-GWU',
    #  'Min': 'ARR'},