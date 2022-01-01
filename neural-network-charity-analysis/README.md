# Neural Network Charity Analysis

## Overview

Create a binary classifier for a dataset containing over 34,000 organizations that have received funding from Alphabet Soup. A neural network model will be designed to create the binary classifier that can predict if an Alphabet Soup–funded organization will be successful based on the features in the dataset. The model will be optimized to achieve a target accuracy score of 75% or better.

<ins>**Alphabet Soup Charity Dataset**</ins>
* EIN and NAME—Identification columns
* APPLICATION_TYPE—Alphabet Soup application type
* AFFILIATION—Affiliated sector of industry
* CLASSIFICATION—Government organization classification
* USE_CASE—Use case for funding
* ORGANIZATION—Organization type
* STATUS—Active status
* INCOME_AMT—Income classification
* SPECIAL_CONSIDERATIONS—Special consideration for application
* ASK_AMT—Funding amount requested
* IS_SUCCESSFUL—Was the money used effectively

## Data Preprocessing
The categorical data was encoded into numeric form using the scikit-learn OneHotEncoder class. The less frequently occurring categorical values for Classification Type and Application Type were binned as "Other". The numeric columns were scaled using the scikit-learn StandardScaler class. The final preprocessed dataframe has 44 feature columns.

The target variable for the deep learning model is the `IS_SUCCESSFUL` column which holds a binary value of one or zero.

The final deep learning model after its optimizations has `39 features` which are listed below.

	1. ASK_AMT 
	2. IS_SUCCESSFUL 
	3. APPLICATION_TYPE_Other
	4. APPLICATION_TYPE_T10 
	5. APPLICATION_TYPE_T19 
	6. APPLICATION_TYPE_T3
	7. APPLICATION_TYPE_T4 
	8. APPLICATION_TYPE_T5 
	9. APPLICATION_TYPE_T6
	10. APPLICATION_TYPE_T7 
	11. APPLICATION_TYPE_T8
	12. AFFILIATION_CompanySponsored 
	13. AFFILIATION_Family/Parent
	14. AFFILIATION_Independent 
	15. AFFILIATION_National AFFILIATION_Other
	16. AFFILIATION_Regional 
	17. CLASSIFICATION_C1000 
	18. CLASSIFICATION_C1200
	19. CLASSIFICATION_C2000 
	20. CLASSIFICATION_C2100 CLASSIFICATION_C3000
	21. CLASSIFICATION_Other 
	22. USE_CASE_CommunityServ 
	23. USE_CASE_Heathcare
	24. USE_CASE_Other 
	25. USE_CASE_Preservation 
	26. USE_CASE_ProductDev
	27. ORGANIZATION_Association 
	28. ORGANIZATION_Co-operative
	29. ORGANIZATION_Corporation 
	30. ORGANIZATION_Trust 
	31. INCOME_AMT_0
	32. INCOME_AMT_1-9999 
	33. INCOME_AMT_10000-24999
	34. INCOME_AMT_100000-499999 
	35. INCOME_AMT_10M-50M 
	36. INCOME_AMT_1M-5M
	37. INCOME_AMT_25000-99999 
	38. INCOME_AMT_50M+
	39. INCOME_AMT_5M-10M

These features were removed from the final model:

    1. EIN
    2. NAME
    3. STATUS
    4. SPECIAL_CONSIDERATIONS_N
    5. SPECIAL_CONSIDERATIONS_Y


## Compile, Train, and Evaluate Model
#### Initial Model
The initial model was created with one input layer, two hidden layers and one output layer. The initial configuration for the hyper-parameters are listed below. The initial model was trained for 50 epochs. The accuracy was 73%.

| Layer            | Neurons | Activation Function |
|------------------|---------|---------------------|
| Hidden Layer 1   | 80      | relu                |
| Hidden Layer 2   | 30      | relu                |
| Activation Layer | 1       | sigmoid             |

- 80 neurons were set for the first hidden layer. As a general rule, the number of neurons for the first hidden layer should double the number of input features which in this case as 39.  

- The relu activation function was used for both hidden layers since relu is one of the most common activation methods used for deep learning models. So this was a good starting point for the initial model.

- The sigmoid activation function was used in the final layer since we are building a binary classifier

#### First Optimization
The first optimization was to remove outliers in the input dataset. The model configuration remained the same as the initial model.  The model was trained on 50 epochs. The accuracy of the model remained unchanged at 72%.

| Layer            | Neurons | Activation Function |
|------------------|---------|---------------------|
| Hidden Layer 1   | 80      | relu                |
| Hidden Layer 2   | 30      | relu                |
| Activation Layer | 1       | sigmoid             |

#### Second Optimization
The second optimization was to remove three columns, 'STATUS', 'SPECIAL_CONSIDERATIONS_N', and  'SPECIAL_CONSIDERATIONS_Y' from the input dataset. The model configuration remained the same as the initial model.  The model was trained on 50 epochs. The accuracy of the model was 73%.

| Layer            | Neurons | Activation Function |
|------------------|---------|---------------------|
| Hidden Layer 1   | 80      | relu                |
| Hidden Layer 2   | 30      | relu                |
| Activation Layer | 1       | sigmoid             |

#### Third Optimization
The third optimization added 20 neurons to the first hidden layer. The model was trained on 50 epochs. The accuracy was 73%.

| Layer            | Neurons | Activation Function |
|------------------|---------|---------------------|
| Hidden Layer 1   | 100     | relu                |
| Hidden Layer 2   | 30      | relu                |
| Activation Layer | 1       | sigmoid             |

#### Fourth Optimization
The final optimization increased the training epochs from 50 to 200. The accuracy was 73%.

| Layer            | Neurons | Activation Function |
|------------------|---------|---------------------|
| Hidden Layer 1   | 100     | relu                |
| Hidden Layer 2   | 30      | relu                |
| Activation Layer | 1       | sigmoid             |

#### Fifth Optimization
An additional hidden layer with 30 neurons was added to the model. The number of neurons for the second hidden layer was increased to 50. The model was trained on 125 epochs. The model produced an accuracy of 73%.

| Layer            | Neurons | Activation Function |
|------------------|---------|---------------------|
| Hidden Layer 1   | 100     | relu                |
| Hidden Layer 2   | 50      | relu                |
| Hidden Layer 3   | 30      | relu                |
| Activation Layer | 1       | sigmoid             |

#### Sixth Optimization
Use the `tanh` activation function on the first hidden layer. Use additional neurons for the second and third hidden layers.  Train model on 150 epochs. The model had an accuracy of 73%.

| Layer            | Neurons | Activation Function |
|------------------|---------|---------------------|
| Hidden Layer 1   | 100     | tanh                |
| Hidden Layer 2   | 65      | relu                |
| Hidden Layer 3   | 40      | relu                |
| Activation Layer | 1       | sigmoid             |

## Summary

The deep learning model failed to achieve an accuracy of 75% or higher. Because the size of the dataset was about 35,000 rows, a supervised machine learning model could have been chosen. A supervised machine learning model may be quicker to setup, but it may require significant pre-processing of the input data to achieve a high accuracy score. For example, a Logistic Regression model was implemented on the pre-processed data in less time and with less configuration. But it only yielded 46% for both the training and test accuracy scores. 

It is still recommended to use a deep learning model in order to reach a 75% accuracy. Since adjusting the number of neurons, hidden layers, activation function, and epochs had little impact on the model's accuracy, it is recommended that the pre-processing stage be revisited by removing additional noisy features and adjusting the binning columns.




