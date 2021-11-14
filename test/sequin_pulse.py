import unittest
from src.animation.pwm_pulse import PwmPulse


class MyTestCase(unittest.TestCase):
    def test_first_run_returns_zero(self):

        pwm_pulse = PwmPulse()
        pwm_pulse.sequin_pulse()
        result = pwm_pulse.get_brightness()
        self.assertEqual(0, result)  # add assertion here

    def test_second_run_returns_first_step(self):
        pwm_pulse = PwmPulse()
        pwm_pulse.sequin_pulse()
        pwm_pulse.sequin_pulse()
        result = pwm_pulse.get_brightness()
        self.assertEqual(1285, result)

    def test_max_brightness(self):
        pwm_pulse = PwmPulse()
        for x in range(0, 52):
            pwm_pulse.sequin_pulse()
        result = pwm_pulse.get_brightness()
        self.assertEqual(65535, result)

    def test_decent_after_max_brightness(self):
        pwm_pulse = PwmPulse()
        for x in range(0, 53):
            pwm_pulse.sequin_pulse()
        result = pwm_pulse.get_brightness()
        self.assertEqual(64250, result)

    def test_ascent_after_min_brightness(self):
        pwm_pulse = PwmPulse()
        for x in range(0, 104):
            pwm_pulse.sequin_pulse()
        result = pwm_pulse.get_brightness()
        self.assertEqual(1285, result)


if __name__ == '__main__':
    unittest.main()
