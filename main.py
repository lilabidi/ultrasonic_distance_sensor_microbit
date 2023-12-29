Distance = 0
basic.show_icon(IconNames.YES)

def on_forever():
    global Distance
    Distance = sonar.ping(DigitalPin.P0, DigitalPin.P1, PingUnit.CENTIMETERS)
    basic.show_string("" + str((Distance)))
    if Distance <= 5:
        servos.P2.set_angle(90)
        led.stop_animation()
    else:
        servos.P2.set_angle(180)
        led.stop_animation()
    basic.pause(1000)
basic.forever(on_forever)
