from apscheduler.schedulers.background import BackgroundScheduler


def start(job, hour):
    scheduler = BackgroundScheduler(timezone="America/Sao_Paulo")
    scheduler.add_job(job, 'cron', hour=hour)
    scheduler.start()





