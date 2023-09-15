# Generated by Django 4.2.2 on 2023-09-09 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0002_creditnote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credititem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(blank=True, max_length=100, null=True)),
                ('hsn', models.PositiveIntegerField()),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tax', models.DecimalField(decimal_places=2, max_digits=5)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('creditnote', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.creditnote')),
            ],
        ),
    ]