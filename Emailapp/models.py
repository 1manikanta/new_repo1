# emailapp/models.py

from django.db import models


class SentEmail(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sender = models.EmailField(default='your_email@example.com')
    recipient = models.EmailField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} - {self.recipient}"
