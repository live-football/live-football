from apps.users.models import User


def get_importer_user():
    return User.objects.get_or_create(username='system_importer')[0]
