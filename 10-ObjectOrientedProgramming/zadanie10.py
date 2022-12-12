class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def set_channel(self, number):
        self.channel_no = number
    def show_status(self):
        if self.is_on:
            print(f'Tv is on, channel {self.channel_no}')
        else:
            print(f'Tv is off, channel')
    
tv = TV()
tv.show_status()
tv.turn_on()
tv.show_status()
tv.set_channel(5)
tv.show_status()
tv.turn_off()
tv.show_status()