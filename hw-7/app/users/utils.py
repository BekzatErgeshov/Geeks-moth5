import logging

from django.conf import settings
from django.core.mail import send_mail

logger = logging.getLogger(__name__)

def send_registration_email(user):
    if not user.email:
        return

    try:
        send_mail(
            subject="Регистрация прошла успешно",
            message=(
                f"Здравствуйте, {user.username}!\n\n"
                "Вы успешно зарегистрировались на нашем сайте.\n"
                "Теперь вы можете войти в свой аккаунт."
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=False,
        )
    except Exception:
        # Письмо не должно ломать регистрацию, если SMTP недоступен
        logger.exception("Не удалось отправить письмо на %s", user.email)
