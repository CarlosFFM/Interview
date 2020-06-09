# to simulate the inputs
lInputs = ["1,2,1,3,M,P,M,7,4,5,M".split(","),
           "1,2,2,1,P,M,P,M,3,12,11,P,12,P,M".split(","),
           "1,P,M".split(","),
           "1,3,2,1,7,1,P,M,P,M,P,P,M,3,12,11,P,12,P,M".split(","),
           "1,2,2,K,P,M,P,M,3,12,11,P,12,P,M".split(",")]

# using lists as stacks, could define an object but it also works like that
# as long as I don't add functionality a stack does not have
def add(p, mainStack, maxConStack):
    if p.isdigit():
        p = int(p)
        if len(mainStack) > 0:
            mainStack.append(p)
            maxConStack.append(max(p, maxConStack[-1]))
        else:
            mainStack.append(p)
            maxConStack.append(p)
        return mainStack, maxConStack
    elif p in "MP":
        if len(mainStack) > 0:
            if p == "P":
                #print(mainStack[-1])
                mainStack = mainStack[:-1]
                maxConStack = maxConStack[:-1]
            else:
                print(maxConStack[-1])
        else:
            print("Stack is empty")
        return mainStack, maxConStack
    else:
        print("{} is not a valid instruction".format(p))
        return mainStack, maxConStack


def check(inputs):
    nStack = []
    mStack = []

    for i in inputs:
        nStack, mStack = add(i, nStack, mStack)

    print(nStack)
    print(mStack)


for l in lInputs:
    print("*********************")
    check(l)
