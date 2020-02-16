### General report - Task 1

1) The aim of this task is to build model to classify iris flowers species.
2) Methods:
    
        2.1) At firs data was analysing and cleaned of missing and non-numerical values.
        2.2) Then data was standardized using StandardScaler.
        2.3) Processed data set was split into 70% train set and 30% test set.
        2.4) Couple of models are build and optimized using GridSearchCV function. Investigation of different
             models differing in hyperparameters such as: type and strength of regularization, 
             number of trees / k-neighbors, type of "kernel trics" or type of distance metric. 
             It will allow you to choose the optimal model (s) used for prediction.
    
        Used models and and range of hyperparameters:
      
            *  K-Neighbors Classifier (KNN):
                * hyperparameters: number of k - odds numbers from range 1-15;
                                   p value: 1 - manhatan distance or 2 - euclidian distance
              
                    
            * Random forest with bootstrap (RFF):
                * hyperparameters: numer of trees - numbers from range 100-1000
            
            
            * Supporting Vector Machines (SVM):
                * hyperparameters: regularization parameter - numbers from range 0.1 - 10
                                   kernel tricks: polynominal (degree 2-5), sigmoidal, radial basis function
                                   kenrel coefficent: scale or auto.
                                   
            * Logistic Regression ElasticNet (LR):
                * hyperparameters: inverse of regularization strength in range 0.1 - 10
                                   l1_ratio, in range 0 - 1.
    
    
            * XGBoost (XGB):
                * hyperparameters: numer of trees - numbers from range 100-1000
             
             For all estimatots and split data random_state is 101, to make results repeatable.
             All of estimators were saved using joblib.
                 
        3) Models are evaluated using metrics such as:
            * Recall
            * Precision
            * F1
            * Cross-validation scores
            * Area under ROC
            
        4) Statistical tests:
            * Level of significance = 0.05
            * Compiliance with normal distribution was tested using Shapiro-Wilk test.
            * Hypothesis that the population median of all of the groups are equal was tested using Kruskal-Wallis test.
             
3) Results:
        
    Models were evaluated, it was observed that all of them have similar general accuracy 
    from 93% - 96% and mean of cross-validation (cv) scores 96% - 98%. The mean and distribution of 
    cv scores visualised on ![plot](figures/box_plot_cross_validation_scores.png). It was noted that 
    SVM and KNN estimators have smaller inter-quartile range than others estimators. It indicate that 
    SVM and KNN retain more stable results, when they are training and testing on different folds of training-set.
    It lets think that in future validation tests these estimators will keep their results at similar level. 
    Distribution of cv scores between samples (models) was tested, because all of the sets with cv scores for each 
    models have no normal distribution, testing was performed using no-parametric test. There were no statistically 
    significance differences between samples.
    
    It is important to note that despite the similar cv scores. Models make mistakes in a different way, 
    differing in the occurrence of false positive (FP) (showed by precision) and false negative (FN) showed by recall
    results for each class of target values [classification report](General%20Models%20Metrics.txt). 
    The highest average of F1 (weighted average of the precision and recall) has LR model.
    
    The highest value of Area Under the ROC, and f1 have LR and SVM models but they differed in precision and recall,
    they were used to create voting classifier with soft system (in case of two estimators majority voting may not work). 
    The metrics of voting classifier does not increase, but it still can be more usefull in case of 
    larger test data sets
    
    