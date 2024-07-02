from scipy.stats import ttest_1samp
import inspect
import re
import numpy as np

def pttest(diff, popmean=0, conf_int = 0.95):
    print("\n\t One Sample t-test\n")
    caller_frame = inspect.currentframe().f_back
    source_lines, _ = inspect.getsourcelines(caller_frame)
    source_code = ''.join(source_lines)

    call_line = None
    for line in source_lines:
        if 'pttest(' in line:
            call_line = line.strip()
            break

    if call_line:
        res = re.findall(r'\(.*?\)', call_line)[0]
        print("data: \t" + re.findall(r'\(.*?\)', res)[0][1:len(res)-1])
    k = ttest_1samp(diff, popmean=0)
    print("t = {}, df = {}, p-value < {}".format(np.round(k.statistic, 3),np.round(k.df, 3), k.pvalue))
    print("{} percent confidence interval:".format(conf_int))
    print("{} {}".format(np.round(k.confidence_interval(confidence_level=conf_int).low, 3), np.round(k.confidence_interval(confidence_level=conf_int).high, 3)))
    print("sample esimates:")
    print("mean of x")
    print(np.round(diff.mean(),4))