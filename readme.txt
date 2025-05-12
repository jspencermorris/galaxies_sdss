
Machine Learning Insights into Astronomical Object Classification and Galaxy Typing from SDSS and GZ2

Dec 2023

Applied classical machine learning techniques to classify astronomical objects and galaxy types; used physics-informed models to engineer new features; explored 12 modeling approaches across both tabular and imagery datasets.

Virtual environment details in ./requirements.txt.

Data Acquisition done using direct download and SQL queries.  Details in ./src/data/.  

Datasets (original) stored locally, but primary transformed tabular data is available in ./data/processed/.

Data preprocessing and modeling done using Jupyter Notebooks.  Details in ./notebooks/. The notebooks included are:
    Primary Notebooks:
        *   Image_Classification_Combined: This notebook condenses all the models and functions we built for the image classification models and operationalizes them. Our results (for image classification) are based on the models built in this notebook.
        *   jsm_modeling_tabular.ipynb: This notebook condenses all the models and functions after the foundation for the tabular preprocessing was finished. Our results (for the tabular data) are based on the models built in this notebook.
    Testing/Supplementary Notebooks:
        -   aa_test_2.ipynb: Testing notebook where we tested various models, and code functionality. These models were used in the Image_Classification_Combined notebook.
        -   CNN_test_r2.ipynb:  Testing notebook where we tested various models, and code functionality. These models were used in the Image_Classification_Combined notebook.
        -   CNN_Test_r3.ipynb:  Testing notebook where we tested various models, and code functionality. These models were used in the Image_Classification_Combined notebook.
        -   CNN_Test.ipynb: Testing notebook where we tested various models, and code functionality. These models were used in the Image_Classification_Combined notebook.
        -   jsm_eda_00.ipynb: Testing notebook where we tested various models, and code functionality. These models and functions were used in the jsm_modeling_tabular notebook.
        -   jsm_eda_01.ipynb: Testing notebook where we tested various models, and code functionality. These models and functions were used in the jsm_modeling_tabular notebook.
        -   jsm_eda_02.ipynb: Testing notebook where we tested various models, and code functionality. These models and functions were used in the jsm_modeling_tabular notebook.
        -   LSTM_Test_r1.ipynb: Testing notebook where we tested various models, and code functionality. These models were used in the Image_Classification_Combined notebook.
        -   testing.ipynb: Testing notebook where we tested various models, and code functionality. These models and functions were used in the jsm_modeling_tabular notebook.

Finalized tuned Models for tabular data were pickled and are available in ./models/.

Key References in ./references/literature/.

Interim and final reports in ./reports/.