def main():
    x = list(input("Type some shit in this: ").lower())
    y = list("frog")

    fs = 0
    rs = 0
    os = 0
    gs = 0

    n = 0

    z = []
    while n < len(x):
        for i in y:
            if x[n] in i:
                z.append(x[n])
        n += 1

    for i in z:
        if i == 'f':
            fs += 1
        elif i == 'r':
            rs += 1
        elif i == 'o':
            os += 1
        elif i == 'g':
            gs += 1

    numberslol = min([fs, rs, os, gs])

    if numberslol >= 1:
        print("congrats I found {} frog(s) in that".format(numberslol))
    if numberslol == 0:
        print("Great dumbass theres no frog in this... DISGUSTING!")

main()
