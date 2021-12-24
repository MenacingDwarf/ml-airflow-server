ML_HOME=/home/stanislav/Pawpularity
echo Start training...
source $ML_HOME/venv/bin/activate
python3 $ML_HOME/train.py --config $ML_HOME/configs_examples/train.yaml
echo Train complete!
