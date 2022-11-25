import os
import subprocess
import sys


dir = os.getcwd()

RPA_categoria_filepath = str(dir)+"/RPA_categoria.py"
RPA_composicion_filepath = str(dir)+"/RPA_composicion.py"
RPA_difusion_filepath = str(dir)+"/RPA_difusion.py"
RPA_evento_filepath = str(dir)+"/RPA_evento.py"
RPA_temporadas_filepath = str(dir)+"/RPA_temporadas.py"
RPA_centro_filepath = str(dir)+"/RPA_centro.py"


def execute_processes(py_filepath):
    args = '"%s" "%s" "%s"' % (sys.executable,                  # command
                            py_filepath,                     # argv[0]
                            os.path.basename(py_filepath))   # argv[1]

    process1 = subprocess.run(args)
    print('subproceso finalizado')
    
execute_processes(RPA_categoria_filepath)
execute_processes(RPA_composicion_filepath)
execute_processes(RPA_difusion_filepath)
execute_processes(RPA_evento_filepath)
execute_processes(RPA_temporadas_filepath)
execute_processes(RPA_centro_filepath)
