from flask import Flask, render_template, request
import json
import requests


application = Flask(__name__)

table_header = ['Артикл', 'Номер', 'Статус', 'Метраж', 'Колличество комнат', 'Стоимость', 'Отделка']
table_data = ['Article', 'Number', 'StatusCodeName', 'Quantity', 'Rooms', 'Sum', 'Decoration']


@application.route("/index", methods=['POST', 'GET'])
@application.route("/", methods=['POST', 'GET'])
def index():

    response = []
    if request.method == 'POST':
        if request.form['url']:
            response = requests.get(request.form['url']).json()
        else:
            with open('data.json', 'r', encoding='utf-8') as f:
                response = json.load(f)

    return render_template("index.html", title="Вывод данных JSON", table_header=table_header, table_data=table_data, response=response)


if __name__ == '__main__':
    application.run(debug=False)
