from django.core.management.base import BaseCommand

class Command(BaseCommand):
    name = 'mycommand'
    help = 'Описание вашей команды'

    def handle(self, *args, **options):
        # Здесь разместите логику вашей команды
        self.stdout.write('Команда успешно выполнена')