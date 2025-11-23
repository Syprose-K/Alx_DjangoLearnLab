from django.apps import AppConfig
from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate

class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'

    def ready(self):
        post_migrate.connect(create_groups, sender=self)

def create_groups(sender, **kwargs):
    from django.contrib.contenttypes.models import ContentType
    from .models import Book

    # Permissions
    content_type = ContentType.objects.get_for_model(Book)
    can_view = Permission.objects.get(codename='can_view', content_type=content_type)
    can_create = Permission.objects.get(codename='can_create', content_type=content_type)
    can_edit = Permission.objects.get(codename='can_edit', content_type=content_type)
    can_delete = Permission.objects.get(codename='can_delete', content_type=content_type)

    # Groups
    editors, _ = Group.objects.get_or_create(name='Editors')
    viewers, _ = Group.objects.get_or_create(name='Viewers')
    admins, _ = Group.objects.get_or_create(name='Admins')

    editors.permissions.set([can_edit, can_create])
    viewers.permissions.set([can_view])
    admins.permissions.set([can_view, can_create, can_edit, can_delete])
