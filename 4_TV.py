class TV:
    channel=1 #default value
    price=0
    inches=0
    OnOFF_status=False
    volume=50 #default value
    #constructor with brand parameter
    def __init__(self,brand):
        self.brand=brand
    #Volume can't never be below 0 or above 100
    def increaseVolume(iv):
       if  iv.volume < 100:
           iv.volume+=1
    def decreaseVolume(dv):
        if dv.volume > 0 :
            dv.volume-=1  
    # TV has only 50 channels
    def setChannel(sc,channel):
          if 1 <= channel <= 50:
            sc.channel = channel
     #eset TV so it goes back to channel 1 and volume 50
    def resetTV(rt):
        rt.channel=1
        rt.volume=50      
    def status(self):
        return f"{self.brand} at channel {self.channel},volume{self.volume}"
    #Inheriting Class TV 
class LEDTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        #calling base class constructor
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def display_details(self):
        print("------Detailed Features of LED TV------")
        print(f"Screen Thickness: {self.screen_thickness} mm")
        print(f"Energy Usage: {self.energy_usage} watts")
        print(f"Lifespan: {self.lifespan} years")
        print(f"Refresh Rate: {self.refresh_rate} Hz")

#Inheriting Class TV 
class PlasmaTV(TV):
    def __init__(self, brand, viewing_angle, backlight):
        #calling base class constructor
        super().__init__(brand)
        self.viewing_angle = viewing_angle
        self.backlight = backlight
      

    def display_details(self):
        print("------Detailed Features of Plasma TV------")
        print(f"Viewing Angle: {self.viewing_angle} degrees")
        print(f"Backlight: {self.backlight}")
      


# calling class with parameters values and assigning to led_tv,plasma_tv variable
led_tv = LEDTV("Samsung", 5, 100, 5, 120)
plasma_tv = PlasmaTV("Sony", 180, "LED")

print("LED TV Details:")
#calling led_tv display method to print inputted values
led_tv.display_details()
print("\nPlasma TV Details:")
#calling plasma_tv display method to print inputted values
plasma_tv.display_details()