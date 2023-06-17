from threading import Thread
from . import service

service_thread = Thread(target=service())
service_thread.run()