class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0
        
    def turn_on(self):
        self.is_on = True
        
    def turn_off(self):
        self.is_on = False
        
    def set_channel(self, number):
        self.channel_no = number
    
    def set_channels(self,channels_list):
        self.channels = channels_list
    
    def increase_volume(self):
         if self.volume >= 0 and self.volume < 11:
            self.volume += 1
            
    def decrease_volume(self):
        if self.volume >= 0 and self.volume < 11:
            self.volume -= 1
    
    def show_channels(self):
        if self.is_on:
            print(f'Avaible channels are: {self.channels}')
        else:
            print("Tv is off")
            
    
        
        
    def show_status(self):
        if self.is_on:
            if self.channel_no < int(len(self.channels)+1):
                print(f'Tv is on, channel {self.channel_no} {self.channels[self.channel_no - 1]} volume: {self.volume}')
            else:
                print(f"Tv is on, channel {self.channel_no} volume: {self.volume}")
        else:
            print(f'Tv is off, channel')
    


tv = TV()
tv.show_status()
tv.turn_on()
tv.set_channels(["TVP1", "TVP2", "Polast", "TVN", "Filmbox", "Discovery", "HBO"])
tv.show_status()
tv.set_channel(2)
tv.increase_volume()
tv.show_status()
tv.set_channel(3)
tv.increase_volume()
tv.show_status()
tv.set_channel(4)
tv.decrease_volume()
tv.show_status()
tv.set_channel(5)
tv.show_status()
tv.set_channel(6)
tv.show_status()
tv.set_channel(7)
tv.show_status()
tv.set_channel(8)
tv.show_status()
tv.turn_off