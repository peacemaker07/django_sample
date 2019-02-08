import logging

from django.core.management import BaseCommand

logger = logging.getLogger('okra.commands')


class Command(BaseCommand):

    def handle(*args, **options):

        print(__name__)

        print("start")
        logger.error("logger start")

        print("proc")
        logger.error("logger proc")

        print("end")
        logger.error("logger proc")
