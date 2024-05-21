from reciever_mod import receiver
import os

if __name__ == '__main__':
    if os.environ.get('DISPLAY', '') == '':
        print("No display found. Using dummy display.")
        os.environ['DISPLAY'] = ':0'
    
    listen = receiver.Receiver()
    listen.main()
