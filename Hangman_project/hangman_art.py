
class HangmanArt:
    stages = ['''
    _____________
    |           |
    |   +---+   |
    |   |   |   |
    |   O   |   |
    |  /|\  |   |
    |  / \  |   |
    |       |   |
    | ========= |
    |___________|
    ''', '''
    _____________
    |   +---+   |
    |   |   |   |
    |   O   |   |
    |  /|\  |   |
    |  /    |   |
    |       |   |
    | ========= |
    |___________|
    ''', '''
    _____________
    |   +---+   |
    |   |   |   |
    |   O   |   |
    |  /|\  |   |
    |       |   |
    |       |   |
    | ========= |
    |___________|
    ''', '''
    _____________
    |   +---+   |
    |   |   |   |
    |   O   |   |
    |  /|   |   |
    |       |   |
    |       |   |
    | ========= |
    |___________|
    ''', '''
    _____________
    |   +---+   |
    |   |   |   |
    |   O   |   |
    |   |   |   |
    |       |   |
    |       |   |
    | ========= |
    |___________|
    ''', '''
    _____________
    |   +---+   |
    |   |   |   |
    |   O   |   |
    |       |   |
    |       |   |
    |       |   |
    | ========= |
    |___________|
    ''', '''
    _____________
    |   +---+   |
    |   |   |   | 
    |       |   |  
    |       |   |
    |       |   |
    |       |   |
    | ========= |
    |___________|
    ''']

    logo = ''' 
=======================================================
     _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                       |___/    
=======================================================
    '''

    def __len__(self):
        return len(self.stages)

    def get_logo(self):
        return self.logo

    def get_stages(self, lives):
        return self.stages[lives]

