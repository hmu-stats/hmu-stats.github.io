import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import truncnorm
import pandas as pd
import os

np.random.seed(0)

N = 500
# bounds_inflam = [0, 1]
mean_inflam_paradoxia = 0.2
std_inflam_paradoxia = 0.05
mean_inflam_control = 0.1
std_inflam_control = 0.03
data_inflam_paradoxia = truncnorm.rvs(a=(bounds_inflam[0] - mean_inflam_paradoxia) / std_inflam_paradoxia, b=(bounds_inflam[1] - mean_inflam_paradoxia) / std_inflam_paradoxia, loc=mean_inflam_paradoxia, scale=std_inflam_paradoxia, size=N)
data_inflam_control = truncnorm.rvs(a=(bounds_inflam[0] - mean_inflam_control) / std_inflam_control, b=(bounds_inflam[1] - mean_inflam_control) / std_inflam_control, loc=mean_inflam_control, scale=std_inflam_control, size=N)

# bounds_paradoxia = [0, 4.5]
mean_tiktok_paradoxia = 1.3
std_tiktok_paradoxia = 0.4
mean_tiktok_control = 0.8
std_tiktok_control = 0.3

data_tiktok_paradoxia = (data_inflam_paradoxia + 0.125*np.random.randn(N))
data_tiktok_paradoxia[data_tiktok_paradoxia < 0] = np.random.rand((data_tiktok_paradoxia < 0).sum())
data_tiktok_control = (data_inflam_control + 0.125*np.random.randn(N))
data_tiktok_control[data_tiktok_control < 0] = np.random.rand((data_tiktok_control < 0).sum())

data_tiktok_paradoxia = truncnorm.rvs(a=(bounds_paradoxia[0] - mean_tiktok_paradoxia) / std_tiktok_paradoxia, b=(bounds_paradoxia[1] - mean_tiktok_paradoxia) / std_tiktok_paradoxia, loc=mean_tiktok_paradoxia, scale=std_tiktok_paradoxia, size=N)
data_tiktok_control = truncnorm.rvs(a=(bounds_paradoxia[0] - mean_tiktok_control) / std_tiktok_control, b=(bounds_paradoxia[1] - mean_tiktok_control) / std_tiktok_control, loc=mean_tiktok_control, scale=std_tiktok_control, size=N)

binsize=0.02
xlim = (0, 0.4)
ylim = (0, 140)





df = pd.DataFrame(index=range(2*N))
df['id'] = range(1, 2*N+1)
df['group'] = np.hstack((np.ones(N, int), 2*np.ones(N, int)))
df['inflammatory value (0-1)'] = np.hstack((data_inflam_control, data_inflam_paradoxia))
df['hours on tiktok per day (0-24)'] = np.hstack((data_tiktok_control, data_tiktok_paradoxia))
print(df.iloc[[0, 1, 499, 500, 501, 999]].round(3))
df.to_csv('data/paradoxia_inflammation.csv')
print(f"Data saved to {os.path.abspath('data/paradoxia_inflammation.csv')}")

fontsize = 15



plt.style.use('dark_background')
plt.figure()
plt.hist(data_inflam_paradoxia, edgecolor='#999', color='#beddff', bins=np.arange(0, 0.51, binsize), label='Paradoxia')
plt.xlabel('Entzündungswert', fontsize=fontsize)
plt.ylabel('Anzahl', fontsize=fontsize)
plt.xlim(xlim)
plt.ylim(ylim)
plt.legend()
plt.savefig('images/paradoxia_histogram_inflammation_paradoxiker.png', bbox_inches="tight")

plt.style.use('default')
plt.figure()
plt.hist(data_inflam_paradoxia, edgecolor='#999', color='#94b9ea', bins=np.arange(0, 0.51, binsize), label='Paradoxia')
plt.xlabel('Entzündungswert', fontsize=fontsize)
plt.ylabel('Anzahl', fontsize=fontsize)
plt.xlim(xlim)
plt.ylim(ylim)
plt.legend()
plt.savefig('images/paradoxia_histogram_inflammation_paradoxiker_whitebg.png', bbox_inches="tight")


plt.style.use('default')
plt.figure()
# hack to make alpha level work in combination with black background
plt.hist(data_inflam_control, edgecolor='#999', color='white', bins=np.arange(0, 0.51, binsize))
# hack to have legend entry without transparency
plt.hist(data_inflam_control+10, edgecolor='#999', color='#f5f5b9', bins=np.arange(0, 0.51, binsize), label='Kontroll')
# hack-end
plt.hist(data_inflam_paradoxia, edgecolor='#999', color='#94b9ea', bins=np.arange(0, 0.51, binsize), label='Paradoxia')
plt.hist(data_inflam_control, edgecolor='#999', color='#dfdf18', bins=np.arange(0, 0.51, binsize), alpha=0.3)
plt.xlabel('Entzündungswert', fontsize=fontsize)
plt.ylabel('Anzahl', fontsize=fontsize)
plt.xlim(xlim)
plt.ylim(ylim)
plt.legend()
plt.savefig('images/paradoxia_histogram_inflammation_whitebg.png', bbox_inches="tight")

plt.style.use('dark_background')
plt.figure()
# hack to make alpha level work in combination with black background
plt.hist(data_inflam_control, edgecolor='#999', color='white', bins=np.arange(0, 0.51, binsize))
# hack to have legend entry without transparency
plt.hist(data_inflam_control+10, edgecolor='#999', color='#fffeef', bins=np.arange(0, 0.51, binsize), label='Kontroll')
# hack-end
plt.hist(data_inflam_paradoxia, edgecolor='#999', color='#beddff', bins=np.arange(0, 0.51, binsize), label='Paradoxia')
plt.hist(data_inflam_control, edgecolor='#999', color='#fffdca', bins=np.arange(0, 0.51, binsize), alpha=0.3)
plt.xlabel('Entzündungswert', fontsize=fontsize)
plt.ylabel('Anzahl', fontsize=fontsize)
plt.xlim(xlim)
plt.ylim(ylim)
plt.legend()
plt.savefig('images/paradoxia_histogram_inflammation.png', bbox_inches="tight")


plt.style.use('dark_background')
plt.figure()
# hack to make alpha level work in combination with black background
plt.hist(data_inflam_control, weights=np.ones(N)/N, edgecolor='#999', color='white', bins=np.arange(0, 0.51, binsize))
# hack to have legend entry without transparency
plt.hist(data_inflam_control+10, weights=np.ones(N)/N, edgecolor='#999', color='#fffeef', bins=np.arange(0, 0.51, binsize), label='Kontroll')
# hack-end
plt.hist(data_inflam_paradoxia, weights=np.ones(N)/N, edgecolor='#999', color='#beddff', bins=np.arange(0, 0.51, binsize), label='Paradoxia')
plt.hist(data_inflam_control, weights=np.ones(N)/N, edgecolor='#999', color='#fffdca', bins=np.arange(0, 0.51, binsize), alpha=0.3)
plt.xlabel('Entzündungswert', fontsize=fontsize)
plt.ylabel('Wahrscheinlichkeit', fontsize=fontsize)
plt.xlim(xlim)
plt.legend()
plt.savefig('images/paradoxia_histogram_inflammation_probability.png', bbox_inches="tight")