# 需要修改 1. 利用AsyncResult取得工作進度
# flask-restx
from flask import Flask, request, render_template, url_for, jsonify
from flask_restx import Resource, Api, Namespace, fields
from flask_redis import FlaskRedis
from tasks import *  # 任務func
# from cltask import Class_test  # 任務 class
import time  # 用到 delay
from celery import current_task  # 取得最近的任務
from celery.result import AsyncResult  # !!!!!!! 用這個

# from celery import current_task  # 取得最近任務的屬性
import ast
import json
import unittest
app = Flask(__name__)

api = Api(app, version='0.0.1',
          title='Flask-RESTX and Swagger test', doc='/api')


idGet = api.model('工作ID', {
    'ID': fields.String(required=True, default="current"),
})


@api.route('/Get_Test', endpoint='cbc')  # 設定API的名稱與endpoint
class Get_test(Resource):  # 建立一個名為MyResource的Class並繼承Resource類別
    @api.doc(params={'name': 'nameis'})  # 設定API輸入的欄位名稱可新增diction格式新增欄位
    @api.marshal_with(idGet)
    def get(self):  # 建立一個 Restfil的func 傳輸方式為 get。 其他function 為 post、get、put、delete
        get_task = upload.delay(request.args.get(
            'name'))  # 將輸入的值傳給Celery的 text任務
        return {'ID': get_task.id}


Get_output = api.model('進度輸出', {
    'current': fields.String(required=True, default="current"),
    'total': fields.String(required=True, default="total")
})


Post_output = api.model('進度輸出', {
    'input': fields.String(required=True, default="current"),
    'output': fields.String(required=True, default="total")
})


@api.route('/Get_task', endpoint='csc')
class Get_task(Resource):
    @api.doc(params={'taskID': ' My_Task'})
    # @api.marshal_with(Get_output)
    def get(self):
        getTask = request.args.get('taskID')
        testinput = AsyncResult(getTask, app=Taskapp)
        return {'status': testinput.status, 'info': testinput.info}


# 輸出模組板(Modles)
output = api.model('基本輸出', {
    'status': fields.String(required=True, default="Mytask"),
    'ID': fields.String(required=True, default="TaskID")
})

input_info = api.model('註冊帳號input', {
    'status': fields.String(required=True, example="example@gmail.com"),
    'ID': fields.String(required=True, example="passwd")
})


@ api.route('/Post_task')
class Post_task(Resource):
    @ api.expect(input_info)
    @ api.marshal_with(output)  # 設定輸出格式
    def post(self):
        data = api.payload  # API輸入的實際輸出
        task_data = text.delay(data)
        return {'status': task_data.status, 'ID': task_data.id}


output_test = api.model('test', {
    'status': fields.String(required=True, example="success"),
})


@api.route('/unittest_GET')  # unittest 輸入輸出測試,要設定輸出格式
class UnitGetTest(Resource):
    @api.doc(params={'status': 'Mytask'})
    @api.marshal_with(output_test)
    def get(self):
        getValue = request.args.get('status')
        return {'status': getValue}


@api.route('/unittest_Post', endpoint='default2')
class unittest_Post(Resource):
    @api.expect(output)
    @api.marshal_with(output)
    def post(self):

        data = api.payload  # API輸入的實際輸出
        print(data)
        task_data = text.delay(data)
        return data


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port="5000")
