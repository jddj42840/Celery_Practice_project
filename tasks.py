# task 修改後Celery必須重新執行!!!!!
from celery import Celery
from celery import current_task, shared_task, Task
import time
import os

CELERY_BROKER_URL = os.environ.get(
    'CELERY_BROKER_URL', 'redis://localhost:6379'),
CELERY_RESULT_BACKEND = os.environ.get(
    'CELERY_RESULT_BACKEND', 'redis://localhost:6379')

# 建立 Celery Application
Taskapp = Celery('tasks', broker=CELERY_BROKER_URL,
                 backend=CELERY_RESULT_BACKEND
                 )
# 定義工作函數


@Taskapp.task
def add(x):
    result = 0
    for i in range(x, 50):
        result += i
        time.sleep(1)
    return result


@Taskapp.task
def text(input_payload):
    # input_TaskID = current_task.request.id
    # print(input_TaskID)
    time.sleep(10)
    return input_payload


# bind=True 參數，告訴Celery 發送一個self 參數到我的函數，我能夠使用它(self)來「記錄狀態更新」。
@Taskapp.task(bind=True)
def upload(self, name: str):
    # print("filenames", filenames)
    for i in range(0, 32):  # file 是取得 filename 集合元素的變數，i為引索
        self.update_state(state='PROGRESS',
                          meta={'current': i, 'total': 32})
        time.sleep(0.5)
    return "success"


class Cltest(Task):
    # ignore_result = True

    def run(self, source, *args, **kwargs):
        self.source = source
        return "success"

# app.tasks.register(Cltest())


task_regester = Taskapp.register_task(Cltest())

# if __name__ == "__main__":
#     seq = ["apple", "banana", "orange"]
#     start = time.perf_counter()
#     total = len(seq)
#     for current in (seq):
#         used = time.perf_counter() - start
#         print(f'\r{current/total:>6.1%}[{"▓"*current}{"-"*(total-current)}]{used:5.2f}s',
#               end="", flush=True)
#         time.sleep(1)
