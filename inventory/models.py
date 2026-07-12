from django.db import models


class House(models.Model):
    name = models.CharField(max_length=100, unique=True)
    founder = models.CharField(max_length=100)
    common_room = models.CharField(max_length=100)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Professor(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    office = models.CharField(max_length=100, blank=True)
    house = models.ForeignKey(
        House,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='professors',
        help_text="House this professor is head of, if any.",
    )

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField()
    house = models.ForeignKey(
        House,
        on_delete=models.CASCADE,
        related_name='students',
    )
    advisor = models.ForeignKey(
        Professor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='advisees',
    )

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(
        Student,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='items',
    )
    house = models.ForeignKey(
        House,
        on_delete=models.CASCADE,
        related_name='items',
    )

    def __str__(self):
        return self.name
