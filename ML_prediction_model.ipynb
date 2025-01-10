{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/home/Jupyterhub/2021105061/.local/lib/python3.8/site-packages/pandas/core/computation/expressions.py:20: UserWarning: Pandas requires version '2.7.3' or newer of 'numexpr' (version '2.7.1' currently installed).\n",
      "  from pandas.core.computation.check import NUMEXPR_INSTALLED\n"
     ]
    }
   ],
   "source": [
    "# This Python 3 environment comes with many helpful analytics libraries installed\n",
    "# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python\n",
    "# For example, here's several helpful packages to load\n",
    "\n",
    "import numpy as np # linear algebra\n",
    "import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)\n",
    "\n",
    "# Input data files are available in the read-only \"../input/\" directory\n",
    "# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory\n",
    "\n",
    "import os\n",
    "for dirname, _, filenames in os.walk('/kaggle/input'):\n",
    "    for filename in filenames:\n",
    "        print(os.path.join(dirname, filename))\n",
    "\n",
    "# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using \"Save & Run All\" \n",
    "# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "#declare header files\n",
    "\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "import warnings # To suppress some warnings\n",
    "warnings.filterwarnings(\"ignore\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 1100 entries, 0 to 1099\n",
      "Data columns (total 14 columns):\n",
      " #   Column                Non-Null Count  Dtype \n",
      "---  ------                --------------  ----- \n",
      " 0   Age                   1100 non-null   int64 \n",
      " 1   Gender                1100 non-null   int64 \n",
      " 2   Air Pollution         1100 non-null   int64 \n",
      " 3   Alcohol use           1100 non-null   int64 \n",
      " 4   OccuPational Hazards  1100 non-null   int64 \n",
      " 5   Genetic Risk          1100 non-null   int64 \n",
      " 6   Balanced Diet         1100 non-null   int64 \n",
      " 7   Obesity               1100 non-null   int64 \n",
      " 8   Smoking               1100 non-null   int64 \n",
      " 9   Passive Smoker        1100 non-null   int64 \n",
      " 10  Shortness of Breath   1100 non-null   int64 \n",
      " 11  Wheezing              1100 non-null   int64 \n",
      " 12  Frequent Cold         1100 non-null   int64 \n",
      " 13  Level                 1100 non-null   object\n",
      "dtypes: int64(13), object(1)\n",
      "memory usage: 120.4+ KB\n"
     ]
    }
   ],
   "source": [
    "df = pd.read_csv('augmented_dataset1.csv') \n",
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Age</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Air Pollution</th>\n",
       "      <th>Alcohol use</th>\n",
       "      <th>OccuPational Hazards</th>\n",
       "      <th>Genetic Risk</th>\n",
       "      <th>Balanced Diet</th>\n",
       "      <th>Obesity</th>\n",
       "      <th>Smoking</th>\n",
       "      <th>Passive Smoker</th>\n",
       "      <th>Shortness of Breath</th>\n",
       "      <th>Wheezing</th>\n",
       "      <th>Frequent Cold</th>\n",
       "      <th>Level</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>33</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>Low</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>17</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>7</td>\n",
       "      <td>8</td>\n",
       "      <td>1</td>\n",
       "      <td>Medium</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>35</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>5</td>\n",
       "      <td>5</td>\n",
       "      <td>5</td>\n",
       "      <td>6</td>\n",
       "      <td>7</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>9</td>\n",
       "      <td>2</td>\n",
       "      <td>6</td>\n",
       "      <td>High</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>37</td>\n",
       "      <td>1</td>\n",
       "      <td>7</td>\n",
       "      <td>7</td>\n",
       "      <td>7</td>\n",
       "      <td>6</td>\n",
       "      <td>7</td>\n",
       "      <td>7</td>\n",
       "      <td>7</td>\n",
       "      <td>7</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>6</td>\n",
       "      <td>High</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>46</td>\n",
       "      <td>1</td>\n",
       "      <td>6</td>\n",
       "      <td>8</td>\n",
       "      <td>7</td>\n",
       "      <td>7</td>\n",
       "      <td>7</td>\n",
       "      <td>7</td>\n",
       "      <td>8</td>\n",
       "      <td>7</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>High</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>35</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>5</td>\n",
       "      <td>5</td>\n",
       "      <td>5</td>\n",
       "      <td>6</td>\n",
       "      <td>7</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>9</td>\n",
       "      <td>2</td>\n",
       "      <td>6</td>\n",
       "      <td>High</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>52</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>Low</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>28</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>3</td>\n",
       "      <td>Low</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>35</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>5</td>\n",
       "      <td>5</td>\n",
       "      <td>6</td>\n",
       "      <td>5</td>\n",
       "      <td>5</td>\n",
       "      <td>6</td>\n",
       "      <td>6</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>2</td>\n",
       "      <td>Medium</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>46</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>3</td>\n",
       "      <td>3</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>6</td>\n",
       "      <td>2</td>\n",
       "      <td>Medium</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Age  Gender  Air Pollution  Alcohol use  OccuPational Hazards  \\\n",
       "0   33       1              2            4                     4   \n",
       "1   17       1              3            1                     3   \n",
       "2   35       1              4            5                     5   \n",
       "3   37       1              7            7                     7   \n",
       "4   46       1              6            8                     7   \n",
       "5   35       1              4            5                     5   \n",
       "6   52       2              2            4                     4   \n",
       "7   28       2              3            1                     3   \n",
       "8   35       2              4            5                     5   \n",
       "9   46       1              2            3                     2   \n",
       "\n",
       "   Genetic Risk  Balanced Diet  Obesity  Smoking  Passive Smoker  \\\n",
       "0             3              2        4        3               2   \n",
       "1             4              2        2        2               4   \n",
       "2             5              6        7        2               3   \n",
       "3             6              7        7        7               7   \n",
       "4             7              7        7        8               7   \n",
       "5             5              6        7        2               3   \n",
       "6             3              2        4        3               2   \n",
       "7             2              4        3        1               4   \n",
       "8             6              5        5        6               6   \n",
       "9             4              3        3        2               3   \n",
       "\n",
       "   Shortness of Breath  Wheezing  Frequent Cold   Level  \n",
       "0                    2         2              2     Low  \n",
       "1                    7         8              1  Medium  \n",
       "2                    9         2              6    High  \n",
       "3                    3         1              6    High  \n",
       "4                    4         1              4    High  \n",
       "5                    9         2              6    High  \n",
       "6                    2         2              2     Low  \n",
       "7                    2         4              3     Low  \n",
       "8                    3         2              2  Medium  \n",
       "9                    4         6              2  Medium  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['Low', 'Medium', 'High'], dtype=object)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Level'].unique() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>count</th>\n",
       "      <th>mean</th>\n",
       "      <th>std</th>\n",
       "      <th>min</th>\n",
       "      <th>25%</th>\n",
       "      <th>50%</th>\n",
       "      <th>75%</th>\n",
       "      <th>max</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Age</th>\n",
       "      <td>1100.0</td>\n",
       "      <td>37.493636</td>\n",
       "      <td>12.585177</td>\n",
       "      <td>14.0</td>\n",
       "      <td>27.0</td>\n",
       "      <td>36.0</td>\n",
       "      <td>45.0</td>\n",
       "      <td>73.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Gender</th>\n",
       "      <td>1100.0</td>\n",
       "      <td>1.416364</td>\n",
       "      <td>0.493180</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Air Pollution</th>\n",
       "      <td>1100.0</td>\n",
       "      <td>3.901818</td>\n",
       "      <td>2.061695</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>8.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Alcohol use</th>\n",
       "      <td>1100.0</td>\n",
       "      <td>4.563636</td>\n",
       "      <td>2.603026</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>7.0</td>\n",
       "      <td>8.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>OccuPational Hazards</th>\n",
       "      <td>1100.0</td>\n",
       "      <td>4.784545</td>\n",
       "      <td>2.116691</td>\n",
       "      <td>1.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>7.0</td>\n",
       "      <td>8.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Genetic Risk</th>\n",
       "      <td>1100.0</td>\n",
       "      <td>4.549091</td>\n",
       "      <td>2.093438</td>\n",
       "      <td>1.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>7.0</td>\n",
       "      <td>7.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Balanced Diet</th>\n",
       "      <td>1100.0</td>\n",
       "      <td>4.446364</td>\n",
       "      <td>2.137204</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>7.0</td>\n",
       "      <td>7.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Obesity</th>\n",
       "      <td>1100.0</td>\n",
       "      <td>4.420000</td>\n",
       "      <td>2.135526</td>\n",
       "      <td>1.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>7.0</td>\n",
       "      <td>7.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Smoking</th>\n",
       "      <td>1100.0</td>\n",
       "      <td>4.016364</td>\n",
       "      <td>2.481910</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>7.0</td>\n",
       "      <td>8.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Passive Smoker</th>\n",
       "      <td>1100.0</td>\n",
       "      <td>4.229091</td>\n",
       "      <td>2.327247</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>7.0</td>\n",
       "      <td>8.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Shortness of Breath</th>\n",
       "      <td>1100.0</td>\n",
       "      <td>4.280909</td>\n",
       "      <td>2.320185</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>6.0</td>\n",
       "      <td>9.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Wheezing</th>\n",
       "      <td>1100.0</td>\n",
       "      <td>3.858182</td>\n",
       "      <td>2.071927</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>8.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Frequent Cold</th>\n",
       "      <td>1100.0</td>\n",
       "      <td>3.574545</td>\n",
       "      <td>1.848908</td>\n",
       "      <td>1.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>7.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                       count       mean        std   min   25%   50%   75%  \\\n",
       "Age                   1100.0  37.493636  12.585177  14.0  27.0  36.0  45.0   \n",
       "Gender                1100.0   1.416364   0.493180   1.0   1.0   1.0   2.0   \n",
       "Air Pollution         1100.0   3.901818   2.061695   1.0   2.0   3.0   6.0   \n",
       "Alcohol use           1100.0   4.563636   2.603026   1.0   2.0   5.0   7.0   \n",
       "OccuPational Hazards  1100.0   4.784545   2.116691   1.0   3.0   5.0   7.0   \n",
       "Genetic Risk          1100.0   4.549091   2.093438   1.0   3.0   5.0   7.0   \n",
       "Balanced Diet         1100.0   4.446364   2.137204   1.0   2.0   4.0   7.0   \n",
       "Obesity               1100.0   4.420000   2.135526   1.0   3.0   4.0   7.0   \n",
       "Smoking               1100.0   4.016364   2.481910   1.0   2.0   3.0   7.0   \n",
       "Passive Smoker        1100.0   4.229091   2.327247   1.0   2.0   4.0   7.0   \n",
       "Shortness of Breath   1100.0   4.280909   2.320185   1.0   2.0   4.0   6.0   \n",
       "Wheezing              1100.0   3.858182   2.071927   1.0   2.0   4.0   5.0   \n",
       "Frequent Cold         1100.0   3.574545   1.848908   1.0   2.0   3.0   5.0   \n",
       "\n",
       "                       max  \n",
       "Age                   73.0  \n",
       "Gender                 2.0  \n",
       "Air Pollution          8.0  \n",
       "Alcohol use            8.0  \n",
       "OccuPational Hazards   8.0  \n",
       "Genetic Risk           7.0  \n",
       "Balanced Diet          7.0  \n",
       "Obesity                7.0  \n",
       "Smoking                8.0  \n",
       "Passive Smoker         8.0  \n",
       "Shortness of Breath    9.0  \n",
       "Wheezing               8.0  \n",
       "Frequent Cold          7.0  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe().T"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0 1 2]\n"
     ]
    }
   ],
   "source": [
    "# Convert the \"Level\" column to string type first\n",
    "df[\"Level\"] = df[\"Level\"].astype(str)\n",
    "\n",
    "# Map cancer levels from Objective(str) to numeric values\n",
    "mapping = {'High': 2, 'Medium': 1, 'Low': 0}\n",
    "df[\"Level\"].replace(mapping, inplace=True)\n",
    "\n",
    "# Display the unique cancer levels after mapping\n",
    "print(df['Level'].unique())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x432 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#check risk level\n",
    "plt.figure(figsize=(10, 6))\n",
    "explode = (0, 0, 0.15)\n",
    "plt.pie(df['Level'].value_counts(), \n",
    "        labels=mapping.keys(), \n",
    "        explode=explode, autopct='%1.1f%%', \n",
    "        shadow=False, startangle=90, \n",
    "        colors=['#75ff33', '#fdff30', '#ff3333'],\n",
    "        textprops={'fontsize': 18})\n",
    "plt.title('Level Distribution')\n",
    "plt.gca().set_facecolor('white')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Each individual column(independent variables) influenced in target column(dependent variables) \n",
    "# function for bar plotting\n",
    "def occ_cht(col, df=df):\n",
    "    return df.groupby(col)['Level'].value_counts(normalize=True).unstack().plot(kind='bar', title = (f'Lungs Disease Based on {col}'), figsize=(12,5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:title={'center':'Lungs Disease Based on Age'}, xlabel='Age'>"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 864x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "occ_cht('Age')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:title={'center':'Lungs Disease Based on Gender'}, xlabel='Gender'>"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 864x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "occ_cht('Gender')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:title={'center':'Lungs Disease Based on Air Pollution'}, xlabel='Air Pollution'>"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 864x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "occ_cht('Air Pollution')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:title={'center':'Lungs Disease Based on Alcohol use'}, xlabel='Alcohol use'>"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 864x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "occ_cht('Alcohol use')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:title={'center':'Lungs Disease Based on OccuPational Hazards'}, xlabel='OccuPational Hazards'>"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 864x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "occ_cht('OccuPational Hazards')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:title={'center':'Lungs Disease Based on Genetic Risk'}, xlabel='Genetic Risk'>"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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ddLsYZ14yy23rIULFw7r9JIkSeqISy+99DdVNX/s/qEF4YULF7Js2bJhnV6SJEkdkWTcx827NEKSJEmdZBCWJElSJxmEJUmS1ElDWyMsSZKkDcPq1atZuXIld91117BLmdDcuXMZGRlhzpw5fbU3CEuSJGlCK1euZLPNNmPhwoUkGXY546oqbrrpJlauXMmiRYv66uPSCEmSJE3orrvu4tGPfvR6G4IBkvDoRz96SrPWBmFJkiRNan0OwaOmWqNBWJIkSdO26aabztjYS5cu5cQTTxz4uAZhSZIkdZJBWJIkSTPi6quvZu+992aXXXbhOc95Dj/96U+55ZZbWLhwIffeey8Ad955JwsWLGD16tXjtp9JBmFJkiTNiKOPPpoPfehDXHrppZx44okcc8wxzJs3jx133JELL7wQgLPPPpu99tqLOXPmjNt+Jm20t09bePw50+p/3Qn7DagSSZKk7rn99tu56KKLOPjgg+/b94c//AGAQw45hM9//vM8//nP5/TTT+eYY46ZsP1M2WiDsCRJkobn3nvvZYsttuCyyy57wLEDDjiAd77zndx8881ceumlvOAFL+COO+5Ya/uZ4tIISZIkDdzmm2/OokWLOOOMM4DmgReXX3450NxhYrfdduO4445j//33Z9asWRO2nykGYUmSJE3bnXfeycjIyH3/3v/+9/OZz3yGU045hR133JHtt9+eL3/5y/e1P+SQQzjttNM45JBD7ts3UfuZ4NIISZIkTdvoXSDGOu+888bd/8pXvpKqut++RYsWjdt+6dKl065vPM4IS5IkqZMMwpIkSeokg7AkSZI6ySAsSZKkTjIIS5IkqZMMwpIkSeokg7AkSZI2COeddx5PfepT2WabbTjhhBOmPZ73EZYkSdKULDz+nIGOd90J+03aZs2aNbz5zW/ma1/7GiMjI+y6664ccMABLF68+EGf1xlhSZIkrfcuvvhittlmG570pCexySabcOihh077yXMGYUmSJK33rr/+ehYsWHDf9sjICNdff/20xjQIS5Ikab039nHMAEmmNaZBWJIkSeu9kZERVqxYcd/2ypUr2WqrraY1pkFYkiRJ671dd92Vn//851x77bXcfffdnH766RxwwAHTGtO7RkiSJGm9N3v2bD784Q+z1157sWbNGo466ii233776Y05oNokSZLUEf3c7mwm7Lvvvuy7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\n",
      "text/plain": [
       "<Figure size 864x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "occ_cht('Genetic Risk')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:title={'center':'Lungs Disease Based on Balanced Diet'}, xlabel='Balanced Diet'>"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 864x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "occ_cht('Balanced Diet')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:title={'center':'Lungs Disease Based on Obesity'}, xlabel='Obesity'>"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 864x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "occ_cht('Obesity')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:title={'center':'Lungs Disease Based on Smoking'}, xlabel='Smoking'>"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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rd6EC8Jrsummm47btufPn8+pp546btuXJEnSxDHpgrAkSZLUDxtEEL7lllvYf//92W233XjVq17FjTfeyP3338+sWbN46qmnAHjkkUeYOXMmK1asGLG9JEmSumWDCMLHH388n/jEJ7jiiis49dRTOfHEE5k+fTo777wzl156KQAXXHAB++23HxtttNGI7SVJktQtE+rxaWPx0EMPcdlll/HmN7/56XmPPfYYAEcccQRf/OIX2XfffVmwYAEnnnjiattLkqTumnf2vDGtt/iYxX2uROvLpA/CTz31FFtssQVXXXXVLyw75JBDeP/73899993HFVdcwa//+q/z8MMPr7K9JEmSumPSD43YfPPNmT17Nueeey7QvPDi6quvBponTOy555685z3v4eCDD2bKlCmrbS9JkqTumHRB+JFHHmFoaOjpr49+9KOcc845nHXWWey8887stNNOfPWrX326/RFHHMHnP/95jjjiiKfnra69JEmSumHSDY1Y+RSI4S6++OIR5x9++OFU1TPmzZ49e8T28+fPX+f6JEmSNDlMuh5hSZIkqR8MwpIkSeokg7AkSZI6ySAsSZKkTjIIS5IkqZMMwpIkSeokg/AILr74YnbccUd22GEHTjnllEGXI0mSpHEwoZ8jPOvki/q6vSWnHLTGNk8++STvete7+MY3vsHQ0BB77LEHhxxyCHPnzu1rLZIkSRose4SH+cEPfsAOO+zAi170IjbeeGOOPPJI3zwnSZK0ATIID3P77bczc+bMp6eHhoa4/fbbB1iRJEmSxoNBeJjhr2MGSDKASiRJkjSeDMLDDA0NsXTp0qenly1bxrbbbjvAiiRJkjQeDMLD7LHHHvz4xz/mtttu4/HHH2fBggUccsghgy5LkiRJfTaqIJxk/yQ3Jbk5yckjLJ+e5IIkVye5Lsk7+l/q+jF16lQ++clPst9++zFnzhze8pa3sNNOOw26LEmSJPXZGh+flmQKcDrwemAZcHmS86vq+p5m7wKur6o3JpkB3JTknKp6fF2KG83jzsbDgQceyIEHHjiQfUuSJGn9GE2P8J7AzVV1axtsFwCHDmtTwGZp7irbFLgPeKKvlUqSJEl9NJogvB2wtGd6WTuv1yeBOcAdwGLgPVX11PANJTk+yaIki5YvXz7GkiVJkqR1N5ogPNKzw4Y/Y2w/4CpgW2AX4JNJNv+FlarO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\n",
      "text/plain": [
       "<Figure size 864x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "occ_cht('Smoking')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:title={'center':'Lungs Disease Based on Passive Smoker'}, xlabel='Passive Smoker'>"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 864x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "occ_cht('Passive Smoker')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:title={'center':'Lungs Disease Based on Shortness of Breath'}, xlabel='Shortness of Breath'>"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 864x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "occ_cht('Shortness of Breath')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:title={'center':'Lungs Disease Based on Wheezing'}, xlabel='Wheezing'>"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 864x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "occ_cht('Wheezing')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:title={'center':'Lungs Disease Based on Frequent Cold'}, xlabel='Frequent Cold'>"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 864x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "occ_cht('Frequent Cold')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "#declaration of header files\n",
    "\n",
    "from sklearn.model_selection import train_test_split \n",
    "from sklearn.preprocessing import StandardScaler \n",
    "from sklearn.metrics import accuracy_score, classification_report, roc_auc_score, roc_curve, RocCurveDisplay\n",
    "from sklearn.metrics import r2_score, precision_score, recall_score, f1_score\n",
    "from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay\n",
    "from sklearn import metrics"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from xgboost import XGBClassifier \n",
    "from sklearn.svm import SVC \n",
    "from sklearn.neighbors import KNeighborsClassifier \n",
    "from sklearn.tree import DecisionTreeClassifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "#declare independent variables in 'x' & dependent variable in 'y'\n",
    "\n",
    "X = df.drop('Level', axis=1) \n",
    "y = df['Level']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Shape of Independent variables - X Training: (880, 13) and X Testing (220, 13)\n",
      "Shape of dependent variable - Y Training: (880,) and Y Testing (220,)\n",
      "\n",
      "Training output counts\n",
      "Level\n",
      "2    304\n",
      "1    290\n",
      "0    286\n",
      "Name: count, dtype: int64\n",
      "\n",
      "Testing output counts\n",
      "Level\n",
      "2    94\n",
      "1    76\n",
      "0    50\n",
      "Name: count, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "#spliting 80% datas as train data(X_train, y_train) & 20% datas as test data(X_test, y_test)\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "print(f'Shape of Independent variables - X Training: {X_train.shape} and X Testing {X_test.shape}')\n",
    "print(f'Shape of dependent variable - Y Training: {y_train.shape} and Y Testing {y_test.shape}')\n",
    "\n",
    "print(f'\\nTraining output counts\\n{y_train.value_counts()}')\n",
    "print(f'\\nTesting output counts\\n{y_test.value_counts()}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Data preprocesing \n",
    "scaler = StandardScaler()\n",
    "X_train_stdscr = scaler.fit_transform(X_train)\n",
    "X_test_stdscr = scaler.transform(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Model Accuracies\n",
    "mdl_accuracies = dict()\n",
    "# Convert the target variable 'y' to integers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "models = { \n",
    "\n",
    "    \"Logistic Regression\": (LogisticRegression(), { \n",
    "        'C': [0.01, 0.1, 1, 10], \n",
    "        'solver': ['lbfgs', 'liblinear'] \n",
    "    }), \n",
    "\n",
    "    \"kNN\":  (KNeighborsClassifier(), { \n",
    "        'n_neighbors': [3, 5, 7, 9], \n",
    "        'weights': ['uniform', 'distance'], \n",
    "        'metric': ['euclidean', 'manhattan'] \n",
    "    }), \n",
    "\n",
    "    \n",
    "    \"SVM\": (SVC(probability=True), { \n",
    "        'C': [0.1, 1, 10], \n",
    "        'kernel': ['linear', 'rbf'], \n",
    "        'gamma': ['scale', 'auto'] \n",
    "    }),\n",
    "\n",
    "     \"Decision Tree\": (DecisionTreeClassifier(), { \n",
    "        'max_depth': [None, 10, 20, 30], \n",
    "        'min_samples_split': [2, 5, 10] \n",
    "    }), \n",
    "\n",
    "    \"Random Forest\": (RandomForestClassifier(), { \n",
    "        'n_estimators': [100, 200, 300], \n",
    "        'max_depth': [None, 10, 20, 30], \n",
    "        'min_samples_split': [2, 5, 10] \n",
    "    }), \n",
    "\n",
    " \n",
    "     \"XGBoost\":(XGBClassifier(use_label_encoder=False, eval_metric='logloss'), { \n",
    "        'n_estimators': [100, 200, 300], \n",
    "        'learning_rate': [0.01, 0.1, 0.2], \n",
    "        'max_depth': [3, 6, 9] \n",
    "    })\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Function to evaluate the model\n",
    "def evaluate_model_1(name, model, param_grid, X_train, X_test, y_train, y_test): \n",
    "    mdl = model.fit(X_train, y_train)\n",
    "    y_pred  = mdl.predict(X_test)\n",
    "    y_prob = mdl.predict_proba(X_test)[:, 1]\n",
    "    \n",
    "    accuracy = accuracy_score(y_test, y_pred)\n",
    "    precision = precision_score(y_test, y_pred,  average='micro')\n",
    "    f1 = f1_score(y_test, y_pred, average='micro')\n",
    "    recall = recall_score(y_test, y_pred, average='micro')\n",
    "    \n",
    "    roc_scr = roc_auc_score(y_test, mdl.predict_proba(X_test), multi_class='ovr')\n",
    "    fpr, tpr, thresholds = roc_curve(y_test, y_prob, pos_label=2)\n",
    "    auc = metrics.auc(fpr, tpr)\n",
    "    r2 = r2_score(y_test, y_pred)\n",
    "    \n",
    "    mdl_accuracies[name] = accuracy_score(y_test, y_pred)\n",
    "\n",
    "    print(f\"\\nModel Name : {name}\\n\")\n",
    "    print(f\"\\t Accuracy : {accuracy}\\t ROC_AUC_Score : {roc_scr}\\t AUC: {auc}\\t  R2_Score : {r2}\\n\")\n",
    "    print(f\"\\t Precision : {precision}\\t F1 Score : {f1}\\t Recall: {recall}\\n\")\n",
    "\n",
    "    \n",
    "    print(classification_report(y_test, y_pred))\n",
    "    \n",
    "    disp = ConfusionMatrixDisplay(confusion_matrix(y_test, y_pred))\n",
    "    disp.plot()\n",
    "    plt.show()\n",
    "    print(\"__________________________________________________________________\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Model Name : Logistic Regression\n",
      "\n",
      "\t Accuracy : 0.9272727272727272\t ROC_AUC_Score : 0.9731694796806366\t AUC: 0.19731509625126648\t  R2_Score : 0.8150887573964497\n",
      "\n",
      "\t Precision : 0.9272727272727272\t F1 Score : 0.9272727272727272\t Recall: 0.9272727272727272\n",
      "\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.87      0.94      0.90        50\n",
      "           1       0.93      0.89      0.91        76\n",
      "           2       0.96      0.95      0.95        94\n",
      "\n",
      "    accuracy                           0.93       220\n",
      "   macro avg       0.92      0.93      0.92       220\n",
      "weighted avg       0.93      0.93      0.93       220\n",
      "\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "__________________________________________________________________\n",
      "\n",
      "Model Name : kNN\n",
      "\n",
      "\t Accuracy : 0.9454545454545454\t ROC_AUC_Score : 0.9711710661806094\t AUC: 0.19896149949341438\t  R2_Score : 0.8224852071005917\n",
      "\n",
      "\t Precision : 0.9454545454545454\t F1 Score : 0.9454545454545454\t Recall: 0.9454545454545454\n",
      "\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.94      0.90      0.92        50\n",
      "           1       0.91      0.99      0.95        76\n",
      "           2       0.98      0.94      0.96        94\n",
      "\n",
      "    accuracy                           0.95       220\n",
      "   macro avg       0.94      0.94      0.94       220\n",
      "weighted avg       0.95      0.95      0.95       220\n",
      "\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "__________________________________________________________________\n",
      "\n",
      "Model Name : SVM\n",
      "\n",
      "\t Accuracy : 0.9363636363636364\t ROC_AUC_Score : 0.9855463843432112\t AUC: 0.16818642350557245\t  R2_Score : 0.8964497041420119\n",
      "\n",
      "\t Precision : 0.9363636363636364\t F1 Score : 0.9363636363636364\t Recall: 0.9363636363636364\n",
      "\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.92      0.96      0.94        50\n",
      "           1       0.91      0.91      0.91        76\n",
      "           2       0.97      0.95      0.96        94\n",
      "\n",
      "    accuracy                           0.94       220\n",
      "   macro avg       0.93      0.94      0.94       220\n",
      "weighted avg       0.94      0.94      0.94       220\n",
      "\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "__________________________________________________________________\n",
      "\n",
      "Model Name : Decision Tree\n",
      "\n",
      "\t Accuracy : 0.9590909090909091\t ROC_AUC_Score : 0.970285744259132\t AUC: 0.21437014522120906\t  R2_Score : 0.8446745562130178\n",
      "\n",
      "\t Precision : 0.9590909090909091\t F1 Score : 0.9590909090909091\t Recall: 0.9590909090909091\n",
      "\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.94      0.96      0.95        50\n",
      "           1       0.95      0.99      0.97        76\n",
      "           2       0.98      0.94      0.96        94\n",
      "\n",
      "    accuracy                           0.96       220\n",
      "   macro avg       0.96      0.96      0.96       220\n",
      "weighted avg       0.96      0.96      0.96       220\n",
      "\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "__________________________________________________________________\n",
      "\n",
      "Model Name : Random Forest\n",
      "\n",
      "\t Accuracy : 0.9454545454545454\t ROC_AUC_Score : 0.9976881625519437\t AUC: 0.18887200270178992\t  R2_Score : 0.8224852071005917\n",
      "\n",
      "\t Precision : 0.9454545454545454\t F1 Score : 0.9454545454545454\t Recall: 0.9454545454545454\n",
      "\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.88      0.98      0.92        50\n",
      "           1       0.96      0.93      0.95        76\n",
      "           2       0.98      0.94      0.96        94\n",
      "\n",
      "    accuracy                           0.95       220\n",
      "   macro avg       0.94      0.95      0.94       220\n",
      "weighted avg       0.95      0.95      0.95       220\n",
      "\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "__________________________________________________________________\n",
      "\n",
      "Model Name : XGBoost\n",
      "\n",
      "\t Accuracy : 0.9636363636363636\t ROC_AUC_Score : 0.9981838863080382\t AUC: 0.1388044579533941\t  R2_Score : 0.8742603550295858\n",
      "\n",
      "\t Precision : 0.9636363636363636\t F1 Score : 0.9636363636363636\t Recall: 0.9636363636363636\n",
      "\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.91      0.98      0.94        50\n",
      "           1       0.97      0.96      0.97        76\n",
      "           2       0.99      0.96      0.97        94\n",
      "\n",
      "    accuracy                           0.96       220\n",
      "   macro avg       0.96      0.97      0.96       220\n",
      "weighted avg       0.97      0.96      0.96       220\n",
      "\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "__________________________________________________________________\n"
     ]
    }
   ],
   "source": [
    "for name, (model, param_grid) in models.items(): \n",
    "    evaluate_model_1(name, model, param_grid, X_train, X_test, y_train, y_test) \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
