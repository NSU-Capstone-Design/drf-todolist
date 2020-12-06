from rest_framework.response import Response
from user.models import User


def authorize(token):
    try:
        if not token:
            return False
        check = User.objects.get(login_id=token)
        return check
    except:
        return False