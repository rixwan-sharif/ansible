from django.contrib.auth.models import User
import sys

username = sys.argv[0]
email = sys.argv[1]
password = sys.argv[2]

User.objects.create_superuser( username, email, password)