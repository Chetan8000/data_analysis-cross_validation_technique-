import pandas as pd
from sklearn import model_selection

#TRANING DATA PATH
TRAIN_PATH = ""

if __name__=="__main__":
    
    '''We can use this process with almost all kinds of datasets. 
    For example, when you have images, you can create a CSV with 
    image id, image location and image label and use the process above.'''
    
    df = pd.read_csv(TRAIN_PATH)
    #we create new column name kfold and field with -1
    df.loc[:,"kfold"] = -1
    #randomize the data 
    df = df.sample(frac=1).reset_index(drop=True)
    #target is the id
    targets = df.drop("id", axis=1).values
    #initiate KFold model
    kf = model_selection.KFold(n_splits=5)
    #fill the kfold column
    for fold, (trn_,val_) in enumerate(kf.split(X=df)):
        df.loc[val_, "kfold"] = fold
    #save the new csv with kfold column
    df.to_csv("train_fold.csv", index=False)