#!/bin/bash
#SBATCH -J separate
#SBATCH -N 2
#SBATCH --ntasks-per-node=2
#SBATCH -t 00:01:10

module purge
module load python-3.6.0
source activate MPIprakt

mpirun -n 4 /gpfs/hpchome/bronto/.conda/envs/MPIprakt/bin/python separate.py
