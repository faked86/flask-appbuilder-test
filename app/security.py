from flask_appbuilder.security.sqla.manager import SecurityManager


class MySecurityManager(SecurityManager):

    def auth_user_db(self, username, password):
        if username == "admin" and password == "admin":
            user = self.find_user(username=username)
            return user
        return None
