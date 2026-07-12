from django.core.management.base import BaseCommand
from django.db import transaction

from inventory.models import House, Item, Professor, Student


class Command(BaseCommand):
    help = "Populate the database with sample data based on the Harry Potter movies."

    @transaction.atomic
    def handle(self, *args, **options):
        Item.objects.all().delete()
        Student.objects.all().delete()
        Professor.objects.all().delete()
        House.objects.all().delete()

        houses = {}
        for name, founder, common_room, points in [
            ("Gryffindor", "Godric Gryffindor", "Gryffindor Tower", 250),
            ("Slytherin", "Salazar Slytherin", "Dungeon", 210),
            ("Hufflepuff", "Helga Hufflepuff", "Basement near the kitchens", 230),
            ("Ravenclaw", "Rowena Ravenclaw", "Ravenclaw Tower", 240),
        ]:
            houses[name] = House.objects.create(
                name=name, founder=founder, common_room=common_room, points=points
            )

        professors = {}
        for name, subject, office, house_name in [
            ("Albus Dumbledore", "Headmaster", "Headmaster's Office", None),
            ("Minerva McGonagall", "Transfiguration", "Transfiguration Courtyard", "Gryffindor"),
            ("Severus Snape", "Potions", "Dungeon Office", "Slytherin"),
            ("Filius Flitwick", "Charms", "Charms Classroom", "Ravenclaw"),
            ("Pomona Sprout", "Herbology", "Greenhouse Three", "Hufflepuff"),
            ("Rubeus Hagrid", "Care of Magical Creatures", "Gamekeeper's Hut", None),
            ("Gilderoy Lockhart", "Defence Against the Dark Arts", "Room 3C", None),
            ("Remus Lupin", "Defence Against the Dark Arts", "Room 3C", None),
            ("Dolores Umbridge", "Defence Against the Dark Arts", "High Inquisitor's Office", None),
            ("Horace Slughorn", "Potions", "Dungeon Office", None),
        ]:
            professors[name] = Professor.objects.create(
                name=name,
                subject=subject,
                office=office,
                house=houses[house_name] if house_name else None,
            )

        students = {}
        for name, year, house_name, advisor_name in [
            ("Harry Potter", 5, "Gryffindor", "Minerva McGonagall"),
            ("Ron Weasley", 5, "Gryffindor", "Minerva McGonagall"),
            ("Hermione Granger", 5, "Gryffindor", "Minerva McGonagall"),
            ("Neville Longbottom", 5, "Gryffindor", "Minerva McGonagall"),
            ("Ginny Weasley", 4, "Gryffindor", "Minerva McGonagall"),
            ("Fred Weasley", 7, "Gryffindor", "Minerva McGonagall"),
            ("George Weasley", 7, "Gryffindor", "Minerva McGonagall"),
            ("Draco Malfoy", 5, "Slytherin", "Severus Snape"),
            ("Pansy Parkinson", 5, "Slytherin", "Severus Snape"),
            ("Vincent Crabbe", 5, "Slytherin", "Severus Snape"),
            ("Gregory Goyle", 5, "Slytherin", "Severus Snape"),
            ("Cedric Diggory", 6, "Hufflepuff", "Pomona Sprout"),
            ("Susan Bones", 5, "Hufflepuff", "Pomona Sprout"),
            ("Luna Lovegood", 4, "Ravenclaw", "Filius Flitwick"),
            ("Cho Chang", 6, "Ravenclaw", "Filius Flitwick"),
            ("Padma Patil", 5, "Ravenclaw", "Filius Flitwick"),
        ]:
            students[name] = Student.objects.create(
                name=name,
                year=year,
                house=houses[house_name],
                advisor=professors[advisor_name],
            )

        for name, category, quantity, description, house_name, owner_name in [
            ("Invisibility Cloak", "Magical Artifact", 1, "Renders the wearer invisible; a Peverell family heirloom.", "Gryffindor", "Harry Potter"),
            ("Marauder's Map", "Magical Artifact", 1, "Reveals every room and person in Hogwarts.", "Gryffindor", "Harry Potter"),
            ("Firebolt", "Broomstick", 1, "One of the fastest racing broomsticks ever made.", "Gryffindor", "Harry Potter"),
            ("Time-Turner", "Magical Device", 1, "Allows the wearer to travel back in time.", "Gryffindor", "Hermione Granger"),
            ("Deluminator", "Magical Device", 1, "Removes and stores light from its surroundings.", "Gryffindor", "Ron Weasley"),
            ("Remembrall", "Magical Trinket", 1, "Glows red when its owner has forgotten something.", "Gryffindor", "Neville Longbottom"),
            ("Sword of Gryffindor", "Weapon", 1, "Goblin-made blade that only presents itself to a true Gryffindor.", "Gryffindor", ""),
            ("Sorting Hat", "Magical Artifact", 1, "Sorts new students into their houses.", "Gryffindor", ""),
            ("Locket of Salazar Slytherin", "Dark Artifact", 1, "A Horcrux containing a fragment of Voldemort's soul.", "Slytherin", ""),
            ("Nimbus 2001", "Broomstick", 1, "Top-of-the-line racing broom bought for the Slytherin Quidditch team.", "Slytherin", "Draco Malfoy"),
            ("Basilisk Fang", "Magical Creature Remains", 3, "Venomous fangs from the Chamber of Secrets basilisk.", "Slytherin", ""),
            ("Diary of Tom Riddle", "Dark Artifact", 1, "A Horcrux that can write back to whoever holds it.", "Slytherin", ""),
            ("Hufflepuff's Cup", "Dark Artifact", 1, "A Horcrux disguised as Helga Hufflepuff's cup.", "Hufflepuff", ""),
            ("Golden Egg", "Tournament Item", 1, "Clue for the second Triwizard Tournament task.", "Hufflepuff", "Cedric Diggory"),
            ("Spectrespecs", "Magical Accessory", 1, "Glasses that let the wearer see Wrackspurts.", "Ravenclaw", "Luna Lovegood"),
            ("Diadem of Ravenclaw", "Dark Artifact", 1, "A Horcrux hidden in the Room of Requirement.", "Ravenclaw", ""),
            ("Butterbeer Cork Necklace", "Magical Accessory", 1, "A necklace strung together from butterbeer corks.", "Ravenclaw", "Luna Lovegood"),
        ]:
            Item.objects.create(
                name=name,
                category=category,
                quantity=quantity,
                description=description,
                house=houses[house_name],
                owner=students[owner_name] if owner_name else None,
            )

        self.stdout.write(self.style.SUCCESS(
            f"Seeded {House.objects.count()} houses, {Professor.objects.count()} professors, "
            f"{Student.objects.count()} students, {Item.objects.count()} items."
        ))
