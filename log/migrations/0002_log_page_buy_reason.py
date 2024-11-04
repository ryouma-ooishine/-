# Generated by Django 4.2.16 on 2024-11-04 02:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("log", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Log",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("company_name", models.CharField(max_length=100, verbose_name="銘柄銘")),
                ("buy_price", models.BigIntegerField(verbose_name="購入金額")),
                ("buy_shares", models.BigIntegerField(verbose_name="株数")),
                ("buy_day", models.DateField(verbose_name="購入日")),
                ("buy_reason", models.TextField(max_length=1000, verbose_name="購入理由")),
                ("sell_price", models.BigIntegerField(verbose_name="売却金額")),
                ("sell_shares", models.BigIntegerField(verbose_name="売却量")),
                ("sell_day", models.DateField(verbose_name="売却日")),
                ("sell_reason", models.TextField(max_length=1000, verbose_name="売却理由")),
                ("benefit", models.BigIntegerField(verbose_name="損益")),
            ],
        ),
        migrations.AddField(
            model_name="page",
            name="buy_reason",
            field=models.TextField(default="未記入", max_length=1000, verbose_name="購入理由"),
        ),
    ]