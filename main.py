from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from gigachat import GigaChat
from gigachat.models import Chat, Messages, MessagesRole

load_dotenv()

app = Flask(__name__)
CREDENTIALS = os.getenv("GIGACHAT_CREDENTIALS")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_message = data.get('message', '')

    with GigaChat(
        credentials=CREDENTIALS,
        verify_ssl_certs=False,
        model="GigaChat-2",
        scope="GIGACHAT_API_PERS"
    ) as giga:
        response = giga.chat(
            Chat(
                messages=[
                    Messages(role=MessagesRole.USER, content=user_message)
                ]
            )
        )
        answer = response.choices[0].message.content

    return jsonify({'answer': answer})


if __name__ == '__main__':
    app.run(debug=True)