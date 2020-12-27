# https://github.com/hjlarry/flask-shop/blob/master/flaskshop/api/api.py

from auth.dao.authorization import AutharizationDAO
class AutharizationService:

    def __init__(self, group, permisstion) -> None:
        self.group = group
        self.permisstion = permisstion

    def is_autharize_group_user(self) -> bool:
        authorization_dao = AutharizationDAO()
        group_permission = authorization_dao.group_user_permission(group_id=self.group, permisstion_name=self.permisstion)
        if group_permission:
            return True
        return False