from mpi4py import MPI
import subprocess

rank = MPI.COMM_WORLD.Get_rank()

a = 6.0
b = 3.0
if rank == 0:
        print (a + b)
if rank == 1:
        print (a * b)
if rank == 2:
        print (max(a,b))

host = subprocess.Popen(["hostname"], stdout=subprocess.PIPE)
print("I am process " + str(rank) +  " on " + str(host.stdout.readlines()[0]))
