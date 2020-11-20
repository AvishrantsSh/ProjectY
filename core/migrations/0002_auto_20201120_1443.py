# Generated by Django 3.0.5 on 2020-11-20 14:43

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('customer_id', models.UUIDField()),
                ('product_id', models.UUIDField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('status', models.CharField(choices=[('Cart', 'Cart'), ('Purchased', 'Purchased'), ('Delivered', 'Delivered')], max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
    ]
