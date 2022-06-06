import os
from typing import Match, cast
import re
import matplotlib.pyplot as plt

def execute_PDDL_files():
    constraint = 15
    syn_real = "synthetic" # or "created"
    #n_constr = ["2", "3", "5"]
    #constr_inverted = ["3","4","6"] ## --> for 10 contraints
    constr_inverted = ["4","6","8"] ## --> for 15 contraints
    #len_traces = ["1-50", "51-100", "101-150", "151-200"]
    len_traces = ["101-150"]
    n_traces = 100
    
    #for n_cons in n_constr:
    for inv in constr_inverted:
        cost_tot = []
        time_tot = []
        for lenght in len_traces:
            cost = 0.0
            time = 0.0
            x = 0
            #for i in range(20, n_traces):
            for i in range(n_traces):
                netx_el = inv+"_"+lenght
                path_domain = "./PDDL/"+syn_real+"/"+"domain_trace_alignment.pddl"
                path_problem = "./PDDL/"+syn_real+"/"+"problem_SYN_"+str(constraint)+"_"+netx_el+"_trace"+str(i+1)+".pddl"
                
                print (path_domain)
                print (path_problem)
                
                output = os.popen("./downward/fast-downward.py "+path_domain+" "+path_problem+" --search 'astar(hmax())'").read()
                #print(output)
                
                if (re.search("Plan cost: (.*)\n", output) is not None and re.search("Search time: (.*)s\n", output) is not None):
                    cost += int(re.search("Plan cost: (.*)\n", output).group(1))
                    time += float(re.search("Total time: (.*)s\n", output).group(1))
                    x+=1
            
            cost_tot.append(cost/x)
            time_tot.append(time/x)
        
        print (cost_tot)
        print (time_tot)
    
        # Save time and cost in .txt
        file1 = open("./results/"+syn_real+"_"+str(constraint)+"_"+netx_el+".txt", "w")
        file1.write("PLAN COST AVG "+str(cost_tot)+"\n"+"TOTAL TIME AVG "+str(time_tot))
        file1.close()
        
        
def main():
    execute_PDDL_files()

if __name__ == "__main__":
    main()
