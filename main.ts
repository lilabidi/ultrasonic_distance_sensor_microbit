let Distance = 0
basic.showIcon(IconNames.Yes)
basic.forever(function () {
    Distance = sonar.ping(
    DigitalPin.P0,
    DigitalPin.P1,
    PingUnit.Centimeters
    )
    basic.showString("" + Distance)
    if (Distance <= 5) {
        servos.P2.setAngle(90)
        led.stopAnimation()
    } else {
        servos.P2.setAngle(180)
        led.stopAnimation()
    }
    basic.pause(1000)
})
