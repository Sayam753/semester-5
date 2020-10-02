"""Group 9 Problem 2 solution."""

from __future__ import absolute_import
from __future__ import division
import numpy as np
import pandas as pd

train_df, test_df = pd.read_csv("train.csv"), pd.read_csv("test.csv")

# Group by each label and calculate statistics
groups = train_df.groupby(["4"])
means, stds, covs = groups.mean(), groups.std(), groups.cov()


def naive_bayes_classifier(x, mu, sigma):  # pylint: disable=invalid-name
    """Calculate gaussian probability for naive bayes classifier."""
    return np.prod(np.exp((-1 / 2) * ((x - mu) / sigma) ** 2) / (sigma * np.sqrt(2 * np.pi)))


def run_classifer(prob_func, dataset, mus, sigmas):
    """Run bayes or naive bayes classifier."""
    correct_ones = 0

    # For each row, find maximum of class conditional probabilities.
    for _, row in dataset.iterrows():
        probabilities = dict()
        for group in groups.groups.keys():
            probabilities[group] = prob_func(
                row[:-1].astype("float").to_numpy(),
                mus.loc[group].to_numpy(),
                sigmas.loc[group].to_numpy(),
            )

        # Checking against true label
        if row[-1] == max(probabilities, key=probabilities.get):
            correct_ones += 1

    func_name = prob_func.__name__.replace("_", " ").title()
    print(f"\tThe accuracy of {func_name} is {correct_ones/dataset.shape[0]*100:.2f} %")


print("For training set - ")
run_classifer(naive_bayes_classifier, train_df, means, stds)

print("\nFor test set - ")
run_classifer(naive_bayes_classifier, test_df, means, stds)


"""
Output -

For training set -
        The accuracy of Naive Bayes Classifier is 95.54 %

For test set -
        The accuracy of Naive Bayes Classifier is 100.00 %
"""
