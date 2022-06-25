class Settings:
    def __init__(self):
        with open(".\\res\\darkStyle.qss", 'r') as qss:
            self.styleSheet = qss.read()

setting = Settings()