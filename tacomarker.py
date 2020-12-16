from kivy.garden.mapview import MapMarkerPopup
from tacomenu import TacoMenu

class TacoMarker(MapMarkerPopup):
    taco_data = []

    def on_release(self):
        # Open up the LocationPopupMenu
        menu = TacoMenu(self.taco_data)
        menu.size_hint=[.8,.9 ]
        menu.open()
