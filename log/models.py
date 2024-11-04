from django.db import models
import uuid
# Create your models here.

class Page(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    company_name = models.CharField(max_length=100,verbose_name="銘柄銘")
    buy_price = models.BigIntegerField(verbose_name="購入金額")
    buy_shares = models.BigIntegerField(verbose_name="株数")
    buy_day = models.DateField(verbose_name="購入日")
    buy_reason = models.TextField(max_length=1000,default="未記入",verbose_name="購入理由")

    def __str__(self):
        return self.company_name
    
class Log(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    company_name = models.CharField(max_length=100,verbose_name="銘柄銘")
    buy_price = models.BigIntegerField(verbose_name="購入金額")
    buy_shares = models.BigIntegerField(verbose_name="株数")
    buy_day = models.DateField(verbose_name="購入日")
    buy_reason = models.TextField(max_length=1000,verbose_name="購入理由")
    sell_price = models.BigIntegerField(verbose_name="売却金額")
    sell_shares = models.BigIntegerField(verbose_name="売却量")
    sell_day = models.DateField(verbose_name="売却日")
    sell_reason = models.TextField(max_length=1000,verbose_name="売却理由")
    benefit = models.BigIntegerField(verbose_name="損益")

    def __str__(self):
        return self.company_name



