ML_HOME=/home/stanislav/Hadoop
echo Start loading...
source $ML_HOME/venv/bin/activate
python3 $ML_HOME/load_data.py
echo Load complete!
