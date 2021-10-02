# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 02:19:00 2021

@author: Partik
"""
import requests
from flask import Flask, request

# webhook_url = 'http://127.0.0.1:5000/webhook'

# data = { 'name': 'Partik', 
#          'Channel URL': 'Kumar' }

# r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})

app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome Guys!'

@app.route('/webhook', methods=['POST'])
def api_wb_message():
    if request.headers['Content-Type'] == 'application/json':
        data = request.get_json()
        # Stocks = data['stocks'].split(",")
        # LTP = data['trigger_prices'].split(",")
        Stocks_1 = 'Intraday 3 minutes bearish: \n'+'\n'.join([ str(myelement) for myelement in data['stocks'].split(",") ])
        base_url = 'https://api.telegram.org/bot2013356064:AAEsHNjIYuW4tqTC1Gu_HSlM5h2epqiArgw/sendMessage?chat_id=-511208986&text={}'.format(Stocks_1)
        requests.get(base_url)
        # data = pd.read_json('request.json')
        # data = json.dumps(request.json)
        # df = pd.DataFrame({'Stocks' : data['stocks'].split(","), 'LTP' : data['trigger_prices'].split(",")})
        # print(tabulate(df, headers = 'keys', tablefmt = 'psql'))
        # print(jsonify({'Stocks' : Stocks, 'LTP' : LTP}))
        # return data
        # return jsonify({'Stocks' : Stocks, 'LTP' : LTP})
        # print(render_template('table.html', your_list=Stocks))
        # return render_template('table.html', your_list=Stocks)
        return Stocks_1

if __name__ == '__main__':
    app.run()