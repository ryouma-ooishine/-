from django.db import models
import uuid
# Create your models here.

class Page(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    company_name = models.CharField(max_length=100,verbose_name="銘柄銘")
    buy_price = models.BigIntegerField(verbose_name="購入金額")
    buy_shares = models.BigIntegerField(verbose_name="株数")
    buy_day = models.DateField(verbose_name="購入日")

    def __str__(self):
        return self.company_name

