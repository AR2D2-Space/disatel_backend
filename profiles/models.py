from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db.models import (CharField, EmailField,
                              IntegerField, DateTimeField)


class Profile(AbstractUser):
    username_validator = UnicodeUsernameValidator()
    username = CharField(
        'Usuario',
        max_length=150,
        unique=True,
        help_text='Requerido. Este campo sólo puede '
                  'contener letras, números, y los carácteres @/./+/-/_',
        validators=[username_validator],
        error_messages={
            'unique': "Ya existe un usuario con los datos ingresados.",
        },
    )
    email = EmailField(
        'Correo',
        blank=True,
        error_messages={
            'unique': "Ya existe un correo con los datos ingresados.",
        },
    )
    dpi = IntegerField(
        'Dpi',
        unique=True,
        error_messages={
            'unique': "Ya existe un dpi con los datos ingresados.",
        },
    )
    last_login = DateTimeField('Último inicio de Sesión', blank=True, null=True)
    created = DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'dpi']

    class Meta:
        ordering = ['id', 'dpi']

    def __str__(self):
        return self.username
