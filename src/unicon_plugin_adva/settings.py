from unicon.plugins.generic.settings import GenericSettings


class ADVASettings(GenericSettings):
    """" Generic platform settings """
    def __init__(self):
        """ initialize
        """
        super().__init__()
        self.HA_INIT_EXEC_COMMANDS = [
        ]
        self.HA_INIT_CONFIG_COMMANDS = []
        self.ERROR_PATTERN = [
            'Error:',
        ]