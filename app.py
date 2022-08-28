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


@api.route('/Get_Test', endpoint='ccc')  # 設定API的名稱與endpoint
class MyResource(Resource):  # 建立一個名為MyResource的Class並繼承Resource類別
    @api.doc(params={'name': 'nameis'})  # 設定API輸入的欄位名稱可新增diction格式新增欄位
    @api.marshal_with(idGet)
    def get(self):  # 建立一個 Restfil的func 傳輸方式為 get。 其他function 為 post、get、put、delete
        get_task = upload.delay(request.args.get(
            'name'))  # 將輸入的值傳給Celery的 text任務
        # class_test = task_regester.delay(
        #     "hello")   # class task 測試只會回傳 "success"
        # while get_task.status == 'PENDING':
        #     # print("=")
        #     pass
        # print(class_test.get())  # class task 要先 get 狀態才會為 success
        # print(class_test.id)
        # print(class_test.status)

        # classTest = Cltest()
        # print(classTest.run("hello"))
        # print(request.args.get('name'))  # 把Get輸入的值print出來
        # print(get_task.id)  # 把最近任務的ID print出來
        # print(get_task.status)  # status:狀態 success、pending、faild
        # print(get_task.get())
        # Task狀態:PENDING代辦的意思(error)，很多用windows作業平台都會出現類似問題
        # 解決方法:關閉當前 celery worker 並 指令改為"celery -A tasks worker --pool=solo -l info"即

        # print("I Get : ", get_task.get()) # task執行的結果
        # global Copy_Task  # 不要用global!
        # Copy_Task = get_task.get()
        # job = AsyncResult(get_task.id)  # 可以新增!記得補齊

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
class MyResource2(Resource):
    @api.doc(params={'taskID': ' My_Task'})
    # @api.marshal_with(Get_output)
    def get(self):
        getTask = request.args.get('taskID')
        # print(AsyncResult(getTask).ready())
        testinput = AsyncResult(getTask, app=Taskapp)
        # process = upload(testinput)
        # get_process = AsyncResult(id=getTask)
        # get_process = ast.literal_eval(str(testinput.info))
        # print(testinput)
        # print(testinput.info)
        # print(process.get())
        # print(get_process)
        # return get_process

        # print("taskid : ", process.id)
        # print(process.ready())
        # print(process.status)
        # print(type(process.info))
        # return {process.info}
        # return message
        # global Copy_Task    # 在flask內使用全域變數有時會出錯
        # get_copy = Copy_Task
        # return {'task_status':test.status}
        # print(testinput.info)
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
        # print(data)
        task_data = text.delay(data)
        # print("ID : ", task_data.id)
        # print("Task status : ", task_data.status)
        # print("Task INFO : ", task_data.get())

        # try:
        # data = str({'email': data['email'], 'password': data['password']})
        # except Exception:
        # message = {'status': "has problem", 'ID': 'error'}
        # else:
        # message = {'status': task_data.status, 'ID': task_data.id}
        # finally:
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
class UnitPostTest(Resource):
    @api.expect(output)
    @api.marshal_with(output)
    def post(self):

        data = api.payload  # API輸入的實際輸出
        print(data)
        task_data = text.delay(data)
        return data

# # ------------flask 後端---------------


# @ app.route('/backend')
# def bk():
#     if not redis.exists("count"):
#         redis.set("count", 0)
#     redis.incr("count")
#     data = int(redis.get("count"))
#     return render_template("index.html", login=data)


# @ app.route("/page", methods=["post", "GET"])  # 啟用路徑'/'
# def print_name():
#     account = request.values.get('name', "chichi")
#     times = int(redis.get("count"))
#     get_task = text.delay(account)
#     process = upload.delay(account)  # 進度測試<<not done>>
#     print(get_task.id)
#     print(get_task.status)
#     print(get_task.get())
#     print(process.get())
#     return render_template("page.html", nameis=get_task.get(), status=get_task.status,
#                            INFO=get_task.id, log=times)


# # -----------------------------------------------


if __name__ == '__main__':
    # unittest.main(verbosity=2)
    app.run(debug=True, host='0.0.0.0', port="5000")


# post 要有 payload 也要有 output   <<OK>>

# post 要有預設輸出 (改 model ) <<OK>>
# golbal 要刪除換其他方法(利用 response task id 回復--手動複製貼上)   <<>>
# 查詢 task 進度    <<>>
