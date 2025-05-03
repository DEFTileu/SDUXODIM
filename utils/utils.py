# utils/utils.py (или your_app/utils.py)
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

def send_mail(subject, recipients, text_body=None, html_body=None, template_name=None, context=None):
    """
    Универсальная функция для отправки писем.
    Args:
        subject (str): Тема письма.
        sender (str): Email отправителя
        recipients (list): Список email-адресов получателей.
        text_body (str, optional): Текстовое содержимое письма.
        html_body (str, optional): HTML-содержимое письма.
        template_name (str, optional): Путь к шаблону (например, 'email/welcome.html').
        context (dict, optional): Контекст для рендеринга шаблона.
    """
    try:
        # Используем sender или EMAIL_HOST_USER из настроек
        from_email = settings.EMAIL_HOST_USER

        # Если указан template_name, рендерим шаблон
        if template_name and context:
            html_body = render_to_string(template_name, context)
            # Текстовое тело можно задать вручную или использовать заглушку
            text_body = text_body or 'Это письмо требует HTML для отображения. Пожалуйста, используйте почтовый клиент с поддержкой HTML.'

        # Проверяем, что есть хотя бы text_body или html_body
        if not text_body and not html_body:
            raise ValueError("Необходимо указать text_body, html_body или template_name с context.")

        # Создаём письмо
        email = EmailMultiAlternatives(
            subject=subject,
            body=text_body or '',
            from_email=from_email,
            to=recipients
        )

        # Если есть HTML-контент, прикрепляем его
        if html_body:
            email.attach_alternative(html_body, "text/html")

        # Отправляем письмо
        email.send()

    except Exception as e:
        print(f"Ошибка отправки письма: {e}")