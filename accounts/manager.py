from django.contrib.auth.base_user import BaseUserManager

from accounts.models import CustomUser

class UserManager(BaseUserManager):
    def create_user(self, username ,password =None, **extra_fields):
        if not username:
            raise ValueError("Invalid")
        extra_fields['email']=self.normalize_email(extra_fields['email'])
        print(extra_fields)
        user = self.model(username=username,**extra_fields)
        user.set_password(password)
        user.save(using = self.db)

        return user

    def create_superuser(self, username ,password =None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        
        return self.create_user(username,password,**extra_fields)
