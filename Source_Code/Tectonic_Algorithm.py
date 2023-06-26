#Tectonic Algorithm : Applied to Discrete Optimization problems (Permutation-Boolean solution representations)

import math
import random
import numpy as np
import matplotlib.pyplot as plt
import itertools
import functools
from scipy.constants import Boltzmann

kb = Boltzmann

N = 50 #Number of plates/solutions
M = 9 #Number of platelets
h = 0.2#Convection coefficient
A = 139000000#Surface Area of the Ocean
Lc = 10000# Characteristic length
EC = 100# Heat Cost (present in all aspects of plate tectonics)s
OT = 9 #Ocean selection threshold
V = A*Lc# Volume of the Ocean



##Initialization:

#Start with a giant compounded Pangaea (List constituting all lists to be split from the Pangaea list)

Pangaea_List = []

for k in range(N*M):
    Pangaea_List.append(int(random.uniform(1,10)))

#Continental Drift equation: Taking Pangaea apart into discrete continents or plates via Continental Drift (the driving force behind their movement: Convection Current)

Solutions = []
s = 0
f = M
for k in range(N):
    Solutions.append(Pangaea_List[s:f])
    s = f + 1
    f = f + M

#Retrieve N plates/continents from the Pangaea list (it means that the length of the Pangaea lsit should be divisible by N)

G_P = Solutions

#Solutions = Plates or Platelets in the form of lists (discrete representation: Permutation or Booleans solution representation)

## Solutions are permutation lists

#Fitness function (any fitness function that takes discrete lists as inputs)

def Fitness(L): #Fitness is meant to represent the density of the plate (solutions): Oceanic plates more fit than Continental plates [threshold selection]
    return np.sum(L)

# Fitness Evaluation
def Coherentist_Fitness_Evaluation(P,SL): #Indirect-Decentralized fitness evaluation that is akin to blockchain technology (coherentism): Triad Fitness evaluation
    P1 = SL[int(random.uniform(0, len(SL)))]
    P2 = SL[int(random.uniform(0, len(SL)))]
    while P1 == P or P2 == P:
        P1 = SL[int(random.uniform(0, len(SL)))]
        P2 = SL[int(random.uniform(0, len(SL)))] #Taking random solutions in the solution space by assuming that the interaction (transform) graph is exhausted ie complete wich means all interactions possible take place :N(N-1)/2 possibilities/edges (assuming of course that interactions are symmetrical and non-reflexive). Otherwise, one has to construct a neighborhood set of solutions for each solution
    Entanglement1 = Transform(P,P1)
    Entanglement2 = Transform(P,P2)
    CoherentistEntanglement = Transform(P1,P2)
    P_Fitness = math.sqrt(Entanglement1*Entanglement2/CoherentistEntanglement)
    return P_Fitness

def Coherentist_Solution_Selection(RFP, SL): #Divide and Conquer methodology
    k = 0
    RP = SL[int(random.uniform(0,len(SL)))]
    SP = Convergence(RP, RFP)  
    while k < int(random.uniform(N/2,N)):
        SP = Coherentist_Solution_Selection(SP, SL)
    return SP

def Centralized_Fitness_Evaluation(SL):
    F = []
    for k in range(len(SL)): # Direct-Centralized Fitness evaluation (assuming independence and no interactions between solutions)
        F.append(Fitness(SL[k]))
    return F

def Centralized_Solution_Selection(SLF,p):
    for j in range(p):
        Best_Index = SLF.index(np.max(SLF))
        SP.append(SLF[Best_Index])
        SLF.pop(Best_Index)
    return SP
    
    
