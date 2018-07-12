import subprocess
import os
import copy



current_env = copy.deepcopy(os.environ)
current_env.update({"ETL_VAR": "Checkio"})

p = subprocess.check_call("/home/andrey/etl.sh", stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=current_env)
print()
print()
print()