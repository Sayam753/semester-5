import numpy as np
import pandas as pd


train_df, test_df = pd.read_csv("train.csv"), pd.read_csv("test.csv")


groups = train_df.groupby(["4"])
means, stds, covs = groups.mean(), groups.std(), groups.cov()


def bayes_classifier(x, mu, cov):
    d = x.shape[0]
    return np.exp((-1/2)*np.matmul(np.matmul((x-mu).T, np.linalg.inv(cov)), (x-mu)))/(((2*np.pi)**d/2)*np.sqrt(np.linalg.det(cov)))


prior = dict()
prior["Iris-setosa"] = 0.8
prior["Iris-versicolor"] = 0.1
prior["Iris-virginica"] = 0.1


def run_classifer(prob_func, dataset, means, sigmas):
    correct_ones = 0
    for index, row in dataset.iterrows():
        probabilities = dict()
        for group in groups.groups.keys():
            probabilities[group] = prob_func(
                row[:-1].astype('float').to_numpy(),
                means.loc[group].to_numpy(),
                sigmas.loc[group].to_numpy()
            ) * prior[group]
        if row[-1] == max(probabilities, key=probabilities.get):
            correct_ones += 1

    func_name = prob_func.__name__.replace('_', ' ').title()
    print(f"\tThe accuracy of {func_name} is {correct_ones/dataset.shape[0]*100:.2f} get_ipython().run_line_magic("")", "")


print("For training set - ")
run_classifer(bayes_classifier, train_df, means, covs)

print("\nFor test set - ")
run_classifer(bayes_classifier, test_df, means, covs)
