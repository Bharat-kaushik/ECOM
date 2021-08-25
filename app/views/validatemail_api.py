from rest_framework.views import Response
from rest_framework.decorators import api_view
from businesslogic.domain.user import User


@api_view(("POST", ))
def validate_email(request):
    """
    code to find if the user with the given email
    is already exists or not.
    """
    email = request.data.get("email", '')

    # check if user exists or not
    status = None
    if User.objects.filter(email=email).exists():
        status = "taken"
    else:
        status = "not_taken"

    return Response(status)