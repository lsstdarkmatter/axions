#!/usr/bin/env python
"""
Generic python script.
"""
__author__ = "Alex Drlica-Wagner"

import numpy as np
import pylab as plt

data = np.genfromtxt('data/gc-hb-rgb.txt',names=True,dtype=None)
# Select metal-poor clusters
d = data[data['feh_gc97'] <= -1.1]

weights = 1./d['sigma']**2
wavg = np.average(d['R'],weights=weights)
wavg_err = 1./np.sqrt(np.sum(weights))

label = "R_avg = %.2f +/- %.2f"%(wavg,wavg_err)
print(label)

plt.figure()
plt.errorbar(x=d['feh_gc97'],y=d['R'],yerr=d['sigma'],marker='o',ls='',ms=10, capthick=2,elinewidth=3,capsize=5,mfc='w',c='k',mew=1.5)
plt.ylabel(r'${\rm Ratio}\ (N_{\rm HB}/N_{\rm RGB})$')
plt.xlabel(r'${\rm [Fe/H]}$')
plt.axhline(wavg,c='gray',lw=2)
plt.axhline(wavg+wavg_err,ls='-',c='gray',lw=2,zorder=-1,label=label)
plt.axhline(wavg-wavg_err,ls='--',c='gray',lw=2,zorder=-1)
plt.legend()

