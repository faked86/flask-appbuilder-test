from flask_appbuilder.security.sqla.manager import SecurityManager


class MySecurityManager(SecurityManager):

    def auth_user_db(self, username, password):
        user = self.find_user(username=username)
        if password == "admin":
            return user
        return None
