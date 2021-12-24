ML_HOME=/home/stanislav/Hadoop
echo Start preprocessing...
source $ML_HOME/venv/bin/activate
python3 $ML_HOME/data_preprocessing.py
echo Preprocessing complete!
