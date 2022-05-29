# The PageRank

This is a semister project for Linear Algebra course at Ukrainian Catholic University aimed at ranking web pages' importance based on Google's PageRank algorithm.

### Implementation

We made 3 implementations of the PageRank algorithm here:

* Eigendecomposition

* Power Method with epsilon

* Power Method without epsilon

### Usage

To run a simple example on generated data:

```bash
python3 src/pagerank.py
```

To test the productivity of each method:

```bash
python3 src/timings.py
```

To run the algorithm on real data:

```bash
python3 src/dataset_example.py
```

### Data

For demonstration we used data from open resourses. This dataset of parsed links from Hollins University website is quite old, though it demonstrates the work of the algorithm pretty well. You don't need to download the dataset, it is already present in the ```data``` folder, though you can do it using this [link](https://www.limfinity.com/ir/data/hollins.dat.gz).


### Contributors

* [Bohdan Ruban](https://github.com/iamthewalrus67)
* [Ostap Trush](https://github.com/Adeon18)
* [Olexiy Hoyev](https://github.com/alexg-lviv)

### Results

All of the steps and conclusions are described in this pdf [document](PageRank.pdf).