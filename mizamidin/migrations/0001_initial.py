# Generated by Django 2.0.3 on 2018-03-14 13:37

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_title', models.CharField(max_length=200)),
                ('summary', models.TextField(help_text='Enter a brief description of the car', max_length=1000)),
                ('isbn', models.CharField(help_text='Gost Nomer', max_length=13, verbose_name='ISBN')),
                ('price_car', models.CharField(max_length=20)),
                ('standart', models.CharField(max_length=20)),
                ('date_vp', models.DateField(blank=True, null=True)),
                ('car_ava', models.ImageField(blank=True, null=True, upload_to='car_avas/')),
            ],
        ),
        migrations.CreateModel(
            name='MarkInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False)),
                ('imprint', models.CharField(max_length=200)),
                ('mark', models.CharField(max_length=20)),
                ('made_in', models.CharField(max_length=20)),
                ('crooked', models.CharField(max_length=20)),
                ('due_back', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('m', 'Cridit'), ('o', 'Satyldy'), ('a', 'Satylady'), ('r', 'Reserved')], default='d', help_text='Car Satylymda', max_length=1)),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mizamidin.Car')),
            ],
            options={
                'ordering': ['due_back'],
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a car type ', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mizamidin.Seller'),
        ),
        migrations.AddField(
            model_name='car',
            name='type',
            field=models.ManyToManyField(help_text='Select a type for this car', to='mizamidin.Type'),
        ),
    ]
