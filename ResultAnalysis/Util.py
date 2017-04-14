#coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
# TODO
fileName = "result/3000-5000-format.csv"
def loadDataSet():
    numFeat = 16
    dataMat = []; labelMat = []
    fr = open(fileName)
    frLines = fr.readlines()
    # shuffle
    np.random.seed(23)
    indices = np.arange(frLines.__len__())
    np.random.shuffle(indices)

    for line in indices:
        lineArr=[]
        currLine = frLines[line].strip().split(',')
        for i in range(numFeat):
            lineArr.append(float(currLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(currLine[numFeat]))
    dataMat = np.mat(dataMat)
    labelMat= np.ravel(np.transpose(np.mat(labelMat))) # ravel() 将(1000,1) 变为 (1000,)
    return dataMat,labelMat

def plot_learning_curve(title,train_sizes,train_scores,test_scores):
    plt.figure()
    plt.title(title)
    plt.ylim((0,1))
    plt.xlabel("Training examples")
    plt.ylabel("Score")
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    plt.grid()

    plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                     train_scores_mean + train_scores_std, alpha=0.1,
                     color="r")
    plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                     test_scores_mean + test_scores_std, alpha=0.1, color="g")
    plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
             label="Training score")
    plt.plot(train_sizes, test_scores_mean, 'o-', color="g",
             label="Cross-validation score")

    plt.legend(loc="best")
    return plt

# linear_model
# http://scikit-learn.org/stable/auto_examples/plot_cv_predict.html#sphx-glr-auto-examples-plot-cv-predict-py
# predicted = cross_val_predict(s, x_test, y_test, cv=10)
#
# fig, ax = plt.subplots()
# ax.scatter(y_test, predicted)
# ax.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], 'k--', lw=4)
# ax.set_xlabel('Measured')
# ax.set_ylabel('Predicted')
# plt.show()