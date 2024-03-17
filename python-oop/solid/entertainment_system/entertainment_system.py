from abc import ABC, abstractmethod


class EntertainmentDevice(ABC):
    @abstractmethod
    def connect_device_to_power_outlet(self, device):
        pass


class ConnectHDMI:
    @staticmethod
    def connect_to_device_via_hdmi_cable(obj):
        return "connecting via hdmi"


class ConnectRCA:
    @staticmethod
    def connect_to_device_via_rca_cable(obj):
        return "connecting via rca"


class ConnectEthernet:
    @staticmethod
    def connect_to_device_via_ethernet_cable():
        return "connecting via ethernet"


class Television(EntertainmentDevice, ConnectRCA, ConnectHDMI):
    def connect_to_dvd(self, dvd_player):
        super().connect_to_device_via_rca_cable(dvd_player)

    def connect_to_game_console(self, game_console):
        super().connect_to_device_via_hdmi_cable(game_console)

    def connect_device_to_power_outlet(self, console):
        return "connected to power"


class DVDPlayer(EntertainmentDevice, ConnectHDMI):
    def connect_to_tv(self, television):
        super().connect_to_device_via_hdmi_cable(television)

    def connect_device_to_power_outlet(self, device):
        return "connected to power"


class GameConsole(EntertainmentDevice, ConnectHDMI, ConnectEthernet):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def connect_to_router(self):
        self.connect_to_device_via_ethernet_cable()

    def connect_device_to_power_outlet(self, device):
        return "connected to power"


class Router(EntertainmentDevice, ConnectEthernet):
    def connect_to_tv(self):
        super().connect_to_device_via_ethernet_cable()

    def connect_to_game_console(self):
        super().connect_to_device_via_ethernet_cable()

    def connect_device_to_power_outlet(self, device):
        return "connected to power"
