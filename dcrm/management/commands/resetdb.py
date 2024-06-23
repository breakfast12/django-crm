from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import connection

class Command(BaseCommand):
    help = 'Reset database and re-running migrations.'

    def handle(self, *args, **options):
        # Dropping all table
        self.stdout.write("Dropping all tables...")
        with connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
            cursor.execute("SHOW TABLES")
            rows = cursor.fetchall()
            for row in rows:
                cursor.execute(f"DROP TABLE IF EXISTS `{row[0]}` CASCADE")
            cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
        self.stdout.write(self.style.SUCCESS('All tables have been dropped.'))

        # Re-running migrations
        self.stdout.write("Re-running migrations...")
        call_command('makemigrations')
        call_command('migrate')

        self.stdout.write(self.style.SUCCESS('Database has been reset and migrations re-run successfully.'))
