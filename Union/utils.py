from .models import Union

def authenticate(request, username=None, password=None):
        user = Union.objects.get_or_none(username=username)

        if user is not None and user.check_password(password):
            return user
        else:
            return None