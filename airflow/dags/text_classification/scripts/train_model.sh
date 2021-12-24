ML_HOME=/home/stanislav/Hadoop
echo Start training...
source $ML_HOME/venv/bin/activate
python3 $ML_HOME/train_model.py
echo Train complete!
