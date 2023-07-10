import numpy as np
from sklearn.linear_model import LinearRegression
from scipy.stats import kstest, norm
import matplotlib.pyplot as plt
import matplotlib
import sys
import util

# Check command line
if len(sys.argv) != 2:
    print(f"{sys.argv[0]} <xlsx>")
    exit(1)

# Read in the argument
infilename = sys.argv[1]

# Read the spreadsheet
X, Y, labels = util.read_excel_data(infilename)

n, d = X.shape
print(f"Read {n} rows, {d-1} features from '{infilename}'.")

# Don't need the intercept added -- X has column of 1s
lin_reg = LinearRegression(fit_intercept=False)

# Fit the model
lin_reg.fit(X, Y)

# Pretty print coefficients
print(util.format_prediction(lin_reg.coef_, labels))

# Get residual
## Your code here
predictions = lin_reg.predict(X)
residual = Y - predictions

# Make a histogram of the residual and save as "res_hist.png"
## Your code here
fig, axs = plt.subplots()
axs.hist(residual, bins=20)
axs.set(xlabel="Residual", ylabel="Density", title="Residual Histogram ")
axs.xaxis.set_major_formatter(
    matplotlib.ticker.FuncFormatter(lambda x, pos: "${:,.0f}".format(x / 1000) + "K")
)

# Write out the plots as an image
plt.tight_layout()
plt.savefig("res_hist.png")

# Do a Kolmogorov-Smirnov to see if the residual is normally
# distributed
## Your code here
result = kstest(residual, norm.cdf)
print(f"Kolmogorov-Smirnov: P-value = {result.pvalue}")
if result.pvalue < 0.05:
    print(f"\tThe residual follows a normal distribution.")
else:
    print(f"\tThe residual does not follow a normal distribution.")

# Calculate the standard deviation
## Your code here
# Find the variance first
variance = ((residual**2).sum()) / (n - d - 1)
# Then the Standard_deviation
standard_deviation = np.sqrt(variance)

print(
    f"68% of predictions with this formula will be within ${standard_deviation:,.02f} of the actual price."
)
print(
    f"95% of predictions with this formula will be within ${2.0 * standard_deviation:,.02f} of the actual price."
)
