from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    '''
    if lowered == ' ':
        return 'Tumben gak berisik, diam diam bae...'
    '''

    if 'halo satpam' in lowered:
        return 'Halo, apa kabar adik adik'
    elif 'satpam, lempar dadu dong' in lowered:
        return f'Ok, jadinya dadu yang terlempar:  {randint(1,6)}'
    else:
        pass

    