#### Final report - task 2

The goal of project was to build classifier to recognize sarcastic or not sarcastic headline content.


**Tokenizing and extracting information from sentence was carried out using (pre-trained) distilBERT 
(a smaller and faster version of BERT). The predictive model was created using random forest classifier using boostrap
method to reduce probability of over-fitting.**

1) At first data was loaded, the sentences were processed into word and sub-words, 
   CLS and SEP tokens were added, then tokens were converted to numerical values to format supported by BERT 
   using DistilBertTokenizer.
  
2) The tokenized sentences need to be the same length, differences in a number of tokens were filled using 0.

3) Because of optimization problems, data was slitted into smaller packages, the process of entering data into
   distilBERT was carried out in google cloud instance. The results was 3-D matrix, for classification 
   problems only CLS tokens for all sentence are needed. The matrix size after reduction is [number_of_sentence x 768], where 768 is 
   number of hidden layers of distilBERT. Processed by distilBERT sets of data were saved as *.npy files.
   
4) [*.npy files](../data/interim/distilBERT_output) containing extracted information from sentences and 
    corresponding labels (sarcastic - 1, not sarcastic - 0) were merged into the full data set, which was split 
    into 70% training set and 30% test set.

5) Random forest classifier was fitted to train set, then evaluated using [classification reports](../reports/model_metrics.txt). 
   Models was saved into [file](../models/classifier). 
   
6) Trained model [metrics](../reports/model_metrics.txt) were compared with the dummy model.

#### Result  

Trained model has 80% accuracy, weighted average of F1 = 0.8. 

For class sarcastic - 1:
    * frequency of false positive values = 19% (1 - precision)
    * frequency of false negative values = 29% (1 - recall)
    
For class not sarcastic - 0:
    * frequency of false positive values = 20% (1 - precision)
    * frequency of false negative values = 13% (1 - recall)
    
Dummy model [metrics](../reports/dummy_model_metrics.txt) were much worse, accuracy = 50% and weighted average of F1 = 0.5 it indicates that our model
is really fitted to data.