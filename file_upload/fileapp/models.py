from django.db import models


class File(models.Model):
    file = models.FileField()
    file_type = models.CharField(max_length=128, default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField()

    def __str__(self):
        return f'файл {self.file.name} формат: {self.file_type}'
