import keyboard
import sys

# def on_key_press(event):
#     if event.name == "esc":
#         keyboard.unhook_all()
#     else:
#         print(f"Key {event.name} pressed")

# ⬆️ We can use either on_key_press or on_key_release, but my observation is that on_key_release suggested that on_key_released is more reliable.




def on_key_release(event, input_string=[]):
    if event.name == "esc":
        keyboard.unhook_all()
        passing_string = ''.join(input_string)
        print(f"The input sting is {passing_string} \nExiting the program...")
        sys.exit(0) # for now lets exit the program using esc key
    else:    
        input_string += str(event.name)
        print(f"Key {event.name} released")



# keyboard.on_press(on_key_press)
keyboard.on_release(on_key_release)

keyboard.wait()