class Configuration:
    # list all options here ...
    DUMMY_OPTION1 = 10
    DUMMY_OPTION2 = 20

    @staticmethod
    def custom_init_app(app):
        """Apply custom configuration steps
        """
        print("custom init app")
        pass


class DevelopmentConfig(Configuration):
    # configuration specific options ...
    DEBUG = True


class ProductionConfig(Configuration):
    # configuration specific options ...
    DEBUG = False


###############################################################################

# All the available configurations
configs = {"development": DevelopmentConfig, "production": ProductionConfig}
