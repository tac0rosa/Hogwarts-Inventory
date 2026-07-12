from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('founder', models.CharField(max_length=100)),
                ('common_room', models.CharField(max_length=100)),
                ('points', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('office', models.CharField(blank=True, max_length=100)),
                ('house', models.ForeignKey(blank=True, help_text='House this professor is head of, if any.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='professors', to='inventory.house')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year', models.PositiveSmallIntegerField()),
                ('advisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='advisees', to='inventory.professor')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='inventory.house')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(blank=True, max_length=100)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('description', models.TextField(blank=True)),
                ('house', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='inventory.house')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='inventory.student')),
            ],
        ),
    ]
