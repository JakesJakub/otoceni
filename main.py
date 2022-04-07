bod1 = 0
bod2 = 0
bod3 = 0
bod4 = 0
bod5 = 0
bod6 = 0


led.plot_brightness(bod1 + 2, bod2 + 2, 100)


def on_button_pressed_a():
    global bod1, bod2, bod3, bod4, bod5, bod6
    bod1 += 4
    bod2 += 2
    led.plot(bod1, bod2)

    bod3 += 0
    bod4 += 0
    led.plot(bod3, bod4)

    bod5 += 0
    bod6 += 4
    led.plot(bod5, bod6)
    led.plot_brightness(2, 2, 100)

    if bod1 == 4 and bod2 == 2 and bod3 == 0 and bod4 == 0 and bod5 == 0 and bod6 == 4:
        basic.clear_screen()
        bod1 -= 2
        bod2 += 2
        led.plot(bod1, bod2)

        bod3 += 4
        bod4 += 0
        led.plot(bod3, bod4)

        bod5 += 0
        bod6 -= 4
        led.plot(bod5, bod6)
        led.plot_brightness(2, 2, 100)

input.on_button_pressed(Button.A, on_button_pressed_a)
