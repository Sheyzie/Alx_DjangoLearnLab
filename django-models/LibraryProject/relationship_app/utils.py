
# check if user is admin
def is_admin(user):
    return user.is_authenticated() and user.role == 'Admin'