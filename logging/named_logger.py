import logging


if __name__ == "__main__":
    logger = logging.getLogger(__name__)

    # If we skip handler setup, a call to debug(), info(), warning(), or error()
    # will call basicConfig() automatically, which will set up a stream handler
    # and set the default level to WARNING for the root logger.
    logger.info("This will not be logged, because the default level is WARNING.")
    logger.warning("This will be logged, because the default level is WARNING.")
    logger.error("This will be logged, because the default level is WARNING.")

    # Contrast that to calling basicConfig() explicitly, which will set up a
    # stream handler and set the default level to INFO for the root logger.
    logging.basicConfig(level=logging.INFO)
    logger.info("This will be logged, because the root logger is configured.")
    logger.debug("This will not be logged, because the level is INFO.")
    logger.error("An error occurred.")

    # we can selectively set the level for the module path-named logger
    logger.setLevel(logging.DEBUG)
    logger.debug("This will be logged, because the named logger level is DEBUG.")
    logging.debug("This will not be logged, because the root logger is at INFO.")
