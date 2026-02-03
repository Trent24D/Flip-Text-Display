class fli_panel:

    def __init__(self, width, height):
        self.curr = 0
        self.characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                           'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6',
                           '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(',
                           ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', "'"]
        
        def display(self):
            print(self.characters[self.curr])
        
        def flip(self, search):
            self.curr = self.change(self.curr)
        
        def change(self, index):
            if index + 1 >= len(self.characters):
                return 0
            else:
                return index + 1

    