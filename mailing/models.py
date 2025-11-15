from django.db import models


class Client(models.Model):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=150, blank=True, default="")
    comment = models.TextField(max_length=150, blank=True, default="")

    def __str__(self):
        return self.email


class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField(max_length=500)

    def __str__(self):
        return self.subject


class Mailing(models.Model):
    STATUS_CHOICES = [
        ('CREATED', 'Создана'),
        ('LAUNCHED', 'Запущена'),
        ('COMPLETED', 'Завершена'),
    ]

    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='CREATED')
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    recipients = models.ManyToManyField(Client)

    def __str__(self):
        return f"Рассылка #{self.id} - {self.status}"

    def get_recipients_list(self):
        return ", ".join(c.email for c in self.recipients.all())


class MailingAttempt(models.Model):
    STATUS_CHOICES = [
        ('SUCCESS', 'Успешно'),
        ('FAIL', 'Не успешно'),
    ]

    attempt_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    server_response = models.TextField(max_length=500, blank=True)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)

    def __str__(self):
        return f"Попытка #{self.id} для рассылки {self.mailing.id}"
