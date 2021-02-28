input.onButtonPressed(Button.A, function () {
    for (let index = 0; index < 50; index++) {
        xindex = randint(0, 4)
        yindex = randint(0, 4)
        led.plotBrightness(xindex, yindex, currentbrightness)
        currentbrightness += 50
        basic.pause(500)
        led.unplot(xindex, yindex)
        currentbrightness += 50
        basic.pause(500)
    }
})
let yindex = 0
let xindex = 0
let currentbrightness = 0
currentbrightness = 10
