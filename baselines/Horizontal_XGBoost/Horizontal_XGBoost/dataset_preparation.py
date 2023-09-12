"""Handle the dataset partitioning and (optionally) complex downloads.

Please add here all the necessary logic to either download, uncompress, pre/post-process
your dataset (or all of the above). If the desired way of running your baseline is to
first download the dataset and partition it and then run the experiments, please
uncomment the lines below and tell us in the README.md (see the "Running the Experiment"
block) that this file should be executed first.
"""
# import hydra
# from hydra.core.hydra_config import HydraConfig
# from hydra.utils import call, instantiate
# from omegaconf import DictConfig, OmegaConf


# @hydra.main(config_path="conf", config_name="base", version_base=None)
# def download_and_preprocess(cfg: DictConfig) -> None:
#     """Does everything needed to get the dataset.

#     Parameters
#     ----------
#     cfg : DictConfig
#         An omegaconf object that stores the hydra config.
#     """

#     ## 1. print parsed config
#     print(OmegaConf.to_yaml(cfg))

#     # Please include here all the logic
#     # Please use the Hydra config style as much as possible specially
#     # for parts that can be customised (e.g. how data is partitioned)

# if __name__ == "__main__":

#     download_and_preprocess()
from typing import Optional

import os
import urllib.request
import bz2
import shutil
import numpy as np

from sklearn.datasets import load_svmlight_file

def download_data(
        dataset_name: Optional[str]="cod-rna"
):
    """
    Downloads (if necessary) and returns the dataset path assigned by the dataset_name parm.
    Parameters
    ----------
    dataset_name : String
        A string stating the name of the dataset that need to be dowenloaded.
    Returns
    -------
    List[Dataset Pathes]
        The pathes for the data that will be used in train and test, with train of full dataset
        in index 0
    """
    
    ALL_DATASETS_PATH="./dataset"
    if dataset_name=="a9a":
        DATASET_PATH=os.path.join(ALL_DATASETS_PATH, "a9a")
        if not os.path.exists(DATASET_PATH):
            os.makedirs(DATASET_PATH)
            urllib.request.urlretrieve(
                "https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/binary/a9a",
                f"{os.path.join(DATASET_PATH, 'a9a')}",
            )
            urllib.request.urlretrieve(
                "https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/binary/a9a.t",
                f"{os.path.join(DATASET_PATH, 'a9a.t')}",
            )
        #trainig then test ✅
        return [os.path.join(DATASET_PATH, 'a9a'),os.path.join(DATASET_PATH, 'a9a.t')]    
    if dataset_name=="cod-rna":
        DATASET_PATH=os.path.join(ALL_DATASETS_PATH, "cod-rna")
        if not os.path.exists(DATASET_PATH):
            os.makedirs(DATASET_PATH)
            urllib.request.urlretrieve(
                "https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/binary/cod-rna",
                f"{os.path.join(DATASET_PATH, 'cod-rna')}",
            )
            urllib.request.urlretrieve(
                "https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/binary/cod-rna.t",
                f"{os.path.join(DATASET_PATH, 'cod-rna.t')}",
            )
            urllib.request.urlretrieve(
                "https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/binary/cod-rna.r",
                f"{os.path.join(DATASET_PATH, 'cod-rna.r')}",
            )
        #trainig then test ✅
        return [os.path.join(DATASET_PATH, 'cod-rna.t'),os.path.join(DATASET_PATH, 'cod-rna.r')]

    if dataset_name=="ijcnn1":
        DATASET_PATH=os.path.join(ALL_DATASETS_PATH, "ijcnn1")
        if not os.path.exists(DATASET_PATH):
            os.makedirs(DATASET_PATH)

            urllib.request.urlretrieve(
                "https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/binary/ijcnn1.bz2",
                f"{os.path.join(DATASET_PATH, 'ijcnn1.tr.bz2')}",
            )
            urllib.request.urlretrieve(
                "https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/binary/ijcnn1.t.bz2",
                f"{os.path.join(DATASET_PATH, 'ijcnn1.t.bz2')}",
            )
            urllib.request.urlretrieve(
                "https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/binary/ijcnn1.tr.bz2",
                f"{os.path.join(DATASET_PATH, 'ijcnn1.tr.bz2')}",
            )
            urllib.request.urlretrieve(
                "https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/binary/ijcnn1.val.bz2",
                f"{os.path.join(DATASET_PATH, 'ijcnn1.val.bz2')}",
            )

            for filepath in os.listdir(DATASET_PATH):
                abs_filepath = os.path.join(DATASET_PATH, filepath)
                with bz2.BZ2File(abs_filepath) as fr, open(abs_filepath[:-4], "wb") as fw:
                    shutil.copyfileobj(fr, fw)
        #trainig then test ✅
        return [os.path.join(DATASET_PATH, 'ijcnn1.t'),os.path.join(DATASET_PATH, 'ijcnn1.tr')]

    if dataset_name=="space_ga":
        DATASET_PATH=os.path.join(ALL_DATASETS_PATH, "space_ga")
        if not os.path.exists(DATASET_PATH):
            os.makedirs(DATASET_PATH)
            urllib.request.urlretrieve(
                "https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/regression/space_ga",
                f"{os.path.join(DATASET_PATH, 'space_ga')}",
            )
            urllib.request.urlretrieve(
                "https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/regression/space_ga_scale",
                f"{os.path.join(DATASET_PATH, 'space_ga_scale')}",
            )
        return [os.path.join(DATASET_PATH, 'space_ga_scale')]
    if dataset_name=="abalone":
        DATASET_PATH=os.path.join(ALL_DATASETS_PATH, "abalone")
        if not os.path.exists(DATASET_PATH): 
            os.makedirs(DATASET_PATH)       
            urllib.request.urlretrieve(
                "https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/regression/abalone",
                f"{os.path.join(DATASET_PATH, 'abalone')}",
            )
            urllib.request.urlretrieve(
                "https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/regression/abalone_scale",
                f"{os.path.join(DATASET_PATH, 'abalone_scale')}",
            )
        return [os.path.join(DATASET_PATH, 'abalone_scale')]
    if dataset_name=="cpusmall":
        DATASET_PATH=os.path.join(ALL_DATASETS_PATH, "cpusmall")
        if not os.path.exists(DATASET_PATH):  
            os.makedirs(DATASET_PATH)      
            urllib.request.urlretrieve(
                "https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/regression/cpusmall",
                f"{os.path.join(DATASET_PATH, 'cpusmall')}",
            )
            urllib.request.urlretrieve(
                "https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/regression/cpusmall_scale",
                f"{os.path.join(DATASET_PATH, 'cpusmall_scale')}",
            )
        return [os.path.join(DATASET_PATH, 'cpusmall_scale')]
    
