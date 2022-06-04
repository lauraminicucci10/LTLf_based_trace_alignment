# LTLf_based_trace_alignment

Repository for the project of Reasoning Agents module (EAI exam)

## 1 - Introduction

This repository contains the project for the course of Reasoning Agents 2022, Sapienza University of Rome, held by Prof. Fabio Patrizi. The tutor of our project is  Dott. Francesco Fuggitti.

## 2 - Problem

The work is focused on the problem of Trace Alignment in Bussiness Process (BP) and is solved by using the Linear Temporal Logic on Finite traces (LTL-f), the automata theory and the Planning Domain Definition Language (PDDL). In particular, the trace alignment problem is the problem of checking whether an actual trace of a BP execution conforms to the expected process behavior and, if not, finding a “minimal set” of changes that align the trace to the process.

## 3 - Installation of the software

1. Follow the logaut installation guide at: https://github.com/whitemech/logaut

2. Modify the file usr/local/bin/lydia with: docker run -v "$(pwd)":/home/default whitemech/lydia lydia "$@"

3. Install LTLf2DFA: pip install git+https://github.com/whitemech/LTLf2DFA.git@develop#egg=ltlf2dfa

4. Install MONA: sudo apt install mona

5. Install Fast-Downward from https://www.fast-downward.org/ObtainingAndRunningFastDownward

## 4 - Dataset

I used a set of syntheric logs and constraints file: the dataset contains logs for 10, 15 and 20 constraints, with different levels of noise (inverted constraints) and different length.
