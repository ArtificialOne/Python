import mouse
import time
import keyboard

running = True

while running:
    if keyboard.is_pressed('ctrl+c'):
        running=False
    else:
        mouse.click()
        #keyboard.press('w')
        time.sleep(0.55502000)
'''
import rbxpy

def main(): 
    client=robloxpy.Client()
    place_id=13510024
    game=client.game_join(place_id)

    player = game.get_current_player()
    player.click()

if __name__ == "__main__":
    main()
    '''
