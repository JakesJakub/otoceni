let bod1 = 0
let bod2 = 0
let bod3 = 0
let bod4 = 0
let bod5 = 0
let bod6 = 0
led.plotBrightness(bod1 + 2, bod2 + 2, 100)
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    bod1 += 4
    bod2 += 2
    led.plot(bod1, bod2)
    bod3 += 0
    bod4 += 0
    led.plot(bod3, bod4)
    bod5 += 0
    bod6 += 4
    led.plot(bod5, bod6)
    led.plotBrightness(2, 2, 100)
    if (bod1 == 4 && bod2 == 2 && bod3 == 0 && bod4 == 0 && bod5 == 0 && bod6 == 4) {
        basic.clearScreen()
        bod1 -= 2
        bod2 += 2
        led.plot(bod1, bod2)
        bod3 += 4
        bod4 += 0
        led.plot(bod3, bod4)
        bod5 += 0
        bod6 -= 4
        led.plot(bod5, bod6)
        led.plotBrightness(2, 2, 100)
    }
    
})
