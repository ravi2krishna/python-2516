# NO Abstraction - We used regular / concrete classes
class Laptop():
    def usb_slot(self):
        pass
    def hdmi_slot(self):
        pass
    def c_port(self):
        pass

class Lenovo(Laptop):
    def usb_slot(self):
        print("Lenovo USB Slot")
    def hdmi_slot(self):
        print("Lenovo HDMI Slot")

class Dell(Laptop):
    def usb_slot(self):
        print("Lenovo USB Slot")
    def c_port(self):
        print("Lenovo C Slot")
    
# User 
print("User Buying Lenovo Laptop")
lenovo = Lenovo()
lenovo.usb_slot()
lenovo.hdmi_slot()

print("User Buying Dell Laptop")
dell = Dell()
dell.usb_slot()
dell.c_port()