from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache

from app.settings.models import Category
from app.settings.views import CATEGORY_LIST_CACHE_KEY


@receiver(post_save, sender=Category)
def invalidate_category_cache_on_save(sender, **kwargs):
    """Сбрасываем кэш категорий при создании или обновлении."""
    cache.delete(CATEGORY_LIST_CACHE_KEY)


@receiver(post_delete, sender=Category)
def invalidate_category_cache_on_delete(sender, **kwargs):
    """Сбрасываем кэш категорий при удалении."""
    cache.delete(CATEGORY_LIST_CACHE_KEY)
