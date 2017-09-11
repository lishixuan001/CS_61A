"""CS 61A Presents The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################

def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    # The perfeted code doesn't save every result in a list but check 1
    # use an boolean and return total or 1
    total = 0
    index = False
    while num_rolls > 0:
        single_turn = dice()
        total += single_turn
        num_rolls -= 1
        if single_turn == 1:
            index = True
    if index:
        return 1
    return total
    # END PROBLEM 1

def free_bacon(opponent_score):
    """Return the points scored from rolling 0 dice (Free Bacon)."""
# BEGIN PROBLEM 2
    digits = []
    while opponent_score // 10 > 0:
        last_digit = opponent_score % 10
        digits.append(last_digit)
        opponent_score = opponent_score // 10
    digits.append(opponent_score)
    the_largest = max(digits)
    return the_largest + 1

# END PROBLEM 2


# Write your prime functions here!


def is_prime(n):
    from math import sqrt
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    k = 2
    while k < sqrt(n) + 1:
        if n % k == 0:
            return False
        k = k + 1
    return True

def next_prime(n):
    n = n + 1
    while not is_prime(n):
        n = n + 1
    return n

def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).
    Return the points scored for the turn by the current player. Also
    implements the Hogtimus Prime rule.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.ˆ
    dice:            A function that simulates a single dice roll outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN PROBLEM 2

    if num_rolls == 0:
        turn_score = free_bacon(opponent_score)
    else:
        turn_score = roll_dice(num_rolls, dice)

    if is_prime(turn_score):
        return next_prime(turn_score)
    else:
        return turn_score

    # END PROBLEM 2


def select_dice(dice_swapped):
    """Return a six-sided dice unless four-sided dice have been swapped in due
    to Perfect Piggy. DICE_SWAPPED is True if and only if four-sided dice are in
    play.
    """
    # BEGIN PROBLEM 3
    if dice_swapped == True:
        return four_sided
    else:
        return six_sided  # Replace this statement
    # END PROBLEM 3


# Write additional helper functions here!


def is_perfect_piggy(turn_score):
    """Returns whether the Perfect Piggy dice-swapping rule should occur."""
    # BEGIN PROBLEM 4
    from math import sqrt
    if turn_score == 1:
        return False
    else:
        cubic = turn_score ** (1/3)
        if sqrt(turn_score) == int(sqrt(turn_score)):
            return True
        elif cubic == int(cubic):
            return True
        else:
            return False
    # END PROBLEM 4


def is_swap(score0, score1):
    """Returns whether one of the scores is double the other."""
    # BEGIN PROBLEM 5
    if score0 == 2 * score1 or score1 == 2 * score0:
        return True
    else:
        return False
    # END PROBLEM 5


def other(player):
    """Return the other player, for a player PLAYER numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - player


def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with Player
    0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0:     The starting score for Player 0
    score1:     The starting score for Player 1
    """
    player = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    dice_swapped = False # Whether 4-sided dice have been swapped for 6-sided
    # BEGIN PROBLEM 6
    # Make the constructor for players, packaging all their scores and strategies into one place
    score_board = [score0, score1]
    strategy_board = [strategy0, strategy1]

    if [x for x in score_board if x >= goal]:
        return score_board[0], score_board[1]
    dice = select_dice(dice_swapped)

    while True:
        # In order to make the code more precise, I made constructor from the top, which
        # are 'score_board' and 'strategy_board', so that we can change players' information
        # easier with their player code(0/1)
        this_turn = take_turn(strategy_board[player](score_board[player], score_board[other(player)]), score_board[other(player)], dice)
        if is_perfect_piggy(this_turn):
            dice_swapped = not dice_swapped

        dice = select_dice(dice_swapped)
        score_board[player] = score_board[player] + this_turn

        if is_swap(score_board[0], score_board[1]):
            score_board[0], score_board[1] = score_board[1], score_board[0]

        if [x for x in score_board if x >= goal]:
            return score_board[0], score_board[1]
        player = other(player)

    # END PROBLEM 6
    return score_board[0], score_board[1]


#######################
# Phase 2: Strategies #
#######################

def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy


def check_strategy_roll(score, opponent_score, num_rolls):
    """Raises an error with a helpful message if NUM_ROLLS is an invalid
    strategy output. All strategy outputs must be integers from -1 to 10.

    >>> check_strategy_roll(10, 20, num_rolls=100)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(10, 20) returned 100 (invalid number of rolls)

    >>> check_strategy_roll(20, 10, num_rolls=0.1)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(20, 10) returned 0.1 (not an integer)

    >>> check_strategy_roll(0, 0, num_rolls=None)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(0, 0) returned None (not an integer)
    """
    msg = 'strategy({}, {}) returned {}'.format(
        score, opponent_score, num_rolls)
    assert type(num_rolls) == int, msg + ' (not an integer)'
    assert 0 <= num_rolls <= 10, msg + ' (invalid number of rolls)'


def check_strategy(strategy, goal=GOAL_SCORE):
    """Checks the strategy with all valid inputs and verifies that the strategy
    returns a valid input. Use `check_strategy_roll` to raise an error with a
    helpful message if the strategy returns an invalid output.

    >>> def fail_15_20(score, opponent_score):
    ...     if score != 15 or opponent_score != 20:
    ...         return 5
    ...
    >>> check_strategy(fail_15_20)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(15, 20) returned None (not an integer)
    >>> def fail_102_115(score, opponent_score):
    ...     if score == 102 and opponent_score == 115:
    ...         return 100
    ...     return 5
    ...
    >>> check_strategy(fail_102_115)
    >>> fail_102_115 == check_strategy(fail_102_115, 120)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(102, 115) returned 100 (invalid number of rolls)
    """
    # BEGIN PROBLEM 7
    for i in range(0,goal):
        for j in range(0,goal):
            num_rolls = strategy(i,j)
            check = check_strategy_roll(i,j,num_rolls)
    return None
    # END PROBLEM 7


# Experiments

def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.0
    """
    # BEGIN PROBLEM 8

    def result(*args):
        output = []
        import numpy
        for i in range(num_samples):
            output.append(fn(*args))
        avg = numpy.mean(output)
        return avg
    return result

    # END PROBLEM 8


