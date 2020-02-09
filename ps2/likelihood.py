import argparse
import sys

import numpy as np

import matplotlib.pyplot as plt




def likelihood(p, data):
    l = 1
    for d in data:
        if d:
            l *= p
        else:
            l *= (1-p)

    return l

def filldata(observed, ones, zeros):
    for i in range(ones):
        observed.append(1)
    for i in range(zeros):
        observed.append(0)
    
    
def main():
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('count', type=int,
                        help="number of samples")
    parser.add_argument('ones', type=int,
                        help="number of ones")
    args = parser.parse_args()

    count = args.count
    ones = args.ones
    zeros = count - ones
    """

    observedf = []
    observedt = []
    observedh = []
    filldata(observedf, 3, 2)
    filldata(observedt, 6, 4)
    filldata(observedh, 60, 40)
            
    
    params = np.linspace(start=0, stop=1, num=100)
    
    likelihoodsf = []
    likelihoodst = []
    likelihoodsh = []
    for param in params:
        likelihoodsf.append(likelihood(param, observedf))
        likelihoodst.append(likelihood(param, observedt))
        likelihoodsh.append(likelihood(param, observedh))
        
    fig, ax = plt.subplots()
    ax.plot(params, likelihoodsf)
    ax.plot(params, likelihoodst)
    ax.plot(params, likelihoodsh)
    ax.legend(['n=5', 'n=10', 'n=100'])
    ax.set_title('Likelihood vs. Parameter')
    ax.xaxis.set_label_text('Parameter')
    ax.yaxis.set_label_text('Likelihood')
    plt.show()
    
if __name__ == "__main__" :
    main()
    
