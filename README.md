# LTLf_based_trace_alignment

Repository for the project of Reasoning Agents module (EAI exam)

## 1 - Introduction

This repository contains the project for the course of Reasoning Agents 2022, Sapienza University of Rome, held by Prof. Fabio Patrizi. The tutor of this project is  Dott. Francesco Fuggitti.

## 2 - Problem

The work is focused on the problem of Trace Alignment in Bussiness Process (BP) and is solved by using the Linear Temporal Logic on Finite traces (LTL-f), the automata theory and the Planning Domain Definition Language (PDDL). In particular, the trace alignment problem is the problem of checking whether an actual trace of a BP execution conforms to the expected process behavior and, if not, finding a “minimal set” of changes that align the trace to the process.

## 3 - Installation of the software

1. Follow the logaut installation guide at: https://github.com/whitemech/logaut

2. Modify the file `usr/local/bin/lydia` with: `docker run -v "$(pwd)":/home/default whitemech/lydia lydia "$@"`

3. Install LTLf2DFA: `pip install git+https://github.com/whitemech/LTLf2DFA.git@develop#egg=ltlf2dfa`

4. Install MONA: `sudo apt install mona`

5. Install Fast-Downward from https://www.fast-downward.org/ObtainingAndRunningFastDownward

## 4 - Dataset

I used a set of syntheric logs and constraints file: the dataset contains logs for 10, 15 and 20 constraints, with different levels of noise (inverted constraints) and different length.

## 5 - Solution

I use a cost-optimal planning to make the input trace conform with the process behavior at a minimal cost. 
Constraints are represented as LTL-f formulas, for both the constraints and the traces I built the corresponding automata:

Given:
* trace ρ
* constraint φ

Define two automatons:
* Augmented trace automaton T+ : accepts all modifications of ρ (where the changes are marked)
* Augmented constraint automaton A+ : accepts all traces that satisfy φ && all modifications of ρ that satisfy φ

Find minimal-cost ρ’ s.t. is accepted by T+ && A+ (satisfies both)
* Corresponds to find minimal-cost accepting path ρ’ on product automaton T+ x A+

Use Planning to search for minimal-cost ρ’
* Domain
    * Models product automaton T+ x A+ 
    * add and del actions with positive cost (changes of input trace)
    * sync actions with null cost model events
* Problem
    * Initial State: all automata in their starting state
    * Goal: all automata in a final state
* Solution
    * Minimal-cost goal-reaching sequence of actions

In the PDDL domain there are 3 actions: add, del and sync. The sync one has cost 0 and stands for no change, while the first two have cost 1 and are used to add or remove events in the trace with the aim of obtaining a correct trace which satisfies all the constraints. The goal is to repair all the traces with the minimal cost, that is, we want to reach the accepting states for both the trace and the constraint automata minimizing the total cost.

In this project I used [LTLf2DFA](https://github.com/whitemech/LTLf2DFA/) tool which transforms an LTL-f formula into a minimal Deterministic Finite state Automaton (DFA). Thanks to [MONA](http://www.brics.dk/mona/) each constraint automaton is translated into an interpretation of 0,1,X for transitions. In this way, is possible to sum up the elements of each label and handle the transitions according to the result of the sum:

* if sum > 1, discard that transition because I work with BP log traces (singleton) so is admitted to have only one true symbol per time
* if sum = 1, then I get the corresponding symbol and build only the transition for this element
* if sum = 0, then I save the symbols which are negated, building the "positive transitions" for all the symbols of both the trace and the constraint except those that must be negated

Important changes from the MONA output transitions when I encode the PDDL problem:
* Remove the state 0 (which goes to state 1 with any symbol) of any constraint and use state 1 as initial state (is an error to consider it!)
* Remove the transitions from the i-th state to the i-th state

## 6 - Repository contents

## 7 - References
- De Giacomo, Giuseppe & Marrella, Andrea & Patrizi, Fabio & Maggi, Fabrizio. (2017). On the Disruptive Effectiveness of Automated Planning for LTLf-based Trace Alignment. 

## 8 - Author
Laura Minicucci
