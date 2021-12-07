from pypresence import Presence
import time

def RPCRunner(client_id, state, details, large_text, large_image, small_text, small_image, buttons):

    kwargs = dict(state=state, details=details, large_text=large_text, large_image=large_image, small_text=small_text, small_image=small_image, buttons=buttons)

    RPC = Presence(client_id) 
    RPC.connect() 
    print(RPC.update(**{k: v for k, v in kwargs.items() if v != ""}, start=time.time()))  # Set the presence

    while True:
        time.sleep(15)