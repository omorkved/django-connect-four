def play_column():
    # Given: choice of column
    # Action: 
    # Return: Success if valid play. Failure if need to pick again.

    '''
    if column is full
        return failure (perhaps input-check in front end. javascript alert)
    else
        play
    '''

    pass

def check_win():
    # Given: x,y coordinates of play, and p_id
    # Check: if win.
    # Return: Success if won. Failure if gameplay continues.
    '''
    Check vertical:
    (Easy. Only need to check if three below.)
    If y_coord < 4:
        skip
    else: 
        if y_coord - 1, - 2, -3 all equal p_id
            success
    
    Check horizontal:
        honestly probably fastest to just scan the whole row--only 7 checks.
        build 7-char string: if p_id piece, write o. if not, write x.
        search string for 'oooo'. If so, win.

    Check diagonal:
        could play into ends of diagonal or middle diagonal so lots of checks.
        Only check decr-y direction if: y_coord + x_coord >= 3 (assuming starts at 0)
        Only check incr-y direction if: y_coord + x_coord <= 


    '''
