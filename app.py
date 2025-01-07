from flask import Flask, render_template , send_from_directory, request, jsonify, redirect
from functions import create_db_connection
from mysql.connector import Error
import requests
# from googletrans import Translator
import logging
from deep_translator import GoogleTranslator



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index-ru.html')

@app.route('/admin')
def admin():
    return redirect('https://cims.cognilabs.org/')

@app.route('/img/<filename>')
def get_image_home(filename):
    return send_from_directory('assets/img', filename)

@app.route('/icon/<filename>')
def get_image_icon(filename):
    return send_from_directory('assets/icon', filename)

@app.route('/partners/<filename>')
def get_image_partners(filename):
    return send_from_directory('assets/partners', filename)

@app.route('/en/education')
def education():
    return render_template('education.html')

@app.route('/ru')
def index_ru():
    return render_template('index-ru.html')

@app.route('/en')
def index_en():
    return render_template('index.html')

@app.route('/ru/education')
def education_ru():
    return render_template('education-ru.html')

@app.route('/cn')
def index_cn():
    return render_template('index-cn.html')

@app.route('/cn/education')
def education_cn():
    return render_template('education-cn.html')

@app.route('/en/exhibitions')
def exhibitions():

    connection = create_db_connection()
    if connection is None:
        return "Error connecting to the database"

    cursor = connection.cursor()

    query = "SELECT * FROM exhibitions_en"
    cursor.execute(query)
    exhibitions = cursor.fetchall()

    return render_template('exhibitions.html', exhibitions=exhibitions)

@app.route('/ru/exhibitions')
def exhibitions_ru():

    connection = create_db_connection()
    if connection is None:
        return "Error connecting to the database"

    cursor = connection.cursor()

    query = "SELECT * FROM exhibitions_en"
    cursor.execute(query)
    exhibitions = cursor.fetchall()

    return render_template('exhibitions-ru.html', exhibitions=exhibitions)


@app.route('/cn/exhibitions')
def exhibitions_cn():
    return render_template('exhibitions-cn.html')

@app.route('/en/faq')
def faq():
    return render_template('faq.html')

@app.route('/cn/faq')
def faq_cn():
    return render_template('faq-cn.html')

@app.route('/ru/faq')
def faq_ru():
    return render_template('faq-ru.html')



TELEGRAM_BOT_TOKEN = '**'
TELEGRAM_CHAT_ID = '6173241480'

@app.route('/send_quote', methods=['POST'])
def send_quote():
    name = request.form.get('name')
    email = request.form.get('mail')
    mobile = request.form.get('mobile')
    service = request.form.get('service')
    message = request.form.get('message')

    telegram_message = f"New Quote Request:\nName: {name}\nEmail: {email}\nMobile: {mobile}\nService: {service}\nMessage: {message}"

    send_telegram_message(telegram_message)

    return jsonify({'status': 'success', 'message': 'Quote request sent successfully!'})

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    requests.post(url, data=data)

if __name__ == '__main__':
    app.run(debug=True)
