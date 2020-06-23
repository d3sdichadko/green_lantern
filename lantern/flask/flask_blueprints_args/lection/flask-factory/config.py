import os


class Config:
    CONFIG_VALUE = 'DEFAULT value'
    POSTGRES_PORT = 5432
    POSTGRES_DB_URL = "psql://"
    DEBUG = True


class DevConfig(Config):
    CONFIG_VALUE = 'DEV value'


class QCConfig(Config):
    CONFIG_VALUE = 'QC value'


class ProdConfig(Config):
    CONFIG_VALUE = 'PROD value'
    DEBUG = False


ENV_CONFIG = {"dev": DevConfig, "qc": QCConfig, "prod": ProdConfig}


def runtime_config(config=None):
    """Returns app configuration class.

    If app configuration class is not provided, the function returns
    config class from the ENV_2_CONFIG collection using name of current
    environment.

    Args:
        config (class): App configuration class.

    Returns:
        class: App configuration class.

    """
    if config is None:
        env = os.environ.get("APP_ENV", "dev")
        assert env in ENV_CONFIG, "Unknown APP_ENV value: " + env
        config = ENV_CONFIG[env]

    return config
