from gpiozero import LED
import tkinter
from tkinter import *

led_green = LED(4)
led_blue = LED(17)
led_red = LED(27)

window = tkinter.Tk()
window.title('Led Selector')
window.geometry('350x160+900+400')

    
def select_led():
    clear_all_leds()
    selected_led_value = led_value.get()
    if selected_led_value == 1:
        led_green.on()
    if selected_led_value == 2:
        led_blue.on()
    if selected_led_value == 3:
        led_red.on()

def clear_all_leds():
    led_green.off()
    led_blue.off()
    led_red.off()

def exit_application():
    clear_all_leds()
    window.destroy()

# Add label for application info
stringVar = StringVar()
lbl = Label(window, textvariable = stringVar)
stringVar.set('Select a radio button below to turn on the LED')
lbl.pack()

# Create radio buttons for Led selection
led_value = IntVar()
rdo1 = Radiobutton(window, text = 'Led Green', variable = led_value , value = 1, command = select_led)
rdo1.pack(anchor = W)

rdo2 = Radiobutton(window, text = 'Led Blue', variable = led_value , value = 2, command = select_led)
rdo2.pack(anchor = W)

rdo3 = Radiobutton(window, text = 'Led Red', variable = led_value , value = 3, command = select_led)
rdo3.pack(anchor = W)

# Create button to exit application
button_a = tkinter.Button(window, text = 'Exit Led Selector', command = exit_application)
button_a.place(x = 25, y = 100)

window.mainloop()  