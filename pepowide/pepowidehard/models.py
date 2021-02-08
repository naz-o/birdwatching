from django.db import models

class Basictest(models.Model):
    full_name = models.CharField(max_length=70)
    def __str__(self):
        return self.full_name
"""
>>> from news.models import Basictest


>>> Basictest.objects.all()
<QuerySet []>

# Create a new Basictest.
>>> r = Basictest(full_name='John Smith')

# Save the object into the database. You have to call save() explicitly.
>>> r.save()

# Now it has an ID.
>>> r.id
1

# Django provides a rich database lookup API.
>>> Basictest.objects.get(id=1)
<Basictest: John Smith>
>>> Basictest.objects.get(full_name__startswith='John')
<Basictest: John Smith>
>>> Basictest.objects.get(full_name__contains='mith')
<Basictest: John Smith>
>>> Basictest.objects.get(id=2)
Traceback (most recent call last)
"""
