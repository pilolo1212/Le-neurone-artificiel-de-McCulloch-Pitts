def step_function(z):
    return 1 if z>=0 else 0


def mc_p_neuron(x, theta, inhibitory=None):
    if(inhibitory != None  ):   
        for i in inhibitory:
            if x[i] == 1: 
                return 1
        s=sum(x)
        return step_function(s - theta)



tests = [[0,0], [0,1], [1,0], [1,1]]
#AND
for x in tests:
    print(x, "->", mc_p_neuron(x, theta=2))

#OR
for x in tests:
    print(x, "->", mc_p_neuron(x, theta=1))


tests = [[0],[1]]
#NOT
for x in tests:
print(x, "->", mc_p_neuron(x, theta=0,inhibitory=[0]))
