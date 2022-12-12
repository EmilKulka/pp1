class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on:
            print(f'Tv is on, channel {self.channel_no}')
        else:
            print(f'Tv is off, channel {self.channel_no}')
    
tv = TV()
tv.show_status()