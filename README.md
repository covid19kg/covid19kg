
# COVID-19 Knowledge Graph [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3748950.svg)](https://doi.org/10.5281/zenodo.3748950)
COVID-19 Knowledge Graph: a computable, multi-modal, cause-and-effect knowledge model of COVID-19 pathophysiology.

## Resource
This Knowledge Graphs comprises information encoded in Biological Expression Language (BEL) for a selected corpus around
COVID-19. A [summary of the corpus](https://github.com/covid19kg/covid19kg/blob/master/supplement/summary.csv) is listed
here. Additional information about customized terms used is available [here](https://github.com/covid19kg/covid19kg/blob/master/supplement/).

### Citation
Daniel Domingo-Fernández, Shounak Baksi, Bruce T Schultz, Yojana Gadiya, Reagon Karki, Tamara Raschka, Christian Ebeling, Martin Hofmann-Apitius, and Alpha Tom Kodamullil (2020). [COVID-19 Knowledge Graph: a computable, multi-modal, cause-and-effect knowledge model of COVID-19 pathophysiology](https://doi.org/10.1101/2020.04.14.040667). *bioRxiv* 2020.04.14.040667. 

### Formats
Although the COVID-19 KG was generated using BEL, it can also be exported to multiple standard formats:

- [Edgelist](https://networkx.github.io/documentation/stable/reference/readwrite/edgelist.html) (.lst)
- Node-Link (.json)
- [GML](http://graphml.graphdrawing.org) (.gml or .xml)
- [GraphML](http://docs.yworks.com/yfiles/doc/developers-guide/gml.html) (.graphml or .xml)
- [SIF](http://www.cbmc.it/fastcent/doc/SifFormat.htm) (.csv, .tsv, or .txt)
- [Pickle](https://docs.python.org/3/library/pickle.html) 
- [CX](https://home.ndexbio.org/data-model/) (.cx)
- [JGF](https://jsongraphformat.info/) (.jgif)

### Releases
The table below contains information of the different releases of the COVID-19 KG. Each release contains the original BEL files are aforementioned formats before.

| Release | Date       | Articles |
|---------|------------|----------|
| 0.0.1   | [12.04.2020](https://github.com/covid19kg/covid19kg/blob/master/releases/12-04-2020.zip) | 145      |
| 0.0.2   | [15.05.2020](https://github.com/covid19kg/covid19kg/blob/master/releases/15-05-2020.zip) | 160      |

## Python Package [![DOI](https://img.shields.io/pypi/pyversions/diffupy.svg)](https://doi.org/10.5281/zenodo.3748950)
The COVID-19 Knowledge Graph can be programmatically used as a Python package. 

### Installation
To install the ``covid19kg`` Python package for programmatic access to the BEL files in this repository, use the
following code in your shell:

```
git clone https://github.com/covid19kg/covid19kg.git
cd covid19kg
pip install -e .
```
   
### Commands
To see all the commands, simply run:

```
covid19kg
 ```   
### Usage
To get the BEL graph, use the following code in Python:

```
>>> import covid19kg
>>> graph = covid19kg.get_graph()
>>> graph.summarize()
```

### Disclaimer
The COVID-19 Knowledge Graph is a resource developed in an academic capacity funded by Fraunhofer-Gesellschaft zur Förderung der angewandten Forschung e. V., and thus comes with no warranty or guarantee of maintenance or support.
