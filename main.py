bod1 = 0
bod2 = 0
bod3 = 0
bod4 = 0
bod5 = 0
bod6 = 0
A = 0

led.plot_brightness(bod1 + 2, bod2 + 2, 100)


def on_button_pressed_a():
    global bod1, bod2, bod3, bod4, bod5, bod6, A
    if A == 0:
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
        A += 1

    if A == 1:
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
