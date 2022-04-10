A = 0
B = 0
led.plot(2, 0)
led.plot(0, 4)
led.plot(4, 4)
led.plot_brightness(2, 2, 100)

def on_button_pressed_a():
    global A
    basic.clear_screen()
    A += 1
    if A == 1:
        led.plot(4, 2)
        led.plot(0, 0)
        led.plot(0, 4)
        led.plot_brightness(2, 2, 100)

    if A == 2:
        basic.clear_screen()
        led.plot(2, 4)
        led.plot(4, 0)
        led.plot(0, 0)
        led.plot_brightness(2, 2, 100)

    if A == 3:
        basic.clear_screen()
        led.plot(0, 2)
        led.plot(4, 0)
        led.plot(4, 4)
        led.plot_brightness(2, 2, 100)

    if A == 4:
        basic.clear_screen()
        led.plot(2, 0)
        led.plot(0, 4)
        led.plot(4, 4)
        led.plot_brightness(2, 2, 100)
        A -= 4
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global B
    basic.clear_screen()
    B += 1
    if B == 1:
        led.plot(2, 0)
        led.plot(0, 4)
        led.plot(4, 4)
        led.plot_brightness(2, 2, 100)

    if B == 2:
        basic.clear_screen()
        led.plot(0, 2)
        led.plot(4, 0)
        led.plot(4, 4)
        led.plot_brightness(2, 2, 100)

    if B == 3:
        basic.clear_screen()
        led.plot(2, 4)
        led.plot(4, 0)
        led.plot(0, 0)
        led.plot_brightness(2, 2, 100)

    if B == 4:
        basic.clear_screen()
        led.plot(4, 2)
        led.plot(0, 0)
        led.plot(0, 4)
        led.plot_brightness(2, 2, 100)
        B -= 4
input.on_button_pressed(Button.B, on_button_pressed_b)
