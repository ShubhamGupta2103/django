from datetime import date
from enum import auto
from tabnanny import verbose
from unicodedata import name
from django.db.models import *

class Movies(Model):
    title = CharField(max_length=50)
    year = IntegerField()
    rating = FloatField()

    def __str__(self):
        return self.title
        
class Show(Model):
    title = CharField(max_length=50)
    year = IntegerField()
    season_count = IntegerField()
    rating = FloatField()
    created_at = DateTimeField(auto_now=True)

class Student(Model):
    name = CharField(max_length=50)
    klass = IntegerField(verbose_name='class')
    rollno = IntegerField(verbose_name='roll number')

    def __str__(self):
        return self.name
class Report(Model):
    english = IntegerField()
    maths = IntegerField()
    science = IntegerField()
    hindi = IntegerField()
    computer = IntegerField()
    student = ForeignKey('Student', on_delete=DO_NOTHING)

    def __str__(self) -> str:
        return f'Report of{self.student.name}'

class Weather(Model):
    temp = DecimalField(verbose_name="Temp(c)", max_digits=5, decimal_places=2)
    wind_speed = DecimalField(max_digits=5, decimal_places=2)
    humidity = DecimalField(max_digits=5, decimal_places=2)
    date = DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.temp

class Singer(Model):
    name = CharField(max_length=50)
    age = IntegerField()
    
    def __str__(self):
        return self.name

class Song(Model):
    song_name = CharField(max_length=100)
    release_date = DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Report of{self.song_name}'

# Create your models here.
