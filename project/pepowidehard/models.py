from django.db import models
from random import randint
from django.utils import timezone
import datetime

class djangodb(models.Model):
    temperature= models.CharField(max_length=5)
    humidity = models.CharField(max_length=5)
    datum = models.DateTimeField('date published')
    bild = models.ImageField(upload_to='posts/', default='posts/frx.png')
    #def __str__(self):
        #return self.temperature

def generateRandom():
    amount = 30
    while  amount != 0:
        rentry = djangodb(temperature=str(randint(0,20))+"°C",humidity=str(randint(0,100))+"%",
                    datum=timezone.now()-datetime.timedelta(days=randint(1,30)))
        rentry.save()
        amount = amount - 1
"""
python manage.py shell
>>> from pepowidehard.models import djangodb


>>> djangodb.objects.all()
<QuerySet []>

# Create a new djangodb.
>>> r = djangodb(full_name='John Smith')



# Save the object into the database. You have to call save() explicitly.
>>> r.save()

# Now it has an ID.
>>> r.id
1

# Django provides a rich database lookup API.
>>> djangodb.objects.get(id=2)
<djangodb: John Smith>
>>> djangodb.objects.get(full_name__startswith='John')
<djangodb: John Smith>
>>> djangodb.objects.get(full_name__contains='mith')
<djangodb: John Smith>
>>> djangodb.objects.get(id=2)
Traceback (most recent call last)
"""
