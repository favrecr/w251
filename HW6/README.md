## HW6  
### Runtimes:
V100 is faster than P100  

V100 1 epoch 1M rows Runtime:  
100% 1/1 [1:52:15<00:00, 6735.95s/it, avg_accuracy=0.952, avg_loss=0.121]  
Validation 500K Runtime:  
100% 15625/15625 [15:42<00:00, 16.58it/s]  

P100 1 epoch 1M rows runtime:  
6hrs  
Validation 500K runtime:
1hr  

## AUC

V100 1 epoch - 0.96990  
V100 2 epochs - 0.96968  
P100 1 epoch - 0.97000  
P100 2 epochs - Couldn't run, RuntimeError: CUDA out of memory  

## Sentences  

#### 1 epoch  
V100  
highest toxicity - "Trump is a mentally unbalanced buffoon.\nHe's ..."  
lowest toxicity - "Rolling Stone supports the nationalization of....."  

P100  
highest toxicity - "What an arrogant piece of shit. This arrogant ..."  
lowest toxicity - "NO , massive tax increases on businesses means..."  

#### 2 Epochs:  
V100:  
highest toxicity - "you are a fool"  
lowest toxicity - "Good idea too have begun your comment with a c..."   
