# Generated by Django 5.1.3 on 2024-11-24 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, unique=True)),
                ('expiry_date', models.DateField()),
                ('description', models.CharField(max_length=255)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'indexes': [models.Index(fields=['code'], name='sales_coupo_code_e19dfb_idx')],
            },
        ),
    ]