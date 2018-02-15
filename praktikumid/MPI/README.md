# Sissejuhatus MPI programmeerimisse Pythoniga.

MPI - Message Passing Interface
Kasutaja tasemel kontroll selle üle, kuidas protsessorid omavahel infot vahetavad.

Miks MPI? 
Siiani kõige kasutatavam standard suuremahuliste arvutuste jaoks HPC süsteemides. 

http://mpitutorial.com/tutorials/
https://mpi4py.scipy.org/docs/usrman/tutorial.html
http://materials.jeremybejarano.com/MPIwithPython/introMPI.html


Loe lähemalt: www.hpc.ut.ee

Näidete käivitamine vedur klastril (kasutame vedurit, kuna selle peal on järjekorrad üldiselt lühemad kui rocketi peal):

vajalik pythoni mooduli laadimine
* module load python-3.6.0

Seejärel teha enda kasutaja alla virtuaalkeskkond (sarnaselt Pythoni virtualenviga, aga Anaconda vahenditega), 
* conda create --name <nimi>

Aktiveeri keskkond
* source activate <nimi>

Seejärel paigaldada MPI kasutamiseks vajalikud moodulid kasutaja keskkonda:
* conda install mpi4py ipython

Lihtsamad, nagu Hello world programmi saab käivitada otse juhtsõlmel, kõik suuremaid arvutusi läbi viivad programmid tuleb käivitada läbi järjekorrahalduse süsteemi SLURM.

* git clone https://github.com/aluhamaa/parallel_computing.git

Käivita kataloogist parallel_computing/praktikumid/MPI/kood programmid, käsuga:

* mpiexec -n <np> <programmi nimi>

kus *np* on protsessori tuumade arv ja *programmi nimi* on vastava koodifaili nimetus

