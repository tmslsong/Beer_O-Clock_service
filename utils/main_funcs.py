def msg_processor(msg_code):
    '''
    msg_processor returns a msg object with 'msg', 'type'
    where 'msg' corresponds to the message user sees
    and 'type' is the color of the alert element

    codes:
        - 0 : Successfully added to database
        - 1 : User does not exist
        - 2 : Successfully updated your beer style to database
        - 3 : Successfully deleted user
    '''

    msg_code = int(msg_code)

    msg_list = [
        (
            'Successfully added to database',
            'success'
        ),
        (
            'User does not exist',
            'warning'
        ),
        (
            'Unable to retrieve tweets',
            'warning'
        ),
        (
            'Successfully deleted user',
            'info'
        )
    ]

    return {
        'msg':msg_list[msg_code][0],
        'type':msg_list[msg_code][1]
    }