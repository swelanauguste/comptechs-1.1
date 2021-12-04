from django.core.management.base import BaseCommand
# from django.conf import settings

# from users.models import User

from ...models import District


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("file_name", type=str)

    def handle(self, *args, **kwargs):
        # District.objects.all().delete()
        file_name = kwargs["file_name"]
        with open(f"{file_name}") as file:
            for row in file:
                name = row.lower().replace("\n", "")
                self.stdout.write(self.style.SUCCESS(f"{name} added"))
                # updated_by = User.objects.get(pk=1)
                # created_by = User.objects.get(pk=1)
                District.objects.get_or_create(name=name)
        self.stdout.write(self.style.SUCCESS("list of objects added"))