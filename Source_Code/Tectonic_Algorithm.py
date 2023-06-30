#Tectonic Algorithm : Applied to Discrete Optimization problems (Permutation-Boolean solution representations)

import math
import random
import numpy as np
import matplotlib.pyplot as plt
import itertools
import functools
from scipy.constants import Boltzmann, pi

kb = Boltzmann

N = 50 #Number of plates/solutions
M = 9 #Number of platelets
MP = 100 #Mass of the plates (assuming homogeneity between continental and ocean plates)
h = 0.2#Convection coefficient
A = 139000000#Surface Area of the Ocean
Lc = 10000# Characteristic length
EC = 100# Heat Cost (present in all aspects of plate tectonics)s
OT = 9 #Ocean selection threshold
V = A*Lc# Volume of the Ocean
gamma = A/N #Proportionality constant
T1 = 20
T2 = 2000
t1 = 0
Max_Iter = 20

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

def Neighborhood_Plates(Plate): #Plates that collided with the given plate (Transform)
    NS = int(random.uniform(2,N)) #Minimum number of transform boundaries for each plate is 2 since that's required in order to evaluate fitness function coherently
    GPC = G_P.copy()
    NLP = GPC.pop(GPC.index(Plate)) #Preventing reflexive loops
    np.random.shuffle(NLP) #Shuffling is used to statistically prevent (make unlikely) all plates having the same exact neighborhoods (unrealistic with Pangaea as exception)
    NP = [] #Neighborhood of plates to the given plate input
    for k in range(NS):
        NP.append(NLP[k])
    return NP
#Solutions = Plates or Platelets in the form of lists (discrete representation: Permutation or Booleans solution representation)

## Solutions are permutation lists
def Permutation_List_Generator(m):
    Perm_List = []
    for k in range(m):
        Perm_List.append(int(random.uniform(1,10)))
    return Perm_List

def Levenshtein_Distance(P1,P2): #minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other.
    dist = 0
    for k in range(len(P1)):
        dist = dist + int(bool(P1[k] != P2[k]))
    return dist #Maximum Levenshtein distance in this case is len(P1)

#Fitness function (any fitness function that takes discrete lists as inputs)

def Fitness(L): #Fitness is meant to represent the density of the plate (solutions): Oceanic plates more fit than Continental plates [threshold selection]
    return np.sum(L)

# Fitness Evaluation
def Coherentist_Fitness_Evaluation(P): #Indirect-Decentralized fitness evaluation that is akin to blockchain technology (coherentism): Triad Fitness evaluation
    SL = Neighborhood_Plates(P)
    P1 = SL[int(random.uniform(0, len(SL)))]
    P2 = SL[int(random.uniform(0, len(SL)))] #Avoiding Overdetermined and Underdetermined system of equations (3 is the perfect numbers)
    Entanglement1 = Transform(P,P1)
    Entanglement2 = Transform(P,P2)
    CoherentistEntanglement = Transform(P1,P2)
    P_Fitness = math.sqrt(Entanglement1*Entanglement2/CoherentistEntanglement)
    return P_Fitness     #Taking random solutions in the solution space by assuming that the interaction (transform) graph is exhausted ie complete wich means all interactions possible take place :N(N-1)/2 possibilities/edges (assuming of course that interactions are symmetrical and non-reflexive). Otherwise, one has to construct a neighborhood set of solutions for each solution


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

def Convection(T,t):
    Q = h*A*(T-T1)*(t-t1) #Q = mc(T2-T1) where m is the mass of the plates and c is the heat capacity of the plates [this equation is not about heat-transfer but still valid]
    return Q

# In order to account for the convergence plate boundary probability of occurence (frequency), it is valid to frame the collisions between plates as a crystallization effect taking place in a Voronoi diagram (Kolmogorov-Avrami equation)
def Kolmogorov_Avrami(y,v,t): #Statistical model/equation describing Crystallization effect via Crystallization Fraction (Fraction of total region covered by crystalls) in Voronoi Cell pattern
    return 1 - math.exp(-pi*y*v*t**2) #sigmoid probability that a randomly selected point will be inside one of crystalls (of which there are infinitely many thus the exponential-saturation effect) = Crystallization Fraction

## The assumptions of this model: Random plate tectonics, Independence plate tectonics, Large Area, N-Area proprotionality, Constant Tectonics speed, Isotropy and Non-Overlapping

# Plate Tectonics operator

# Plate Tectonics types of plate boundaries (causes)


def Divergence(P1,P2): # Self-Adaptation phase (Exploration)
    P1 = Earthquake(P1)
    P2 = Earthquake(P2)
    return P1, P2

