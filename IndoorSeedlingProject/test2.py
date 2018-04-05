import onionGpio

led = onionGpio.OnionGpio(2)

#led.setInputDirection()

print led.getValue()

