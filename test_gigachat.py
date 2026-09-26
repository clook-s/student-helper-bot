from gigachat import GigaChat
from gigachat.models import Chat, Messages, MessagesRole
import os
CREDENTIALS = os.getenv("GIGACHAT_CREDENTIALS")


with GigaChat(credentials=CREDENTIALS, verify_ssl_certs=False) as giga:
    response = giga.chat(
        Chat(
            messages=[
                Messages(
                    role=MessagesRole.USER,
                    content="Привет! Как дела?"
                )
            ]
        )
    )
    print(response.choices[0].message.content)