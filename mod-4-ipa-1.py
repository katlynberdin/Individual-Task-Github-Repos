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
    pos1 = 0 
    pos2 = 0
    
    for i in board:
        for j in i:
            if board[pos1][pos2] == "X":
                board[pos1][pos2] = 1
            
            elif board[pos1][pos2] == "O":
                board[pos1][pos2] = -1
            
            else:
                board[pos1][pos2] = 0
            
            pos2 += 1
        pos2 = 0
        pos1 += 1
        
    cap = len(board) - 1
    score = len(board)
    
    horizontal = [sum(x) for x in board]
    vertical = [sum(x) for x in zip(*board)]
    updown_diagonal = [sum([board[i][i] for i,v in enumerate(board)])]
    downup_diagonal = [sum([board[cap-i][i] for i,v in enumerate(board)])]
    
    if max(horizontal) == score or max(vertical) == score or max(updown_diagonal) == score or max(downup_diagonal) == score:
        return "X"
    elif min(horizontal) == -score or min(vertical) == -score or min(updown_diagonal) == -score or min(downup_diagonal) == -score:
        return "O"
    else:
        return "NO WINNER"
    
    
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
    route = (first_stop, second_stop)
    
    if route in route_map:
        return route_map[route]["travel_time_mins"]
    else:
        keys = list(route_map.keys())
        total_time = 0
        i = 0
        for i in range(len(keys)):
            if first_stop == keys[i][0]:
                total_time += route_map[keys[i]]["travel_time_mins"]
                break 
                
        def destination(second_stop, keys):
            time_passed = 0
            j = i + 1
            while j < len(keys):
                time_passed += route_map[keys[j]]["travel_time_mins"]
                if second_stop != keys[j][1]:
                    j += 1
                else:
                    break
                    
            if j == len(keys):
                j = 0
                while j < len(keys):
                    time_passed += route_map[keys[j]]["travel_time_mins"]
                    if second_stop != keys[j][1]:
                        j += 1
                    else:
                        break
                        
            return time_passed 
        
        total_time += destination(second_stop, keys)
        return total_time