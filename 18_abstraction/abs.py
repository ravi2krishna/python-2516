# Achieve Abstraction - We use abc (Abstract Base Class - ABC)
from abc import ABC,abstractmethod

class Laptop(ABC):
    @abstractmethod
    def usb_slot(self):
        pass
    @abstractmethod
    def hdmi_slot(self):
        pass
    @abstractmethod
    def c_port(self):
        pass
    
class Lenovo(Laptop):
    def usb_slot(self):
        print("Lenovo USB Slot")
    def hdmi_slot(self):
        print("Lenovo HDMI Slot")
    def c_port(self):
        print("Lenovo C Slot")
    

class Dell(Laptop):
    def usb_slot(self):
        print("Dell USB Slot")
    def c_port(self):
        print("Dell C Slot")
    def hdmi_slot(self):
        print("Dell HDMI Slot")
    def bluetooth(self):
        print("Dell Provided Bluetooth")
    
# User 
print("User Buying Lenovo Laptop")
lenovo = Lenovo()
lenovo.usb_slot()
lenovo.hdmi_slot()
lenovo.c_port()

print("User Buying Dell Laptop")
dell = Dell()
dell.usb_slot()
dell.c_port()
dell.hdmi_slot()
dell.bluetooth()