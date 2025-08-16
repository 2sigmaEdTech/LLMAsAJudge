# Terminal output

## Environment setup
(venv) [zhengwb@arcc2 LLMAsAJudge]$ module load anaconda
(venv) [zhengwb@arcc2 LLMAsAJudge]$ python3 main.py --criterion distraction
Traceback (most recent call last):
  File "/home/zhengwb/ondemand/LLMAsAJudge/main.py", line 7, in <module>
    from src.models.model import BaseModel
  File "/home/zhengwb/ondemand/LLMAsAJudge/src/models/model.py", line 2, in <module>
    import torch
ModuleNotFoundError: No module named 'torch'
(venv) [zhengwb@arcc2 LLMAsAJudge]$ pip3 install --user -r requirements.txt
Requirement already satisfied: pandas in /opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages (from -r requirements.txt (line 1)) (1.4.2)
Collecting torch
  Using cached torch-2.7.0-cp39-cp39-manylinux_2_28_x86_64.whl (865.2 MB)
Collecting transformers
  Using cached transformers-4.51.3-py3-none-any.whl (10.4 MB)
Requirement already satisfied: scikit-learn in /opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages (from -r requirements.txt (line 4)) (1.0.2)
Requirement already satisfied: matplotlib in /opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages (from -r requirements.txt (line 5)) (3.5.1)
Requirement already satisfied: seaborn in /opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages (from -r requirements.txt (line 6)) (0.11.2)
Requirement already satisfied: openpyxl in /opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages (from -r requirements.txt (line 7)) (3.0.9)
Requirement already satisfied: python-dateutil>=2.8.1 in /opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages (from pandas->-r requirements.txt (line 1)) (2.8.2)
Requirement already satisfied: pytz>=2020.1 in /opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages (from pandas->-r requirements.txt (line 1)) (2021.3)
Requirement already satisfied: numpy>=1.18.5 in /opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages (from pandas->-r requirements.txt (line 1)) (1.21.5)
Collecting nvidia-cusparse-cu12==12.5.4.2
  Using cached nvidia_cusparse_cu12-12.5.4.2-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (216.6 MB)
Collecting nvidia-cuda-cupti-cu12==12.6.80
  Using cached nvidia_cuda_cupti_cu12-12.6.80-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (8.9 MB)
Collecting triton==3.3.0
  Using cached triton-3.3.0-cp39-cp39-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (156.4 MB)
Collecting typing-extensions>=4.10.0
  Using cached typing_extensions-4.13.2-py3-none-any.whl (45 kB)
Collecting sympy>=1.13.3
  Downloading sympy-1.13.3-py3-none-any.whl (6.2 MB)
     |████████████████████████████████| 6.2 MB 17 kB/s 
Collecting nvidia-cuda-runtime-cu12==12.6.77
  Using cached nvidia_cuda_runtime_cu12-12.6.77-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (897 kB)
Collecting nvidia-curand-cu12==10.3.7.77
  Using cached nvidia_curand_cu12-10.3.7.77-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (56.3 MB)
Collecting nvidia-cublas-cu12==12.6.4.1
  Using cached nvidia_cublas_cu12-12.6.4.1-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (393.1 MB)
Collecting nvidia-cudnn-cu12==9.5.1.17
  Downloading nvidia_cudnn_cu12-9.5.1.17-py3-none-manylinux_2_28_x86_64.whl (571.0 MB)
     |████████████████████████████████| 571.0 MB 31 kB/s 
Requirement already satisfied: filelock in /opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages (from torch->-r requirements.txt (line 2)) (3.6.0)
Collecting nvidia-nccl-cu12==2.26.2
  Using cached nvidia_nccl_cu12-2.26.2-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (201.3 MB)
Collecting nvidia-nvtx-cu12==12.6.77
  Using cached nvidia_nvtx_cu12-12.6.77-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (89 kB)
Collecting nvidia-nvjitlink-cu12==12.6.85
  Downloading nvidia_nvjitlink_cu12-12.6.85-py3-none-manylinux2010_x86_64.manylinux_2_12_x86_64.whl (19.7 MB)
     |████████████████████████████████| 19.7 MB 142.6 MB/s 
Collecting nvidia-cuda-nvrtc-cu12==12.6.77
  Using cached nvidia_cuda_nvrtc_cu12-12.6.77-py3-none-manylinux2014_x86_64.whl (23.7 MB)
Requirement already satisfied: fsspec in /opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages (from torch->-r requirements.txt (line 2)) (2022.2.0)
Collecting nvidia-cusparselt-cu12==0.6.3
  Using cached nvidia_cusparselt_cu12-0.6.3-py3-none-manylinux2014_x86_64.whl (156.8 MB)
Collecting nvidia-cufile-cu12==1.11.1.6
  Using cached nvidia_cufile_cu12-1.11.1.6-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (1.1 MB)
Requirement already satisfied: jinja2 in /opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages (from torch->-r requirements.txt (line 2)) (2.11.3)
Collecting nvidia-cusolver-cu12==11.7.1.2
  Using cached nvidia_cusolver_cu12-11.7.1.2-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (158.2 MB)
Requirement already satisfied: networkx in /opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages (from torch->-r requirements.txt (line 2)) (2.7.1)
Collecting nvidia-cufft-cu12==11.3.0.4
  Using cached nvidia_cufft_cu12-11.3.0.4-py3-none-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (200.2 MB)
Requirement already satisfied: setuptools>=40.8.0 in /opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages (from triton==3.3.0->torch->-r requirements.txt (line 2)) (61.2.0)
Requirement already satisfied: regex!=2019.12.17 in /opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages (from transformers->-r requirements.txt (line 3)) (2022.3.15)
Requirement already satisfied: tqdm>=4.27 in /opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages (from transformers->-r requirements.txt (line 3)) (4.64.0)
Requirement already satisfied: requests in /opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages (from transformers->-r requirements.txt (line 3)) (2.27.1)
Collecting huggingface-hub<1.0,>=0.30.0
  Downloading huggingface_hub-0.30.2-py3-none-any.whl (481 kB)
     |████████████████████████████████| 481 kB 133.9 MB/s 
Requirement already satisfied: packaging>=20.0 in /opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages (from transformers->-r requirements.txt (line 3)) (21.3)
Requirement already satisfied: pyyaml>=5.1 in /opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages (from transformers->-r requirements.txt (line 3)) (6.0)
Collecting safetensors>=0.4.3
  Downloading safetensors-0.5.3-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (471 kB)
     |████████████████████████████████| 471 kB 138.4 MB/s 
Collecting tokenizers<0.22,>=0.21
  Downloading tokenizers-0.21.1-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.0 MB)
     |████████████████████████████████| 3.0 MB 70 kB/s 
Requirement already satisfied: threadpoolctl>=2.0.0 in /opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages (from scikit-learn->-r requirements.txt (line 4)) (2.2.0)
Requirement already satisfied: joblib>=0.11 in /opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages (from scikit-learn->-r requirements.txt (line 4)) (1.1.0)
Requirement already satisfied: scipy>=1.1.0 in /opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages (from scikit-learn->-r requirements.txt (line 4)) (1.7.3)
Requirement already satisfied: cycler>=0.10 in /opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages (from matplotlib->-r requirements.txt (line 5)) (0.11.0)
Requirement already satisfied: kiwisolver>=1.0.1 in /opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages (from matplotlib->-r requirements.txt (line 5)) (1.3.2)
Requirement already satisfied: fonttools>=4.22.0 in /opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages (from matplotlib->-r requirements.txt (line 5)) (4.25.0)
Requirement already satisfied: pillow>=6.2.0 in /opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages (from matplotlib->-r requirements.txt (line 5)) (9.0.1)
Requirement already satisfied: pyparsing>=2.2.1 in /opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages (from matplotlib->-r requirements.txt (line 5)) (3.0.4)
Requirement already satisfied: et-xmlfile in /opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages (from openpyxl->-r requirements.txt (line 7)) (1.1.0)
Collecting fsspec
  Downloading fsspec-2025.3.2-py3-none-any.whl (194 kB)
     |████████████████████████████████| 194 kB 142.3 MB/s 
Requirement already satisfied: six>=1.5 in /opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages (from python-dateutil>=2.8.1->pandas->-r requirements.txt (line 1)) (1.16.0)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in /opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages (from sympy>=1.13.3->torch->-r requirements.txt (line 2)) (1.2.1)
Requirement already satisfied: MarkupSafe>=0.23 in /opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages (from jinja2->torch->-r requirements.txt (line 2)) (2.0.1)
Requirement already satisfied: certifi>=2017.4.17 in /opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages (from requests->transformers->-r requirements.txt (line 3)) (2021.10.8)
Requirement already satisfied: charset-normalizer~=2.0.0 in /opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages (from requests->transformers->-r requirements.txt (line 3)) (2.0.4)
Requirement already satisfied: idna<4,>=2.5 in /opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages (from requests->transformers->-r requirements.txt (line 3)) (3.3)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages (from requests->transformers->-r requirements.txt (line 3)) (1.26.9)
Installing collected packages: typing-extensions, nvidia-nvjitlink-cu12, fsspec, nvidia-cusparse-cu12, nvidia-cublas-cu12, huggingface-hub, triton, tokenizers, sympy, safetensors, nvidia-nvtx-cu12, nvidia-nccl-cu12, nvidia-cusparselt-cu12, nvidia-cusolver-cu12, nvidia-curand-cu12, nvidia-cufile-cu12, nvidia-cufft-cu12, nvidia-cudnn-cu12, nvidia-cuda-runtime-cu12, nvidia-cuda-nvrtc-cu12, nvidia-cuda-cupti-cu12, transformers, torch
Successfully installed fsspec-2025.3.2 huggingface-hub-0.30.2 nvidia-cublas-cu12-12.6.4.1 nvidia-cuda-cupti-cu12-12.6.80 nvidia-cuda-nvrtc-cu12-12.6.77 nvidia-cuda-runtime-cu12-12.6.77 nvidia-cudnn-cu12-9.5.1.17 nvidia-cufft-cu12-11.3.0.4 nvidia-cufile-cu12-1.11.1.6 nvidia-curand-cu12-10.3.7.77 nvidia-cusolver-cu12-11.7.1.2 nvidia-cusparse-cu12-12.5.4.2 nvidia-cusparselt-cu12-0.6.3 nvidia-nccl-cu12-2.26.2 nvidia-nvjitlink-cu12-12.6.85 nvidia-nvtx-cu12-12.6.77 safetensors-0.5.3 sympy-1.13.3 tokenizers-0.21.1 torch-2.7.0 transformers-4.51.3 triton-3.3.0 typing-extensions-4.13.2

## Test the training with distraction
(venv) [zhengwb@arcc2 LLMAsAJudge]$ python3 main.py --criterion distraction
=== Loading data ===
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/openpyxl/worksheet/_reader.py:312: UserWarning: Data Validation extension is not supported and will be removed
  warn(msg)
Loaded fuzzy.coding.dataDW.xlsx: 2302 rows, 10 columns
Merged data shape: (2302, 11)

=== Processing Distraction Criterion ===
Number of classes for distraction: 4
Preprocessing data for distraction...
Processed data shape: (2302, 12)
Splitting data for distraction...
Train set: 1610 rows
Validation set: 231 rows
Test set: 461 rows
Saved processed data to data/processed/distraction

