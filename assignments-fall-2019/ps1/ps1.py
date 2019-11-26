################################################################################
# 6.0002 Fall 2019
# Problem Set 1
# Written By: yunb, mkebede
# Name:
# Collaborators:
# Time:


# Problem 1
class State():
    """
    A class representing the election results for a given state. 
    Assumes there are no ties between dem and gop votes. The party with a 
    majority of votes receives all the Electoral College (EC) votes for 
    the given state.
    """

    def __init__(self, name, dem, gop, ec):
        """
        Parameters:
        name - the 2 letter abbreviation of a state
        dem - number of Democrat votes cast
        gop - number of Republican votes cast
        ec - number of EC votes a state has 

        Attributes:
        self.name - str, the 2 letter abbreviation of a state
        self.winner - str, the winner of the state, "dem" or "gop"
        self.margin - int, difference in votes cast between the two parties, a positive number
        self.ec - int, number of EC votes a state has
        """
        pass
        # TODO

    def get_name(self):
        """
        Returns:
        str, the 2 letter abbreviation of the state  
        """
        pass
        # TODO

    def get_num_ecvotes(self):
        """
        Returns:
        int, the number of EC votes the state has 
        """
        pass
        # TODO

    def get_margin(self):
        """
        Returns: 
        int, difference in votes cast between the two parties, a positive number
        """
        pass
        # TODO

    def get_winner(self):
        """
        Returns:
        str, the winner of the state, "dem" or "gop"
        """
        pass
        # TODO

    def __str__(self):
        """
        Returns:
        str, representation of this state in the following format,
        "In <state>, <ec> EC votes were won by <winner> by a <margin> vote margin."
        """
        pass
        # TODO

    def __eq__(self, other):
        """
        Determines if two State instances are the same.
        They are the same if they have the same state name, winner, margin and ec votes.
        Be sure to check for instance type equality as well! 

        Note: 
        1. Allows you to check if State_1 == State_2
                2. Make sure to check for instance type (Hint: look up isinstance())

        Param:
        other - State object to compare against  

        Returns:
        bool, True if the two states are the same, False otherwise
        """
        pass
        # TODO


# Problem 2
def load_election(filename):
    """
    Reads the contents of a file, with data given in the following tab-delimited format,
    State   Democrat_votes    Republican_votes    EC_votes 

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a list of State instances
    """
    pass
    # TODO


# Problem 3
def find_winner(election):
    """
    Finds the winner of the election based on who has the most amount of EC votes.
    Note: In this simplified representation, all of EC votes from a state go
    to the party with the majority vote.

    Parameters:
    election - a list of State instances 

    Returns:
    a tuple, (winner, loser) of the election i.e. ('dem', 'gop') if Democrats won, else ('gop', 'dem')
    """
    pass
    # TODO


def get_winner_states(election):
    """
    Finds the list of States that were won by the winning candidate (lost by the losing candidate).

    Parameters:
    election - a list of State instances 

    Returns:
    A list of State instances won by the winning candidate
    """
    pass
    # TODO


def ec_votes_reqd(election, total=538):
    """
    Finds the number of additional EC votes required by the loser to change election outcome.
    Note: A party wins when they earn half the total number of EC votes plus 1.

    Parameters:
    election - a list of State instances 
    total - total possible number of EC votes

    Returns:
    int, number of additional EC votes required by the loser to change the election outcome
    """
    pass
    # TODO


# Problem 4
def greedy_election(winner_states, ec_votes_needed):
    """
    Finds a subset of winner_states that would change an election outcome if
    voters moved into those states. First chooses the states with the smallest 
    win margin, i.e. state that was won by the smallest difference in number of voters. 
    Continues to choose other states up until it meets or exceeds the ec_votes_needed. 
    Should only return states that were originally won by the winner in the election.

    Parameters:
    winner_states - a list of State instances that were won by the winner 
    ec_votes_needed - int, number of EC votes needed to change the election outcome

    Returns:
    A list of State instances such that the election outcome would change if additional
    voters relocated to those states (also can be referred to as our swing states)
    The empty list, if no possible swing states
    """
    pass
    # TODO


# Problem 5
def dp_move_max_voters(winner_states, ec_votes, memo=None):
    """
    Finds the largest number of voters needed to relocate to get at most ec_votes
    for the election loser. 

    Analogy to the knapsack problem:
    Given a list of states each with a weight(#ec_votes) and value(#margin),
    determine the states to include in a collection so the total weight(#ec_votes)
    is less than or equal to the given limit(ec_votes) and the total value(#voters displaced)
    is as large as possible.

        Hint: If using a top-down implementation, it may be helpful to create a helper function

    Parameters:
    winner_states - a list of State instances that were won by the winner 
    ec_votes - int, number of EC votes (relocation should result in gain of AT MOST ec_votes)
    memo - dictionary, an OPTIONAL parameter for memoization (don't delete!).
    Note: If you decide to use the memo make sure to override the default value when it's first called.

    Returns:
    A list of State instances such that the maximum number of voters need to be relocated
    to these states in order to get at most ec_votes 
    The empty list, if every state has a # EC votes greater than ec_votes
    """
    pass
    # TODO


