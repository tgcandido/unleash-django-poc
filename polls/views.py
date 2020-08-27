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


def index(request):
    payload = {'custom_parameter' : request.GET['typeOfBike']}  
    if feature_flag_client.is_enabled("custom_strategy_toggle", payload):
        return JsonResponse({'status' : 'success', 'flag': 'custom_flexible', 'custom_parameter': payload['custom_parameter']})
    else:
        return JsonResponse({'status' : 'failure', 'flag': 'custom_flexible', 'custom_parameter': payload['custom_parameter']})



        
    