=== Training model for Distraction ===
tokenizer_config.json: 100%|██████████████████████████████████████████████████████████████████████████| 48.0/48.0 [00:00<00:00, 14.7kB/s]
config.json: 100%|███████████████████████████████████████████████████████████████████████████████████████| 570/570 [00:00<00:00, 221kB/s]
vocab.txt: 100%|██████████████████████████████████████████████████████████████████████████████████████| 232k/232k [00:00<00:00, 23.4MB/s]
tokenizer.json: 100%|█████████████████████████████████████████████████████████████████████████████████| 466k/466k [00:00<00:00, 37.2MB/s]
Xet Storage is enabled for this repo, but the 'hf_xet' package is not installed. Falling back to regular HTTP download. For better performance, install the package with: `pip install huggingface_hub[hf_xet]` or `pip install hf_xet`
model.safetensors: 100%|███████████████████████████████████████████████████████████████████████████████| 440M/440M [00:01<00:00, 440MB/s]
Some weights of BertForSequenceClassification were not initialized from the model checkpoint at bert-base-uncased and are newly initialized: ['classifier.bias', 'classifier.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
Epoch 1/3 - Train Loss: 0.9500 - Val Loss: 0.8003 - Val Acc: 0.7100
Epoch 2/3 - Train Loss: 0.6502 - Val Loss: 0.7494 - Val Acc: 0.7229
Epoch 3/3 - Train Loss: 0.4845 - Val Loss: 0.8046 - Val Acc: 0.7359

=== Evaluating Distraction model ===
Model loaded from outputs/distraction/best_model
Distraction Test Loss: 0.7033
Distraction Test Accuracy: 0.7484
Classification Report:
                        precision  recall  f1-score  support
Highly distracting          0.632   0.914     0.747  152.000
Moderately distracting      0.667   0.063     0.116   63.000
Questionable                1.000   0.121     0.216   33.000
Not distracting             0.857   0.930     0.892  213.000
accuracy                    0.748   0.748     0.748    0.748
macro avg                   0.789   0.507     0.493  461.000
weighted avg                0.767   0.748     0.690  461.000

=== Distraction model saved to outputs/distraction/best_model ===

=== Training Summary ===
Distraction model: outputs/distraction/best_model

=== Done! ===

## Fine-tunning all criteria
(venv) [zhengwb@arcc2 LLMAsAJudge]$ python3 main.py
=== Loading data ===
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/openpyxl/worksheet/_reader.py:312: UserWarning: Data Validation extension is not supported and will be removed
  warn(msg)
Loaded fuzzy.coding.dataDW.xlsx: 2302 rows, 10 columns
Merged data shape: (2302, 11)

=== Processing Professionalism Criterion ===
Number of classes for professionalism: 3
Preprocessing data for professionalism...
Processed data shape: (2302, 12)
Splitting data for professionalism...
Train set: 1610 rows
Validation set: 231 rows
Test set: 461 rows
Saved processed data to data/processed/professionalism

=== Training model for Professionalism ===
Some weights of BertForSequenceClassification were not initialized from the model checkpoint at bert-base-uncased and are newly initialized: ['classifier.bias', 'classifier.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
Epoch 1/3 - Train Loss: 0.6929 - Val Loss: 0.5452 - Val Acc: 0.8095
Epoch 2/3 - Train Loss: 0.5403 - Val Loss: 0.5384 - Val Acc: 0.7706
Epoch 3/3 - Train Loss: 0.3663 - Val Loss: 0.5405 - Val Acc: 0.8312

=== Evaluating Professionalism model ===
Model loaded from outputs/professionalism/best_model
Professionalism Test Loss: 0.5083
Professionalism Test Accuracy: 0.7918
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
Classification Report:
                precision  recall  f1-score  support
Unprofessional      0.466   0.621     0.532   66.000
Borderline          0.000   0.000     0.000   39.000
Appropriate         0.869   0.910     0.889  356.000
accuracy            0.792   0.792     0.792    0.792
macro avg           0.445   0.510     0.474  461.000
weighted avg        0.737   0.792     0.763  461.000

=== Professionalism model saved to outputs/professionalism/best_model ===

=== Processing Relevance Criterion ===
Number of classes for relevance: 3
Preprocessing data for relevance...
Processed data shape: (2302, 12)
Splitting data for relevance...
Train set: 1610 rows
Validation set: 231 rows
Test set: 461 rows
Saved processed data to data/processed/relevance

=== Training model for Relevance ===
Some weights of BertForSequenceClassification were not initialized from the model checkpoint at bert-base-uncased and are newly initialized: ['classifier.bias', 'classifier.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
Epoch 1/3 - Train Loss: 0.7522 - Val Loss: 0.5778 - Val Acc: 0.7835
Epoch 2/3 - Train Loss: 0.4664 - Val Loss: 0.6266 - Val Acc: 0.7749
Epoch 3/3 - Train Loss: 0.2826 - Val Loss: 0.7015 - Val Acc: 0.8052

=== Evaluating Relevance model ===
Model loaded from outputs/relevance/best_model
Relevance Test Loss: 0.6076
Relevance Test Accuracy: 0.7549
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
Classification Report:
                    precision  recall  f1-score  support
Irrelevant              0.662   0.874     0.754  175.000
Partially relevant      0.000   0.000     0.000   66.000
Relevant                0.848   0.886     0.867  220.000
accuracy                0.755   0.755     0.755    0.755
macro avg               0.503   0.587     0.540  461.000
weighted avg            0.656   0.755     0.700  461.000

=== Relevance model saved to outputs/relevance/best_model ===

=== Processing Ethics Criterion ===
Number of classes for ethics: 5
Preprocessing data for ethics...
Processed data shape: (2302, 12)
Splitting data for ethics...
Train set: 1610 rows
Validation set: 231 rows
Test set: 461 rows
Saved processed data to data/processed/ethics

=== Training model for Ethics ===
Some weights of BertForSequenceClassification were not initialized from the model checkpoint at bert-base-uncased and are newly initialized: ['classifier.bias', 'classifier.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
Epoch 1/3 - Train Loss: 0.7642 - Val Loss: 0.5841 - Val Acc: 0.8398
Epoch 2/3 - Train Loss: 0.5812 - Val Loss: 0.5997 - Val Acc: 0.8182
Epoch 3/3 - Train Loss: 0.3778 - Val Loss: 0.5747 - Val Acc: 0.8312

=== Evaluating Ethics model ===
Model loaded from outputs/ethics/best_model
Ethics Test Loss: 0.5607
Ethics Test Accuracy: 0.8351
Classification Report:
              precision  recall  f1-score  support
Dangerous         0.400   0.429     0.414   14.000
Unsafe            0.429   0.125     0.194   24.000
Questionable      0.318   0.241     0.275   29.000
Mostly safe       0.800   0.235     0.364   17.000
Safe              0.886   0.968     0.925  377.000
accuracy          0.835   0.835     0.835    0.835
macro avg         0.567   0.400     0.434  461.000
weighted avg      0.808   0.835     0.810  461.000

=== Ethics model saved to outputs/ethics/best_model ===

=== Processing Distraction Criterion ===
Number of classes for distraction: 4
Preprocessing data for distraction...
Processed data shape: (2302, 12)
Splitting data for distraction...
Train set: 1610 rows
Validation set: 231 rows
Test set: 461 rows
Saved processed data to data/processed/distraction

=== Training model for Distraction ===
Some weights of BertForSequenceClassification were not initialized from the model checkpoint at bert-base-uncased and are newly initialized: ['classifier.bias', 'classifier.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
Epoch 1/3 - Train Loss: 1.0116 - Val Loss: 0.8276 - Val Acc: 0.7013
Epoch 2/3 - Train Loss: 0.7163 - Val Loss: 0.7202 - Val Acc: 0.7403
Epoch 3/3 - Train Loss: 0.4954 - Val Loss: 0.7127 - Val Acc: 0.7792

=== Evaluating Distraction model ===
Model loaded from outputs/distraction/best_model
Distraction Test Loss: 0.7072
Distraction Test Accuracy: 0.7614
Classification Report:
                        precision  recall  f1-score  support
Highly distracting          0.756   0.816     0.785  152.000
Moderately distracting      0.490   0.397     0.439   63.000
Questionable                0.500   0.091     0.154   33.000
Not distracting             0.829   0.934     0.879  213.000
accuracy                    0.761   0.761     0.761    0.761
macro avg                   0.644   0.559     0.564  461.000
weighted avg                0.735   0.761     0.736  461.000

=== Distraction model saved to outputs/distraction/best_model ===

=== Training Summary ===
Professionalism model: outputs/professionalism/best_model
Relevance model: outputs/relevance/best_model
Ethics model: outputs/ethics/best_model
Distraction model: outputs/distraction/best_model

=== Done! ===
## after updates the labels and models
(venv) [zhengwb@arcc2 LLMAsAJudge]$ python3 main.py
=== Loading data ===
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/openpyxl/worksheet/_reader.py:312: UserWarning: Data Validation extension is not supported and will be removed
  warn(msg)
Loaded fuzzy.coding.dataDW.xlsx: 2302 rows, 10 columns
Merged data shape: (2302, 11)

### === Processing Professionalism Criterion ===
Number of classes for professionalism: 3
Preprocessing data for professionalism...
Processed data shape: (2302, 12)
Splitting data for professionalism...
Train set: 1610 rows
Validation set: 231 rows
Test set: 461 rows
Saved processed data to data/processed/professionalism

=== Training model for Professionalism ===
Some weights of BertForSequenceClassification were not initialized from the model checkpoint at bert-base-uncased and are newly initialized: ['classifier.bias', 'classifier.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
Epoch 1/3 - Train Loss: 0.9959 - Val Loss: 0.8035 - Val Acc: 0.6710
Epoch 2/3 - Train Loss: 0.7535 - Val Loss: 0.8184 - Val Acc: 0.5801
Epoch 3/3 - Train Loss: 0.4844 - Val Loss: 0.6341 - Val Acc: 0.7749

=== Evaluating Professionalism model ===
Model loaded from outputs/professionalism/best_model
Professionalism Test Loss: 0.5433
Professionalism Test Accuracy: 0.8156
Classification Report:
                precision  recall  f1-score  support
Unprofessional      0.583   0.636     0.609   66.000
Borderline          0.364   0.205     0.262   39.000
Appropriate         0.888   0.916     0.902  356.000
accuracy            0.816   0.816     0.816    0.816
macro avg           0.612   0.586     0.591  461.000
weighted avg        0.800   0.816     0.806  461.000

=== Professionalism model saved to outputs/professionalism/best_model ===

### === Processing Relevance Criterion ===
Number of classes for relevance: 3
Preprocessing data for relevance...
Processed data shape: (2302, 12)
Splitting data for relevance...
Train set: 1610 rows
Validation set: 231 rows
Test set: 461 rows
Saved processed data to data/processed/relevance

=== Training model for Relevance ===
Some weights of BertForSequenceClassification were not initialized from the model checkpoint at bert-base-uncased and are newly initialized: ['classifier.bias', 'classifier.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
Epoch 1/3 - Train Loss: 0.9013 - Val Loss: 0.7703 - Val Acc: 0.7056
Epoch 2/3 - Train Loss: 0.6472 - Val Loss: 0.6119 - Val Acc: 0.7532
Epoch 3/3 - Train Loss: 0.4127 - Val Loss: 0.7824 - Val Acc: 0.7186

=== Evaluating Relevance model ===
Model loaded from outputs/relevance/best_model
Relevance Test Loss: 0.6482
Relevance Test Accuracy: 0.7289
Classification Report:
                    precision  recall  f1-score  support
Irrelevant              0.824   0.669     0.738  175.000
Partially relevant      0.357   0.621     0.453   66.000
Relevant                0.873   0.809     0.840  220.000
accuracy                0.729   0.729     0.729    0.729
macro avg               0.684   0.700     0.677  461.000
weighted avg            0.780   0.729     0.746  461.000

=== Relevance model saved to outputs/relevance/best_model ===

### === Processing Ethics Criterion ===
Number of classes for ethics: 5
Preprocessing data for ethics...
Processed data shape: (2302, 12)
Splitting data for ethics...
Train set: 1610 rows
Validation set: 231 rows
Test set: 461 rows
Saved processed data to data/processed/ethics

=== Training model for Ethics ===
Some weights of BertForSequenceClassification were not initialized from the model checkpoint at bert-base-uncased and are newly initialized: ['classifier.bias', 'classifier.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
Epoch 1/3 - Train Loss: 1.5397 - Val Loss: 0.9403 - Val Acc: 0.8398
Epoch 2/3 - Train Loss: 1.3818 - Val Loss: 1.1723 - Val Acc: 0.6104
Epoch 3/3 - Train Loss: 1.1137 - Val Loss: 0.9387 - Val Acc: 0.7100

=== Evaluating Ethics model ===
Model loaded from outputs/ethics/best_model
Ethics Test Loss: 0.8478
Ethics Test Accuracy: 0.7158
Classification Report:
              precision  recall  f1-score  support
Dangerous         0.158   0.429     0.231   14.000
Unsafe            0.125   0.375     0.188   24.000
Questionable      0.083   0.034     0.049   29.000
Mostly safe       0.385   0.294     0.333   17.000
Safe              0.948   0.820     0.879  377.000
accuracy          0.716   0.716     0.716    0.716
macro avg         0.340   0.390     0.336  461.000
weighted avg      0.806   0.716     0.751  461.000

=== Ethics model saved to outputs/ethics/best_model ===

### === Processing Distraction Criterion ===
Number of classes for distraction: 4
Preprocessing data for distraction...
Processed data shape: (2302, 12)
Splitting data for distraction...
Train set: 1610 rows
Validation set: 231 rows
Test set: 461 rows
Saved processed data to data/processed/distraction

=== Training model for Distraction ===
Some weights of BertForSequenceClassification were not initialized from the model checkpoint at bert-base-uncased and are newly initialized: ['classifier.bias', 'classifier.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
Epoch 1/3 - Train Loss: 1.2075 - Val Loss: 0.9490 - Val Acc: 0.7013
Epoch 2/3 - Train Loss: 0.9453 - Val Loss: 0.8601 - Val Acc: 0.6580
Epoch 3/3 - Train Loss: 0.6834 - Val Loss: 0.7996 - Val Acc: 0.7273

=== Evaluating Distraction model ===
Model loaded from outputs/distraction/best_model
Distraction Test Loss: 0.7610
Distraction Test Accuracy: 0.7115
Classification Report:
                        precision  recall  f1-score  support
Highly distracting          0.772   0.691     0.729  152.000
Moderately distracting      0.326   0.444     0.376   63.000
Questionable                0.375   0.455     0.411   33.000
Not distracting             0.905   0.845     0.874  213.000
accuracy                    0.711   0.711     0.711    0.711
macro avg                   0.594   0.609     0.597  461.000
weighted avg                0.744   0.711     0.725  461.000

=== Distraction model saved to outputs/distraction/best_model ===

=== Training Summary ===
Professionalism model: outputs/professionalism/best_model
Relevance model: outputs/relevance/best_model
Ethics model: outputs/ethics/best_model
Distraction model: outputs/distraction/best_model

=== Done! ===

## new learning rate and batch size and epochs
(venv) [zhengwb@arcc2 LLMAsAJudge]$ python3 main.py --criterion professionalism --learning_rate 2e-5 --batch_size 8 --epochs 3
=== Loading data ===
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/openpyxl/worksheet/_reader.py:312: UserWarning: Data Validation extension is not supported and will be removed
  warn(msg)
Loaded fuzzy.coding.dataDW.xlsx: 2302 rows, 10 columns
Merged data shape: (2302, 11)

=== Processing Professionalism Criterion ===
Number of classes for professionalism: 3
Preprocessing data for professionalism...
Processed data shape: (2302, 12)
Splitting data for professionalism...
Train set: 1610 rows
Validation set: 231 rows
Test set: 461 rows
Saved processed data to data/processed/professionalism

=== Training model for Professionalism ===
Some weights of BertForSequenceClassification were not initialized from the model checkpoint at bert-base-uncased and are newly initialized: ['classifier.bias', 'classifier.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
Epoch 1/3 - Train Loss: 1.0356 - Val Loss: 0.7510 - Val Acc: 0.7403
Epoch 2/3 - Train Loss: 0.8193 - Val Loss: 0.6821 - Val Acc: 0.6926
Epoch 3/3 - Train Loss: 0.5557 - Val Loss: 0.5965 - Val Acc: 0.7619

=== Evaluating Professionalism model ===
Model loaded from outputs/professionalism/best_model
Professionalism Test Loss: 0.5091
Professionalism Test Accuracy: 0.8221
Classification Report:
                precision  recall  f1-score  support
Unprofessional      0.582   0.803     0.675   66.000
Borderline          0.316   0.154     0.207   39.000
Appropriate         0.912   0.899     0.905  356.000
accuracy            0.822   0.822     0.822    0.822
macro avg           0.603   0.619     0.596  461.000
weighted avg        0.814   0.822     0.813  461.000

=== Professionalism model saved to outputs/professionalism/best_model ===

=== Training Summary ===
Professionalism model: outputs/professionalism/best_model

=== Done! ===

## New model emilyalsentzer/Bio_ClinicalBERT
 python3 main.py --criterion professionalism --model_name emilyalsentzer/Bio_ClinicalBERT --learning_rate 2e-5 --batch_siz
e 8 --epochs 3
=== Loading data ===
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/openpyxl/worksheet/_reader.py:312: UserWarning: Data Validation extension is not supported and will be removed
  warn(msg)
Loaded fuzzy.coding.dataDW.xlsx: 2302 rows, 10 columns
Merged data shape: (2302, 11)

=== Processing Professionalism Criterion ===
Number of classes for professionalism: 3
Preprocessing data for professionalism...
Processed data shape: (2302, 12)
Splitting data for professionalism...
Train set: 1610 rows
Validation set: 231 rows
Test set: 461 rows
Saved processed data to data/processed/professionalism

=== Training model for Professionalism ===
config.json: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████| 385/385 [00:00<00:00, 149kB/s]
vocab.txt: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████| 213k/213k [00:00<00:00, 23.5MB/s]
pytorch_model.bin: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████| 436M/436M [00:02<00:00, 148MB/s]
Some weights of BertForSequenceClassification were not initialized from the model checkpoint at emilyalsentzer/Bio_ClinicalBERT and are newly initialized: ['classifier.bias', 'classifier.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
model.safetensors: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████| 436M/436M [00:02<00:00, 194MB/s]
Epoch 1/3 - Train Loss: 1.0360 - Val Loss: 0.6551 - Val Acc: 0.7662
Epoch 2/3 - Train Loss: 0.8879 - Val Loss: 0.6614 - Val Acc: 0.7316
Epoch 3/3 - Train Loss: 0.6717 - Val Loss: 0.6855 - Val Acc: 0.6970

=== Evaluating Professionalism model ===
Model loaded from outputs/professionalism/best_model
Professionalism Test Loss: 0.6464
Professionalism Test Accuracy: 0.7744
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
Classification Report:
                precision  recall  f1-score  support
Unprofessional      0.388   0.288     0.330   66.000
Borderline          0.000   0.000     0.000   39.000
Appropriate         0.820   0.949     0.880  356.000
accuracy            0.774   0.774     0.774    0.774
macro avg           0.403   0.412     0.404  461.000
weighted avg        0.689   0.774     0.727  461.000

=== Professionalism model saved to outputs/professionalism/best_model ===

=== Training Summary ===
Professionalism model: outputs/professionalism/best_model

## New model: microsoft/deberta-v3-base

python3 main.py --criterion professionalism --model_name microsoft/deberta-v3-base --learning_rate 2e-5 --batch_size 8 --epochs 3
=== Loading data ===
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/openpyxl/worksheet/_reader.py:312: UserWarning: Data Validation extension is not supported and will be removed
  warn(msg)
Loaded fuzzy.coding.dataDW.xlsx: 2302 rows, 10 columns
Merged data shape: (2302, 11)

=== Processing Professionalism Criterion ===
Number of classes for professionalism: 3
Preprocessing data for professionalism...
Processed data shape: (2302, 12)
Splitting data for professionalism...
Train set: 1610 rows
Validation set: 231 rows
Test set: 461 rows
Saved processed data to data/processed/professionalism

=== Training model for Professionalism ===
/home/zhengwb/.local/lib/python3.9/site-packages/transformers/convert_slow_tokenizer.py:559: UserWarning: The sentencepiece tokenizer that you are converting to a fast tokenizer uses the byte fallback option which is not implemented in the fast tokenizers. In practice this means that the fast version of the tokenizer can produce unknown tokens whereas the sentencepiece version would have converted these unknown tokens into a sequence of byte tokens matching the original piece of text.
  warnings.warn(
pytorch_model.bin: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████| 371M/371M [00:01<00:00, 268MB/s]
model.safetensors:  48%|███████████████████████████████████████████████▌                                                   | 178M/371M [00:00<00:00, 392MB/s]Some weights of DebertaV2ForSequenceClassification were not initialized from the model checkpoint at microsoft/deberta-v3-base and are newly initialized: ['classifier.bias', 'classifier.weight', 'pooler.dense.bias', 'pooler.dense.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
model.safetensors: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████| 371M/371M [00:01<00:00, 360MB/s]
Epoch 1/3 - Train Loss: 1.0390 - Val Loss: 0.8240 - Val Acc: 0.6797
Epoch 2/3 - Train Loss: 0.8721 - Val Loss: 1.1030 - Val Acc: 0.5844
Epoch 3/3 - Train Loss: 0.6441 - Val Loss: 0.6320 - Val Acc: 0.7706

=== Evaluating Professionalism model ===
Model loaded from outputs/professionalism/best_model
Professionalism Test Loss: 0.5276
Professionalism Test Accuracy: 0.8004
Classification Report:
                precision  recall  f1-score  support
Unprofessional      0.512   0.667     0.579     66.0
Borderline          0.364   0.308     0.333     39.0
Appropriate         0.915   0.879     0.897    356.0
accuracy            0.800   0.800     0.800      0.8
macro avg           0.597   0.618     0.603    461.0
weighted avg        0.811   0.800     0.804    461.0

=== Professionalism model saved to outputs/professionalism/best_model ===

=== Training Summary ===
Professionalism model: outputs/professionalism/best_model

=== Done! ===

## new try:
(venv) [zhengwb@arcc2 LLMAsAJudge]$ module load anaconda
(venv) [zhengwb@arcc2 LLMAsAJudge]$ python3 main.py --criterion professionalism --model_name meta-llama/Meta-Llama-3.1-8B-Instruct --learning_rate 2e-5 --batch_size 8 --epochs 3
=== Loading data ===
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/openpyxl/worksheet/_reader.py:312: UserWarning: Data Validation extension is not supported and will be removed
  warn(msg)
Loaded fuzzy.coding.dataDW.xlsx: 2302 rows, 10 columns
Merged data shape: (2302, 11)

=== Processing Professionalism Criterion ===
Number of classes for professionalism: 3
Preprocessing data for professionalism...
Processed data shape: (2302, 12)
Splitting data for professionalism...
Train set: 1610 rows
Validation set: 231 rows
Test set: 461 rows
Saved processed data to data/processed/professionalism

=== Training model for Professionalism ===
Loading checkpoint shards: 100%|██████████████████████████████████████████████████████████████████| 4/4 [00:21<00:00,  5.31s/it]
Some weights of LlamaForSequenceClassification were not initialized from the model checkpoint at meta-llama/Meta-Llama-3.1-8B-Instruct and are newly initialized: ['score.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
Epoch 1/3 - Train Loss: 1.6333 - Val Loss: 0.7033 - Val Acc: 0.7056
Epoch 2/3 - Train Loss: 0.9604 - Val Loss: 0.5972 - Val Acc: 0.7835
Terminated

## GPU 
(venv) [zhengwb@arcc2 LLMAsAJudge]$ srun -p gpu-h100 -n 12 -N 1 --gpus=1 -t 4:00:00 --pty /bin/bash
(venv) [zhengwb@gpu-compute-12 LLMAsAJudge]$ python3 main.py --criterion professionalism --model_name meta-llama/Meta-Llama-3.1-8B-Instruct --learning_rate 2e-5 --batch_size 8 --epochs 3
Traceback (most recent call last):
  File "/home/zhengwb/ondemand/LLMAsAJudge/main.py", line 3, in <module>
    import pandas as pd
ModuleNotFoundError: No module named 'pandas'
(venv) [zhengwb@gpu-compute-12 LLMAsAJudge]$ module load anaconda
(venv) [zhengwb@gpu-compute-12 LLMAsAJudge]$ python3 main.py --criterion professionalism --model_name meta-llama/Meta-Llama-3.1-8B-Instruct --learning_rate 2e-5 --batch_size 8 --epochs 3

(venv) [zhengwb@gpu-compute-12 LLMAsAJudge]$ squeue -u $USER
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
           2842098  gpu-h100     bash  zhengwb  R    1:09:02      1 gpu-compute-12
           2842099    public     bash  zhengwb  R      45:54      1 compute-03
(venv) [zhengwb@gpu-compute-12 LLMAsAJudge]$ scancel 2842098
srun: Job step aborted: Waiting up to 32 seconds for job step to finish.
(venv) [zhengwb@gpu-compute-12 LLMAsAJudge]$ slurmstepd: error: *** STEP 2842098.0 ON gpu-compute-12 CANCELLED AT 2025-04-28T19:18:10 ***
exit

## Qwen/Qwen3-8B
(venv) [zhengwb@gpu-compute-12 LLMAsAJudge]$ module load anaconda
(venv) [zhengwb@gpu-compute-12 LLMAsAJudge]$ python3 main.py --criterion professionalism --model_name Qwen/Qwen3-8B --learning_rate 2e-5 --batch_size 2 --epochs 3

(venv) [zhengwb@gpu-compute-12 LLMAsAJudge]$ nvidia-smi
Mon Apr 28 22:46:00 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 560.35.03              Driver Version: 560.35.03      CUDA Version: 12.6     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA H100 80GB HBM3          Off |   00000001:1B:00.0 Off |                    0 |
| N/A   37C    P0             73W /  700W |       1MiB /  81559MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+

## Qwen/Qwen3-4B
(venv) [zhengwb@gpu-compute-12 LLMAsAJudge]$ python3 main.py --criterion professionalism --model_name Qwen/Qwen3-4B --learning_rate 2e-5 --batch_size 1 --epochs 3
=== Loading data ===
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/openpyxl/worksheet/_reader.py:312: UserWarning: Data Validation extension is not supported and will be removed
  warn(msg)
Loaded fuzzy.coding.dataDW.xlsx: 2302 rows, 10 columns
Merged data shape: (2302, 11)

=== Processing Professionalism Criterion ===
Number of classes for professionalism: 3
Preprocessing data for professionalism...
Processed data shape: (2302, 12)
Splitting data for professionalism...
Train set: 1610 rows
Validation set: 231 rows
Test set: 461 rows
Saved processed data to data/processed/professionalism

=== Training model for Professionalism ===
tokenizer_config.json: 100%|████████████████████████████████████████████████| 9.68k/9.68k [00:00<00:00, 3.20MB/s]
vocab.json: 100%|███████████████████████████████████████████████████████████| 2.78M/2.78M [00:00<00:00, 32.7MB/s]
merges.txt: 100%|███████████████████████████████████████████████████████████| 1.67M/1.67M [00:00<00:00, 7.66MB/s]
tokenizer.json: 100%|████████████████████████████████████████████████████████| 11.4M/11.4M [00:00<00:00, 102MB/s]
config.json: 100%|███████████████████████████████████████████████████████████████| 726/726 [00:00<00:00, 711kB/s]
model.safetensors.index.json: 100%|█████████████████████████████████████████| 32.8k/32.8k [00:00<00:00, 31.6MB/s]
model-00003-of-00003.safetensors: 100%|█████████████████████████████████████| 99.6M/99.6M [00:02<00:00, 40.1MB/s]
model-00001-of-00003.safetensors: 100%|█████████████████████████████████████| 3.96G/3.96G [01:08<00:00, 57.4MB/s]
model-00002-of-00003.safetensors: 100%|█████████████████████████████████████| 3.99G/3.99G [01:10<00:00, 56.7MB/s]
Fetching 3 files: 100%|████████████████████████████████████████████████████████████| 3/3 [01:10<00:00, 23.56s/it]
Loading checkpoint shards: 100%|███████████████████████████████████████████████████| 3/3 [00:13<00:00,  4.41s/it]
Some weights of Qwen3ForSequenceClassification were not initialized from the model checkpoint at Qwen/Qwen3-4B and are newly initialized: ['score.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.

(venv) [zhengwb@gpu-compute-12 LLMAsAJudge]$ python3 main.py --criterion professionalism --model_name Qwen/Qwen3-4B --learning_rate 2e-5 --batch_size 1 --epochs 3
=== Loading data ===
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/openpyxl/worksheet/_reader.py:312: UserWarning: Data Validation extension is not supported and will be removed
  warn(msg)
Loaded fuzzy.coding.dataDW.xlsx: 2302 rows, 10 columns
Merged data shape: (2302, 11)

=== Processing Professionalism Criterion ===
Number of classes for professionalism: 3
Preprocessing data for professionalism...
Processed data shape: (2302, 12)
Splitting data for professionalism...
Train set: 1610 rows
Validation set: 231 rows
Test set: 461 rows
Saved processed data to data/processed/professionalism

=== Training model for Professionalism ===
tokenizer_config.json: 100%|████████████████████████████████████████████████| 9.68k/9.68k [00:00<00:00, 3.20MB/s]
vocab.json: 100%|███████████████████████████████████████████████████████████| 2.78M/2.78M [00:00<00:00, 32.7MB/s]
merges.txt: 100%|███████████████████████████████████████████████████████████| 1.67M/1.67M [00:00<00:00, 7.66MB/s]
tokenizer.json: 100%|████████████████████████████████████████████████████████| 11.4M/11.4M [00:00<00:00, 102MB/s]
config.json: 100%|███████████████████████████████████████████████████████████████| 726/726 [00:00<00:00, 711kB/s]
model.safetensors.index.json: 100%|█████████████████████████████████████████| 32.8k/32.8k [00:00<00:00, 31.6MB/s]
model-00003-of-00003.safetensors: 100%|█████████████████████████████████████| 99.6M/99.6M [00:02<00:00, 40.1MB/s]
model-00001-of-00003.safetensors: 100%|█████████████████████████████████████| 3.96G/3.96G [01:08<00:00, 57.4MB/s]
model-00002-of-00003.safetensors: 100%|█████████████████████████████████████| 3.99G/3.99G [01:10<00:00, 56.7MB/s]
Fetching 3 files: 100%|████████████████████████████████████████████████████████████| 3/3 [01:10<00:00, 23.56s/it]
Loading checkpoint shards: 100%|███████████████████████████████████████████████████| 3/3 [00:13<00:00,  4.41s/it]
Some weights of Qwen3ForSequenceClassification were not initialized from the model checkpoint at Qwen/Qwen3-4B and are newly initialized: ['score.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
Epoch 1/3 - Train Loss: 0.8048 - Val Loss: 0.6448 - Val Acc: 0.7879
Epoch 2/3 - Train Loss: 0.5543 - Val Loss: 0.5968 - Val Acc: 0.7879
Epoch 3/3 - Train Loss: 0.3875 - Val Loss: 0.6839 - Val Acc: 0.7879

=== Evaluating Professionalism model ===
Some weights of the model checkpoint at outputs/professionalism/best_model were not used when initializing Qwen3ForSequenceClassification: ['model.classifier.bias', 'model.classifier.weight', 'model.deberta.embeddings.LayerNorm.bias', 'model.deberta.embeddings.LayerNorm.weight', 'model.deberta.embeddings.word_embeddings.weight', 'model.deberta.encoder.LayerNorm.bias', 'model.deberta.encoder.LayerNorm.weight', 'model.deberta.encoder.layer.0.attention.output.LayerNorm.bias', 'model.deberta.encoder.layer.0.attention.output.LayerNorm.weight', 'model.deberta.encoder.layer.0.attention.output.dense.bias', 'model.deberta.encoder.layer.0.attention.output.dense.weight', 'model.deberta.encoder.layer.0.attention.self.key_proj.bias', 'model.deberta.encoder.layer.0.attention.self.key_proj.weight', 'model.deberta.encoder.layer.0.attention.self.query_proj.bias', 'model.deberta.encoder.layer.0.attention.self.query_proj.weight', 'model.deberta.encoder.layer.0.attention.self.value_proj.bias', 'model.deberta.encoder.layer.0.attention.self.value_proj.weight', 'model.deberta.encoder.layer.0.intermediate.dense.bias', 'model.deberta.encoder.layer.0.intermediate.dense.weight', 'model.deberta.encoder.layer.0.output.LayerNorm.bias', 'model.deberta.encoder.layer.0.output.LayerNorm.weight', 'model.deberta.encoder.layer.0.output.dense.bias', 'model.deberta.encoder.layer.0.output.dense.weight', 'model.deberta.encoder.layer.1.attention.output.LayerNorm.bias', 'model.deberta.encoder.layer.1.attention.output.LayerNorm.weight', 'model.deberta.encoder.layer.1.attention.output.dense.bias', 'model.deberta.encoder.layer.1.attention.output.dense.weight', 'model.deberta.encoder.layer.1.attention.self.key_proj.bias', 'model.deberta.encoder.layer.1.attention.self.key_proj.weight', 'model.deberta.encoder.layer.1.attention.self.query_proj.bias', 'model.deberta.encoder.layer.1.attention.self.query_proj.weight', 'model.deberta.encoder.layer.1.attention.self.value_proj.bias', 'model.deberta.encoder.layer.1.attention.self.value_proj.weight', 'model.deberta.encoder.layer.1.intermediate.dense.bias', 'model.deberta.encoder.layer.1.intermediate.dense.weight', 'model.deberta.encoder.layer.1.output.LayerNorm.bias', 'model.deberta.encoder.layer.1.output.LayerNorm.weight', 'model.deberta.encoder.layer.1.output.dense.bias', 'model.deberta.encoder.layer.1.output.dense.weight', 'model.deberta.encoder.layer.10.attention.output.LayerNorm.bias', 'model.deberta.encoder.layer.10.attention.output.LayerNorm.weight', 'model.deberta.encoder.layer.10.attention.output.dense.bias', 'model.deberta.encoder.layer.10.attention.output.dense.weight', 'model.deberta.encoder.layer.10.attention.self.key_proj.bias', 'model.deberta.encoder.layer.10.attention.self.key_proj.weight', 'model.deberta.encoder.layer.10.attention.self.query_proj.bias', 'model.deberta.encoder.layer.10.attention.self.query_proj.weight', 'model.deberta.encoder.layer.10.attention.self.value_proj.bias', 'model.deberta.encoder.layer.10.attention.self.value_proj.weight', 'model.deberta.encoder.layer.10.intermediate.dense.bias', 'model.deberta.encoder.layer.10.intermediate.dense.weight', 'model.deberta.encoder.layer.10.output.LayerNorm.bias', 'model.deberta.encoder.layer.10.output.LayerNorm.weight', 'model.deberta.encoder.layer.10.output.dense.bias', 'model.deberta.encoder.layer.10.output.dense.weight', 'model.deberta.encoder.layer.11.attention.output.LayerNorm.bias', 'model.deberta.encoder.layer.11.attention.output.LayerNorm.weight', 'model.deberta.encoder.layer.11.attention.output.dense.bias', 'model.deberta.encoder.layer.11.attention.output.dense.weight', 'model.deberta.encoder.layer.11.attention.self.key_proj.bias', 'model.deberta.encoder.layer.11.attention.self.key_proj.weight', 'model.deberta.encoder.layer.11.attention.self.query_proj.bias', 'model.deberta.encoder.layer.11.attention.self.query_proj.weight', 'model.deberta.encoder.layer.11.attention.self.value_proj.bias', 'model.deberta.encoder.layer.11.attention.self.value_proj.weight', 'model.deberta.encoder.layer.11.intermediate.dense.bias', 'model.deberta.encoder.layer.11.intermediate.dense.weight', 'model.deberta.encoder.layer.11.output.LayerNorm.bias', 'model.deberta.encoder.layer.11.output.LayerNorm.weight', 'model.deberta.encoder.layer.11.output.dense.bias', 'model.deberta.encoder.layer.11.output.dense.weight', 'model.deberta.encoder.layer.2.attention.output.LayerNorm.bias', 'model.deberta.encoder.layer.2.attention.output.LayerNorm.weight', 'model.deberta.encoder.layer.2.attention.output.dense.bias', 'model.deberta.encoder.layer.2.attention.output.dense.weight', 'model.deberta.encoder.layer.2.attention.self.key_proj.bias', 'model.deberta.encoder.layer.2.attention.self.key_proj.weight', 'model.deberta.encoder.layer.2.attention.self.query_proj.bias', 'model.deberta.encoder.layer.2.attention.self.query_proj.weight', 'model.deberta.encoder.layer.2.attention.self.value_proj.bias', 'model.deberta.encoder.layer.2.attention.self.value_proj.weight', 'model.deberta.encoder.layer.2.intermediate.dense.bias', 'model.deberta.encoder.layer.2.intermediate.dense.weight', 'model.deberta.encoder.layer.2.output.LayerNorm.bias', 'model.deberta.encoder.layer.2.output.LayerNorm.weight', 'model.deberta.encoder.layer.2.output.dense.bias', 'model.deberta.encoder.layer.2.output.dense.weight', 'model.deberta.encoder.layer.3.attention.output.LayerNorm.bias', 'model.deberta.encoder.layer.3.attention.output.LayerNorm.weight', 'model.deberta.encoder.layer.3.attention.output.dense.bias', 'model.deberta.encoder.layer.3.attention.output.dense.weight', 'model.deberta.encoder.layer.3.attention.self.key_proj.bias', 'model.deberta.encoder.layer.3.attention.self.key_proj.weight', 'model.deberta.encoder.layer.3.attention.self.query_proj.bias', 'model.deberta.encoder.layer.3.attention.self.query_proj.weight', 'model.deberta.encoder.layer.3.attention.self.value_proj.bias', 'model.deberta.encoder.layer.3.attention.self.value_proj.weight', 'model.deberta.encoder.layer.3.intermediate.dense.bias', 'model.deberta.encoder.layer.3.intermediate.dense.weight', 'model.deberta.encoder.layer.3.output.LayerNorm.bias', 'model.deberta.encoder.layer.3.output.LayerNorm.weight', 'model.deberta.encoder.layer.3.output.dense.bias', 'model.deberta.encoder.layer.3.output.dense.weight', 'model.deberta.encoder.layer.4.attention.output.LayerNorm.bias', 'model.deberta.encoder.layer.4.attention.output.LayerNorm.weight', 'model.deberta.encoder.layer.4.attention.output.dense.bias', 'model.deberta.encoder.layer.4.attention.output.dense.weight', 'model.deberta.encoder.layer.4.attention.self.key_proj.bias', 'model.deberta.encoder.layer.4.attention.self.key_proj.weight', 'model.deberta.encoder.layer.4.attention.self.query_proj.bias', 'model.deberta.encoder.layer.4.attention.self.query_proj.weight', 'model.deberta.encoder.layer.4.attention.self.value_proj.bias', 'model.deberta.encoder.layer.4.attention.self.value_proj.weight', 'model.deberta.encoder.layer.4.intermediate.dense.bias', 'model.deberta.encoder.layer.4.intermediate.dense.weight', 'model.deberta.encoder.layer.4.output.LayerNorm.bias', 'model.deberta.encoder.layer.4.output.LayerNorm.weight', 'model.deberta.encoder.layer.4.output.dense.bias', 'model.deberta.encoder.layer.4.output.dense.weight', 'model.deberta.encoder.layer.5.attention.output.LayerNorm.bias', 'model.deberta.encoder.layer.5.attention.output.LayerNorm.weight', 'model.deberta.encoder.layer.5.attention.output.dense.bias', 'model.deberta.encoder.layer.5.attention.output.dense.weight', 'model.deberta.encoder.layer.5.attention.self.key_proj.bias', 'model.deberta.encoder.layer.5.attention.self.key_proj.weight', 'model.deberta.encoder.layer.5.attention.self.query_proj.bias', 'model.deberta.encoder.layer.5.attention.self.query_proj.weight', 'model.deberta.encoder.layer.5.attention.self.value_proj.bias', 'model.deberta.encoder.layer.5.attention.self.value_proj.weight', 'model.deberta.encoder.layer.5.intermediate.dense.bias', 'model.deberta.encoder.layer.5.intermediate.dense.weight', 'model.deberta.encoder.layer.5.output.LayerNorm.bias', 'model.deberta.encoder.layer.5.output.LayerNorm.weight', 'model.deberta.encoder.layer.5.output.dense.bias', 'model.deberta.encoder.layer.5.output.dense.weight', 'model.deberta.encoder.layer.6.attention.output.LayerNorm.bias', 'model.deberta.encoder.layer.6.attention.output.LayerNorm.weight', 'model.deberta.encoder.layer.6.attention.output.dense.bias', 'model.deberta.encoder.layer.6.attention.output.dense.weight', 'model.deberta.encoder.layer.6.attention.self.key_proj.bias', 'model.deberta.encoder.layer.6.attention.self.key_proj.weight', 'model.deberta.encoder.layer.6.attention.self.query_proj.bias', 'model.deberta.encoder.layer.6.attention.self.query_proj.weight', 'model.deberta.encoder.layer.6.attention.self.value_proj.bias', 'model.deberta.encoder.layer.6.attention.self.value_proj.weight', 'model.deberta.encoder.layer.6.intermediate.dense.bias', 'model.deberta.encoder.layer.6.intermediate.dense.weight', 'model.deberta.encoder.layer.6.output.LayerNorm.bias', 'model.deberta.encoder.layer.6.output.LayerNorm.weight', 'model.deberta.encoder.layer.6.output.dense.bias', 'model.deberta.encoder.layer.6.output.dense.weight', 'model.deberta.encoder.layer.7.attention.output.LayerNorm.bias', 'model.deberta.encoder.layer.7.attention.output.LayerNorm.weight', 'model.deberta.encoder.layer.7.attention.output.dense.bias', 'model.deberta.encoder.layer.7.attention.output.dense.weight', 'model.deberta.encoder.layer.7.attention.self.key_proj.bias', 'model.deberta.encoder.layer.7.attention.self.key_proj.weight', 'model.deberta.encoder.layer.7.attention.self.query_proj.bias', 'model.deberta.encoder.layer.7.attention.self.query_proj.weight', 'model.deberta.encoder.layer.7.attention.self.value_proj.bias', 'model.deberta.encoder.layer.7.attention.self.value_proj.weight', 'model.deberta.encoder.layer.7.intermediate.dense.bias', 'model.deberta.encoder.layer.7.intermediate.dense.weight', 'model.deberta.encoder.layer.7.output.LayerNorm.bias', 'model.deberta.encoder.layer.7.output.LayerNorm.weight', 'model.deberta.encoder.layer.7.output.dense.bias', 'model.deberta.encoder.layer.7.output.dense.weight', 'model.deberta.encoder.layer.8.attention.output.LayerNorm.bias', 'model.deberta.encoder.layer.8.attention.output.LayerNorm.weight', 'model.deberta.encoder.layer.8.attention.output.dense.bias', 'model.deberta.encoder.layer.8.attention.output.dense.weight', 'model.deberta.encoder.layer.8.attention.self.key_proj.bias', 'model.deberta.encoder.layer.8.attention.self.key_proj.weight', 'model.deberta.encoder.layer.8.attention.self.query_proj.bias', 'model.deberta.encoder.layer.8.attention.self.query_proj.weight', 'model.deberta.encoder.layer.8.attention.self.value_proj.bias', 'model.deberta.encoder.layer.8.attention.self.value_proj.weight', 'model.deberta.encoder.layer.8.intermediate.dense.bias', 'model.deberta.encoder.layer.8.intermediate.dense.weight', 'model.deberta.encoder.layer.8.output.LayerNorm.bias', 'model.deberta.encoder.layer.8.output.LayerNorm.weight', 'model.deberta.encoder.layer.8.output.dense.bias', 'model.deberta.encoder.layer.8.output.dense.weight', 'model.deberta.encoder.layer.9.attention.output.LayerNorm.bias', 'model.deberta.encoder.layer.9.attention.output.LayerNorm.weight', 'model.deberta.encoder.layer.9.attention.output.dense.bias', 'model.deberta.encoder.layer.9.attention.output.dense.weight', 'model.deberta.encoder.layer.9.attention.self.key_proj.bias', 'model.deberta.encoder.layer.9.attention.self.key_proj.weight', 'model.deberta.encoder.layer.9.attention.self.query_proj.bias', 'model.deberta.encoder.layer.9.attention.self.query_proj.weight', 'model.deberta.encoder.layer.9.attention.self.value_proj.bias', 'model.deberta.encoder.layer.9.attention.self.value_proj.weight', 'model.deberta.encoder.layer.9.intermediate.dense.bias', 'model.deberta.encoder.layer.9.intermediate.dense.weight', 'model.deberta.encoder.layer.9.output.LayerNorm.bias', 'model.deberta.encoder.layer.9.output.LayerNorm.weight', 'model.deberta.encoder.layer.9.output.dense.bias', 'model.deberta.encoder.layer.9.output.dense.weight', 'model.deberta.encoder.rel_embeddings.weight', 'model.pooler.dense.bias', 'model.pooler.dense.weight']
- This IS expected if you are initializing Qwen3ForSequenceClassification from the checkpoint of a model trained on another task or with another architecture (e.g. initializing a BertForSequenceClassification model from a BertForPreTraining model).
- This IS NOT expected if you are initializing Qwen3ForSequenceClassification from the checkpoint of a model that you expect to be exactly identical (initializing a BertForSequenceClassification model from a BertForSequenceClassification model).
Some weights of Qwen3ForSequenceClassification were not initialized from the model checkpoint at outputs/professionalism/best_model and are newly initialized: ['model.embed_tokens.weight', 'model.layers.0.input_layernorm.weight', 'model.layers.0.mlp.down_proj.weight', 'model.layers.0.mlp.gate_proj.weight', 'model.layers.0.mlp.up_proj.weight', 'model.layers.0.post_attention_layernorm.weight', 'model.layers.0.self_attn.k_norm.weight', 'model.layers.0.self_attn.k_proj.weight', 'model.layers.0.self_attn.o_proj.weight', 'model.layers.0.self_attn.q_norm.weight', 'model.layers.0.self_attn.q_proj.weight', 'model.layers.0.self_attn.v_proj.weight', 'model.layers.1.input_layernorm.weight', 'model.layers.1.mlp.down_proj.weight', 'model.layers.1.mlp.gate_proj.weight', 'model.layers.1.mlp.up_proj.weight', 'model.layers.1.post_attention_layernorm.weight', 'model.layers.1.self_attn.k_norm.weight', 'model.layers.1.self_attn.k_proj.weight', 'model.layers.1.self_attn.o_proj.weight', 'model.layers.1.self_attn.q_norm.weight', 'model.layers.1.self_attn.q_proj.weight', 'model.layers.1.self_attn.v_proj.weight', 'model.layers.10.input_layernorm.weight', 'model.layers.10.mlp.down_proj.weight', 'model.layers.10.mlp.gate_proj.weight', 'model.layers.10.mlp.up_proj.weight', 'model.layers.10.post_attention_layernorm.weight', 'model.layers.10.self_attn.k_norm.weight', 'model.layers.10.self_attn.k_proj.weight', 'model.layers.10.self_attn.o_proj.weight', 'model.layers.10.self_attn.q_norm.weight', 'model.layers.10.self_attn.q_proj.weight', 'model.layers.10.self_attn.v_proj.weight', 'model.layers.11.input_layernorm.weight', 'model.layers.11.mlp.down_proj.weight', 'model.layers.11.mlp.gate_proj.weight', 'model.layers.11.mlp.up_proj.weight', 'model.layers.11.post_attention_layernorm.weight', 'model.layers.11.self_attn.k_norm.weight', 'model.layers.11.self_attn.k_proj.weight', 'model.layers.11.self_attn.o_proj.weight', 'model.layers.11.self_attn.q_norm.weight', 'model.layers.11.self_attn.q_proj.weight', 'model.layers.11.self_attn.v_proj.weight', 'model.layers.12.input_layernorm.weight', 'model.layers.12.mlp.down_proj.weight', 'model.layers.12.mlp.gate_proj.weight', 'model.layers.12.mlp.up_proj.weight', 'model.layers.12.post_attention_layernorm.weight', 'model.layers.12.self_attn.k_norm.weight', 'model.layers.12.self_attn.k_proj.weight', 'model.layers.12.self_attn.o_proj.weight', 'model.layers.12.self_attn.q_norm.weight', 'model.layers.12.self_attn.q_proj.weight', 'model.layers.12.self_attn.v_proj.weight', 'model.layers.13.input_layernorm.weight', 'model.layers.13.mlp.down_proj.weight', 'model.layers.13.mlp.gate_proj.weight', 'model.layers.13.mlp.up_proj.weight', 'model.layers.13.post_attention_layernorm.weight', 'model.layers.13.self_attn.k_norm.weight', 'model.layers.13.self_attn.k_proj.weight', 'model.layers.13.self_attn.o_proj.weight', 'model.layers.13.self_attn.q_norm.weight', 'model.layers.13.self_attn.q_proj.weight', 'model.layers.13.self_attn.v_proj.weight', 'model.layers.14.input_layernorm.weight', 'model.layers.14.mlp.down_proj.weight', 'model.layers.14.mlp.gate_proj.weight', 'model.layers.14.mlp.up_proj.weight', 'model.layers.14.post_attention_layernorm.weight', 'model.layers.14.self_attn.k_norm.weight', 'model.layers.14.self_attn.k_proj.weight', 'model.layers.14.self_attn.o_proj.weight', 'model.layers.14.self_attn.q_norm.weight', 'model.layers.14.self_attn.q_proj.weight', 'model.layers.14.self_attn.v_proj.weight', 'model.layers.15.input_layernorm.weight', 'model.layers.15.mlp.down_proj.weight', 'model.layers.15.mlp.gate_proj.weight', 'model.layers.15.mlp.up_proj.weight', 'model.layers.15.post_attention_layernorm.weight', 'model.layers.15.self_attn.k_norm.weight', 'model.layers.15.self_attn.k_proj.weight', 'model.layers.15.self_attn.o_proj.weight', 'model.layers.15.self_attn.q_norm.weight', 'model.layers.15.self_attn.q_proj.weight', 'model.layers.15.self_attn.v_proj.weight', 'model.layers.16.input_layernorm.weight', 'model.layers.16.mlp.down_proj.weight', 'model.layers.16.mlp.gate_proj.weight', 'model.layers.16.mlp.up_proj.weight', 'model.layers.16.post_attention_layernorm.weight', 'model.layers.16.self_attn.k_norm.weight', 'model.layers.16.self_attn.k_proj.weight', 'model.layers.16.self_attn.o_proj.weight', 'model.layers.16.self_attn.q_norm.weight', 'model.layers.16.self_attn.q_proj.weight', 'model.layers.16.self_attn.v_proj.weight', 'model.layers.17.input_layernorm.weight', 'model.layers.17.mlp.down_proj.weight', 'model.layers.17.mlp.gate_proj.weight', 'model.layers.17.mlp.up_proj.weight', 'model.layers.17.post_attention_layernorm.weight', 'model.layers.17.self_attn.k_norm.weight', 'model.layers.17.self_attn.k_proj.weight', 'model.layers.17.self_attn.o_proj.weight', 'model.layers.17.self_attn.q_norm.weight', 'model.layers.17.self_attn.q_proj.weight', 'model.layers.17.self_attn.v_proj.weight', 'model.layers.18.input_layernorm.weight', 'model.layers.18.mlp.down_proj.weight', 'model.layers.18.mlp.gate_proj.weight', 'model.layers.18.mlp.up_proj.weight', 'model.layers.18.post_attention_layernorm.weight', 'model.layers.18.self_attn.k_norm.weight', 'model.layers.18.self_attn.k_proj.weight', 'model.layers.18.self_attn.o_proj.weight', 'model.layers.18.self_attn.q_norm.weight', 'model.layers.18.self_attn.q_proj.weight', 'model.layers.18.self_attn.v_proj.weight', 'model.layers.19.input_layernorm.weight', 'model.layers.19.mlp.down_proj.weight', 'model.layers.19.mlp.gate_proj.weight', 'model.layers.19.mlp.up_proj.weight', 'model.layers.19.post_attention_layernorm.weight', 'model.layers.19.self_attn.k_norm.weight', 'model.layers.19.self_attn.k_proj.weight', 'model.layers.19.self_attn.o_proj.weight', 'model.layers.19.self_attn.q_norm.weight', 'model.layers.19.self_attn.q_proj.weight', 'model.layers.19.self_attn.v_proj.weight', 'model.layers.2.input_layernorm.weight', 'model.layers.2.mlp.down_proj.weight', 'model.layers.2.mlp.gate_proj.weight', 'model.layers.2.mlp.up_proj.weight', 'model.layers.2.post_attention_layernorm.weight', 'model.layers.2.self_attn.k_norm.weight', 'model.layers.2.self_attn.k_proj.weight', 'model.layers.2.self_attn.o_proj.weight', 'model.layers.2.self_attn.q_norm.weight', 'model.layers.2.self_attn.q_proj.weight', 'model.layers.2.self_attn.v_proj.weight', 'model.layers.20.input_layernorm.weight', 'model.layers.20.mlp.down_proj.weight', 'model.layers.20.mlp.gate_proj.weight', 'model.layers.20.mlp.up_proj.weight', 'model.layers.20.post_attention_layernorm.weight', 'model.layers.20.self_attn.k_norm.weight', 'model.layers.20.self_attn.k_proj.weight', 'model.layers.20.self_attn.o_proj.weight', 'model.layers.20.self_attn.q_norm.weight', 'model.layers.20.self_attn.q_proj.weight', 'model.layers.20.self_attn.v_proj.weight', 'model.layers.21.input_layernorm.weight', 'model.layers.21.mlp.down_proj.weight', 'model.layers.21.mlp.gate_proj.weight', 'model.layers.21.mlp.up_proj.weight', 'model.layers.21.post_attention_layernorm.weight', 'model.layers.21.self_attn.k_norm.weight', 'model.layers.21.self_attn.k_proj.weight', 'model.layers.21.self_attn.o_proj.weight', 'model.layers.21.self_attn.q_norm.weight', 'model.layers.21.self_attn.q_proj.weight', 'model.layers.21.self_attn.v_proj.weight', 'model.layers.22.input_layernorm.weight', 'model.layers.22.mlp.down_proj.weight', 'model.layers.22.mlp.gate_proj.weight', 'model.layers.22.mlp.up_proj.weight', 'model.layers.22.post_attention_layernorm.weight', 'model.layers.22.self_attn.k_norm.weight', 'model.layers.22.self_attn.k_proj.weight', 'model.layers.22.self_attn.o_proj.weight', 'model.layers.22.self_attn.q_norm.weight', 'model.layers.22.self_attn.q_proj.weight', 'model.layers.22.self_attn.v_proj.weight', 'model.layers.23.input_layernorm.weight', 'model.layers.23.mlp.down_proj.weight', 'model.layers.23.mlp.gate_proj.weight', 'model.layers.23.mlp.up_proj.weight', 'model.layers.23.post_attention_layernorm.weight', 'model.layers.23.self_attn.k_norm.weight', 'model.layers.23.self_attn.k_proj.weight', 'model.layers.23.self_attn.o_proj.weight', 'model.layers.23.self_attn.q_norm.weight', 'model.layers.23.self_attn.q_proj.weight', 'model.layers.23.self_attn.v_proj.weight', 'model.layers.24.input_layernorm.weight', 'model.layers.24.mlp.down_proj.weight', 'model.layers.24.mlp.gate_proj.weight', 'model.layers.24.mlp.up_proj.weight', 'model.layers.24.post_attention_layernorm.weight', 'model.layers.24.self_attn.k_norm.weight', 'model.layers.24.self_attn.k_proj.weight', 'model.layers.24.self_attn.o_proj.weight', 'model.layers.24.self_attn.q_norm.weight', 'model.layers.24.self_attn.q_proj.weight', 'model.layers.24.self_attn.v_proj.weight', 'model.layers.25.input_layernorm.weight', 'model.layers.25.mlp.down_proj.weight', 'model.layers.25.mlp.gate_proj.weight', 'model.layers.25.mlp.up_proj.weight', 'model.layers.25.post_attention_layernorm.weight', 'model.layers.25.self_attn.k_norm.weight', 'model.layers.25.self_attn.k_proj.weight', 'model.layers.25.self_attn.o_proj.weight', 'model.layers.25.self_attn.q_norm.weight', 'model.layers.25.self_attn.q_proj.weight', 'model.layers.25.self_attn.v_proj.weight', 'model.layers.26.input_layernorm.weight', 'model.layers.26.mlp.down_proj.weight', 'model.layers.26.mlp.gate_proj.weight', 'model.layers.26.mlp.up_proj.weight', 'model.layers.26.post_attention_layernorm.weight', 'model.layers.26.self_attn.k_norm.weight', 'model.layers.26.self_attn.k_proj.weight', 'model.layers.26.self_attn.o_proj.weight', 'model.layers.26.self_attn.q_norm.weight', 'model.layers.26.self_attn.q_proj.weight', 'model.layers.26.self_attn.v_proj.weight', 'model.layers.27.input_layernorm.weight', 'model.layers.27.mlp.down_proj.weight', 'model.layers.27.mlp.gate_proj.weight', 'model.layers.27.mlp.up_proj.weight', 'model.layers.27.post_attention_layernorm.weight', 'model.layers.27.self_attn.k_norm.weight', 'model.layers.27.self_attn.k_proj.weight', 'model.layers.27.self_attn.o_proj.weight', 'model.layers.27.self_attn.q_norm.weight', 'model.layers.27.self_attn.q_proj.weight', 'model.layers.27.self_attn.v_proj.weight', 'model.layers.28.input_layernorm.weight', 'model.layers.28.mlp.down_proj.weight', 'model.layers.28.mlp.gate_proj.weight', 'model.layers.28.mlp.up_proj.weight', 'model.layers.28.post_attention_layernorm.weight', 'model.layers.28.self_attn.k_norm.weight', 'model.layers.28.self_attn.k_proj.weight', 'model.layers.28.self_attn.o_proj.weight', 'model.layers.28.self_attn.q_norm.weight', 'model.layers.28.self_attn.q_proj.weight', 'model.layers.28.self_attn.v_proj.weight', 'model.layers.29.input_layernorm.weight', 'model.layers.29.mlp.down_proj.weight', 'model.layers.29.mlp.gate_proj.weight', 'model.layers.29.mlp.up_proj.weight', 'model.layers.29.post_attention_layernorm.weight', 'model.layers.29.self_attn.k_norm.weight', 'model.layers.29.self_attn.k_proj.weight', 'model.layers.29.self_attn.o_proj.weight', 'model.layers.29.self_attn.q_norm.weight', 'model.layers.29.self_attn.q_proj.weight', 'model.layers.29.self_attn.v_proj.weight', 'model.layers.3.input_layernorm.weight', 'model.layers.3.mlp.down_proj.weight', 'model.layers.3.mlp.gate_proj.weight', 'model.layers.3.mlp.up_proj.weight', 'model.layers.3.post_attention_layernorm.weight', 'model.layers.3.self_attn.k_norm.weight', 'model.layers.3.self_attn.k_proj.weight', 'model.layers.3.self_attn.o_proj.weight', 'model.layers.3.self_attn.q_norm.weight', 'model.layers.3.self_attn.q_proj.weight', 'model.layers.3.self_attn.v_proj.weight', 'model.layers.30.input_layernorm.weight', 'model.layers.30.mlp.down_proj.weight', 'model.layers.30.mlp.gate_proj.weight', 'model.layers.30.mlp.up_proj.weight', 'model.layers.30.post_attention_layernorm.weight', 'model.layers.30.self_attn.k_norm.weight', 'model.layers.30.self_attn.k_proj.weight', 'model.layers.30.self_attn.o_proj.weight', 'model.layers.30.self_attn.q_norm.weight', 'model.layers.30.self_attn.q_proj.weight', 'model.layers.30.self_attn.v_proj.weight', 'model.layers.31.input_layernorm.weight', 'model.layers.31.mlp.down_proj.weight', 'model.layers.31.mlp.gate_proj.weight', 'model.layers.31.mlp.up_proj.weight', 'model.layers.31.post_attention_layernorm.weight', 'model.layers.31.self_attn.k_norm.weight', 'model.layers.31.self_attn.k_proj.weight', 'model.layers.31.self_attn.o_proj.weight', 'model.layers.31.self_attn.q_norm.weight', 'model.layers.31.self_attn.q_proj.weight', 'model.layers.31.self_attn.v_proj.weight', 'model.layers.32.input_layernorm.weight', 'model.layers.32.mlp.down_proj.weight', 'model.layers.32.mlp.gate_proj.weight', 'model.layers.32.mlp.up_proj.weight', 'model.layers.32.post_attention_layernorm.weight', 'model.layers.32.self_attn.k_norm.weight', 'model.layers.32.self_attn.k_proj.weight', 'model.layers.32.self_attn.o_proj.weight', 'model.layers.32.self_attn.q_norm.weight', 'model.layers.32.self_attn.q_proj.weight', 'model.layers.32.self_attn.v_proj.weight', 'model.layers.33.input_layernorm.weight', 'model.layers.33.mlp.down_proj.weight', 'model.layers.33.mlp.gate_proj.weight', 'model.layers.33.mlp.up_proj.weight', 'model.layers.33.post_attention_layernorm.weight', 'model.layers.33.self_attn.k_norm.weight', 'model.layers.33.self_attn.k_proj.weight', 'model.layers.33.self_attn.o_proj.weight', 'model.layers.33.self_attn.q_norm.weight', 'model.layers.33.self_attn.q_proj.weight', 'model.layers.33.self_attn.v_proj.weight', 'model.layers.34.input_layernorm.weight', 'model.layers.34.mlp.down_proj.weight', 'model.layers.34.mlp.gate_proj.weight', 'model.layers.34.mlp.up_proj.weight', 'model.layers.34.post_attention_layernorm.weight', 'model.layers.34.self_attn.k_norm.weight', 'model.layers.34.self_attn.k_proj.weight', 'model.layers.34.self_attn.o_proj.weight', 'model.layers.34.self_attn.q_norm.weight', 'model.layers.34.self_attn.q_proj.weight', 'model.layers.34.self_attn.v_proj.weight', 'model.layers.35.input_layernorm.weight', 'model.layers.35.mlp.down_proj.weight', 'model.layers.35.mlp.gate_proj.weight', 'model.layers.35.mlp.up_proj.weight', 'model.layers.35.post_attention_layernorm.weight', 'model.layers.35.self_attn.k_norm.weight', 'model.layers.35.self_attn.k_proj.weight', 'model.layers.35.self_attn.o_proj.weight', 'model.layers.35.self_attn.q_norm.weight', 'model.layers.35.self_attn.q_proj.weight', 'model.layers.35.self_attn.v_proj.weight', 'model.layers.4.input_layernorm.weight', 'model.layers.4.mlp.down_proj.weight', 'model.layers.4.mlp.gate_proj.weight', 'model.layers.4.mlp.up_proj.weight', 'model.layers.4.post_attention_layernorm.weight', 'model.layers.4.self_attn.k_norm.weight', 'model.layers.4.self_attn.k_proj.weight', 'model.layers.4.self_attn.o_proj.weight', 'model.layers.4.self_attn.q_norm.weight', 'model.layers.4.self_attn.q_proj.weight', 'model.layers.4.self_attn.v_proj.weight', 'model.layers.5.input_layernorm.weight', 'model.layers.5.mlp.down_proj.weight', 'model.layers.5.mlp.gate_proj.weight', 'model.layers.5.mlp.up_proj.weight', 'model.layers.5.post_attention_layernorm.weight', 'model.layers.5.self_attn.k_norm.weight', 'model.layers.5.self_attn.k_proj.weight', 'model.layers.5.self_attn.o_proj.weight', 'model.layers.5.self_attn.q_norm.weight', 'model.layers.5.self_attn.q_proj.weight', 'model.layers.5.self_attn.v_proj.weight', 'model.layers.6.input_layernorm.weight', 'model.layers.6.mlp.down_proj.weight', 'model.layers.6.mlp.gate_proj.weight', 'model.layers.6.mlp.up_proj.weight', 'model.layers.6.post_attention_layernorm.weight', 'model.layers.6.self_attn.k_norm.weight', 'model.layers.6.self_attn.k_proj.weight', 'model.layers.6.self_attn.o_proj.weight', 'model.layers.6.self_attn.q_norm.weight', 'model.layers.6.self_attn.q_proj.weight', 'model.layers.6.self_attn.v_proj.weight', 'model.layers.7.input_layernorm.weight', 'model.layers.7.mlp.down_proj.weight', 'model.layers.7.mlp.gate_proj.weight', 'model.layers.7.mlp.up_proj.weight', 'model.layers.7.post_attention_layernorm.weight', 'model.layers.7.self_attn.k_norm.weight', 'model.layers.7.self_attn.k_proj.weight', 'model.layers.7.self_attn.o_proj.weight', 'model.layers.7.self_attn.q_norm.weight', 'model.layers.7.self_attn.q_proj.weight', 'model.layers.7.self_attn.v_proj.weight', 'model.layers.8.input_layernorm.weight', 'model.layers.8.mlp.down_proj.weight', 'model.layers.8.mlp.gate_proj.weight', 'model.layers.8.mlp.up_proj.weight', 'model.layers.8.post_attention_layernorm.weight', 'model.layers.8.self_attn.k_norm.weight', 'model.layers.8.self_attn.k_proj.weight', 'model.layers.8.self_attn.o_proj.weight', 'model.layers.8.self_attn.q_norm.weight', 'model.layers.8.self_attn.q_proj.weight', 'model.layers.8.self_attn.v_proj.weight', 'model.layers.9.input_layernorm.weight', 'model.layers.9.mlp.down_proj.weight', 'model.layers.9.mlp.gate_proj.weight', 'model.layers.9.mlp.up_proj.weight', 'model.layers.9.post_attention_layernorm.weight', 'model.layers.9.self_attn.k_norm.weight', 'model.layers.9.self_attn.k_proj.weight', 'model.layers.9.self_attn.o_proj.weight', 'model.layers.9.self_attn.q_norm.weight', 'model.layers.9.self_attn.q_proj.weight', 'model.layers.9.self_attn.v_proj.weight', 'model.norm.weight', 'score.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
Model loaded from outputs/professionalism/best_model
Professionalism Test Loss: nan
Professionalism Test Accuracy: 0.1432
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
Classification Report:
                precision  recall  f1-score  support
Unprofessional      0.143   1.000     0.250   66.000
Borderline          0.000   0.000     0.000   39.000
Appropriate         0.000   0.000     0.000  356.000
accuracy            0.143   0.143     0.143    0.143
macro avg           0.048   0.333     0.083  461.000
weighted avg        0.020   0.143     0.036  461.000

=== Professionalism model saved to outputs/professionalism/best_model ===

=== Training Summary ===
Professionalism model: outputs/professionalism/best_model

=== Done! ===

Some weights of LlamaForSequenceClassification were not initialized from the model checkpoint at meta-llama/Meta-Llama-3.1-8B-Instruct and are newly initialized: ['score.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.

[Input Text] → [Tokenizer] → [Embedding Layer] → [Transformer Layers] → [Classification Head] → [Output: Class Probabilities]

## google-bert/bert-base-uncased
(venv) [zhengwb@gpu-compute-12 LLMAsAJudge]$ python3 main.py  --model_name google-bert/bert-base-uncased --learning_rate 2e-5 --batch_s
ize 2 --epochs 3
=== Loading data ===
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/openpyxl/worksheet/_reader.py:312: UserWarning: Data Validation extension is not supported and will be removed
  warn(msg)
Loaded fuzzy.coding.dataDW.xlsx: 2302 rows, 10 columns
Merged data shape: (2302, 11)

=== Processing Professionalism Criterion ===
Number of classes for professionalism: 3
Preprocessing data for professionalism...
Processed data shape: (2302, 12)
Splitting data for professionalism...
Train set: 1610 rows
Validation set: 231 rows
Test set: 461 rows
Saved processed data to data/processed/professionalism

=== Training model for Professionalism ===
tokenizer_config.json: 100%|████████████████████████████████████████████████████████████████████████| 48.0/48.0 [00:00<00:00, 22.2kB/s]
config.json: 100%|█████████████████████████████████████████████████████████████████████████████████████| 570/570 [00:00<00:00, 283kB/s]
vocab.txt: 100%|████████████████████████████████████████████████████████████████████████████████████| 232k/232k [00:00<00:00, 22.6MB/s]
tokenizer.json: 100%|███████████████████████████████████████████████████████████████████████████████| 466k/466k [00:00<00:00, 23.2MB/s]
Xet Storage is enabled for this repo, but the 'hf_xet' package is not installed. Falling back to regular HTTP download. For better performance, install the package with: `pip install huggingface_hub[hf_xet]` or `pip install hf_xet`
model.safetensors: 100%|█████████████████████████████████████████████████████████████████████████████| 440M/440M [00:03<00:00, 116MB/s]
Some weights of BertForSequenceClassification were not initialized from the model checkpoint at google-bert/bert-base-uncased and are newly initialized: ['classifier.bias', 'classifier.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
Epoch 1/3 - Train Loss: 0.8518 - Val Loss: 0.5726 - Val Acc: 0.7662
Epoch 2/3 - Train Loss: 0.5917 - Val Loss: 0.4608 - Val Acc: 0.8485
Epoch 3/3 - Train Loss: 0.3244 - Val Loss: 0.5707 - Val Acc: 0.7835

=== Evaluating Professionalism model ===
Model loaded from outputs/professionalism/best_model
Professionalism Test Loss: 0.4875
Professionalism Test Accuracy: 0.8395
Classification Report:
                precision  recall  f1-score  support
Unprofessional      0.698   0.561     0.622   66.000
Borderline          1.000   0.077     0.143   39.000
Appropriate         0.857   0.975     0.912  356.000
accuracy            0.839   0.839     0.839    0.839
macro avg           0.852   0.537     0.559  461.000
weighted avg        0.846   0.839     0.805  461.000

=== Professionalism model saved to outputs/professionalism/best_model ===

=== Processing Relevance Criterion ===
Number of classes for relevance: 3
Preprocessing data for relevance...
Processed data shape: (2302, 12)
Splitting data for relevance...
Train set: 1610 rows
Validation set: 231 rows
Test set: 461 rows
Saved processed data to data/processed/relevance

=== Training model for Relevance ===
Some weights of BertForSequenceClassification were not initialized from the model checkpoint at google-bert/bert-base-uncased and are newly initialized: ['classifier.bias', 'classifier.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
Epoch 1/3 - Train Loss: 0.8401 - Val Loss: 0.5638 - Val Acc: 0.7965
Epoch 2/3 - Train Loss: 0.5624 - Val Loss: 0.5537 - Val Acc: 0.7879
Epoch 3/3 - Train Loss: 0.3227 - Val Loss: 0.8191 - Val Acc: 0.7316

=== Evaluating Relevance model ===
Model loaded from outputs/relevance/best_model
Relevance Test Loss: 0.5535
Relevance Test Accuracy: 0.7852
Classification Report:
                    precision  recall  f1-score  support
Irrelevant              0.697   0.931     0.797  175.000
Partially relevant      0.632   0.182     0.282   66.000
Relevant                0.899   0.850     0.874  220.000
accuracy                0.785   0.785     0.785    0.785
macro avg               0.742   0.654     0.651  461.000
weighted avg            0.784   0.785     0.760  461.000

=== Relevance model saved to outputs/relevance/best_model ===

=== Processing Ethics Criterion ===
Number of classes for ethics: 5
Preprocessing data for ethics...
Processed data shape: (2302, 12)
Splitting data for ethics...
Train set: 1610 rows
Validation set: 231 rows
Test set: 461 rows
Saved processed data to data/processed/ethics

=== Training model for Ethics ===
Some weights of BertForSequenceClassification were not initialized from the model checkpoint at google-bert/bert-base-uncased and are newly initialized: ['classifier.bias', 'classifier.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
Epoch 1/3 - Train Loss: 1.0972 - Val Loss: 0.6259 - Val Acc: 0.8398
Epoch 2/3 - Train Loss: 0.8486 - Val Loss: 0.5403 - Val Acc: 0.8442
Epoch 3/3 - Train Loss: 0.5698 - Val Loss: 0.6316 - Val Acc: 0.7965

=== Evaluating Ethics model ===
Model loaded from outputs/ethics/best_model
Ethics Test Loss: 0.5654
Ethics Test Accuracy: 0.8308
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
Classification Report:
              precision  recall  f1-score  support
Dangerous         0.429   0.214     0.286   14.000
Unsafe            0.000   0.000     0.000   24.000
Questionable      0.500   0.069     0.121   29.000
Mostly safe       1.000   0.176     0.300   17.000
Safe              0.839   0.995     0.910  377.000
accuracy          0.831   0.831     0.831    0.831
macro avg         0.553   0.291     0.323  461.000
weighted avg      0.767   0.831     0.772  461.000

=== Ethics model saved to outputs/ethics/best_model ===

=== Processing Distraction Criterion ===
Number of classes for distraction: 4
Preprocessing data for distraction...
Processed data shape: (2302, 12)
Splitting data for distraction...
Train set: 1610 rows
Validation set: 231 rows
Test set: 461 rows
Saved processed data to data/processed/distraction

=== Training model for Distraction ===
Some weights of BertForSequenceClassification were not initialized from the model checkpoint at google-bert/bert-base-uncased and are newly initialized: ['classifier.bias', 'classifier.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
Epoch 1/3 - Train Loss: 1.0962 - Val Loss: 0.8812 - Val Acc: 0.6840
Epoch 2/3 - Train Loss: 0.7744 - Val Loss: 0.8303 - Val Acc: 0.7186
Epoch 3/3 - Train Loss: 0.5428 - Val Loss: 0.7473 - Val Acc: 0.7489

=== Evaluating Distraction model ===
Model loaded from outputs/distraction/best_model
Distraction Test Loss: 0.7553
Distraction Test Accuracy: 0.7354
Classification Report:
                        precision  recall  f1-score  support
Highly distracting          0.788   0.757     0.772  152.000
Moderately distracting      0.327   0.587     0.420   63.000
Questionable                0.875   0.212     0.341   33.000
Not distracting             0.928   0.845     0.885  213.000
accuracy                    0.735   0.735     0.735    0.735
macro avg                   0.729   0.600     0.605  461.000
weighted avg                0.796   0.735     0.745  461.000

=== Distraction model saved to outputs/distraction/best_model ===

=== Training Summary ===
Professionalism model: outputs/professionalism/best_model
Relevance model: outputs/relevance/best_model
Ethics model: outputs/ethics/best_model
Distraction model: outputs/distraction/best_model

## meta-llama/Llama-3.2-3B-Instruct
(venv) [zhengwb@gpu-compute-12 LLMAsAJudge]$ python3 main.py  --model_name meta-llama/Llama-3.2-3B-Instruct --learning_rate 2e-5 --batch_size 2 --epochs 3

## Similar model with Llama-3-8b-instruct
Summary Table
| Model Name | Size | Instruction-tuned | Open Weights | Notable Strengths |
|-----------------------------|-------|-------------------|--------------|--------------------------|
| Llama-3-8B-Instruct | 8B | Yes | Yes | Meta, strong English |
| Qwen2-7B-Instruct/Qwen3-8B | 7B/8B | Yes | Yes | Multilingual, strong |
| Mistral-7B-Instruct | 7B | Yes | Yes | Efficient, strong |
| Mixtral-8x7B-Instruct | 46.7B | Yes | Yes | MoE, high performance |
| Gemma-7B-It | 7B | Yes | Yes | Google, efficient |
| Falcon-7B-Instruct | 7B | Yes | Yes | Good for chat |
| Yi-6B-Chat | 6B | Yes | Yes | Multilingual |
| Baichuan2-7B-Chat | 7B | Yes | Yes | Multilingual |


Summary Table
| Method | Command Example | Notes |
|-----------------------|------------------------------------------------------|------------------------------|
| Redirect stdout | > output.log or >> output.log | Only stdout |
| Redirect all output | > output.log 2>&1 | stdout + stderr |
| Use tee | | tee output.log | See + save output |
| Record full session | script my_terminal_session.log | Everything, interactive |


## roberta-large
(venv) [zhengwb@gpu-compute-12 LLMAsAJudge]$ python3 main.py --model_name roberta-large --learning_
rate 2e-5 --batch_size 3 --epochs 3 
=== Loading data ===
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/openpyxl/worksheet/_reader.py:312: UserWarning: Data Validation extension is not supported and will be removed
  warn(msg)
Loaded fuzzy.coding.dataDW.xlsx: 2302 rows, 10 columns
Merged data shape: (2302, 11)

=== Processing Professionalism Criterion ===
Number of classes for professionalism: 3
Preprocessing data for professionalism...
Processed data shape: (2302, 12)
Splitting data for professionalism...
Train set: 1610 rows
Validation set: 231 rows
Test set: 461 rows
Saved processed data to data/processed/professionalism

=== Training model for Professionalism ===
tokenizer_config.json: 100%|████████████████████████████████████| 25.0/25.0 [00:00<00:00, 10.6kB/s]
config.json: 100%|█████████████████████████████████████████████████| 482/482 [00:00<00:00, 235kB/s]
vocab.json: 100%|███████████████████████████████████████████████| 899k/899k [00:00<00:00, 9.31MB/s]
merges.txt: 100%|███████████████████████████████████████████████| 456k/456k [00:00<00:00, 7.26MB/s]
tokenizer.json: 100%|█████████████████████████████████████████| 1.36M/1.36M [00:00<00:00, 29.7MB/s]
Xet Storage is enabled for this repo, but the 'hf_xet' package is not installed. Falling back to regular HTTP download. For better performance, install the package with: `pip install huggingface_hub[hf_xet]` or `pip install hf_xet`
model.safetensors: 100%|███████████████████████████████████████| 1.42G/1.42G [00:12<00:00, 114MB/s]
Some weights of RobertaForSequenceClassification were not initialized from the model checkpoint at roberta-large and are newly initialized: ['classifier.dense.bias', 'classifier.dense.weight', 'classifier.out_proj.bias', 'classifier.out_proj.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
Epoch 1/3 - Train Loss: 1.0150 - Val Loss: 0.8266 - Val Acc: 0.7879
Epoch 2/3 - Train Loss: 0.9969 - Val Loss: 0.7204 - Val Acc: 0.7879
Epoch 3/3 - Train Loss: 0.9932 - Val Loss: 0.8131 - Val Acc: 0.7879

=== Evaluating Professionalism model ===
Model loaded from outputs/professionalism/best_model
Professionalism Test Loss: 0.7493
Professionalism Test Accuracy: 0.7722
Sample predictions and confidences:
Text: Have the authorities found the kid yet? | Pred: 2 | Confidence: 0.6068
Text: Any recent travel? | Pred: 2 | Confidence: 0.6068
Text: First year medical student, patient encounter in er | Pred: 2 | Confidence: 0.6068
Text: I quickly invent a medical device that allows me to use telekinetic powers | Pred: 2 | Confidence: 0.6068
Text: Hello babe? Back for more??? Wink | Pred: 2 | Confidence: 0.6068
Text: Hey what brings you in | Pred: 2 | Confidence: 0.6068
Text: The AI diagnoses and treats the patient | Pred: 2 | Confidence: 0.6068
Text: What did I think of? | Pred: 2 | Confidence: 0.6068
Text: Echo | Pred: 2 | Confidence: 0.6068
Text: I'm gonna administer heparin while we wait to see what we can do next. Guys, prep the helicopter. We are gonna have to take him somewhere safe | Pred: 2 | Confidence: 0.6068
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
Classification Report:
                precision  recall  f1-score  support
Unprofessional      0.000   0.000     0.000   66.000
Borderline          0.000   0.000     0.000   39.000
Appropriate         0.772   1.000     0.871  356.000
accuracy            0.772   0.772     0.772    0.772
macro avg           0.257   0.333     0.290  461.000
weighted avg        0.596   0.772     0.673  461.000
Cohen's Kappa: 0.0000
Mean confidence: 0.6068
Accuracy (recomputed): 0.7722
Weighted F1 score: 0.6730

=== Professionalism model saved to outputs/professionalism/best_model ===

=== Processing Relevance Criterion ===
Number of classes for relevance: 3
Preprocessing data for relevance...
Processed data shape: (2302, 12)
Splitting data for relevance...
Train set: 1610 rows
Validation set: 231 rows
Test set: 461 rows
Saved processed data to data/processed/relevance

=== Training model for Relevance ===
Some weights of RobertaForSequenceClassification were not initialized from the model checkpoint at roberta-large and are newly initialized: ['classifier.dense.bias', 'classifier.dense.weight', 'classifier.out_proj.bias', 'classifier.out_proj.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
Epoch 1/3 - Train Loss: 1.0994 - Val Loss: 1.0641 - Val Acc: 0.4935
Epoch 2/3 - Train Loss: 1.0890 - Val Loss: 1.0381 - Val Acc: 0.4935
Epoch 3/3 - Train Loss: 1.0831 - Val Loss: 1.0361 - Val Acc: 0.3853

=== Evaluating Relevance model ===
Model loaded from outputs/relevance/best_model
Relevance Test Loss: 1.0450
Relevance Test Accuracy: 0.3796
Sample predictions and confidences:
Text: Have the authorities found the kid yet? | Pred: 0 | Confidence: 0.4133
Text: Any recent travel? | Pred: 0 | Confidence: 0.4133
Text: First year medical student, patient encounter in er | Pred: 0 | Confidence: 0.4134
Text: I quickly invent a medical device that allows me to use telekinetic powers | Pred: 0 | Confidence: 0.4133
Text: Hello babe? Back for more??? Wink | Pred: 0 | Confidence: 0.4133
Text: Hey what brings you in | Pred: 0 | Confidence: 0.4133
Text: The AI diagnoses and treats the patient | Pred: 0 | Confidence: 0.4133
Text: What did I think of? | Pred: 0 | Confidence: 0.4133
Text: Echo | Pred: 0 | Confidence: 0.4133
Text: I'm gonna administer heparin while we wait to see what we can do next. Guys, prep the helicopter. We are gonna have to take him somewhere safe | Pred: 0 | Confidence: 0.4132
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
Classification Report:
                    precision  recall  f1-score  support
Irrelevant              0.380   1.000     0.550   175.00
Partially relevant      0.000   0.000     0.000    66.00
Relevant                0.000   0.000     0.000   220.00
accuracy                0.380   0.380     0.380     0.38
macro avg               0.127   0.333     0.183   461.00
weighted avg            0.144   0.380     0.209   461.00
Cohen's Kappa: 0.0000
Mean confidence: 0.4133
Accuracy (recomputed): 0.3796
Weighted F1 score: 0.2089

=== Relevance model saved to outputs/relevance/best_model ===

=== Processing Ethics Criterion ===
Number of classes for ethics: 5
Preprocessing data for ethics...
Processed data shape: (2302, 12)
Splitting data for ethics...
Train set: 1610 rows
Validation set: 231 rows
Test set: 461 rows
Saved processed data to data/processed/ethics

=== Training model for Ethics ===
Some weights of RobertaForSequenceClassification were not initialized from the model checkpoint at roberta-large and are newly initialized: ['classifier.dense.bias', 'classifier.dense.weight', 'classifier.out_proj.bias', 'classifier.out_proj.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
Epoch 1/3 - Train Loss: 1.3364 - Val Loss: 0.9654 - Val Acc: 0.8398
Epoch 2/3 - Train Loss: 1.3425 - Val Loss: 0.9438 - Val Acc: 0.8398
Epoch 3/3 - Train Loss: 1.3438 - Val Loss: 0.8536 - Val Acc: 0.8398

=== Evaluating Ethics model ===
Model loaded from outputs/ethics/best_model
Ethics Test Loss: 0.8932
Ethics Test Accuracy: 0.8178
Sample predictions and confidences:
Text: Have the authorities found the kid yet? | Pred: 4 | Confidence: 0.5433
Text: Any recent travel? | Pred: 4 | Confidence: 0.5433
Text: First year medical student, patient encounter in er | Pred: 4 | Confidence: 0.5433
Text: I quickly invent a medical device that allows me to use telekinetic powers | Pred: 4 | Confidence: 0.5433
Text: Hello babe? Back for more??? Wink | Pred: 4 | Confidence: 0.5433
Text: Hey what brings you in | Pred: 4 | Confidence: 0.5433
Text: The AI diagnoses and treats the patient | Pred: 4 | Confidence: 0.5433
Text: What did I think of? | Pred: 4 | Confidence: 0.5433
Text: Echo | Pred: 4 | Confidence: 0.5433
Text: I'm gonna administer heparin while we wait to see what we can do next. Guys, prep the helicopter. We are gonna have to take him somewhere safe | Pred: 4 | Confidence: 0.5433
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
Classification Report:
              precision  recall  f1-score  support
Dangerous         0.000   0.000     0.000   14.000
Unsafe            0.000   0.000     0.000   24.000
Questionable      0.000   0.000     0.000   29.000
Mostly safe       0.000   0.000     0.000   17.000
Safe              0.818   1.000     0.900  377.000
accuracy          0.818   0.818     0.818    0.818
macro avg         0.164   0.200     0.180  461.000
weighted avg      0.669   0.818     0.736  461.000
Cohen's Kappa: 0.0000
Mean confidence: 0.5433
Accuracy (recomputed): 0.8178
Weighted F1 score: 0.7358

=== Ethics model saved to outputs/ethics/best_model ===

=== Processing Distraction Criterion ===
Number of classes for distraction: 4
Preprocessing data for distraction...
Processed data shape: (2302, 12)
Splitting data for distraction...
Train set: 1610 rows
Validation set: 231 rows
Test set: 461 rows
Saved processed data to data/processed/distraction

=== Training model for Distraction ===
Some weights of RobertaForSequenceClassification were not initialized from the model checkpoint at roberta-large and are newly initialized: ['classifier.dense.bias', 'classifier.dense.weight', 'classifier.out_proj.bias', 'classifier.out_proj.weight']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
Epoch 1/3 - Train Loss: 1.2983 - Val Loss: 1.0723 - Val Acc: 0.6667
Epoch 2/3 - Train Loss: 1.2969 - Val Loss: 1.2898 - Val Acc: 0.4805
Epoch 3/3 - Train Loss: 1.3524 - Val Loss: 1.2677 - Val Acc: 0.4805

=== Evaluating Distraction model ===
Model loaded from outputs/distraction/best_model
Distraction Test Loss: 1.1021
Distraction Test Accuracy: 0.6811
Sample predictions and confidences:
Text: Have the authorities found the kid yet? | Pred: 0 | Confidence: 0.2981
Text: Any recent travel? | Pred: 3 | Confidence: 0.5199
Text: First year medical student, patient encounter in er | Pred: 0 | Confidence: 0.2846
Text: I quickly invent a medical device that allows me to use telekinetic powers | Pred: 0 | Confidence: 0.3524
Text: Hello babe? Back for more??? Wink | Pred: 3 | Confidence: 0.4083
Text: Hey what brings you in | Pred: 3 | Confidence: 0.4596
Text: The AI diagnoses and treats the patient | Pred: 0 | Confidence: 0.3428
Text: What did I think of? | Pred: 3 | Confidence: 0.4613
Text: Echo | Pred: 3 | Confidence: 0.3366
Text: I'm gonna administer heparin while we wait to see what we can do next. Guys, prep the helicopter. We are gonna have to take him somewhere safe | Pred: 0 | Confidence: 0.3664
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
/opt/ohpc/pub/apps/anaconda/3/lib/python3.9/site-packages/sklearn/metrics/_classification.py:1318: UndefinedMetricWarning: Precision and F-score are ill-defined and being set to 0.0 in labels with no predicted samples. Use `zero_division` parameter to control this behavior.
  _warn_prf(average, modifier, msg_start, len(result))
Classification Report:
                        precision  recall  f1-score  support
Highly distracting          0.618   0.809     0.701  152.000
Moderately distracting      0.000   0.000     0.000   63.000
Questionable                0.000   0.000     0.000   33.000
Not distracting             0.729   0.897     0.804  213.000
accuracy                    0.681   0.681     0.681    0.681
macro avg                   0.337   0.426     0.376  461.000
weighted avg                0.541   0.681     0.603  461.000
Cohen's Kappa: 0.4642
Mean confidence: 0.3906
Accuracy (recomputed): 0.6811
Weighted F1 score: 0.6027

=== Distraction model saved to outputs/distraction/best_model ===

=== Training Summary ===
Professionalism model: outputs/professionalism/best_model
Relevance model: outputs/relevance/best_model
Ethics model: outputs/ethics/best_model
Distraction model: outputs/distraction/best_model

=== Further Fine-Tuning Professionalism with Prompt Engineering ===
Model loaded from outputs/professionalism/best_model
Epoch 1/3 - Train Loss: 0.9887 - Val Loss: 0.7628 - Val Acc: 0.7879
Epoch 2/3 - Train Loss: 0.9798 - Val Loss: 0.7707 - Val Acc: 0.7879
Epoch 3/3 - Train Loss: 0.9876 - Val Loss: 0.7373 - Val Acc: 0.7879
=== Further fine-tuned Professionalism model saved to outputs/professionalism/best_model ===

=== Further Fine-Tuning Relevance with Prompt Engineering ===
Model loaded from outputs/relevance/best_model
Epoch 1/3 - Train Loss: 1.0950 - Val Loss: 1.0213 - Val Acc: 0.3853
Epoch 2/3 - Train Loss: 1.0895 - Val Loss: 1.0130 - Val Acc: 0.3853
Epoch 3/3 - Train Loss: 1.0840 - Val Loss: 1.0204 - Val Acc: 0.4935
=== Further fine-tuned Relevance model saved to outputs/relevance/best_model ===

=== Further Fine-Tuning Ethics with Prompt Engineering ===
Model loaded from outputs/ethics/best_model
Epoch 1/3 - Train Loss: 1.3118 - Val Loss: 0.7374 - Val Acc: 0.8398
Epoch 2/3 - Train Loss: 1.3178 - Val Loss: 0.7988 - Val Acc: 0.8398
Epoch 3/3 - Train Loss: 1.3109 - Val Loss: 0.8811 - Val Acc: 0.8398
=== Further fine-tuned Ethics model saved to outputs/ethics/best_model ===

=== Further Fine-Tuning Distraction with Prompt Engineering ===
Model loaded from outputs/distraction/best_model
Epoch 1/3 - Train Loss: 1.1217 - Val Loss: 1.0309 - Val Acc: 0.6580
Epoch 2/3 - Train Loss: 1.1140 - Val Loss: 1.0462 - Val Acc: 0.6320
Epoch 3/3 - Train Loss: 1.2915 - Val Loss: 1.2692 - Val Acc: 0.4805
=== Further fine-tuned Distraction model saved to outputs/distraction/best_model ===

=== Done! ===
(venv) [zhengwb@gpu-compute-12 LLMAsAJudge]$ srun: Job step aborted: Waiting up to 32 seconds for job step to finish.
slurmstepd: error: *** STEP 2842761.0 ON gpu-compute-12 CANCELLED AT 2025-04-30T18:08:36 DUE TO TIME LIMIT ***
exit


#