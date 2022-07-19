'''Module 4: Individual Programming Assignment 1
Parsing Data
This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.
    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.
    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.
    This function describes the relationship that two users have with each other.
    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.
    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    
    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    Status = all([from_member in social_graph[to_member]['following'],to_member in social_graph[from_member]['following']])
    if Status == True:
        Results = ("friends")
    elif (to_member in social_graph[from_member]['following']) == True:
        Results = ("follower")
    elif (from_member in social_graph[to_member]['following']) == True:
        Results = ("followed by")
    else:
        Results = ("no relationship")
    return(Results)


def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.
    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.
    This function evaluates a tic tac toe board and returns the winner.
    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.
    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists
    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    demoset = ()
    demoset = [board[i][i] for i in range(3)]
    vertical = [x for x in zip(*board)]
    
    #diagonals
    if all([s=='X' for s in demoset]) == True:
        result = ('X')
    elif all([s=='O' for s in demoset]) == True:
        result = ('O')
        
    #horizontals
    elif all([s=='X' for s in board[0]]) == True:
        result = ('X')
    elif all([s=='X' for s in board[1]]) == True:
        result = ('X')
    elif all([s=='X' for s in board[2]]) == True:
        result = ('X')
    elif all([s=='O' for s in board[0]]) == True:
        result = ('O')
    elif all([s=='O' for s in board[1]]) == True:
        result = ('O')
    elif all([s=='O' for s in board[2]]) == True:
        result = ('O')
        
    #verticals
    elif all([s=='X' for s in vertical[0]]) == True:
        result = ('X')
    elif all([s=='X' for s in vertical[1]]) == True:
        result = ('X')
    elif all([s=='X' for s in vertical[2]]) == True:
        result = ('X')
    elif all([s=='O' for s in vertical[0]]) == True:
        result = ('O')
    elif all([s=='O' for s in vertical[1]]) == True:
        result = ('O')
    elif all([s=='O' for s in vertical[2]]) == True:
        result = ('O')
    
    else:
        result = ('NO WINNER')
    return result

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.
    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.
    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.
    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.
    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes
    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if first_stop == 'upd' and second_stop == 'dlsu':
        eta = route_map['upd','admu']['travel_time_mins'] + route_map['admu','dlsu']['travel_time_mins']
    elif first_stop == 'admu' and second_stop == 'upd':
        eta = route_map['admu','dlsu']['travel_time_mins'] + route_map['dlsu','upd']['travel_time_mins']
    else:
        eta = route_map[first_stop,second_stop]['travel_time_mins']
    return eta


# for second legs:

    if first_stop == 'a1' and second_stop == 'b1':
        eta = route_map['a1','a2']['travel_time_mins'] + route_map['a2','b1']['travel_time_mins']
    elif first_stop == 'a2' and second_stop == 'a1':
        eta = route_map['a2','b1']['travel_time_mins'] + route_map['b1','a1']['travel_time_mins']
    else:
        eta = route_map'[first_stop,second_stop]['travel_time_mins']
    return eta