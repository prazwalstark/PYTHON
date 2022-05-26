class Settings():
    '''A class to store all settings for Alien Invasion.'''
    def __init__(self):
        '''Initialize game's settings.'''
        #Screen Settings.
        self.screen_width=1200
        self.screen_height=800
        self.screen_bg_color=(230,230,230)
        self.ship_speed_factor = 0.75
        #Bullet Settings.
        self.bullet_speed_factor = 1
        self.bullet_width =3
        self.bullet_height =15
        self.bullet_color =(60,60,60)