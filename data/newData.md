Classification Report:
                precision  recall  f1-score  support
Unprofessional      0.571   0.163     0.254   98.000
Borderline          0.000   0.000     0.000   17.000
Appropriate         0.778   0.974     0.865  346.000
accuracy            0.766   0.766     0.766    0.766
macro avg           0.450   0.379     0.373  461.000
weighted avg        0.706   0.766     0.703  461.000
Cohen's Kappa: 0.1696
Mean confidence: 0.6132
Accuracy (recomputed): 0.7657
Weighted F1 score: 0.7034

## (venv) [zhengwb@gpu-compute-12 LLMAsAJudge]$ python3 main.py --model_name emilyalsentzer/Bio_ClinicalBERT --learning_rate 2e-5 --batch_size 3 --epochs 3  

Model loaded from outputs/distraction/best_model
Epoch 1/3 - Train Loss: 0.4104 - Val Loss: 0.5729 - Val Acc: 0.8312
Epoch 2/3 - Train Loss: 0.2538 - Val Loss: 0.6346 - Val Acc: 0.8225
Epoch 3/3 - Train Loss: 0.1326 - Val Loss: 0.5451 - Val Acc: 0.8528
=== Further fine-tuned Distraction model saved to outputs/distraction/best_model ===

=== Done! ===
(venv) [zhengwb@gpu-compute-12 LLMAsAJudge]$ python3 main.py --model_name emilyalsentzer/Bio_ClinicalBERT --learning_rate 2e-5 --batch_size 3 --epochs 3  
/home/zhengwb/.local/lib/python3.9/site-packages/pandas/core/computation/expressions.py:21: UserWarning: Pandas requires version '2.8.4' or newer of 'numexpr' (version '2.8.1' currently installed).
  from pandas.core.computation.check import NUMEXPR_INSTALLED
