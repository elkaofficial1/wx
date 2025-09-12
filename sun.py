import os
import time
from textual.widgets import Static
from textual.timer import Timer


sun_frames = [
    """
      \\  |  /      ☼
       .-*-.
    -- ( ^ ) --
       '-*-'
      /  |  \\
    """,
    """
    . ' \\ | / ' .
      .-*-.
   -- ( o ) --
      '-*-'
    . / | \\ .
    """,
    """
      \\  |  /      ☼
       .-*-.
    -- ( U ) --
       '-*-'
      /  |  \\
    """,
    """
    . ' \\ | / ' .
      .-*-.
   -- ( ^ ) --
      '-*-'
    . / | \\ .
    """
]

class SunWidget(Static):
    def on_mount(self):
        self.frame = 0
        self.timer = self.set_interval(0.5, self.animate)
        self.update(sun_frames[self.frame])
    def animate(self):
        self.frame = (self.frame + 1) % len(sun_frames)
        self.update(sun_frames[self.frame])

# Облачно
cloud_frames = [
    """
      .--.   .--.
   .-(    ).(    )-.
  (___.__) (___.__)
    """,
    """
      .--.   .--.
   .-(    ).(    )-.
  (___.__) (___.__)
     ~ ~     ~ ~
    """
]

class CloudWidget(Static):
    def on_mount(self):
        self.frame = 0
        self.timer = self.set_interval(0.7, self.animate)
        self.update(cloud_frames[self.frame])
    def animate(self):
        self.frame = (self.frame + 1) % len(cloud_frames)
        self.update(cloud_frames[self.frame])

# Дождь
rain_frames = [
    """
      .--.   .--.
   .-(    ).(    )-.
  (___.__) (___.__)
     ' '   ' ' ' '
    """,
    """
      .--.   .--.
   .-(    ).(    )-.
  (___.__) (___.__)
    ' ' '   ' ' '
    """
]

class RainWidget(Static):
    def on_mount(self):
        self.frame = 0
        self.timer = self.set_interval(0.4, self.animate)
        self.update(rain_frames[self.frame])
    def animate(self):
        self.frame = (self.frame + 1) % len(rain_frames)
        self.update(rain_frames[self.frame])

# Снег
snow_frames = [
    """
      .--.   .--.
   .-(    ).(    )-.
  (___.__) (___.__)
     * *   * * *
    """,
    """
      .--.   .--.
   .-(    ).(    )-.
  (___.__) (___.__)
    * * *   * * *
    """
]

class SnowWidget(Static):
    def on_mount(self):
        self.frame = 0
        self.timer = self.set_interval(0.6, self.animate)
        self.update(snow_frames[self.frame])
    def animate(self):
        self.frame = (self.frame + 1) % len(snow_frames)
        self.update(snow_frames[self.frame])

# День
class DayWidget(Static):
    def on_mount(self):
        self.update("""
        \  |  /
          .-.
       --( o )--
          '-'
        /  |  \\
    """)

# Ночь
class NightWidget(Static):
    def on_mount(self):
        self.update("""
        .     *     .
      *    .   *    .
         .     *
        (   )
         '-' 
    """)

