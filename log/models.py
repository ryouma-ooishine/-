from django.db import models
import uuid
# Create your models here.

class Page(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_name = models.CharField(max_length=100)
    buy_price = models.BigIntegerField()
    buy_shares = models.BigAutoField()
    sell_price = models.BigIntegerField()
    sell_shares = models.BigAutoField()
    buy_day = models.DateField()
    sell_day = models.DateField()

