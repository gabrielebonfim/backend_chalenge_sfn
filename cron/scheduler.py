from apscheduler.schedulers.background import BackgroundScheduler

from restore_data.restore_data import RestoreData


def start(job, hour):
    scheduler = BackgroundScheduler(timezone="America/Sao_Paulo")
    scheduler.add_job(job, 'cron', hour=hour)
    scheduler.start()