/home/zhengwb/.local/lib/python3.9/site-packages/pandas/core/arrays/masked.py:60: UserWarning: Pandas requires version '1.3.6' or newer of 'bottleneck' (version '1.3.4' currently installed).
  from pandas.core import (
=== Loading data ===

Merged data saved to merged_data.xlsx
Merged data shape: (2303, 10)

=== Processing Professionalism Criterion ===
Number of classes for professionalism: 3
Preprocessing data for professionalism...
Processed data shape: (2303, 11)
Splitting data for professionalism...
Train set: 1611 rows
Validation set: 231 rows
Test set: 461 rows
Saved processed data to data/processed/professionalism

=== Training model for Professionalism ===
Some weights of BertForSequenceClassification were not initialized from the model checkpoint at emilyalsentzer/Bio_ClinicalBERT and are newly initialized: ['classifier.bias', 'classifier.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
Epoch 1/3 - Train Loss: 0.7683 - Val Loss: 0.5634 - Val Acc: 0.7749
Epoch 2/3 - Train Loss: 0.5584 - Val Loss: 0.5176 - Val Acc: 0.8009
Epoch 3/3 - Train Loss: 0.3297 - Val Loss: 0.7697 - Val Acc: 0.7749

=== Evaluating Professionalism model ===
Model loaded from outputs/professionalism/best_model
Professionalism Test Loss: 0.5850
Professionalism Test Accuracy: 0.7918
Sample predictions and confidences:
Text: I try to contact Satan. I asked if he knows what happened to the kid | Pred: 2 | Confidence: 0.6194
Text: Are you drunk? | Pred: 0 | Confidence: 0.8444
Text: I am an M2 wanting to do a case about purple finger licking good chicken disease | Pred: 0 | Confidence: 0.5768
Text: I quickly invent a medical device that allows me to use telekinetic powers | Pred: 2 | Confidence: 0.7545
Text: Hi mr. Johnson | Pred: 2 | Confidence: 0.7310
Text: Repeat scenario | Pred: 2 | Confidence: 0.7396
Text: I say wow! | Pred: 0 | Confidence: 0.6861
Text: What did I think of? | Pred: 2 | Confidence: 0.8483
Text: Chest xray | Pred: 2 | Confidence: 0.6499
Text: what if i told you there was nothing that could be done, because our cardiologists are stuck in Israel | Pred: 0 | Confidence: 0.7472
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
Classification Report:
                precision  recall  f1-score  support
Unprofessional      0.535   0.857     0.659   98.000
Borderline          0.000   0.000     0.000   17.000
Appropriate         0.924   0.812     0.865  346.000
accuracy            0.792   0.792     0.792    0.792
macro avg           0.486   0.556     0.508  461.000
weighted avg        0.807   0.792     0.789  461.000
Cohen's Kappa: 0.5187
Mean confidence: 0.7218
Accuracy (recomputed): 0.7918
Weighted F1 score: 0.7890

=== Professionalism model saved to outputs/professionalism/best_model ===

=== Processing Relevance Criterion ===
Number of classes for relevance: 3
Preprocessing data for relevance...
Processed data shape: (2303, 11)
Splitting data for relevance...
Train set: 1611 rows
Validation set: 231 rows
Test set: 461 rows
Saved processed data to data/processed/relevance

=== Training model for Relevance ===
Some weights of BertForSequenceClassification were not initialized from the model checkpoint at emilyalsentzer/Bio_ClinicalBERT and are newly initialized: ['classifier.bias', 'classifier.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
Epoch 1/3 - Train Loss: 0.6829 - Val Loss: 0.4498 - Val Acc: 0.8225
Epoch 2/3 - Train Loss: 0.4109 - Val Loss: 0.4806 - Val Acc: 0.8268
Epoch 3/3 - Train Loss: 0.2475 - Val Loss: 0.5462 - Val Acc: 0.8225

=== Evaluating Relevance model ===
Model loaded from outputs/relevance/best_model
Relevance Test Loss: 0.4726
Relevance Test Accuracy: 0.8373
Sample predictions and confidences:
Text: I try to contact Satan. I asked if he knows what happened to the kid | Pred: 0 | Confidence: 0.8202
Text: Are you drunk? | Pred: 0 | Confidence: 0.7156
Text: I am an M2 wanting to do a case about purple finger licking good chicken disease | Pred: 0 | Confidence: 0.8448
Text: I quickly invent a medical device that allows me to use telekinetic powers | Pred: 0 | Confidence: 0.6077
Text: Hi mr. Johnson | Pred: 0 | Confidence: 0.7512
Text: Repeat scenario | Pred: 2 | Confidence: 0.5245
Text: I say wow! | Pred: 0 | Confidence: 0.8703
Text: What did I think of? | Pred: 2 | Confidence: 0.7697
Text: Chest xray | Pred: 2 | Confidence: 0.8993
Text: what if i told you there was nothing that could be done, because our cardiologists are stuck in Israel | Pred: 0 | Confidence: 0.8036
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
Classification Report:
                    precision  recall  f1-score  support
Irrelevant              0.710   0.933     0.806  165.000
Partially relevant      0.000   0.000     0.000    8.000
Relevant                0.951   0.806     0.872  288.000
accuracy                0.837   0.837     0.837    0.837
macro avg               0.553   0.580     0.559  461.000
weighted avg            0.848   0.837     0.833  461.000
Cohen's Kappa: 0.6752
Mean confidence: 0.7639
Accuracy (recomputed): 0.8373
Weighted F1 score: 0.8335

=== Relevance model saved to outputs/relevance/best_model ===

=== Processing Ethics Criterion ===
Number of classes for ethics: 5
Preprocessing data for ethics...
Processed data shape: (2303, 11)
Splitting data for ethics...
Train set: 1611 rows
Validation set: 231 rows
Test set: 461 rows
Saved processed data to data/processed/ethics

=== Training model for Ethics ===
Some weights of BertForSequenceClassification were not initialized from the model checkpoint at emilyalsentzer/Bio_ClinicalBERT and are newly initialized: ['classifier.bias', 'classifier.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
Epoch 1/3 - Train Loss: 1.0605 - Val Loss: 0.6953 - Val Acc: 0.8182
Epoch 2/3 - Train Loss: 0.9140 - Val Loss: 0.5278 - Val Acc: 0.8312
Epoch 3/3 - Train Loss: 0.7241 - Val Loss: 0.5537 - Val Acc: 0.8225

=== Evaluating Ethics model ===
Model loaded from outputs/ethics/best_model
Ethics Test Loss: 0.4904
Ethics Test Accuracy: 0.8590
Sample predictions and confidences:
Text: I try to contact Satan. I asked if he knows what happened to the kid | Pred: 4 | Confidence: 0.9026
Text: Are you drunk? | Pred: 4 | Confidence: 0.9158
Text: I am an M2 wanting to do a case about purple finger licking good chicken disease | Pred: 4 | Confidence: 0.6767
Text: I quickly invent a medical device that allows me to use telekinetic powers | Pred: 4 | Confidence: 0.7398
Text: Hi mr. Johnson | Pred: 4 | Confidence: 0.9152
Text: Repeat scenario | Pred: 4 | Confidence: 0.8492
Text: I say wow! | Pred: 4 | Confidence: 0.6978
Text: What did I think of? | Pred: 4 | Confidence: 0.9280
Text: Chest xray | Pred: 4 | Confidence: 0.9024
Text: what if i told you there was nothing that could be done, because our cardiologists are stuck in Israel | Pred: 4 | Confidence: 0.5756
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
Classification Report:
              precision  recall  f1-score  support
Dangerous         0.700   0.375     0.488   56.000
Unsafe            0.000   0.000     0.000   11.000
Questionable      0.000   0.000     0.000    8.000
Mostly safe       0.000   0.000     0.000    4.000
Safe              0.870   0.982     0.923  382.000
accuracy          0.859   0.859     0.859    0.859
macro avg         0.314   0.271     0.282  461.000
weighted avg      0.806   0.859     0.824  461.000
Cohen's Kappa: 0.3514
Mean confidence: 0.7950
Accuracy (recomputed): 0.8590
Weighted F1 score: 0.8237

=== Ethics model saved to outputs/ethics/best_model ===

=== Processing Distraction Criterion ===
Number of classes for distraction: 4
Preprocessing data for distraction...
Processed data shape: (2303, 11)
Splitting data for distraction...
Train set: 1611 rows
Validation set: 231 rows
Test set: 461 rows
Saved processed data to data/processed/distraction

=== Training model for Distraction ===
Some weights of BertForSequenceClassification were not initialized from the model checkpoint at emilyalsentzer/Bio_ClinicalBERT and are newly initialized: ['classifier.bias', 'classifier.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
Epoch 1/3 - Train Loss: 0.9583 - Val Loss: 0.5747 - Val Acc: 0.7965
Epoch 2/3 - Train Loss: 0.6590 - Val Loss: 0.5345 - Val Acc: 0.8182
Epoch 3/3 - Train Loss: 0.4692 - Val Loss: 0.6115 - Val Acc: 0.8009

=== Evaluating Distraction model ===
Model loaded from outputs/distraction/best_model
Distraction Test Loss: 0.5257
Distraction Test Accuracy: 0.8265
Sample predictions and confidences:
Text: I try to contact Satan. I asked if he knows what happened to the kid | Pred: 0 | Confidence: 0.7985
Text: Are you drunk? | Pred: 0 | Confidence: 0.6316
Text: I am an M2 wanting to do a case about purple finger licking good chicken disease | Pred: 0 | Confidence: 0.8495
Text: I quickly invent a medical device that allows me to use telekinetic powers | Pred: 0 | Confidence: 0.4945
Text: Hi mr. Johnson | Pred: 3 | Confidence: 0.9539
Text: Repeat scenario | Pred: 3 | Confidence: 0.8645
Text: I say wow! | Pred: 0 | Confidence: 0.8656
Text: What did I think of? | Pred: 0 | Confidence: 0.6744
Text: Chest xray | Pred: 3 | Confidence: 0.9597
Text: what if i told you there was nothing that could be done, because our cardiologists are stuck in Israel | Pred: 0 | Confidence: 0.8382
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
Classification Report:
                        precision  recall  f1-score  support
Highly distracting          0.735   0.882     0.802  170.000
Moderately distracting      1.000   0.158     0.273   19.000
Questionable                0.000   0.000     0.000    7.000
Not distracting             0.898   0.860     0.879  265.000
accuracy                    0.826   0.826     0.826    0.826
macro avg                   0.658   0.475     0.488  461.000
weighted avg                0.828   0.826     0.812  461.000
Cohen's Kappa: 0.6662
Mean confidence: 0.7860
Accuracy (recomputed): 0.8265
Weighted F1 score: 0.8121

=== Distraction model saved to outputs/distraction/best_model ===

=== Training Summary ===
Professionalism model: outputs/professionalism/best_model
Relevance model: outputs/relevance/best_model
Ethics model: outputs/ethics/best_model
Distraction model: outputs/distraction/best_model

=== Further Fine-Tuning Professionalism with Prompt Engineering ===
Model loaded from outputs/professionalism/best_model
Epoch 1/3 - Train Loss: 0.3557 - Val Loss: 0.6377 - Val Acc: 0.7879
Epoch 2/3 - Train Loss: 0.2274 - Val Loss: 0.5939 - Val Acc: 0.8009
Epoch 3/3 - Train Loss: 0.1154 - Val Loss: 0.8003 - Val Acc: 0.8009
=== Further fine-tuned Professionalism model saved to outputs/professionalism/best_model ===

=== Further Fine-Tuning Relevance with Prompt Engineering ===
Model loaded from outputs/relevance/best_model
Epoch 1/3 - Train Loss: 0.4144 - Val Loss: 0.4557 - Val Acc: 0.8225
Epoch 2/3 - Train Loss: 0.2372 - Val Loss: 0.6001 - Val Acc: 0.8095
Epoch 3/3 - Train Loss: 0.1777 - Val Loss: 0.6365 - Val Acc: 0.7922
=== Further fine-tuned Relevance model saved to outputs/relevance/best_model ===

=== Further Fine-Tuning Ethics with Prompt Engineering ===
Model loaded from outputs/ethics/best_model
Epoch 1/3 - Train Loss: 0.7175 - Val Loss: 0.6084 - Val Acc: 0.7922
Epoch 2/3 - Train Loss: 0.4785 - Val Loss: 0.6757 - Val Acc: 0.7879
Epoch 3/3 - Train Loss: 0.3041 - Val Loss: 0.8573 - Val Acc: 0.7446
=== Further fine-tuned Ethics model saved to outputs/ethics/best_model ===

=== Further Fine-Tuning Distraction with Prompt Engineering ===
Model loaded from outputs/distraction/best_model
Epoch 1/3 - Train Loss: 0.4470 - Val Loss: 0.6089 - Val Acc: 0.8009
Epoch 2/3 - Train Loss: 0.3128 - Val Loss: 0.7713 - Val Acc: 0.7489
Epoch 3/3 - Train Loss: 0.1791 - Val Loss: 0.7377 - Val Acc: 0.8225
=== Further fine-tuned Distraction model saved to outputs/distraction/best_model ===

=== Done! ===
(venv) [zhengwb@gpu-compute-12 LLMAsAJudge]$ python3 main.py --model_name microsoft/deberta-v3-base --learning_rate 2e-5 --batch_size 3 --epochs 3 
/home/zhengwb/.local/lib/python3.9/site-packages/pandas/core/computation/expressions.py:21: UserWarning: Pandas requires version '2.8.4' or newer of 'numexpr' (version '2.8.1' currently installed).
  from pandas.core.computation.check import NUMEXPR_INSTALLED
/home/zhengwb/.local/lib/python3.9/site-packages/pandas/core/arrays/masked.py:60: UserWarning: Pandas requires version '1.3.6' or newer of 'bottleneck' (version '1.3.4' currently installed).
  from pandas.core import (
=== Loading data ===
/home/zhengwb/.local/lib/python3.9/site-packages/openpyxl/worksheet/_reader.py:329: UserWarning: Data Validation extension is not supported and will be removed
  warn(msg)
Loaded fuzzy.coding.dataCP.xlsx: 2302 rows, 11 columns
/home/zhengwb/.local/lib/python3.9/site-packages/openpyxl/worksheet/_reader.py:329: UserWarning: Data Validation extension is not supported and will be removed
  warn(msg)
Loaded fuzzy.coding.dataCZ.xlsx: 2302 rows, 10 columns
/home/zhengwb/.local/lib/python3.9/site-packages/openpyxl/worksheet/_reader.py:329: UserWarning: Data Validation extension is not supported and will be removed
  warn(msg)
Loaded fuzzy.coding.dataDF.xlsx: 2302 rows, 10 columns
/home/zhengwb/.local/lib/python3.9/site-packages/openpyxl/worksheet/_reader.py:329: UserWarning: Data Validation extension is not supported and will be removed
  warn(msg)
Loaded fuzzy.coding.dataDW.xlsx: 2302 rows, 10 columns
/home/zhengwb/.local/lib/python3.9/site-packages/openpyxl/worksheet/_reader.py:329: UserWarning: Data Validation extension is not supported and will be removed
  warn(msg)
Loaded fuzzy.coding.dataMG.xlsx: 2302 rows, 11 columns
/home/zhengwb/.local/lib/python3.9/site-packages/openpyxl/worksheet/_reader.py:329: UserWarning: Data Validation extension is not supported and will be removed
  warn(msg)
Loaded fuzzy.coding.dataMK.xlsx: 2302 rows, 10 columns
/home/zhengwb/.local/lib/python3.9/site-packages/openpyxl/worksheet/_reader.py:329: UserWarning: Data Validation extension is not supported and will be removed
  warn(msg)
Loaded fuzzy.coding.dataMS.xlsx: 2302 rows, 10 columns
/home/zhengwb/ondemand/LLMAsAJudge/src/data/data_loader.py:310: UserWarning: Pandas requires version '3.0.5' or newer of 'xlsxwriter' (version '3.0.3' currently installed).
  conflicts_df.to_excel(conflict_output_path, index=False)
Conflicts saved to conflicts_output.xlsx
Conflicting rows found and saved to 'conflicts_output.xlsx'.
/home/zhengwb/ondemand/LLMAsAJudge/main.py:258: UserWarning: Pandas requires version '3.0.5' or newer of 'xlsxwriter' (version '3.0.3' currently installed).
  merged_data.to_excel(merged_data_file, index=False)
Merged data saved to merged_data.xlsx
Merged data shape: (2303, 10)

=== Processing Professionalism Criterion ===
Number of classes for professionalism: 3
Preprocessing data for professionalism...
Processed data shape: (2303, 11)
Splitting data for professionalism...
Train set: 1611 rows
Validation set: 231 rows
Test set: 461 rows
Saved processed data to data/processed/professionalism

=== Training model for Professionalism ===
/home/zhengwb/.local/lib/python3.9/site-packages/transformers/convert_slow_tokenizer.py:559: UserWarning: The sentencepiece tokenizer that you are converting to a fast tokenizer uses the byte fallback option which is not implemented in the fast tokenizers. In practice this means that the fast version of the tokenizer can produce unknown tokens whereas the sentencepiece version would have converted these unknown tokens into a sequence of byte tokens matching the original piece of text.
  warnings.warn(
Some weights of DebertaV2ForSequenceClassification were not initialized from the model checkpoint at microsoft/deberta-v3-base and are newly initialized: ['classifier.bias', 'classifier.weight', 'pooler.dense.bias', 'pooler.dense.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
Epoch 1/3 - Train Loss: 0.8392 - Val Loss: 0.6077 - Val Acc: 0.7316
Epoch 2/3 - Train Loss: 0.6853 - Val Loss: 0.4964 - Val Acc: 0.8052
Epoch 3/3 - Train Loss: 0.5494 - Val Loss: 0.7005 - Val Acc: 0.7662

=== Evaluating Professionalism model ===
Model loaded from outputs/professionalism/best_model
Professionalism Test Loss: 0.4913
Professionalism Test Accuracy: 0.8069
Sample predictions and confidences:
Text: I try to contact Satan. I asked if he knows what happened to the kid | Pred: 0 | Confidence: 0.5928
Text: Are you drunk? | Pred: 2 | Confidence: 0.7765
Text: I am an M2 wanting to do a case about purple finger licking good chicken disease | Pred: 0 | Confidence: 0.7280
Text: I quickly invent a medical device that allows me to use telekinetic powers | Pred: 2 | Confidence: 0.6580
Text: Hi mr. Johnson | Pred: 2 | Confidence: 0.8373
Text: Repeat scenario | Pred: 2 | Confidence: 0.8915
Text: I say wow! | Pred: 2 | Confidence: 0.7281
Text: What did I think of? | Pred: 2 | Confidence: 0.9299
Text: Chest xray | Pred: 2 | Confidence: 0.8791
Text: what if i told you there was nothing that could be done, because our cardiologists are stuck in Israel | Pred: 2 | Confidence: 0.5732
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
Classification Report:
                precision  recall  f1-score  support
Unprofessional      0.688   0.449     0.543   98.000
Borderline          0.000   0.000     0.000   17.000
Appropriate         0.826   0.948     0.883  346.000
accuracy            0.807   0.807     0.807    0.807
macro avg           0.505   0.466     0.475  461.000
weighted avg        0.766   0.807     0.778  461.000
Cohen's Kappa: 0.4044
Mean confidence: 0.8043
Accuracy (recomputed): 0.8069
Weighted F1 score: 0.7781

=== Professionalism model saved to outputs/professionalism/best_model ===

=== Processing Relevance Criterion ===
Number of classes for relevance: 3
Preprocessing data for relevance...
Processed data shape: (2303, 11)
Splitting data for relevance...
Train set: 1611 rows
Validation set: 231 rows
Test set: 461 rows
Saved processed data to data/processed/relevance

=== Training model for Relevance ===
/home/zhengwb/.local/lib/python3.9/site-packages/transformers/convert_slow_tokenizer.py:559: UserWarning: The sentencepiece tokenizer that you are converting to a fast tokenizer uses the byte fallback option which is not implemented in the fast tokenizers. In practice this means that the fast version of the tokenizer can produce unknown tokens whereas the sentencepiece version would have converted these unknown tokens into a sequence of byte tokens matching the original piece of text.
  warnings.warn(
Some weights of DebertaV2ForSequenceClassification were not initialized from the model checkpoint at microsoft/deberta-v3-base and are newly initialized: ['classifier.bias', 'classifier.weight', 'pooler.dense.bias', 'pooler.dense.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
Epoch 1/3 - Train Loss: 0.7397 - Val Loss: 0.4282 - Val Acc: 0.8312
Epoch 2/3 - Train Loss: 0.4716 - Val Loss: 0.4838 - Val Acc: 0.8268
Epoch 3/3 - Train Loss: 0.3373 - Val Loss: 0.4843 - Val Acc: 0.8571

=== Evaluating Relevance model ===
Model loaded from outputs/relevance/best_model
Relevance Test Loss: 0.4585
Relevance Test Accuracy: 0.8113
Sample predictions and confidences:
Text: I try to contact Satan. I asked if he knows what happened to the kid | Pred: 0 | Confidence: 0.8234
Text: Are you drunk? | Pred: 0 | Confidence: 0.5111
Text: I am an M2 wanting to do a case about purple finger licking good chicken disease | Pred: 0 | Confidence: 0.7706
Text: I quickly invent a medical device that allows me to use telekinetic powers | Pred: 0 | Confidence: 0.8193
Text: Hi mr. Johnson | Pred: 0 | Confidence: 0.5673
Text: Repeat scenario | Pred: 2 | Confidence: 0.8297
Text: I say wow! | Pred: 0 | Confidence: 0.7092
Text: What did I think of? | Pred: 0 | Confidence: 0.6700
Text: Chest xray | Pred: 2 | Confidence: 0.9366
Text: what if i told you there was nothing that could be done, because our cardiologists are stuck in Israel | Pred: 0 | Confidence: 0.6582
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
Classification Report:
                    precision  recall  f1-score  support
Irrelevant              0.677   0.915     0.778  165.000
Partially relevant      0.000   0.000     0.000    8.000
Relevant                0.937   0.774     0.848  288.000
accuracy                0.811   0.811     0.811    0.811
macro avg               0.538   0.563     0.542  461.000
weighted avg            0.828   0.811     0.808  461.000
Cohen's Kappa: 0.6258
Mean confidence: 0.7682
Accuracy (recomputed): 0.8113
Weighted F1 score: 0.8083

=== Relevance model saved to outputs/relevance/best_model ===

=== Processing Ethics Criterion ===
Number of classes for ethics: 5
Preprocessing data for ethics...
Processed data shape: (2303, 11)
Splitting data for ethics...
Train set: 1611 rows
Validation set: 231 rows
Test set: 461 rows
Saved processed data to data/processed/ethics

=== Training model for Ethics ===
/home/zhengwb/.local/lib/python3.9/site-packages/transformers/convert_slow_tokenizer.py:559: UserWarning: The sentencepiece tokenizer that you are converting to a fast tokenizer uses the byte fallback option which is not implemented in the fast tokenizers. In practice this means that the fast version of the tokenizer can produce unknown tokens whereas the sentencepiece version would have converted these unknown tokens into a sequence of byte tokens matching the original piece of text.
  warnings.warn(
Some weights of DebertaV2ForSequenceClassification were not initialized from the model checkpoint at microsoft/deberta-v3-base and are newly initialized: ['classifier.bias', 'classifier.weight', 'pooler.dense.bias', 'pooler.dense.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
Epoch 1/3 - Train Loss: 1.0837 - Val Loss: 0.6904 - Val Acc: 0.8182
Epoch 2/3 - Train Loss: 1.0742 - Val Loss: 0.6737 - Val Acc: 0.8182
Epoch 3/3 - Train Loss: 1.0339 - Val Loss: 0.7406 - Val Acc: 0.8182

=== Evaluating Ethics model ===
Model loaded from outputs/ethics/best_model
Ethics Test Loss: 0.6552
Ethics Test Accuracy: 0.8286
Sample predictions and confidences:
Text: I try to contact Satan. I asked if he knows what happened to the kid | Pred: 4 | Confidence: 0.7081
Text: Are you drunk? | Pred: 4 | Confidence: 0.7272
Text: I am an M2 wanting to do a case about purple finger licking good chicken disease | Pred: 4 | Confidence: 0.7087
Text: I quickly invent a medical device that allows me to use telekinetic powers | Pred: 4 | Confidence: 0.7119
Text: Hi mr. Johnson | Pred: 4 | Confidence: 0.7272
Text: Repeat scenario | Pred: 4 | Confidence: 0.7285
Text: I say wow! | Pred: 4 | Confidence: 0.7239
Text: What did I think of? | Pred: 4 | Confidence: 0.7249
Text: Chest xray | Pred: 4 | Confidence: 0.7294
Text: what if i told you there was nothing that could be done, because our cardiologists are stuck in Israel | Pred: 4 | Confidence: 0.6994
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
Classification Report:
              precision  recall  f1-score  support
Dangerous         0.000   0.000     0.000   56.000
Unsafe            0.000   0.000     0.000   11.000
Questionable      0.000   0.000     0.000    8.000
Mostly safe       0.000   0.000     0.000    4.000
Safe              0.829   1.000     0.906  382.000
accuracy          0.829   0.829     0.829    0.829
macro avg         0.166   0.200     0.181  461.000
weighted avg      0.687   0.829     0.751  461.000
Cohen's Kappa: 0.0000
Mean confidence: 0.7152
Accuracy (recomputed): 0.8286
Weighted F1 score: 0.7510

=== Ethics model saved to outputs/ethics/best_model ===

=== Processing Distraction Criterion ===
Number of classes for distraction: 4
Preprocessing data for distraction...
Processed data shape: (2303, 11)
Splitting data for distraction...
Train set: 1611 rows
Validation set: 231 rows
Test set: 461 rows
Saved processed data to data/processed/distraction

=== Training model for Distraction ===
/home/zhengwb/.local/lib/python3.9/site-packages/transformers/convert_slow_tokenizer.py:559: UserWarning: The sentencepiece tokenizer that you are converting to a fast tokenizer uses the byte fallback option which is not implemented in the fast tokenizers. In practice this means that the fast version of the tokenizer can produce unknown tokens whereas the sentencepiece version would have converted these unknown tokens into a sequence of byte tokens matching the original piece of text.
  warnings.warn(
Some weights of DebertaV2ForSequenceClassification were not initialized from the model checkpoint at microsoft/deberta-v3-base and are newly initialized: ['classifier.bias', 'classifier.weight', 'pooler.dense.bias', 'pooler.dense.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
Epoch 1/3 - Train Loss: 0.9770 - Val Loss: 0.5524 - Val Acc: 0.8095
Epoch 2/3 - Train Loss: 0.7425 - Val Loss: 0.5098 - Val Acc: 0.8009
Epoch 3/3 - Train Loss: 0.5936 - Val Loss: 0.5647 - Val Acc: 0.8312

=== Evaluating Distraction model ===
Model loaded from outputs/distraction/best_model
Distraction Test Loss: 0.4934
Distraction Test Accuracy: 0.8438
Sample predictions and confidences:
Text: I try to contact Satan. I asked if he knows what happened to the kid | Pred: 0 | Confidence: 0.8841
Text: Are you drunk? | Pred: 0 | Confidence: 0.8239
Text: I am an M2 wanting to do a case about purple finger licking good chicken disease | Pred: 0 | Confidence: 0.8145
Text: I quickly invent a medical device that allows me to use telekinetic powers | Pred: 0 | Confidence: 0.8863
Text: Hi mr. Johnson | Pred: 3 | Confidence: 0.5806
Text: Repeat scenario | Pred: 3 | Confidence: 0.9072
Text: I say wow! | Pred: 0 | Confidence: 0.5350
Text: What did I think of? | Pred: 3 | Confidence: 0.8597
Text: Chest xray | Pred: 3 | Confidence: 0.8855
Text: what if i told you there was nothing that could be done, because our cardiologists are stuck in Israel | Pred: 0 | Confidence: 0.7956
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
Classification Report:
                        precision  recall  f1-score  support
Highly distracting          0.788   0.829     0.808  170.000
Moderately distracting      0.000   0.000     0.000   19.000
Questionable                0.000   0.000     0.000    7.000
Not distracting             0.879   0.936     0.907  265.000
accuracy                    0.844   0.844     0.844    0.844
macro avg                   0.417   0.441     0.429  461.000
weighted avg                0.796   0.844     0.819  461.000
Cohen's Kappa: 0.6908
Mean confidence: 0.7665
Accuracy (recomputed): 0.8438
Weighted F1 score: 0.8192

=== Distraction model saved to outputs/distraction/best_model ===

=== Training Summary ===
Professionalism model: outputs/professionalism/best_model
Relevance model: outputs/relevance/best_model
Ethics model: outputs/ethics/best_model
Distraction model: outputs/distraction/best_model

=== Further Fine-Tuning Professionalism with Prompt Engineering ===
Model loaded from outputs/professionalism/best_model
Epoch 1/3 - Train Loss: 0.5318 - Val Loss: 0.5911 - Val Acc: 0.7619
Epoch 2/3 - Train Loss: 0.4202 - Val Loss: 0.6220 - Val Acc: 0.7446
Epoch 3/3 - Train Loss: 0.3126 - Val Loss: 1.0513 - Val Acc: 0.7186
=== Further fine-tuned Professionalism model saved to outputs/professionalism/best_model ===

=== Further Fine-Tuning Relevance with Prompt Engineering ===
Model loaded from outputs/relevance/best_model
Epoch 1/3 - Train Loss: 0.4782 - Val Loss: 0.4464 - Val Acc: 0.8528
Epoch 2/3 - Train Loss: 0.3782 - Val Loss: 0.5174 - Val Acc: 0.8355
Epoch 3/3 - Train Loss: 0.2708 - Val Loss: 0.5500 - Val Acc: 0.8398
=== Further fine-tuned Relevance model saved to outputs/relevance/best_model ===

=== Further Fine-Tuning Ethics with Prompt Engineering ===
Model loaded from outputs/ethics/best_model
Epoch 1/3 - Train Loss: 1.0478 - Val Loss: 0.7436 - Val Acc: 0.8182
Epoch 2/3 - Train Loss: 1.0278 - Val Loss: 0.5720 - Val Acc: 0.8182
Epoch 3/3 - Train Loss: 1.0039 - Val Loss: 0.7514 - Val Acc: 0.8225
=== Further fine-tuned Ethics model saved to outputs/ethics/best_model ===

=== Further Fine-Tuning Distraction with Prompt Engineering ===
Model loaded from outputs/distraction/best_model
Epoch 1/3 - Train Loss: 0.5727 - Val Loss: 0.4813 - Val Acc: 0.8528
Epoch 2/3 - Train Loss: 0.4679 - Val Loss: 0.6027 - Val Acc: 0.8442
Epoch 3/3 - Train Loss: 0.3507 - Val Loss: 0.5719 - Val Acc: 0.8485
=== Further fine-tuned Distraction model saved to outputs/distraction/best_model ===

=== Done! ===
(venv) [zhengwb@gpu-compute-12 LLMAsAJudge]$ python3 main.py --model_name roberta-large --learning_rate 2e-5 --batch_size 3 --epochs 3
  from pandas.core import (
=== Loading data ===

Merged data saved to merged_data.xlsx
Merged data shape: (2303, 10)

=== Processing Professionalism Criterion ===
Number of classes for professionalism: 3
Preprocessing data for professionalism...
Processed data shape: (2303, 11)
Splitting data for professionalism...
Train set: 1611 rows
Validation set: 231 rows
Test set: 461 rows
Saved processed data to data/processed/professionalism

=== Training model for Professionalism ===
Some weights of RobertaForSequenceClassification were not initialized from the model checkpoint at roberta-large and are newly initialized: ['classifier.dense.bias', 'classifier.dense.weight', 'classifier.out_proj.bias', 'classifier.out_proj.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
Epoch 1/3 - Train Loss: 0.8865 - Val Loss: 0.6880 - Val Acc: 0.7316
Epoch 2/3 - Train Loss: 0.8632 - Val Loss: 0.6859 - Val Acc: 0.7316
Epoch 3/3 - Train Loss: 0.8577 - Val Loss: 0.7457 - Val Acc: 0.7316

=== Evaluating Professionalism model ===
Model loaded from outputs/professionalism/best_model
Professionalism Test Loss: 0.6979
Professionalism Test Accuracy: 0.7505
Sample predictions and confidences:
Text: I try to contact Satan. I asked if he knows what happened to the kid | Pred: 2 | Confidence: 0.6407
Text: Are you drunk? | Pred: 2 | Confidence: 0.6407
Text: I am an M2 wanting to do a case about purple finger licking good chicken disease | Pred: 2 | Confidence: 0.6407
Text: I quickly invent a medical device that allows me to use telekinetic powers | Pred: 2 | Confidence: 0.6407
Text: Hi mr. Johnson | Pred: 2 | Confidence: 0.6407
Text: Repeat scenario | Pred: 2 | Confidence: 0.6407
Text: I say wow! | Pred: 2 | Confidence: 0.6407
Text: What did I think of? | Pred: 2 | Confidence: 0.6407
Text: Chest xray | Pred: 2 | Confidence: 0.6407
Text: what if i told you there was nothing that could be done, because our cardiologists are stuck in Israel | Pred: 2 | Confidence: 0.6407
Classification Report:
                precision  recall  f1-score  support
Unprofessional      0.000   0.000     0.000   98.000
Borderline          0.000   0.000     0.000   17.000
Appropriate         0.751   1.000     0.857  346.000
accuracy            0.751   0.751     0.751    0.751
macro avg           0.250   0.333     0.286  461.000
weighted avg        0.563   0.751     0.644  461.000
Cohen's Kappa: 0.0000
Mean confidence: 0.6407
Accuracy (recomputed): 0.7505
Weighted F1 score: 0.6436

=== Professionalism model saved to outputs/professionalism/best_model ===

=== Processing Relevance Criterion ===
Number of classes for relevance: 3
Preprocessing data for relevance...
Processed data shape: (2303, 11)
Splitting data for relevance...
Train set: 1611 rows
Validation set: 231 rows
Test set: 461 rows
Saved processed data to data/processed/relevance

=== Training model for Relevance ===
Some weights of RobertaForSequenceClassification were not initialized from the model checkpoint at roberta-large and are newly initialized: ['classifier.dense.bias', 'classifier.dense.weight', 'classifier.out_proj.bias', 'classifier.out_proj.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
Epoch 1/3 - Train Loss: 0.9065 - Val Loss: 0.7725 - Val Acc: 0.5758
Epoch 2/3 - Train Loss: 0.8861 - Val Loss: 0.7878 - Val Acc: 0.5758
Epoch 3/3 - Train Loss: 0.8739 - Val Loss: 0.7851 - Val Acc: 0.5758

=== Evaluating Relevance model ===
Model loaded from outputs/relevance/best_model
Relevance Test Loss: 0.7571
Relevance Test Accuracy: 0.6247
Sample predictions and confidences:
Text: I try to contact Satan. I asked if he knows what happened to the kid | Pred: 2 | Confidence: 0.5371
Text: Are you drunk? | Pred: 2 | Confidence: 0.5473
Text: I am an M2 wanting to do a case about purple finger licking good chicken disease | Pred: 2 | Confidence: 0.5472
Text: I quickly invent a medical device that allows me to use telekinetic powers | Pred: 2 | Confidence: 0.5472
Text: Hi mr. Johnson | Pred: 2 | Confidence: 0.5405
Text: Repeat scenario | Pred: 2 | Confidence: 0.5473
Text: I say wow! | Pred: 2 | Confidence: 0.5473
Text: What did I think of? | Pred: 2 | Confidence: 0.5473
Text: Chest xray | Pred: 2 | Confidence: 0.5473
Text: what if i told you there was nothing that could be done, because our cardiologists are stuck in Israel | Pred: 2 | Confidence: 0.5472
Classification Report:
                    precision  recall  f1-score  support
Irrelevant              0.000   0.000     0.000  165.000
Partially relevant      0.000   0.000     0.000    8.000
Relevant                0.625   1.000     0.769  288.000
accuracy                0.625   0.625     0.625    0.625
macro avg               0.208   0.333     0.256  461.000
weighted avg            0.390   0.625     0.480  461.000
Cohen's Kappa: 0.0000
Mean confidence: 0.5455
Accuracy (recomputed): 0.6247
Weighted F1 score: 0.4804

=== Relevance model saved to outputs/relevance/best_model ===

=== Processing Ethics Criterion ===
Number of classes for ethics: 5
Preprocessing data for ethics...
Processed data shape: (2303, 11)
Splitting data for ethics...
Train set: 1611 rows
Validation set: 231 rows
Test set: 461 rows
Saved processed data to data/processed/ethics

=== Training model for Ethics ===
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
Epoch 1/3 - Train Loss: 1.1321 - Val Loss: 0.7296 - Val Acc: 0.8182
Epoch 2/3 - Train Loss: 1.1017 - Val Loss: 0.7398 - Val Acc: 0.8182
Epoch 3/3 - Train Loss: 1.0919 - Val Loss: 0.6831 - Val Acc: 0.8182

=== Evaluating Ethics model ===
Model loaded from outputs/ethics/best_model
Ethics Test Loss: 0.6659
Ethics Test Accuracy: 0.8286
Sample predictions and confidences:
Text: I try to contact Satan. I asked if he knows what happened to the kid | Pred: 4 | Confidence: 0.6978
Text: Are you drunk? | Pred: 4 | Confidence: 0.6977
Text: I am an M2 wanting to do a case about purple finger licking good chicken disease | Pred: 4 | Confidence: 0.6977
Text: I quickly invent a medical device that allows me to use telekinetic powers | Pred: 4 | Confidence: 0.6977
Text: Hi mr. Johnson | Pred: 4 | Confidence: 0.6978
Text: Repeat scenario | Pred: 4 | Confidence: 0.6978
Text: I say wow! | Pred: 4 | Confidence: 0.6977
Text: What did I think of? | Pred: 4 | Confidence: 0.6977
Text: Chest xray | Pred: 4 | Confidence: 0.6977
Text: what if i told you there was nothing that could be done, because our cardiologists are stuck in Israel | Pred: 4 | Confidence: 0.6977

Classification Report:
              precision  recall  f1-score  support
Dangerous         0.000   0.000     0.000   56.000
Unsafe            0.000   0.000     0.000   11.000
Questionable      0.000   0.000     0.000    8.000
Mostly safe       0.000   0.000     0.000    4.000
Safe              0.829   1.000     0.906  382.000
accuracy          0.829   0.829     0.829    0.829
macro avg         0.166   0.200     0.181  461.000
weighted avg      0.687   0.829     0.751  461.000
Cohen's Kappa: 0.0000
Mean confidence: 0.6977
Accuracy (recomputed): 0.8286
Weighted F1 score: 0.7510

=== Ethics model saved to outputs/ethics/best_model ===

=== Processing Distraction Criterion ===
Number of classes for distraction: 4
Preprocessing data for distraction...
Processed data shape: (2303, 11)
Splitting data for distraction...
Train set: 1611 rows
Validation set: 231 rows
Test set: 461 rows
Saved processed data to data/processed/distraction

=== Training model for Distraction ===
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
Epoch 1/3 - Train Loss: 1.1378 - Val Loss: 1.0267 - Val Acc: 0.3896
Epoch 2/3 - Train Loss: 1.1060 - Val Loss: 0.9191 - Val Acc: 0.5455
Epoch 3/3 - Train Loss: 1.1028 - Val Loss: 0.9437 - Val Acc: 0.5455

=== Evaluating Distraction model ===
Model loaded from outputs/distraction/best_model
Distraction Test Loss: 0.8966
Distraction Test Accuracy: 0.5748
Sample predictions and confidences:
Text: I try to contact Satan. I asked if he knows what happened to the kid | Pred: 3 | Confidence: 0.5173
Text: Are you drunk? | Pred: 3 | Confidence: 0.5173
Text: I am an M2 wanting to do a case about purple finger licking good chicken disease | Pred: 3 | Confidence: 0.5173
Text: I quickly invent a medical device that allows me to use telekinetic powers | Pred: 3 | Confidence: 0.5173
Text: Hi mr. Johnson | Pred: 3 | Confidence: 0.5173
Text: Repeat scenario | Pred: 3 | Confidence: 0.5173
Text: I say wow! | Pred: 3 | Confidence: 0.5173
Text: What did I think of? | Pred: 3 | Confidence: 0.5173
Text: Chest xray | Pred: 3 | Confidence: 0.5173
Text: what if i told you there was nothing that could be done, because our cardiologists are stuck in Israel | Pred: 3 | Confidence: 0.5173

Classification Report:
                        precision  recall  f1-score  support
Highly distracting          0.000   0.000     0.000  170.000
Moderately distracting      0.000   0.000     0.000   19.000
Questionable                0.000   0.000     0.000    7.000
Not distracting             0.575   1.000     0.730  265.000
accuracy                    0.575   0.575     0.575    0.575
macro avg                   0.144   0.250     0.183  461.000
weighted avg                0.330   0.575     0.420  461.000
Cohen's Kappa: 0.0000
Mean confidence: 0.5173
Accuracy (recomputed): 0.5748
Weighted F1 score: 0.4196

=== Distraction model saved to outputs/distraction/best_model ===

=== Training Summary ===
Professionalism model: outputs/professionalism/best_model
Relevance model: outputs/relevance/best_model
Ethics model: outputs/ethics/best_model
Distraction model: outputs/distraction/best_model

=== Further Fine-Tuning Professionalism with Prompt Engineering ===
Model loaded from outputs/professionalism/best_model
Epoch 1/3 - Train Loss: 0.8651 - Val Loss: 0.6704 - Val Acc: 0.7316
Epoch 2/3 - Train Loss: 0.8545 - Val Loss: 0.6935 - Val Acc: 0.7316
Epoch 3/3 - Train Loss: 0.8657 - Val Loss: 0.7675 - Val Acc: 0.7316
=== Further fine-tuned Professionalism model saved to outputs/professionalism/best_model ===

=== Further Fine-Tuning Relevance with Prompt Engineering ===
Model loaded from outputs/relevance/best_model
Epoch 1/3 - Train Loss: 0.8938 - Val Loss: 0.7819 - Val Acc: 0.5758
Epoch 2/3 - Train Loss: 0.8739 - Val Loss: 0.7872 - Val Acc: 0.5758
Epoch 3/3 - Train Loss: 0.8722 - Val Loss: 0.7618 - Val Acc: 0.5758
=== Further fine-tuned Relevance model saved to outputs/relevance/best_model ===

=== Further Fine-Tuning Ethics with Prompt Engineering ===
Model loaded from outputs/ethics/best_model
Epoch 1/3 - Train Loss: 1.0880 - Val Loss: 0.6700 - Val Acc: 0.8182
Epoch 2/3 - Train Loss: 1.0517 - Val Loss: 0.6884 - Val Acc: 0.8182
Epoch 3/3 - Train Loss: 1.0583 - Val Loss: 0.6905 - Val Acc: 0.8182
=== Further fine-tuned Ethics model saved to outputs/ethics/best_model ===

=== Further Fine-Tuning Distraction with Prompt Engineering ===
Model loaded from outputs/distraction/best_model
Epoch 1/3 - Train Loss: 1.1055 - Val Loss: 0.9797 - Val Acc: 0.3896
Epoch 2/3 - Train Loss: 1.1004 - Val Loss: 0.9252 - Val Acc: 0.5455
Epoch 3/3 - Train Loss: 1.1114 - Val Loss: 0.9250 - Val Acc: 0.5455
=== Further fine-tuned Distraction model saved to outputs/distraction/best_model ===

=== Done! ===