def on_button_pressed_a():
    global xindex, yindex, currentbrightness
    for index in range(50):
        xindex = randint(0, 4)
        yindex = randint(0, 4)
        led.plot_brightness(xindex, yindex, currentbrightness)
        currentbrightness += 50
        basic.pause(500)
        led.unplot(xindex, yindex)
        currentbrightness += 50
        basic.pause(500)
input.on_button_pressed(Button.A, on_button_pressed_a)

yindex = 0
xindex = 0
currentbrightness = 0
currentbrightness = 10