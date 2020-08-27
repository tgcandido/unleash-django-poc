from UnleashClient import UnleashClient
from UnleashClient.strategies import Strategy

class CustomStrategy(Strategy):
    def apply(self, context: dict = None) -> bool:
        default_value = False

        if "custom_parameter" in context.keys():
            default_value = context['custom_parameter'] == self.parameters['custom_parameter']

        return default_value

custom_strategies = {
    'custom_strategy' : CustomStrategy
}

feature_flag_client = UnleashClient(
    "http://localhost:4242/api", 
    "Tembici", 
    custom_strategies = custom_strategies,
    refresh_interval=1)

feature_flag_client.initialize_client()
