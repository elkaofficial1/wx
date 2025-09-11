import weather
from textual.app import App
from textual.widgets import Static

class OutAscll(Static):
    def __init__(self):
        super().__init__("")
        import sun
        permission = weather.get_current_weather_type()
        if permission == "sunny":
            self.widget = sun.SunWidget()
        elif permission == "cloudy":
            self.widget = sun.CloudWidget()
        elif permission == "rain":
            self.widget = sun.RainWidget()
        elif permission == "snow":
            self.widget = sun.SnowWidget()
        elif permission == "night":
            self.widget = sun.NightWidget()
        elif permission == "day":
            self.widget = sun.DayWidget()
        else:
            self.widget = sun.SunWidget()
    def on_mount(self):
        self.mount(self.widget)
