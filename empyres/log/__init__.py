import logging
import logging.config
import os

logging.config.fileConfig(os.path.join(os.path.dirname(__file__), 'logging.conf'))

logger = logging.getLogger(__name__)
logger.info('Logging set up.')