def move_min_voters(winner_states, ec_votes_needed):
    """
    Finds a subset of winner_states that would change an election outcome if
    voters moved into those states. Should minimize the number of voters being relocated. 
    Only return states that were originally won by the winner (lost by the loser)
    of the election.

    Hint: This problem is simply the complement of dp_move_max_voters

    Parameters:
    winner_states - a list of State instances that were won by the winner 
    ec_votes_needed - int, number of EC votes needed to change the election outcome

    Returns:
    A list of State instances such that the election outcome would change if additional
    voters relocated to those states (also can be referred to as our swing states)
    The empty list, if no possible swing states
    """
    pass
    # TODO


# Problem 6
def flip_election(election, swing_states):
    """
    Finds a way to shuffle voters in order to flip an election outcome. 
    Moves voters from states that were won by the losing candidate (states not in winner_states), 
    to each of the states in swing_states.
    To win a swing state, you must move (margin + 1) new voters into that state. Any state that voters are
    moved from should still be won by the loser even after voters are moved.
    Reminder that you cannot move voters out of California, Washington, Texas, or Tennessee. 

    Also finds the number of EC votes gained by this rearrangement, as well as the minimum number of 
    voters that need to be moved.

    Parameters:
    election - a list of State instances representing the election 
    swing_states - a list of State instances where people need to move to flip the election outcome 
                   (result of move_min_voters or greedy_election)

    Return:
    A tuple that has 3 elements in the following order:
        - a dictionary with the following (key, value) mapping: 
            - Key: a 2 element tuple, (from_state, to_state), the 2 letter abbreviation of the State 
            - Value: int, number of people that are being moved 
        - an int, the total number of EC votes gained by moving the voters 
        - an int, the total number of voters moved 
    None, if it is not possible to sway the election
    """
    pass
    # TODO


if __name__ == "__main__":
    pass
    # Uncomment the following lines to test each of the problems

    # # tests Problem 1 
    # ma = State("MA", 100000, 20000, 8)
    # print(isinstance(ma, State))
    # print(ma)

    # # tests Problem 2 
    # year = 2012
    # election = load_election("%s_results.txt" % year)
    # print(len(election))
    # print(election[0])

    # # tests Problem 3
    # winner, loser = find_winner(election)
    # won_states = get_winner_states(election)
    # names_won_states = [state.get_name() for state in won_states]
    # ec_votes_needed = ec_votes_reqd(election)
    # print("Winner:", winner, "\nLoser:", loser)
    # print("States won by the winner: ", names_won_states)
    # print("EC votes needed:",ec_votes_needed, "\n")

    # # tests Problem 4
    # print("greedy_election")
    # greedy_swing = greedy_election(won_states, ec_votes_needed)
    # names_greedy_swing = [state.get_name() for state in greedy_swing]
    # voters_greedy = sum([state.get_margin()+1 for state in greedy_swing])
    # ecvotes_greedy = sum([state.get_num_ecvotes() for state in greedy_swing])
    # print("Greedy swing states results:", names_greedy_swing)
    # print("Greedy voters displaced:", voters_greedy, "for a total of", ecvotes_greedy, "Electoral College votes.\n")

    # # tests Problem 5: dp_move_max_voters
    # print("dp_move_max_voters")
    # total_lost = sum(state.get_num_ecvotes() for state in won_states)
    # move_max = dp_move_max_voters(won_states, total_lost-ec_votes_needed)
    # max_states_names = [state.get_name() for state in move_max]
    # max_voters_displaced = sum([state.get_margin()+1 for state in move_max])
    # max_ec_votes = sum([state.get_num_ecvotes() for state in move_max])
    # print("States with the largest margins:", max_states_names)
    # print("Max voters displaced:", max_voters_displaced, "for a total of", max_ec_votes, "Electoral College votes.", "\n")

    # # tests Problem 5: move_min_voters
    # print("move_min_voters")
    # swing_states = move_min_voters(won_states, ec_votes_needed)
    # swing_state_names = [state.get_name() for state in swing_states]
    # min_voters = sum([state.get_margin()+1 for state in swing_states])
    # swing_ec_votes = sum([state.get_num_ecvotes() for state in swing_states])
    # print("Complementary knapsack swing states results:", swing_state_names)
    # print("Min voters displaced:", min_voters, "for a total of", swing_ec_votes, "Electoral College votes. \n")

    # # tests Problem 6: flip_election
    # print("flip_election")
    # flipped_election = flip_election(election, swing_states)
    # print("Flip election mapping:", flipped_election)
