from kivy.garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from tacomarker import TacoMarker


class TacoView(MapView):
    tacos_timer = None
    taco_names=[]

    def start_getting_tacos_in_fov(self):
        # After one second, get the markets in the field of view
        try:
            self.tacos_timer.cancel()
        except:
            pass

        self.tacos_timer = Clock.schedule_once(self.get_tacos_in_fov, 1)

    def get_tacos_in_fov(self, *args):
        # Get reference to main app and the database cursor
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        app = App.get_running_app()
        sql_statement = "SELECT * FROM tacos_and_burritos WHERE longitude > %s AND longitude < %s AND latitude > %s AND latitude < %s "%(min_lon, max_lon, min_lat, max_lat)
        app.cursor.execute(sql_statement)
        tacos = app.cursor.fetchall()
        for taco in tacos:
            name=taco[1]
            if name in self.taco_names:
                continue
            else:
                self.add_taco(taco)

    def add_taco(self, taco):
        lon, lat = taco[7], taco[6]
        marker = TacoMarker(lon=lon, lat=lat, source='burrito (2).png')
        marker.taco_data=taco
        self.add_widget(marker)
        name = taco[16]
        self.taco_names.append(name)
