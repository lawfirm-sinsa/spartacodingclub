from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/order', methods=['POST'])
def order():
   name_receive = request.form['name_give']
   count_receive = request.form['count_give']
   address_receive = request.form['address_give']
   phone_receive = request.form['phone_give']
   item_receive = request.form['item_give']

   receive_data = {
      'name':name_receive,
      'count':count_receive,
      'address':address_receive,
      'phone':phone_receive,
      'item':item_receive
   }

   db.order.insert_one(receive_data)
   return jsonify({'result':'success'})

@app.route('/order', methods=['GET'])
def listing():
   item_receive = request.args.get('item_give')
   result = list(db.order.find({'item':item_receive},{'_id':0}))

   return jsonify({'result':'success','orders':result}) 

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)
