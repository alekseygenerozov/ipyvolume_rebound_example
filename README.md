The code in this repository can animate
orbits from a REBOUND simulation, using
IpyVolume. (If you have not already 
done so please install this package).

I have tried to make the code fairly "universal"
for those of us who use REBOUND. For example,
the "plot_orbits_compile_archive.py" reads in data from a rebound SimulationArchive
and pre--processes. The x, y, and z data for all orbits and snapshots are stored a separate numpy arrays, and written to the files x.npz, y.npz, and z.npz.

This code takes one command line argument which is the location of
the simulation archive data you would like to animate.

Then you can open and run the included Jupyter notebook. This should produce 
an inline animation you can play. 

You should able to use this code on your own SimulationArchive, but for completeness 
I have provided some example data you can play with. Just follow these steps:

1. Download the data from here https://figshare.com/articles/archive_bin/9917228. 
For simplicity let's download it to the directory where you cloned this git repository. 
Make sure it is called archive.bin
2. Then do "python plot_orbits_compile_archive.py ./"
3. If all goes well this should produce the 3 .npz files mentioned 
above.
4. Then open and run the Jupyter notebook (make_movie.ipynb).
 
