memory = None

def save_to_memory(result):
    global memory
    memory = result

def get_from_memory():
    return memory