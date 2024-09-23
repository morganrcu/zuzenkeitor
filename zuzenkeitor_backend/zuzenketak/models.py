from django.db import models

class Student(models.Model):
    idal = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)

class Exercise(models.Model):
    name = models.CharField(max_length=128)
    statement = models.TextField()
    reference_solution = models.TextField()

class Submission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.RESTRICT)
    exercise = models.ForeignKey(Exercise, on_delete=models.RESTRICT)
    content  = models.TextField()

class Correction(models.Model):
    submission = models.OneToOneField(Submission, on_delete=models.RESTRICT, primary_key=True)
    llm_output = models.TextField()