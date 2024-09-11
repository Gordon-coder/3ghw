from django.db import models

CHOICES = (
    ("None", "None"),
    ("Chi", "Chi"), 
    ("Eng", "Eng"), 
    ("Math", "Math"), 
    ("Phy", "Phy"), 
    ("Chem", "Chem"), 
    ("Bio", "Bio"), 
    ("PTH", "PTH"), 
    ("ICT", "ICT"), 
    ("L&S", "L&S"), 
    ("Econ", "Econ"), 
    ("Geog", "Geog"), 
    ("C Hist", "C Hist"), 
    ("Hist", "Hist"), 
    ("Music", "Music"), 
    ("BAFS", "BAFS"), 
    ("VA", "VA"), 
    ("PE", "PE"), 
    ("RE", "RE")
)

# Create your models here.
class Assignment(models.Model):
    ("VA", "VA"), 
    date = models.DateField(null=True, blank=True)
    subject = models.CharField(max_length=10, choices=CHOICES, default="None")
    obj = models.CharField(max_length=69)
    

    def __str__(self):
        return f"{"" if str(self.date) == "None" else self.date} {"" if str(self.subject) == "None" else self.subject} {self.obj}"