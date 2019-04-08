import meanwhile
import board
import digitalio


#async
def blink1(pin):
    io = digitalio.DigitalInputOutput(pin)
    io.switch_to_output()
    while True:
        io.value = not pin.value
        #await
        yield from meanwhile.sleep(1)

#async
def blink2(pin):
    #await
    yield from meanwhile.sleep(0.5)
    #await
    yield from blink1(pin)


meanwhile.run(blink1(board.D1), blink2(board.D2))