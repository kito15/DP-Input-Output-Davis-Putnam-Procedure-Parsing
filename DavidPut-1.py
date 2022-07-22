import os
import sys

def SingleLiteral(Sentenced):
    for clause in Sentenced:
        if len(clause) == 1:
            return clause[0]
    return None

def DavisPutnam(atoms, clauses):
    value = {}
    for atom in atoms:
        value[atom] = 0
    return DPHelper(atoms, clauses, value)
def DPHelper(atoms, Sentenced, value):
    while True:
        if(Sentenced == []):
            #we have statified every clause and have popped it off the stack
            #assign all remaning unbound atoms to T or F arbitrarily
            for atom in atoms:
                if value[atom] == 0:
                    value[atom] = 1
            return value
       
        L = SingleLiteral(Sentenced)
        if(L):
            #a clause in S is a single literal
            #assign T/F appropriately since it must be satisfied
            if L > 0:
                l = abs(L)
                value[l] = 1
            if L < 0:
                l = abs(L)
                value[l] = -1
        
        #propagate assignment in S
        #means if there exists a literal L in S with 1 sign or single literal L in S         assign all other clauses containing L in S the value assigned.
        # conditional break if S hasnt changed
        SNEW = Sentenced.copy()
        Sentenced = propagator(Sentenced, value)
        if SNEW == Sentenced:
            break
    #outside the loop
    for atom in value.items():
        if atom[1] == 0:
            break
    if atom[1] == 1 or atom[1] == -1:
        value[atom[0]] == 0
        return None
    SC = Sentenced.copy()
    VC = value.copy()
    VC[atom[0]] = 1 #true
    #PROPAGATE IN SC
    SC = propagator(SC, VC)
    VNEW = DPHelper(atoms, SC, VC)
    if (VNEW != None):
        return VNEW
    value[atom[0]] = -1 #false
    #PROPAGATE IN S
    
    #print(S)
    Sentenced = propagator(Sentenced, value)
    #print(S)
    return DPHelper(atoms, Sentenced, value)
                 
def propagator(Sentenced, value):
    satisfied_clauses = []
    for value_pair in value.items():
        for clause in Sentenced:
            satisfied = 0
            for i in range(0, len(clause)):
                if abs(clause[i]) == value_pair[0]:
                    if value_pair[1] > 0:
                        if clause[i] > 0:
                            satisfied = 1
                    elif value_pair[1] < 0:
                        if clause[i] < 0:
                            satisfied = 1
                        
            if satisfied:
                satisfied_clauses.append(clause)
    for clause in satisfied_clauses:
        Sentenced.remove(clause)
    return Sentenced     

