# ADM-HW2 Videogames Reviews
![image](https://github.com/user-attachments/assets/801e7c0e-179b-4a1c-b220-aa1355957162)

About the project
This project analyzes user reviews of the Steam platform for 2021. 
We used an open [dataset](https://www.kaggle.com/datasets/najzeko/steam-reviews-2021) provided on Kaggle to carry out various analytical tasks, such as assessing the popularity of games, analyzing user sentiment, and identifying key factors influencing game ratings

### Note to TA's and reviewers
Due to GitHub's limitations with displaying interactive graphs from the Plotly library, we followed the TA's recommendation to place `main.ipynb` in a public Google Drive folder. The code has been executed there, and now the interactive graphs, which couldn't be shown on GitHub, are available.

Here is the link to the Google Drive folder containing the file: [main.ipynb](https://drive.google.com/drive/folders/1ZWrlP-N5ttht2Jc-yq8jASG9YffF13rp)



```bash
ADM-HW2/
│             
|   ├── main.ipynb  (contain all solutions)             
│   ├── functions.py  (functions)
│   ├── input.txt     (values for AQ)
|   ├── images
├── tests/                        
│   ├── test_input.py (test_values for AQ)      
│   ├── test_functions.py (test )
│   ├── __init__.py               

├── README.md    
├── LISENSE  
```
Step 1: Cloning the repository

```bash
git clone 
```

Step 2: Install Dependencies
```bash
export env_name="ADM-HW2"

conda create -n $env_name python=3.10

conda activate $env_name

conda install --file requirements.txt
```
Step 3: Run tests

```bash
pytest-v
```







