import json
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gamma
with open("thetas.json", "r") as f:
    data = json.load(f)

thetas = [item for item in data if item != None]

#X is 1 if person ahead wins, 0 otherwise
#Theta > 0 is by how much the person ahead is ahead by


pos_thetas = []
neg_thetas = []

for theta in thetas:
    #if abs(theta) > 60000:
        #continue
    if theta > 0:
        pos_thetas.append(theta/1000)
    else:
        neg_thetas.append(-theta/1000)
print(len(pos_thetas))
print(len(neg_thetas))

pos_alpha, _, pos_scale = gamma.fit(pos_thetas,floc = 0)
neg_alpha, _, neg_scale = gamma.fit(neg_thetas, floc = 0)
#print(pos_params, neg_params)
x = np.linspace(0.5,200)
print(pos_alpha,pos_scale)
print(neg_alpha, neg_scale)
#plt.plot(x,10000*gamma.pdf(x,pos_alpha, scale=pos_scale), color="b")
#plt.plot(x,10000*gamma.pdf(x,neg_alpha, scale=neg_scale), color="r")
#plt.hist(pos_thetas,bins=100)
#plt.hist(neg_thetas,bins=100)
plt.hist(thetas, bins=100)


plt.show()

prob_X = len(pos_thetas)/(len(pos_thetas) + len(neg_thetas))
with open("parameters.json", "w") as f:
    json.dump([[pos_alpha, pos_scale], [neg_alpha, neg_scale], prob_X], f)
 

pos_pdf = lambda x: gamma.pdf(x,pos_alpha, scale=pos_scale)
neg_pdf = lambda x: gamma.pdf(x,neg_alpha, scale=neg_scale)




def probOfWinning(theta):
    if theta == 0:
        return 0.5
    if theta < 0:
        return 1-probOfWinning(-theta)
        
    numerator = pos_pdf(theta) * prob_X
    denominator = pos_pdf(theta)*prob_X + neg_pdf(theta)*(1-prob_X) 
    return numerator/denominator

probOfOneEye = 0.71757
def probWinIfSent(theta):
    x = np.linspace(theta+10,theta+39.95)
    fx = [probOfWinning(xi) for xi in x]
    return np.average(fx)*probOfOneEye
    

poss_times_ahead = np.linspace(-60,60, 240)

gainedProb = []



#plt.plot(poss_times_ahead, gainedTime)

unsentWinProbValues = np.array([probOfWinning(i) for i in poss_times_ahead])
sentWinProbValues = np.array([probWinIfSent(i) for i in poss_times_ahead])

plt.plot(poss_times_ahead, unsentWinProbValues)

plt.plot(poss_times_ahead, sentWinProbValues)
plt.show()

minGoodTime = None 
maxGoodTime = None
maxWinProbGained = 0
for i in range(len(poss_times_ahead)):
    if minGoodTime == None and sentWinProbValues[i]> unsentWinProbValues[i]:
        minGoodTime = poss_times_ahead[i]
    if sentWinProbValues[i] > unsentWinProbValues[i]:
        maxGoodTime = poss_times_ahead[i]
    maxWinProbGained = max(maxWinProbGained, sentWinProbValues[i] - unsentWinProbValues[i])

print(f"Send if behind by {-maxGoodTime} to {-minGoodTime} seconds")
print()
print(f"At most this increases your win probability by {maxWinProbGained*100}%")
    

#plt.show()
    
    





    




