# -*- coding: utf-8 -*-

"""COVID-19 Knowledge Graph."""

import os

from bel_repository import BELMetadata, BELRepository
from bel_repository.utils import serialize_authors

__all__ = [
    'repository',
    'metadata',
    'get_graph',
    'get_graphs',
    'get_summary_df',
    'main',
]

HERE = os.path.dirname(__file__)
VERSION = '0.0.1-dev'

# Author list will be sorted by name
AUTHORS = [
    'Alpha Tom Kodamullil',
    'Daniel Domingo-Fernández',
    'Martin Hofmann-Apitius',
    'Reagon Karki',
    'Shounak Baksi',
    'Yojana Gadiya',
]

# All metadata is grouped here
metadata = BELMetadata(
    name='COVID-19 Knowledge Graph',
    version=VERSION,
    authors=serialize_authors(AUTHORS),
    contact='alpha.tom.kodamullil@scai.fraunhofer.de',
    description="Knowledge graph for analysis of COVID-19 disease and potential drug and drug-targets.",
    license='Creative Commons Zero v1.0 Universal',
)

repository = BELRepository(
    HERE,
    metadata=metadata,
)

get_graph = repository.get_graph
get_graphs = repository.get_graphs
get_summary_df = repository.get_summary_df

main = repository.build_cli()
