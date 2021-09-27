from kivy.app import App
import pyrebase
# from collections import OrderedDict

from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget

config = {
    "apiKey": "AIzaSyDMr21CvaLoZbfu9C83CMIBCAH-dlc8DEM",
    "authDomain": "fir-esp32-9999d.firebaseapp.com",
    "firebase_url": "https://fir-esp32-9999d-default-rtdb.asia-southeast1.firebasedatabase.app",
    "storageBucket": "fir-esp32-9999d.appspot.com",
    "databaseURL": "https://fir-esp32-9999d-default-rtdb.asia-southeast1.firebasedatabase.app",
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()


class ProjectApp(App):
    pass


class TopLayout(RelativeLayout):
    pass


class Sensor(GridLayout):
    temp_text = StringProperty("0")
    humid_text = StringProperty("0")
    light_text = StringProperty("0")
    sol_text = StringProperty("0")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update, 1)

    def update(self, dt):
        print("update")
        self.temp_text = (str(float(self.get_temp())) + "°C")
        self.humid_text = (str(float(self.get_humid())) + " %")
        self.light_text = str(float(self.get_light()))
        self.sol_text = (str(float(self.get_sol())) + " %")

    def get_temp(self):
        # lay OrderedDict tu firebase
        key_val = db.child("Sensor").child("Temperature").order_by_key().limit_to_last(1).get()
        # luu cac gia tri key va value vao bien
        for temp_key, temp_value in key_val.val().items():
            return temp_value

    def get_humid(self):
        # lay OrderedDict tu firebase
        key_val = db.child("Sensor").child("Humidity").order_by_key().limit_to_last(1).get()
        # luu cac gia tri key va value vao bien
        for humid_key, humid_value in key_val.val().items():
            return humid_value

    def get_light(self):
        # lay OrderedDict tu firebase
        key_val = db.child("Sensor").child("Light").order_by_key().limit_to_last(1).get()
        # luu cac gia tri key va value vao bien
        for light_key, light_value in key_val.val().items():
            return light_value

    def get_sol(self):
        # lay OrderedDict tu firebase
        key_val = db.child("Sensor").child("SolHumidity").order_by_key().limit_to_last(1).get()
        # luu cac gia tri key va value vao bien
        for sol_key, sol_value in key_val.val().items():
            return sol_value


'''class WidgetExample(GridLayout):
    count = 0
    my_text = StringProperty("0")
    text_input_str = StringProperty("FCK")
    count_enabled = BooleanProperty(False)

    def on_text_validate(self, widget):
        self.text_input_str = widget.text

    # slider_value_txt = StringProperty("Value")

    def on_button_click(self):
        print("Button clicked")
        if self.count_enabled:
            self.count += 1
            self.my_text = str(float(get_temp()))

    def on_toggle_button_state(self, widget):
        print("toggle state: " + widget.state)
        if widget.state == "down":
            # On state
            widget.text = "ON"
            self.count_enabled = True
        else:
            # Off state
            widget.text = "OFF"
            self.count_enabled = False

    def on_switch_active(self, widget):
        print("Switch: " + str(widget.active))'''

ProjectApp().run()
