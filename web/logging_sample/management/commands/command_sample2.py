import logging

from django.core.management import BaseCommand
from logging_sample.management.commands.utils.util_sample import logger_util

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(*args, **options):

        # logging_sample.management.commands.command_sample
        print(__name__)

        print("start")
        logger.info("logger start")

        logger_util()

        print("proc")
        logger.info("logger proc")

        # time.sleep(60)

        print("end")
        logger.info("logger end")
