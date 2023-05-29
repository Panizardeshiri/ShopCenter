from sms import send_sms
from datetime import timedelta
from rest_framework_simplejwt.tokens import RefreshToken
def send_sms_code(code:str,phone:str):
    send_sms(
        f'welcome this is your code: {code}',
        '+12065550100',
        [phone],
        fail_silently=False
    )

class customRefreshToken(RefreshToken):
    lifetime = timedelta(minutes=5)

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    access = refresh.access_token
    return str(refresh), str(access)