from . import get_logger
import inspect

# logger = logging.getLogger(__name__)
# logger.info("=======")
# current_obj = inspect.currentframe()
# f_back = inspect.currentframe().f_back
# f_back_name = inspect.currentframe().f_back.f_globals['__name__']
# logger.info(f_back_name)
# logger.info("=======")


def logger_util():

    # try:
    #     logger_name = inspect.currentframe().f_back.f_globals['__name__']
    #     logger = logging.getLogger(logger_name)
    # except:
    #     logger = logging.getLogger(__name__)

    global logger
    logger = get_logger(inspect.currentframe(), __name__)

    logger.info("utils start")

    logger.info(dir(logger_util))
    logger.info(__name__)

    logger.info("sub start")
    logger_util_sub()
    logger.info("sub end")

    logger.info('utils')


def logger_util_sub():

    # logger = get_logger(inspect.currentframe())

    # logger.info("start")
    #
    # logger.info("proc")
    #
    # logger.info("end")

    logger_util_sub_sub()


def logger_util_sub_sub():

    logger.info("=start")

    logger.info("=proc")

    logger.info("=end")

