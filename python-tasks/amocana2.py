def change(coin):
    x = 0
    a = 1
    b = 5
    c = 10
    d = 20
    e = 50
    if coin > 0:
        while coin >= 1:
            while coin / e >= 1:
                coin = coin - e
                x += 1
                
            while coin / d >= 1:
                coin = coin - d
                x += 1

            while coin / c >= 1:
                coin = coin - c
                x += 1

            while coin / b >= 1:
                coin = coin - b
                x += 1

            while coin / a >= 1:
                coin = coin - a
                x += 1

        return print('dasashlelad sachiroa', x ,'moneta')