if [ -z "$ECHECS_PYTHON_PATH" ];
then
    export ECHECS_PYTHON_PATH=$ECHECS_DIR/python/
    export PYTHONPATH=$ECHECS_PYTHON_PATH:$PYTHONPATH
fi

alias echecs-blindfold="python3 -m echecs.cli.blindfold"
