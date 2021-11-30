import statistics
class StatsData:
    def __init__(self, lista):
        self.l_data = lista
        self.mean = statistics.mean(self.l_data)
        self.median = statistics.median(self.l_data)
        self.varance = statistics.variance(lista)