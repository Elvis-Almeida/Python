def leiadinheiro(tex=''):
    while True:
        p = False
        a = input(tex).strip()
        d = ''
        for b in a:
            if b == ',':
                d = d + '.'
            else:
                d = d + b
        a = d
        for o in a:
            if o not in '1234567890.':
                p = False
                break
            else:
                p = True
        if p:
            break
        else:
            print(f'\033[1;31mERRO! "{a}" não é um numero inválido\033[m')

    return float(d)

