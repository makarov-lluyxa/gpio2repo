import RPi.GPIO as GPIO
#dynamic_range = 3.3
dac_bits = [16, 20, 21, 25, 26, 17, 27, 22]
class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)
    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()
    def set_number(self, number):
        bins = [int(element) for element in bin(number)[2:].zfill(8)]
        i = 0
        for led in dac_bits:
            GPIO.output(led, bins[i])
            i += 1
    def set_voltage(self, voltage):
        normalized = voltage / 3.183
        digital_value = int(normalized * 255)
        digital_value = max(0, min(255, digital_value))
        self.set_number(digital_value)
if __name__ == '__main__':
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)
        while True:
            try:
                voltage = float(input('Введите напряжение в Вольтах: '))
                dac.set_voltage(voltage)
            except ValueError:
                print('Вы ввели не число. Попробуйте ещё раз\n')
    finally:
        dac.deinit()