def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    # According to the meaning of the variable, I named them 'max_score' and 'max_scoring_num'.
    find_avg = make_averaged(roll_dice, num_samples)
    max_score, max_scoring_num = 0, 0
    for i in range(1,11):
        score = find_avg(i, dice)
        if score > max_score:
            max_scoring_num = i
            max_score = score
    return max_scoring_num
    # END PROBLEM 9


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(4)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    if True:  # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        four_sided_max = max_scoring_num_rolls(four_sided)
        print('Max scoring num rolls for four-sided dice:', four_sided_max)

    if False:  # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if False:  # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if False:  # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))

    "*** You may add additional experiments as you wish ***"


# Strategies

def bacon_strategy(score, opponent_score, margin=8, num_rolls=4):
    """This strategy rolls 0 dice if that gives at least MARGIN points, and
    rolls NUM_ROLLS otherwise.
    """
    # BEGIN PROBLEM 10
    result = free_bacon(opponent_score)
    if is_prime(result):
        result = next_prime(result)
    if result >= margin:
        return 0
    else:
        return num_rolls  # Replace this statement
    # END PROBLEM 10
check_strategy(bacon_strategy)


def swap_strategy(score, opponent_score, margin=8, num_rolls=4):
    """This strategy rolls 0 dice when it triggers a beneficial swap. It also
    rolls 0 dice if it gives at least MARGIN points. Otherwise, it rolls
    NUM_ROLLS.
    """
    # BEGIN PROBLEM 11
    result = free_bacon(opponent_score)
    if opponent_score == 2 * (score + result):
        return 0
    if opponent_score == 0.5 * (score + result):
        return num_rolls
    return bacon_strategy(score, opponent_score, margin, num_rolls)
    # END PROBLEM 11
check_strategy(swap_strategy)



def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    # BEGIN PROBLEM
    # Calculated that make_averaged(roll_dice, 1000000)(4) = 8.25
    # six_sided: max when 6
    # four_sided: max when 4
    # make_averaged(roll_dice, 1000000)(4, four_sided) = 4.5

    # if the opponent_score < 10, return the best choice no matter what
    # Take the bacon_score as a creteria for change dice and swap
    # Two conditions: 1\Good Swap.  2\Bad Swap
    # if bad swap, do not return 0
    # conditions: score > oppo and score < oppo
    # if score < oppo, be aggresive
    # if score > oppo, be protective
    # if bacon_score makes result good, change the dice
    """

    if opponent_score < 10:
        return swap_strategy(score, opponent_score, 8, 6)

    bacon_score = free_bacon(opponent_score)
    if is_prime(bacon_score):
        bacon_score = next_prime(bacon_score)

    if 2 * (score + bacon_score) == opponent_score:
        return 0
    else:
        if (score + bacon_score) == 2 * opponent_score:
            if score <= opponent_score:
                choice = swap_strategy(score, opponent_score, 4.5, 6)
                if choice == 0:
                    return 6
                return choice
            else:
                choice = swap_strategy(score, opponent_score, 8, 6)
                if choice == 0:
                    return 6
                return choice
        else:
            # if score > 90:
            #     return 0
            if score <= opponent_score:
                # if is_prime(bacon_score):
                #     return 0
                # if score > 90:
                #     return 0
                if bacon_score >= 8 and is_perfect_piggy(bacon_score):
                    return 0
                # if opponent_score >= 80:
                #     return 0
                return swap_strategy(score, opponent_score, 8, 6)
            else:
                # if is_prime(bacon_score):
                #     return 0
                if bacon_score >= 4 and is_perfect_piggy(bacon_score):
                    return 0
                if score > 90:
                    return 0
                # if opponent_score >= 80:
                #     return 0
                return swap_strategy(score, opponent_score, 4.5, 4)

    # END PROBLEM 12
check_strategy(final_strategy)


##########################
# Command Line Interface #
##########################

# NOTE: Functions in this section do not need to be changed. They use features
# of Python not yet covered in the course.

@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
