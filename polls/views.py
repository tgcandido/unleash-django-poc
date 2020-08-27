from django.http import JsonResponse
from .flags import feature_flag_client


# def index(request):
#     if feature_flag_client.is_enabled('release'):
#         return JsonResponse({'status' : 'success', 'flag': 'release'})
#     else:
#         return JsonResponse({'status' : 'failure', 'flag': 'release'})

# def index(request):
#     if feature_flag_client.is_enabled('flexibleRollout'):
#         return JsonResponse({'status' : 'success', 'flag': 'flexibleRollout'})
#     else:
#         return JsonResponse({'status' : 'failure', 'flag': 'flexibleRollout'})

# def index(request):
#     payload = {'userId' : request.GET['userId']}
#     if feature_flag_client.is_enabled('flexibleRolloutWithID', payload):
#         return JsonResponse({'status' : 'success', 'flag': 'flexibleRolloutWithID'})
#     else:
#         return JsonResponse({'status' : 'failure', 'flag': 'flexibleRolloutWithID'})


# def index(request):
#     payload = {'userId' : request.GET['userId']}
#     if feature_flag_client.is_enabled('clientIds', payload):
#         return JsonResponse({'status' : 'success', 'flag': 'clientIds', 'userId': payload['userId']})
#     else:
#         return JsonResponse({'status' : 'failure', 'flag': 'clientIds', 'userId': payload['userId']})


# def index(request):
#     payload = {'custom_parameter' : request.GET['typeOfBike']}  
#     if feature_flag_client.is_enabled("custom_strategy_toggle", payload):
#         return JsonResponse({'status' : 'success', 'flag': 'custom_flexible', 'custom_parameter': payload['custom_parameter']})
#     else:
#         return JsonResponse({'status' : 'failure', 'flag': 'custom_flexible', 'custom_parameter': payload['custom_parameter']})

# Abstraction for Flags - Deve hospedar todas as Feature Toggle associado a feature de Greetings.
class IGreetingFlags:
    def isReleaseEnable():
        pass


class GreetingFlags(IGreetingFlags):
    def isReleaseEnable(self):
        return feature_flag_client.is_enabled('release')


class AlwaysFailureFeature:
    def handle(self):
        return {
            'status': 'failure',
            'flag': 'flag',
        }


class AlwaysSuccessFeature:
    def handle(self):
        return {
            'status': 'success',
            'flag': 'flag',
        }


class GreetingFeaturesHandlersFactory:
    def __init__(self, flags):
        self.flags = flags

    def createHandler(self):
        if (self.flags.isReleaseEnable()):
            return AlwaysSuccessFeature()
        else:
            return AlwaysFailureFeature()


class GreetingService:

    def __init__(self, factoryHandler):
        self.factoryHandler = factoryHandler

    def execute(self):
        handler = self.factoryHandler.createHandler()
        return handler.handle()


service = GreetingService(GreetingFeaturesHandlersFactory(GreetingFlags()))


def index(request):
    return JsonResponse(service.execute())