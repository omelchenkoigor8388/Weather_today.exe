import Weather_form
from PyQt5 import QtWidgets
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils.config import get_default_config

class Weather(QtWidgets.QMainWindow, Weather_form.Ui_MainWindow):
    config_dict = get_default_config()
    config_dict['language'] = 'ua'

    def __init__(self):
        super(Weather, self).__init__()
        self.setupUi(self)

        self.pushButton.pressed.connect(self.go)

    def go(self):
        place = self.lineEdit.text()
        self.weather(place)

    def weather(self, place):
        owm = OWM('1b0a48e855dbaf376a83372d2afd5244')
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(place)

        w = observation.weather

        status = w.detailed_status
        w.wind()
        humidity = w.humidity
        temp = w.temperature('celsius')[
            'temp']
        print("В місті " + str(place) + " зараз " + str(status) +
              "\nТемпература " + str(
            round(temp)) + " градусів за цельсієм" +
              "\nВологість складає " + str(humidity) + "%" +
              "\nШвидкість вітру " + str(w.wind()['speed']) + " метрів за секунду")

        self.label.setText("В місті " + str(place) + " зараз " + str(status) +
              "\nТемпература " + str(
            round(temp)) + " градусів за цельсієм" +
              "\nВологість складвє " + str(humidity) + "%" +
              "\nШвидкість вітру " + str(w.wind()['speed']) + " метрів за секунду")


App = QtWidgets.QApplication([])
window = Weather()
window.show()
App.exec()