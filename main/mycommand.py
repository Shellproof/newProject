from django.core.management.base import BaseCommand

class Command(BaseCommand):
    name = 'mycommand'
    help = 'Описание команды'

    def handle(self, *args, **options):
        self.stdout.write('Команда успешно выполнена')