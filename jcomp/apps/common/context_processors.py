from datetime import datetime


def get_current_datetime(request):
    return {
        'current_minute': datetime.now().minute,
        'current_hour': datetime.now().hour,
        'current_day': datetime.now().day,
        'current_month': datetime.now().month,
    }
