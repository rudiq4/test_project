from django.db import models

class Subscriber(models.Model):# Поле Субскрайберс у ДБ де є 2 поля емейл і нейм.
    email = models.EmailField()
    name = models.CharField(max_length=11)

    def __str__(self):#В адмінці замість Subsriber object виводить людський вигляд
        return "%s %s" % (self.name, self.email)

    class Meta:
        verbose_name = 'Підписник'
        verbose_name_plural = 'Підписники'



