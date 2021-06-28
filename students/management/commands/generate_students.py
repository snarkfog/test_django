from django.core.management.base import BaseCommand
from students.models import Student


# Homework 8
class Command(BaseCommand):
    help = 'Generate students user command.'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of generated students')

    def handle(self, *args, **options):
        return Student.generate_students(count=options['count'])
