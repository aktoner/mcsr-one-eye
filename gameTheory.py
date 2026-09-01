from scipy.stats import gamma
import json
import numpy as np
import matplotlib.pyplot as plt

with open("parameters.json", "r") as f:
    pos_params, neg_params,prob_X = json.load(f)
pos_alpha, pos_scale = pos_params
neg_alpha, neg_scale = neg_params
    


pos_pdf = lambda x: gamma.pdf(x,pos_alpha, scale=pos_scale)
neg_pdf = lambda x: gamma.pdf(x,neg_alpha, scale=neg_scale)



def unsentVsUnsent(theta):
    if theta == 0:
        return 0.5
    if theta < 0:
        return 1-unsentVsUnsent(-theta)
        
    numerator = pos_pdf(theta) * prob_X
    denominator = pos_pdf(theta)*prob_X + neg_pdf(theta)*(1-prob_X) 
    return numerator/denominator


probOfOneEye = 0.71757
def sentVsUnsent(theta):
    x = np.linspace(theta+10,theta+39.95)
    fx = [unsentVsUnsent(xi) for xi in x]
    return np.average(fx)*probOfOneEye

def unsentVsSent(theta):
    return 1-sentVsUnsent(-theta)

def sentVsSent(theta): # This is probably a bit higher than it should be but data for this is annoying to extract and probably insuffiecent
    return unsentVsUnsent(theta)

def howOftenShouldYouSend(theta):
    a = unsentVsUnsent(theta)
    b = sentVsUnsent(theta)
    c = unsentVsSent(theta)
    d = sentVsSent(theta)
    if (a >= b and c >= d):
        return 0
    if (a <= b and c <= d):
        return 1
    probOfNotSending = (d-b)/(a-b-c+d)
    return 1-probOfNotSending

def gameTheoryOptimalWinProb(theta):
    a = unsentVsUnsent(theta)
    b = sentVsUnsent(theta)
    c = unsentVsSent(theta)
    d = sentVsSent(theta)
    P1 = 1-howOftenShouldYouSend(theta)
    P2 = 1-howOftenShouldYouSend(-theta) 

    return a*P1*P2 + b*(1-P1)*P2+ c*P1*(1-P2)+d*(1-P1)*(1-P2)

theta = 10
print(unsentVsUnsent(theta),sentVsUnsent(theta))
print(unsentVsSent(theta),sentVsSent(theta))
print(howOftenShouldYouSend(theta))
print(gameTheoryOptimalWinProb(theta))

x = np.linspace(-30, 30, 100)
plt.plot(x, [unsentVsUnsent(xi) for xi in x])
plt.plot(x, [sentVsUnsent(xi) for xi in x])
plt.plot(x, [gameTheoryOptimalWinProb(xi) for xi in x], color='k') 
plt.plot([-30,30], [0.5,0.5], color="r")

#plt.scatter(x, [howOftenShouldYouSend(xi) for xi in x])
plt.show()
    




