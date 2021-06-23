class BaseConfig:
    DEBUG = False
    TESTING = False


class DevlopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False


config_factory = {"development": DevlopmentConfig, "testing": TestingConfig, "production": ProductionConfig}
