# Threshold на епидемија

**Threshold на ER мрежа**

import pickle


with open('epidemic-threshold.pkl', 'rb') as f:
    df = pickle.load(f)

import numpy
import networkx
import epyc
import epydemic
import pandas

import matplotlib
%matplotlib inline
%config InlineBackend.figure_format = 'png'
matplotlib.rcParams['figure.dpi'] = 100
import matplotlib.pyplot as plt
import seaborn
matplotlib.style.use('seaborn')
seaborn.set_context("notebook", font_scale=.65)

**Наш експеримент** 

fig = plt.figure(figsize=(8, 8))
ax = fig.gca()

# plot the size of the removed population
ax.plot(df[epydemic.SIR.P_INFECT],
        df[epydemic.SIR.REMOVED], 'r.')
ax.set_xlabel('$p_{\\mathit{infect}}$')
ax.set_ylabel('population that is...')
ax.set_title('Epidemic size vs $p_{\\mathit{infect}}$', y=1.05)

plt.show()

fig = plt.figure(figsize=(8, 8))
ax = fig.gca()

# plot the size of the removed population
pInfects = df[[pInfect > 0.00003 and pInfect < 0.00008
               for pInfect in df[epydemic.SIR.P_INFECT]]]
ax.plot(pInfects[epydemic.SIR.P_INFECT],
        pInfects[epydemic.SIR.REMOVED], 'r.')
ax.set_xlabel('$p_{\\mathit{infect}}$')
ax.set_ylabel('population that is...')
ax.set_title('Epidemic size vs $p_{\\mathit{infect}}$ (detail)', y=1.05)

plt.show()

fig = plt.figure(figsize=(8, 8))
ax = fig.gca()

# plot the size of the removed population
pInfects = sorted(df[epydemic.SIR.P_INFECT].unique())
repetitions = int(len(df[epydemic.SIR.P_INFECT]) / len(pInfects))
removeds = []
stdErrors = []
for pInfect in pInfects:
    removeds.append(df[df[epydemic.SIR.P_INFECT] == pInfect][epydemic.SIR.REMOVED].mean())
    stdErrors.append(df[df[epydemic.SIR.P_INFECT] == pInfect][epydemic.SIR.REMOVED].std())
ax.errorbar(pInfects, removeds, yerr=stdErrors, fmt='r-', ecolor='0.75', capsize=2.0)
ax.set_xlabel('$p_{\\mathit{infect}}$')
ax.set_ylabel('population that is...')
ax.set_title('Epidemic size vs $p_{\\mathit{infect}}$' + ', mean of {r} repetitions'.format(r=repetitions), y=1.05)

plt.show()

**100 пати експеримент (во теорија)**

----- СЛИКА 1 -----

----- СЛИКА 2 -----

----- СЛИКА 3 -----