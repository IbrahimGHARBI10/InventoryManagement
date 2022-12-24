# Generated by Django 4.0.3 on 2022-03-15 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=b'I01\n')),
                ('category', models.CharField(choices=[('stationnary', 'stationnary'), ('electronics', 'electronics'), ('food', 'food')], max_length=20, null=b'I01\n')),
                ('quantity', models.PositiveBigIntegerField(null=b'I01\n')),
            ],
        ),
    ]
