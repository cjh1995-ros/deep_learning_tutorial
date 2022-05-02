KILLO_TO_BYTE = 1024
MEGA_TO_KILLO = 1024

def get_model_size(model):
    import os
    foo = "test.h5"
    model.save(foo)
    size = os.path.getsize(foo) / (MEGA_TO_KILLO * KILLO_TO_BYTE)}
    os.remove(foo)
    print(f"Model Size is {size:.5f}MB")
    return size