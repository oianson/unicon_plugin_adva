from unicon.plugins.generic import GenericSingleRpConnection, service_implementation as svc
from unicon.plugins.generic import ServiceList, service_implementation as svc

from unicon.plugins.generic.connection_provider import GenericSingleRpConnectionProvider
from unicon.plugins.generic.settings import GenericSettings

from .statemachine import ADVAStateMachine
from .settings import ADVASettings

class ADVAConnectionProvider(GenericSingleRpConnectionProvider):
    """
        Connection provider class for ADVA connections.
    """

class ADVAServiceList(ServiceList):
    def __init__(self):
        super().__init__()

class ADVASingleRPConnection(GenericSingleRpConnection):
    os = 'adva'
    series = None
    chassis_type = 'single_rp'
    state_machine_class = ADVAStateMachine
    connection_provider_class = ADVAConnectionProvider
    subcommand_list = ADVAServiceList
    settings = ADVASettings()