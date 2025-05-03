from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    role = models.CharField(max_length=15)
    
    class Meta:
        db_table = 'Role'
    
    def __str__(self):
        return self.role

class User(AbstractUser):
    # Campos personalizados
    role = models.ForeignKey(Role, on_delete=models.PROTECT, db_column='roleId')
    status = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True, db_column='createdAt')
    
    # Configuración para usar email como username
    username = None
    email = models.EmailField(unique=True, db_column='email')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    # Solución al error E304 - Agrega related_name únicos
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name="dashboard_user_groups",  # Nombre único
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="dashboard_user_permissions",  # Nombre único
        related_query_name="user",
    )
    
    class Meta:
        db_table = 'User'
    
    def __str__(self):
        return self.email