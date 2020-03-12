from landscapeGenerator import *
import findTarget
import numpy as np
import sys
import matplotlib.pyplot as plt

# prints avrage over 1000 trials for each all rules
def search_destroy(dimension, typ="stationary"):
    rep=40
    print (typ+str(rep)+"\n")
    rules=[3]
    searches=[[] for _ in range(len(rules))]
    if typ!="stationary":
        costs=[]
    d=[{0:[], 1:[],2:[],3:[]} for _ in range(len(rules))]
    for i in range(rep):
        landscape, target=landscape_generator(dimension)
        for rule_no, rule in enumerate(rules):
            sys.stdout.write("\r maze_no: "+ str(i) + ", rule_no: "+ str(rule)+"                  ")
            if typ=="stationary":
                search_count=findTarget.findTarget(landscape, target, rule)
            else:
                search_count=findTarget.findTarget(landscape, target, rule, "moving")
                if rule == 3:
                    costs.append(findTarget.total_cost)
            d[rule_no][landscape[target]].append(search_count)
            searches[rule_no].append(search_count)
            
    for rule_no in range(len(rules)):
        if rule_no == 3:
                print("\n total cost for rule 3 = "+str(np.mean(costs)))
        print("\n Average number of searches for rule no. "+str(rule_no+1)+" = "+str(np.mean(searches[rule_no])))
    new_dict=[{0:[], 1:[],2:[],3:[]} for _ in range(len(rules))]
    for item_no,item in enumerate(d):
        for key, val in item.items():
            new_dict[item_no][key]=np.mean(val)
    
    plt.figure(1)
    for rule_no, rule in enumerate(new_dict[:-1]):
        plt.plot(rule.keys(), rule.values())
    plt.legend(("Rule1", "Rule2"), loc="upper left")
    plt.xlabel("Type of terrain containing the target")
    plt.xticks([0,1,2,3],["Flat", "Hill", "Forest","Cave"])
    plt.ylabel("Average number of searches")
    plt.title("Average number of searches on 50x50 board")
    plt.savefig(typ+"-"+str(rep)+".png")

if __name__ == '__main__':
    search_destroy(50)
