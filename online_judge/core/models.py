from django.db import models
from django.contrib.auth.models import User

class Problem(models.Model):
    title=models.CharField(max_length=225)
    description=models.TextField()
    sample_input=models.TextField()
    sample_output=models.TextField()
    hidden_inputs=models.JSONField() # stores list of input strings
    hidden_outputs=models.JSONField()   # stores list of correct outputs
    tags=models.CharField(max_length=225) #comma separated tags
    rating=models.IntegerField(default=0)
    total_submissions=models.IntegerField(default=0)
    correct_submissions=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    time_limit=models.IntegerField(default=1)
    memory_limit=models.IntegerField(default=128)

    def __str__(self):
        return self.title


class Submission(models.Model):
    LANGUAGE_CHOICES = [
        ('cpp', 'C++'),
        ('java', 'Java'),
        ('python', 'Python'),
        ('c', 'C'),
    ]
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('TLE', 'Time Limit Exceeded'),
        ('WA', 'Wrong Answer'),
        ('RTE', 'Runtime Error'),
        ('CE', 'Compilation Error'),
    ]
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    problem=models.ForeignKey(Problem, on_delete=models.CASCADE)
    language=models.CharField(max_length=10, choices=LANGUAGE_CHOICES)
    code=models.TextField()
    compiled_code=models.TextField(blank=True, null=True)
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    submitted_at=models.DateTimeField(auto_now_add=True)
    submission_time=models.IntegerField(default=0)
    submission_memory=models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.problem.title} - {self.status}"
