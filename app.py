from main_window import MainWindow


from twitter import twitter

class KvitterApp:
    def __init__(self):
        self.username_str = "username"
        self.password_str = "password"
        self.api = twitter.Api(username=self.username_str, password=self.password_str, input_encoding=None)
        self.main_window = MainWindow()


    def run(self):
        self.main_window.show(self.api, self.username_str)
        pass

