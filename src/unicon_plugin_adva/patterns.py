from unicon.plugins.generic.patterns import GenericPatterns

class ADVAPatterns(GenericPatterns):
    def __init__(self):
        super().__init__()
        self.enable_prompt = r'(.*?)(%N)(-\w+-\d+)?-->\s*$'
        self.configure_prompt = r'^(.*?)(%N)(-\w+-\d+)?(?::([^>]+)-->|$)'
