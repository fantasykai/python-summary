# coding:utf-8

from apscheduler.schedulers.blocking import BlockingScheduler
import datetime


def aps_test():
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '定时执行，呵呵哒')


scheduler = BlockingScheduler()
scheduler.add_job(func=aps_test, trigger='cron', second='*/5')
scheduler.start()