def Classification(Q): #Solution representation dependent
    interval = 1000  # Width of each interval
    num_intervals = 9  # Number of intervals

    X = min(int(Q // interval) + 1, num_intervals)
    return X

    

#Main Equation: Heat Transfer through Convection : Lithosphere floating on semi-fluid layer of molten magma (asthenosphere)

def Convection(T1,T2, t1, t2):
    Q = h*A*(T2-T1)*(t2-t1)
    return Q



# Plate Tectonics operator

# Plate Tectonics types of plate boundaries (causes)


def Divergence(P1,P2): # Self-Adaptation phase (Exploration)
    P1 = Earthquake(P1)
    P2 = Earthquake(P2)
    return P1, P2

def Transform(P1,P2): # Information exchange phase (Cooperation): Fossil record correlation, Rock-Mountain correlation, Paleoclimate correlation, Jigsaw Puzzle fitting
    Entanglement = Fitness(P1)*Fitness(P2) #It can be any sort of mathematical operation. The point is just to encode interactions numerically (private keys)
    return Entanglement #Zero conditional entropy = maximum mutual information = Fitness(P1,P2) is not Fitness(P1)*Fitness(P2) which itself can't be decomposed into individual fitnesses due to information loss

def Convergence(P1,P2): #Collision = Selection and Replacement (Competition, Exploitation)
    SP = [1,2,3,4,5,6,7,8,9]
    F1 = Fitness(P1)
    F2 = Fitness(P2)
    if F1>F2: #Subduction
        SP = P1
    if F2>F1: #Subduction
        SP = P2
    if F2 == F1:
        SP = random.choice([P1,P2])
    return SP

def Convergence_Likelihood(PC, P1, P2): #PC is independent of plates (thus global) due to principle of equidistance (Maximum Entropy principle + Principle of Indifference) otherwise we need a neighborhood set for each plate
    pth = random.uniform(0,1)
    SP = []
    if PC > pth:
        SP = Convergence(P1,P2)
    else:
        pass
    return SP
    

    
# Plate Tectonics effects: Plate boundary type + Plate type (Neighborhood topology-wise)

## Convergence effects: Permutation XOR minimization (or any distance/norm metric)
## Divergence effects: Permutation XOR maximization (or any distance/norm metric)

def Hot_Spot_Volcano(): #Hot Spot (no interaction/boundary) and thus not needing for plates as inputs
    P = []
    for j in range(M):
        P.append(int(random.uniform(1,10)))
    return P

def Earthquake(P): #Algorithmic shaking (Fitness-dependent)
    u = int(random.uniform(0,len(P)))
    S = P.copy()
    S.pop(u)
    P[u] = random.choice(S)
    return P

def Convergent_Volcano(Q, P1, P2): #Continental-Continental (Collision zone)
    Volcanic_Activity = Classification(Q)
    for j in range(Volcanic_Activity):
        while P1[k] != P2[k]: 
            P1[k] = int(random.uniform(1,10)) #P2 as a reference for differentiation
    np.random.shuffle(P1)
    return P1
    

def MountainBuilding(Q,CP1,CP2): #Continental-Continental (Collision zone)
    Mountain_Granite = Classification(Q)
    for j in range(Mountain_Granite):
        while CP1[k] != CP2[k]: 
            CP1[k] = int(random.uniform(1,10)) #P2 as a reference for differentiation
    return CP1

def OceanTrench(Q,CP,OP): #Continental-Oceanic crust collision (Subduction zone)
    Ocean_Basalt = Classification(Q)
    for j in range(Ocean_Basalt):
        while OP[k] != CP[k]: 
            OP[k] = int(random.uniform(1,10)) #P2 as a reference for differentiation
    return OP

def IslandFormation(Q,OP1,OP2):  #Oceanic-Oceanic (Island arc)
    IslandSplitter = Classification(Q)
    O1 = OP1.copy()
    O2 = OP2.copy()
    split = O1[0:IslandSplitter]
    O2[0:IslandSplitter] = split
    Island = O2
    return Island

def Mid_Ocean_Ridge(Q,P1,P2): #Seafloor Spreading: there is a possibility where Seafloor Spreading may end up just reshuffling the plate but it's very unlikely
    Seafloor_Spreader = Classification(Q)
    for k in range(Seafloor_Spreader):
        while P1[k] == P2[k]: 
            P1[k] = int(random.uniform(1,10)) #P2 as a reference for differentiation
    np.random.shuffle(P1)
    return P1
            
### Effects dicitionary:

## Convergence dictionary:

Conv_Dict ={
    1:'Convergent_Volcano',
    2:'MountainBuilding',
    3:'IslandFormation',
    4:'OceanTrench'
    
}

### Feedback loops operators

def Conveyor_Belt_Principle(Q,P1,P2): #Conveyor Belt-Crust Conservation principle (Convergence effects -> Divergence)
    SP = Convergence(P1,P2)
    k = int(random.uniform(1,5))
    DivSol = Conv_Dict[k](Q,P1,P2)
    return DivSol
    
    #Earthquake is eliminated here since it is used in Divergence as algorithmic shaking in order to diversify solutions in search space
    

def Likelihood_Increasing(Q,P1,P2): #Likelihood increasing (Divergence effects -> Convergence)
    Div_Sol = Mid_Ocean_Ridge(Q,P1,P2)
    PC = PC + random.uniform(0,1-PC)
    return PC
    

def EE_Feedback_Loop(P1,P2):  
    DivSOL = Conveyor_Belt_Principle(Q,P1,P2)
    PC = Likelihood_Increasing(Q,P1,P2)
    return DivSOL, PC

#Flowchart functions

def Threshold_Selection(th,SL):
    P1 = SL[int(random.uniform(0, len(SL)))]
    P2 = SL[int(random.uniform(0, len(SL)))]
    if Fitness(P1) >= th and Fitness(P2) >= th:
        P1, P2 = Divergence(P1,P2)
    else:
         Threshold_Selection(SL) 

t = 0
Max_Iter = 20
t1 = t 
t2 = Max_Iter
T1 = 20 
T2 = 2000
Q = Convection(T1,T2,t1,t2)
PC = N*kb*Q/V #Probability of convergent plate boundary occurence (collision frequency) which is the kinetic theory definiton of Pressure
F = []
SP = [] #Selected Plates: Fossil paleontological record (a sort of a memory structure to avoid costful current solutions systematically)
en = 3 #Elitism number
while t < Max_Iter and Q != 0:
    # Initial Elitism: Centralized Fitness evaluation due to the initially absent interactions between plates
    P = Centralized_Fitness_Evaluation(G_P)
    F = P
    SP.append(Centralized_Solution_Selection(F,en))

#Self-Adaptation in the Exploration phase (Divergent/Constructive Plate boundary [Seafloor Spreading]-> Volcanic activity)
    Threshold_Selection(OT,G_P)
        
#Cooperation: Information exchange (Fossil record sharing/correlation + Jigsaw Puzzle fitness molding + Rock/Mountain correlation + Glacial Striation + Bituminous Coal) through Communication protocol (Transform/Conservative Plate boundary -> Earthquakes) [Exploration-Exploitation]
    for k in range(len(G_P)):
        F.append(Coherentist_Fitness_Evaluation(G_P[k], G_P))


#Competition: Survival, Selection and Elimination after comparing solutions in the Exploitation phase (Convergent/Destructive Plate boundary: Subduction -> Mountain-building, Ocean trenches or Earthquakes)
    k = 0
    while k < int(random.uniform(N/2,N)):
        P1 = G_P[int(random.uniform(0,len(G_P)))]
        P2 = G_P[int(random.uniform(0,len(G_P)))]
        if P1 != P2:
            SP.append(Convergence_Likelihood(PC,P1,P2))

## Exploration Exploitation paradigm:

#Likelihood Feedback loop via Convection currents: Divergent plate boundaries (Self-Adaptation, Exploration) causes colliding plates to move away from each others, but given the finite nature of the earth surface, what results is that some other plate gets nearer the colliding plates allowing for Convergent plate boundary to take place and thus Subduction occurs (Competition, Exploitation) [statistical in nature]. In the inverse direction, it is thanks to the Conveyor Belt principle (Earth Surface Area[Crust] Conservation) that whenever Subduction (Competition, Exploitation) takes place, the lost surface is balanced by the formation of new oceanic crust or platelets via Seafloor Spreading thus creating novel solution plates for further exploration (Self-Adaptation, Exploration)

    BI = F.index(np.max(F))
    SP1 = SP[BI]
    O = F.copy()
    O.pop(BI)
    OI = O.index(np.max(O))
    SP2 = SP[OI]
    DivSol, PC = EE_Feedback_Loop(SP1,SP2)
    Q = Q - EC
    t = t + 1


FFT = np.max(F)
BEST = F.index(FFT)
Sol = SP[BEST]

print(Sol)
print(FFT)




