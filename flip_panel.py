import time, sys

class flip_panel:

    ALL_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                           'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6',
                           '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(',
                           ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', "'", " "]

    def __init__(self, current_index='a', target_index='a', flip_duration=3.0):

        self.current_index = self.ALL_CHARACTERS.index(current_index)
        self.target_index = self.ALL_CHARACTERS.index(target_index)
        self.duration = flip_duration

        self.flips_needed = self.get_flips_needed()
        self.seconds_per_flip = self.get_seconds_per_flip()

        self.last_flip = time.monotonic()


    def get_flips_needed(self):

        return (self.target_index - self.current_index) % len(self.ALL_CHARACTERS)
    
    def get_seconds_per_flip(self):
        return self.duration / self.flips_needed if self.flips_needed > 0 else 0

    def update(self, now):
        if self.current_index == self.target_index:
            return

        if now - self.last_flip >= self.seconds_per_flip:
            self.current_index = (self.current_index + 1) % len(self.ALL_CHARACTERS)
            self.last_flip = now

    def char(self):
        return self.ALL_CHARACTERS[self.current_index]

    def done(self):
        return self.current_index == self.target_index

    