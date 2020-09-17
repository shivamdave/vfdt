
import subprocess

subprocess.popen()
args = shlex.split(exp.cmd)

subprocess.Popen(args, stdout=open(output_file, "w+"))