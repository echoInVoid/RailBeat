import logging as log

class Settings:
    def __init__(self):
        with open(".\\res\\darkStyle.qss", 'r') as qss:
            self.styleSheet = qss.read()

        self.LOG_FORMAT = "[%(asctime)s][%(levelname)s][%(filename)s:%(lineno)d] %(message)s"
        self.logLevel = log.INFO

setting = Settings()