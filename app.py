from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from SMS_collector import SMSBooming

app = Flask(__name__)


@app.route('/sms/<phone>')
def sms_boom(phone):
    if not phone or len(phone) != 11:
        return 'error'
    work(phone)
    return 'ok'


def work(phone):
    s = BackgroundScheduler()
    s.add_job(SMSBooming(phone).run)
    s.start()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)