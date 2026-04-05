def step_function(z):
    return 1 if z>=0 else 0


def mc_p_neuron(x, theta, inhibitory=None):
    if(inhibitory == None ):   
        s=sum(x)
        return step_function(s - theta)
    else :
        for i in inhibitory:
            if x[i] == 1:   # inhibitory input active
                return 0
        s=sum(x)
        return step_function(s - theta)
        

