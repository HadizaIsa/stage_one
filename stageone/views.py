from django.http import JsonResponse
from datetime import datetime


# Create your views here.
def get_info(request):
    # Get the query parameters
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')

    # Get current day and time in UTC
    utc_time = datetime.now()
    current_day = utc_time.strftime("%A")

    # Construct GitHub URLs
    github_file_url = "https://github.com/HadizaIsa/stageone"
    github_repo_url = "https://github.com/HadizaIsa/stageone"

    # create a JSON response
    response_data = {
        "slack_name": slack_name,
        "track": track,
        "current_day": current_day,
        "utc_time": utc_time,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200,
    }

    return JsonResponse(response_data)
