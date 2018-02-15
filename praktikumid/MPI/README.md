# Sissejuhatus MPI programmeerimisse Pythoniga.

MPI - Message Passing Interface
Kasutaja tasemel kontroll selle üle, kuidas protsessorid omavahel infot vahetavad.

Miks MPI? 



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

Esimese, Hello world programmi saab käivitada otse juhtsõlmel, kõik keerukamad programmid tuleb käivitada läbi järjekorrahalduse süsteemi SLURM.

