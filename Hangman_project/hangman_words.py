import random


class WordList:
    word_list = ("abruptly absurd abyss affix askew avenue awkward axiom azure bagpipes bandwagon banjo "
                 "bayou beekeeper bikini blitz blizzard boggle bookworm boxcar boxful buckaroo buffalo "
                 "buffoon buxom buzzard buzzing buzzwords caliph cobweb cockiness croquet crypt curacao cycle "
                 "daiquiri dirndl disavow dizzying duplex dwarves embezzle equip espionage exodus faking "
                 "fishhook fixable fjord flapjack flopping fluffiness flyby foxglove frazzled frizzled "
                 "fuchsia funny gabby galaxy galvanize gazebo gizmo glowworm glyph gnarly gnostic gossip "
                 "grogginess haiku haphazard hyphen iatrogenic icebox injury ivory ivy jackpot jaundice "
                 "jawbreaker jaywalk jazziest jazzy jelly jigsaw jinx jiujitsu jockey jogging joking jovial"
                 "joyful juicy jukebox jumbo kayak kazoo keyhole khaki kilobyte kiosk kitsch kiwifruit klutz "
                 "knapsack larynx lengths lucky luxury lymph marquis matrix megahertz microwave mnemonic "
                 "mystify naphtha nightclub nowadays numskull nymph onyx ovary oxidize oxygen pajama peekaboo "
                 "phlegm pixel pizazz pneumonia polka pshaw psyche puppy puzzling quartz queue quips quixotic "
                 "quiz quizzes quorum razzmatazz rhubarb rhythm rickshaw schnapps scratch shiv snazzy sphinx "
                 "spritz squawk staff strength strengths stretch stronghold stymied subway swivel syndrome "
                 "thriftless thumbscrew topaz transcript transgress transplant twelfth twelfths unknown "
                 "unworthy unzip uptown vaporize vixen vodka voodoo vortex voyeurism walkway waltz wave wavy "
                 "waxy wellspring wheezy whiskey whizzing whomever wimpy witchcraft wizard woozy wristwatch "
                 "xylophone yachtsman yippee yoked youthful yummy zephyr zigzag zigzagging zilch zipper zodiac "
                 "zombie ").split()

    alphabets = "abcdefghijklmnopqrstuvwxyz"

    def get_chosen_word(self):
        return random.choice(self.word_list)

    def get_alphabets(self):
        self.alphabets = [x for x in self.alphabets]
        return self.alphabets
