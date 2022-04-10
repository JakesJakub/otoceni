let A = 0
led.plot(2, 0)
led.plot(0, 4)
led.plot(4, 4)
led.plotBrightness(2, 2, 100)
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    basic.clearScreen()
    A += 1
    if (A == 1) {
        led.plot(4, 2)
        led.plot(0, 0)
        led.plot(0, 4)
        led.plotBrightness(2, 2, 100)
    }
    
    if (A == 2) {
        basic.clearScreen()
        led.plot(2, 4)
        led.plot(4, 0)
        led.plot(0, 0)
        led.plotBrightness(2, 2, 100)
    }
    
    if (A == 3) {
        basic.clearScreen()
        led.plot(0, 2)
        led.plot(4, 0)
        led.plot(4, 4)
        led.plotBrightness(2, 2, 100)
    }
    
    if (A == 4) {
        basic.clearScreen()
        led.plot(2, 0)
        led.plot(0, 4)
        led.plot(4, 4)
        led.plotBrightness(2, 2, 100)
        A -= 4
    }
    
})
