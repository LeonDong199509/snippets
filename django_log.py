LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d [%(module)s:%(lineno)s] %(message)s"
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG" if DEBUG else "INFO",
            "formatter": "simple",
        },
        "file": {
            "level": "DEBUG" if DEBUG else "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "maxBytes": LOGGING_MAX_BYTES,
            "backupCount": LOGGING_BACKUP_COUNT,
            "filename": "/path/django.log",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django": {"handlers": ["console", "file"], "level": "INFO", "propagate": False},
        "logger_name": {"handlers": ["console", "file"], "level": "DEBUG" if DEBUG else "INFO", "propagate": False},
    },
}
