from machine import Pin, Timer

led = Pin(25, Pin.OUT)
LED_State = True
tim = Timer()

def tick(timer):
    global led, LED_State
    LED_State = not LED_State
    led.value(LED_State)
    
tim.init(freq=1, mode=Timer.PERIODIC, callback=tick)