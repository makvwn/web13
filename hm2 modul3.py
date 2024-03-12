from scipy import stats

dist = stats.norm(loc=0, scale=1)
pdf_value = dist.pdf(0)
cdf_value = dist.cdf(1)
random_values = dist.rvs(size=10)

from scipy import stats

sample = [1, 2, 3, 4, 5]
t_statistic, p_value = stats.ttest_isamp(sample, popmean=3)

sample1 = [1, 2, 3, 4, 5]
sample2 = [6, 7, 8, 9, 10]
t_statistic, p_value = stats.ttest_ind(sample1,sample2)