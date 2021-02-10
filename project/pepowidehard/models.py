from django.db import models

class djangodb(models.Model):
    temperature= models.CharField(max_length=5)
    humidity = models.CharField(max_length=5)
    datum = models.DateTimeField('date published')
    bild = models.ImageField(upload_to='posts/', default='posts/frx.png')
    #def __str__(self):
        #return self.temperature
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
