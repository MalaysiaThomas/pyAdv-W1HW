class Weather:
    def __init__(self, city, temperature = "Loading Data", condition = "Loading Data"):
        self.city = city.title()
        self.temperature = temperature
        self.condition = condition.title()

    def displayWeather(self):
        return (f"City: {self.city}\nTemperature: {self.temperature}\nCondition: {self.condition}\n")

    def setWeather(self, update_temperature = "Loading Data", update_condition = "Loading Data"):
        self.temperature = int(round(update_temperature))
        self.condition = update_condition