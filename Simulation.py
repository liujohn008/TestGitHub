import numpy as np
from scipy.stats import norm
import pandas as pd

Sim_result = pd.DataFrame(columns=['ro', 'Count0', 'Count1', 'Count2', 'Count3', 'Count4', 'Count5'])
threshold = norm.ppf(0.2)
for ro in np.arange(0, 1.2, 0.2):
    cov = np.array([[1, ro, ro, ro, ro]
                   ,[ro, 1, ro, ro, ro]
                   ,[ro, ro, 1, ro, ro]
                   ,[ro, ro, ro, 1, ro]
                   ,[ro, ro, ro, ro, 1]])
    mean = np.array([0, 0, 0, 0, 0])
    sample = np.random.multivariate_normal(mean=mean, cov=cov, size=1000)

    for i in range(len(sample)):
        sample[i] = (sample[i] <= threshold) * 1
    bi_result = pd.DataFrame(columns=['Y1', 'Y2', 'Y3', 'Y4', 'Y5'], data=sample, dtype=int)
    bi_result['SUM'] = bi_result['Y1'] + bi_result['Y2'] + bi_result['Y3'] + bi_result['Y4'] + bi_result['Y5']

    Count0 = len(bi_result[bi_result['SUM'] == 0])
    Count1 = len(bi_result[bi_result['SUM'] == 1])
    Count2 = len(bi_result[bi_result['SUM'] == 2])
    Count3 = len(bi_result[bi_result['SUM'] == 3])
    Count4 = len(bi_result[bi_result['SUM'] == 4])
    Count5 = len(bi_result[bi_result['SUM'] == 5])

    # result = pd.DataFrame(data = np.transpose([ro,Count0,Count1,Count2,Count3,Count4,Count5]), columns=['ro','Count0','Count1','Count2','Count3','Count4','Count5'])
    Sim_result.loc[len(Sim_result)] = [ro, Count0, Count1, Count2, Count3, Count4, Count5]

print Sim_result
