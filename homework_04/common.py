import logging


def configure_logging():
    logging.basicConfig(
        format="[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)s - %(message)s",
        level=logging.INFO,
        datefmt="%Y-%m-%d",
    )
