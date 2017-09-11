# CS 61A World Game Data:
from classes import *

# Characters:

cale = Character('Cale',
                  'Kevin went to Soda to start grading. You can find him there.')
kevin = Character('Instructor Kevin',
                 "I can't believe I lost my wallet again! "
                 "I wish someone could find it for me.")
mitas = Character('Mitas',
                  'No one brought food to the potluck! '
                  'Maybe the Golden Bear Cafe (GBC) is open; we can get food there.')
michelle = Character('Michelle',
                     'Why is Soda so darn far from everything?')
kyle = Character('Kyle',
                 "What do you mean Ok doesn't work?")
jerry = Character('Jerry',
                  'I heard you like games, so I put some games in this game. '
                  'Have you gone to Games of Berkeley on Shattuck?')
kelly = Character('Kelly',
                  'Hey! Want to play ultimate frisbee?')
student = Character('Student',
                    'I once went into Dwinelle and got lost for 3 days! '
                    'That place is a maze!')
scared_student = Character('Terrified Student',
                           "I've been lost in Dwinelle for weeks")
spooked_student = Character('Spooked Student',
                            'Help')

# Things:
wallet = Thing('Wallet',
               "Looks like Kevin's wallet. We should return it to him.")
lemon = Thing('Lemon',
               'Hmmm... try bringing it to a TA')
coffee = Thing('Coffee',
               'The sweet, caffeinated nectar of the gods')
monopoly = Thing('Monopoly',
              'Just right for 61A study breaks!')
strange_skull = Thing('Strange Skull',
                      'A strange skull. Dinosaur? Giraffe? Who knows.')

# Keys:
try:
    skeleton_key = Key('Skeleton Key', 'A key that unlocks many doors')
except NameError as e:
    skeleton_key = Thing('Not a Skeleton Key', 'You must first implement the Key class')

# Places:

sather_gate = Place('Sather Gate', 'Sather Gate - A fairly ineffective gate',
                    [], [])
fsm = Place('FSM', 'Free Speech Cafe - Home of Coffee',
            [], [wallet, coffee])
vlsb = Place('VLSB', 'VLSB - CS61A lectures are held here.',
             [cale], [skeleton_key])
soda = Place('Soda', 'Soda Hall - A building where Soda is not allowed',
             [kevin, mitas, michelle], [])
gbc = Place('GBC', 'Golden Bear Cafe - Now with healthy food',
            [], [lemon])
campanile = Place('Campanile', 'The Campanile - A great tower!',
                  [kyle], [])
game_store = Place('Games of Berkeley', 'Games of Berkeley',
                   [], [monopoly])
hp = Place('HP', 'HP Auditorium',
            [], [])
shattuck = Place('Shattuck', 'Shattuck Avenue',
                 [], [])
mlk = Place('MLK Student Union ', 'Martin Luther King Jr. Student Union - A great place to study.',
                [jerry], [])
dwinelle = Place('Dwinelle Hall', 'Dwinelle Hall - A Maze',
                 [student], [])
deep_dwinelle = Place('Deep in Dwinelle Hall', 'You are lost in Dwinelle Hall',
                      [scared_student, spooked_student], [strange_skull])
memorial_glade = Place('Memorial Glade', 'Memorial Glade on a beautiful day',
                       [kelly], [])


# Exits:
sather_gate.add_exits([gbc, mlk, dwinelle, memorial_glade])
gbc.add_exits([sather_gate])
mlk.add_exits([sather_gate, campanile])
deep_dwinelle.add_exits([deep_dwinelle, dwinelle])
dwinelle.add_exits([sather_gate, vlsb, mlk, deep_dwinelle])
memorial_glade.add_exits([sather_gate, fsm, campanile, soda])
campanile.add_exits([memorial_glade, mlk])
vlsb.add_exits([fsm, soda, shattuck, dwinelle])
shattuck.add_exits([vlsb, game_store])
fsm.add_exits([vlsb, memorial_glade])
soda.add_exits([hp, vlsb, memorial_glade])
hp.add_exits([soda])
game_store.add_exits([shattuck])

# Locked Buildings
fsm.locked = True

# Player:
# The Player should start at sather_gate.
me = Player('Wayne', sather_gate)
