from apscheduler.schedulers.blocking import BlockingScheduler
from scrapper import Scrapper

sched = BlockingScheduler()

scrapper_obj=Scrapper()

#This is a Job scheduler , Which updates the MonogDb collections in every 15 minutes.
@sched.scheduled_job('interval', minutes=15)
def timed_job():
    print('This cron job has started.')
    scrapper_obj.general_info()
    scrapper_obj.state_wise_details()
    print('This cron job job has ended')

sched.start()
