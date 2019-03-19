import logging


def get_logger(current_frame, name):

    try:
        logger_name = current_frame.f_back.f_globals['__name__']
        logger_obj = logging.getLogger(logger_name)
    except:
        logger_obj = logging.getLogger(name)

    return logger_obj
