from ps1_partition import get_partitions
import time

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    cows = {}
    with open(filename, 'r') as file:
        line = file.readline()
        while True:
            try:
                cow_name, cow_weight = line.split(',')
            except Exception:
                break
            cows.update({cow_name:int(cow_weight)})
            line = file.readline()
    return cows

def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cows_copy = cows.copy()
    cows_ordered = sorted(cows.items(), key=lambda x: x[1], reverse=True)
    trips = []

    while sum(cows_copy.values()) > 0:
        single_trip = []
        total = 0
        for cow_name, cow_weight in cows_ordered:
            if cows_copy[cow_name]!= 0 and cow_weight + total <= limit:
                single_trip.append(cow_name)
                total += cow_weight
                cows_copy[cow_name] = 0
        trips.append(single_trip)
    return trips

def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    possible_combinations = []
    for partition in get_partitions(cows.keys()):
        possible_combinations.append(partition)
    possible_combinations.sort(key=len)

    valid_combinations = possible_combinations.copy()

    ## Remove invalid partitions
    for partition in possible_combinations:
        for trip in partition:
            total = sum([cows.get(cow) for cow in trip])
            if total > limit:
                valid_combinations.remove(partition)
                break

    ## Return valid partition of minimum length
    return min(valid_combinations, key=len)

# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows('ps1_cow_data.txt')
    start = time.time()
    trips = greedy_cow_transport(cows)
    end = time.time()
    print('Time:', end - start)
    print(trips)
    start = time.time()
    trips = brute_force_cow_transport(cows)
    end = time.time()
    print('Time:', end - start)
    print(trips)

if __name__ == '__main__':
    compare_cow_transport_algorithms()