def Transform(P1,P2): # Information exchange phase (Cooperation): Fossil record correlation, Rock-Mountain correlation, Paleoclimate correlation, Jigsaw Puzzle fitting
    Joint_Fitness = Fitness(P1)*Fitness(P2) #It can be any sort of mathematical operation. The point is just to encode interactions numerically in one unique value (relational private keys, information loss) in the form of joint "knot" fitness (coupled fitness functions) that needs to be decoupled or untied during evaluation
    return Joint_Fitness #Zero conditional entropy due to entanglement/superposition = maximum mutual information due to entanglement/superposition = Joint Fitness(P1,P2)

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
    PC = PC + random.uniform(0,(1-PC)/2)
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

t = t1
T = T1
F = []
SP = [] #Selected Plates
en = 3 #Elitism number
# Initial Elitism: Centralized Fitness evaluation due to the initially absent interactions between plates
P = Centralized_Fitness_Evaluation(G_P)
F = P
SP.append(Centralized_Solution_Selection(F,en))
GF = []
GF.append(F)
Q = 0.00001 #a non zero start
while t < Max_Iter and Q != 0 and T < T2:
    Q = Convection(T,t)
    AvgSpeed = 3*kb*T/MP
    PC = Kolmogorov_Avrami(gamma,AvgSpeed,t) #PC = N*kb*AvgT/V :Probability of convergent plate boundary occurence (collision frequency) which is the kinetic theory definiton of Pressure (which is not compatible with heat transfer since Pressure is a state variable) or we can otherwise use Voronoi Cell patterns to describe Crystallization in the sense that Crystallization Fraction replaces the Pressure definition of PC

#Self-Adaptation in the Exploration phase (Divergent/Constructive Plate boundary [Seafloor Spreading]-> Volcanic activity)
    Threshold_Selection(OT,G_P)
        
#Cooperation: Information exchange (Fossil record sharing/correlation + Jigsaw Puzzle fitness molding + Rock/Mountain correlation + Glacial Striation + Bituminous Coal) through Communication protocol (Transform/Conservative Plate boundary -> Earthquakes) [Exploration-Exploitation]
    FF = []
    for k in range(len(G_P)):
        FF.append(Coherentist_Fitness_Evaluation(G_P[k]))
    GF.append(FF)

#Competition: Survival, Selection and Elimination after comparing solutions in the Exploitation phase (Convergent/Destructive Plate boundary: Subduction -> Mountain-building, Ocean trenches or Earthquakes)
    k = 0
    while k < int(random.uniform(N/2,N)):
        P1 = G_P[int(random.uniform(0,len(G_P)))]
        P2 = G_P[int(random.uniform(0,len(G_P)))]
        if P1 != P2:
            SP.append(Convergence_Likelihood(PC,P1,P2))
        k = k + 1

## Exploration Exploitation paradigm:

#Likelihood Feedback loop via Convection currents: Divergent plate boundaries (Self-Adaptation, Exploration) causes colliding plates to move away from each others, but given the finite nature of the earth surface, what results is that some other plate gets nearer the colliding plates allowing for Convergent plate boundary to take place and thus Subduction occurs (Competition, Exploitation) [statistical in nature]. In the inverse direction, it is thanks to the Conveyor Belt principle (Earth Surface Area[Crust] Conservation) that whenever Subduction (Competition, Exploitation) takes place, the lost surface is balanced by the formation of new oceanic crust or platelets via Seafloor Spreading thus creating novel solution plates for further exploration (Self-Adaptation, Exploration)

    BI = GF[len(GF)-1].index(np.max(GF[len(GF)-1]))
    SP1 = SP[BI]
    O = F.copy()
    O.pop(BI)
    OI = O.index(np.max(O))
    SP2 = SP[OI]
    DivSol, PC = EE_Feedback_Loop(SP1,SP2)
    SP.append(DivSol)
    Q = Q - EC
    t = t + 1
    T = T + 1

def membership(x,A):
    return np.any(A == x)
    
FFT = np.max(F)
BEST = F.index(FFT)
Sol = SP[BEST] #Depth 
#Coverage Post-Analysis (Ergodicity): Law of Large Numbers and Monte Carlo
MC = 100
MCDist = []
for k in range(MC):
    Unvisited_Sol = Permutation_List_Generator(9)
    while membership(Unvisited_Sol, SP) or membership(Unvisited_Sol, G_P):
        Unvisited_Sol = Permutation_List_Generator(9)
    MCDist.append(Levenshtein_Distance(Sol,Unvisited_Sol))

print(Sol)
print(FFT)
print(np.max(MCDist)) #Coverage






