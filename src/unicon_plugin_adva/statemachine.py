from unicon.plugins.generic.statements import GenericStatements
from unicon.plugins.generic.statemachine import default_statement_list
from unicon.statemachine import Path, State, StateMachine

from .patterns import ADVAPatterns

patterns = ADVAPatterns()
statements = GenericStatements()

class ADVAStateMachine(StateMachine):

    def create(self):
        enable = State('enable', patterns.enable_prompt)
        configure = State('configure', patterns.configure_prompt)

        self.add_state(enable)
        self.add_state(configure)

        enable_to_configure = Path(enable, configure, 'configure', None)
        configure_to_enable = Path(configure, enable, 'back', None)

        self.add_path(enable_to_configure)
        self.add_path(configure_to_enable)

        self.add_default_statements(default_statement_list)
