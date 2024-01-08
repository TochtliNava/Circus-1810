import winsound, time, random

time.sleep(random.randint(1, 10))
winsound.PlaySound("pipe.wav", winsound.SND_FILENAME)