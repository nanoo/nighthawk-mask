class PwmPulse:

    def __init__(self):
        self.brightness = 0
        self.next_brightness = 0
        self.fade_amount = 1285

    def sequin_pulse(self):
        self.next_brightness = self.brightness
        # And send to LED as PWM level
        # change the brightness for next time through the loop:
        self.brightness = self.brightness + self.fade_amount
        # reverse the direction of the fading at the ends of the fade:
        if self.brightness <= 0:
            self.fade_amount = -self.fade_amount
        elif self.brightness >= 65535:
            self.fade_amount = -self.fade_amount

    def get_brightness(self):
        return self.next_brightness
