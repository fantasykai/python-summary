# coding:utf-8

from apscheduler.schedulers.blocking import BlockingScheduler
import datetime


def aps_test():
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '定时执行，呵呵哒')


def aps_test(x):
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), x)


scheduler = BlockingScheduler()
scheduler.add_job(func=aps_test, trigger='cron', second='*/5')
scheduler.add_job(func=aps_test, args=('带个参数带执行任务，呵呵哒',), trigger='cron', second='*/5')
scheduler.add_job(func=aps_test, args=('定时任务',), trigger='cron', second='*/5')
scheduler.add_job(func=aps_test, args=('一次性任务',),
                  next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=12))
scheduler.add_job(func=aps_test, args=('循环任务',), trigger='interval', seconds=3)
scheduler.start()
