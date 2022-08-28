import json
import unittest
from . import BaseTestCase
from unittest.mock import patch
from unittest.mock import Mock
from tasks import *
import app
from celery.result import AsyncResult


class Test_api_get(BaseTestCase):
    def test_UnitGetTest(self):
        res = self.client.get(
            '/unittest_GET',
            query_string=({
                'status': 'f8db12ee-75e5-408c-aa30-f7296553cfb6'
            })
        )

        self.assertEqual(
            res.json, {'status': 'f8db12ee-75e5-408c-aa30-f7296553cfb6'})  # get抓不到東西


class Test_api_post(BaseTestCase):
    def test_UnitPostTest(self):
        response = self.client.post(
            '/unittest_Post',
            data=json.dumps({
                'status': 'abc',
                'ID': 'fff'
            }),  # }
            content_type='application/json'
        )
        self.assertEqual(response.json, {'status': 'abc', 'ID': 'fff'})


class Test_Get_test(BaseTestCase):
    @patch('app.upload.delay')
    def test_Get_test(self, mock_upload_delay):
        # mock_upload_delay.upload.return_value = AsyncResult()
        GetResponse = self.client.get(
            '/Get_Test',
            query_string=({
                'name': 'nameiss'
            })
        )
        self.assertTrue(mock_upload_delay.called)
        self.assertEqual(GetResponse.status_code, 200)
        # self.assertEqual(GetResponse.json, {
        #                  'name': 'nameis'})

# 利用AsyncResult創建一個ID「查看Response」-> 主要任務

# 第二支API是利用 AsyncResult 取得 upload 任務的進度
# 問題在第一支測試API就把我的app.upload屏蔽掉了那第二支該如何抓給予的進度?
# 利用 mock 的 return value ?

# unittest  /Get_task API


class Test_Get_task(BaseTestCase):
    @patch('app.AsyncResult')
    def test_Get_task(self, mock_AsyncResult):
        GetResponse = self.client.get(
            '/Get_task',
            query_string=({
                'taskID': 'My_Task'
            })
        )
        self.assertTrue(mock_AsyncResult.called)
        self.assertEqual(GetResponse.status_code, 200)
        # self.assertEqual(GetResponse.json, {
        #  'ID': 'f8db12ee-75e5-408c-aa30-f7296553cfb6'})


class Test_Post_task(BaseTestCase):
    @patch('app.text.delay')
    def test_Post_task(self, mock_text_delay):
        PostResponse = self.client.post(
            '/Post_task',
            data=json.dumps({
                'status': 'SUCCESS',
                'ID': '666b311d-a4ee-474d-88b9-a5f95d44dd11'
            }),
            content_type='application/json'
        )
        self.assertTrue(mock_text_delay.called)
        self.assertEqual(PostResponse.status_code, 200)
        # self.assertEqual(PostResponse.json, {
        #  'status': 'success', 'ID': '666b311d-a4ee-474d-88b9-a5f95d44dd11'})
