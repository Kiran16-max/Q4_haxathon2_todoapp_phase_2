# backend/src/utils/logger.py
import logging
import sys
from datetime import datetime
from typing import Any, Dict

class Logger:
    def __init__(self, name: str = __name__, level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        # Prevent adding multiple handlers if logger already exists
        if not self.logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
    
    def info(self, message: str, extra: Dict[str, Any] = None):
        self.logger.info(message, extra=extra)
    
    def warning(self, message: str, extra: Dict[str, Any] = None):
        self.logger.warning(message, extra=extra)
    
    def error(self, message: str, extra: Dict[str, Any] = None):
        self.logger.error(message, extra=extra)
    
    def debug(self, message: str, extra: Dict[str, Any] = None):
        self.logger.debug(message, extra=extra)
    
    def exception(self, message: str, extra: Dict[str, Any] = None):
        self.logger.exception(message, extra=extra)

# Create a global logger instance
logger = Logger()

def get_logger(name: str = __name__) -> Logger:
    return Logger(name)