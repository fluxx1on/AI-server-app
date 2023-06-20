import time
from threading import Thread
from daemon.general import main_service as service

service_thread = Thread(target=service)
service_thread.daemon = True
service_thread.start()
