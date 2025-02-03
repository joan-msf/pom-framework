import logging
import os


def get_logger(name=__name__):
    """
    Returns a logger instance with a specified name.

    Configures the logger to output to both the console and a file.
    Log files are stored in 'reports/logs/automation.log'.
    """
    logger = logging.getLogger(name)

    # Prevent adding duplicate handlers if the logger is already configured
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)

        # Define a common formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Console handler configuration
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # Ensure the log directory exists
        log_dir = os.path.join(os.getcwd(), "reports", "logs")
        os.makedirs(log_dir, exist_ok=True)

        # File handler configuration
        file_handler = logging.FileHandler(os.path.join(log_dir, "automation.log"))
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
