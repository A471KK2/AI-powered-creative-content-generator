from loguru import logger
import sys

def setup_logger():
    logger.remove()
    
    logger.add(
        sys.stdout,
        level="INFO",
        format="<green>{time}</green> | <level>{level}</level> | {message}"
    )
    
    logger.add(
        "app.log",
        rotation="1 MB",
        retention="10 days",
        level="DEBUG"
    )

    return logger