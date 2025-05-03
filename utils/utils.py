from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings


def send_mail(subject, recipients, text_body=None, template_name=None, context=None):
    """
    Универсальная функция для отправки писем с поддержкой HTML.
    """
    try:
        if isinstance(recipients, str):
            recipients = [recipients]

        # Контекст по умолчанию
        context = context or {}
        from_email = "sduxodim@gmail.com"  # Используем значение из settings

        # Рендерим HTML, если указан шаблон
        html_content = render_to_string(template_name, context) if template_name else None

        # Формируем текстовое содержимое
        if not text_body:
            username = str(context.get("username", "пользователь"))
            text_content = f"Здравствуйте, {username}! Добро пожаловать!"
        else:
            text_content = text_body

        if not text_content and not html_content:
            raise ValueError("Необходимо указать text_body или template_name с context.")

        # Формируем письмо
        email = EmailMultiAlternatives(
            subject=subject,
            body=text_content,
            from_email=from_email,
            to=recipients
        )

        if html_content:
            email.attach_alternative(html_content, "text/html")

        email.send(fail_silently=False)
        return True

    except Exception as e:
        print(f"Ошибка отправки письма: {e}")
        return False
