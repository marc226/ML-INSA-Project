import load_data

class faceDetector():
    def __init__(self):
        self.net = load_data.net

    # feed a 36x36x1 array into
    def identify36x36Image(numpyArray):

