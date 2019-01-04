__author__ = "Yaswanth Sai Palaghat"

import Strategy
import Singleton


class Moviekit:
    def __init__(self):
        self.dataset = Strategy.LoadDataset()
        self.database = Singleton.Singleton()

    def start_app(self):
        self.dataset.parseAll()
        self.database.getInstance(self.dataset.data, self.dataset.item, self.dataset.genre)