def datafiles_fusion(data_paths):
    """
    Merge (if necessary) the data files and returns the features and labels sperated in
    numpy arrays.

    Parameters
    ----------
    data_paths: List[Dataset Pathes]
        The pathes for the data that will be used in train and test, with train of full dataset
        in index 0    
    Returns
    -------
    X: Numpy array
        The full features of the dataset.
    y: Numpy array
        The full labels of the dataset.
    """
    
    data=load_svmlight_file(data_paths[0], zero_based=False)
    X=data[0].toarray()
    Y=data[1]
    for i in range(1,len(data_paths)):
        data= load_svmlight_file(data_paths[i], zero_based=False,n_features=X.shape[1])
        X=np.concatenate((X,data[0].toarray()), axis=0)
        Y=np.concatenate((Y,data[1]), axis=0)
    return X,Y

def train_test_split(X,y,train_ratio=.75):
    """
    Split the dataset into training and testing 

    Parameters
    ----------
        X: Numpy array
            The full features of the dataset.
        y: Numpy array
            The full labels of the dataset.
        train_ratio: float
            the ratio that training should take from the full dataset
    Returns
    -------
        X_train: Numpy array
            The training dataset features.
        y_train: Numpy array
            The labels of the training dataset.
        X_test: Numpy array
            The testing dataset features.
        y_test: Numpy array
            The labels of the testing dataset.
    """
    q=int(X.shape[0]*train_ratio)

    X_train = X[0:q]
    y_train = y[0:q]

    X_test = X[q:]
    y_test = y[q:]

    X_train.flags.writeable = True
    y_train.flags.writeable = True
    X_test.flags.writeable = True
    y_test.flags.writeable = True

    return X_train,y_train,X_test,y_test

def modify_labels(y_train,y_test):
    """
    Switch the -1 in the classification dataset with 0

    Parameters
    ----------
        y_train: Numpy array
            The labels of the training dataset.
        y_test: Numpy array
            The labels of the testing dataset.
    Returns
    -------
        y_train: Numpy array
            The labels of the training dataset.
        y_test: Numpy array
            The labels of the testing dataset.
    """
    y_train[y_train == -1] = 0
    y_test[y_test == -1] = 0
    return y_train,y_test

