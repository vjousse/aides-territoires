pip install geojson
sudo apt-get update
sudo apt-get install gdal-bin
sudo apt-get install libgdal-dev numpy-devel
pip install GDAL
sudo apt-get install binutils libproj-dev gdal-bin
sudo apt install postgis postgresql-12-postgis-3

* * *


from perimeters.models import Perimeter
from django.contrib.gis.utils import LayerMapping
from django.contrib.gis.gdal import DataSource
from django.db import transaction


# ds = DataSource(shape_file)

mapping = {'name': 'nom', 'insee': 'insee', 'wikipedia': 'wikipedia', 'poly': 'POLYGON'}
shape_file = '../shape/communes-20210101/communes-20210101.shp'
lm = LayerMapping(Perimeter, shape_file, mapping, transaction_mode='autocommit')
lm.save(verbose=True)

mapping = {'name': 'nom', 'insee': 'code_insee', 'wikipedia': 'wikipedia', 'poly': 'POLYGON'}
shape_file = '../shape/regions-20180101-shp/regions-20180101.shp'
lm = LayerMapping(Perimeter, shape_file, mapping, transaction_mode='autocommit')
lm.save(verbose=True)

mapping = {'name': 'nom', 'insee': 'code_insee', 'wikipedia': 'wikipedia', 'poly': 'POLYGON'}
shape_file = '../shape/departements-20180101-shp/departements-20180101.shp'
lm = LayerMapping(Perimeter, shape_file, mapping, transaction_mode='autocommit')
lm.save(verbose=True)

mapping = {'name': 'nom_epci', 'insee': 'siren_epci', 'wikipedia': 'wikipedia', 'poly': 'POLYGON'}
shape_file = '../shape/epci-20140306-5m-shp/epci-20140306-5m.shp'
lm = LayerMapping(Perimeter, shape_file, mapping, encoding='ISO-8859-1', transaction_mode='autocommit')
lm.save(verbose=True)


mapping = {'name': 'nom', 'insee': 'insee_ar', 'wikipedia': 'wikipedia', 'poly': 'POLYGON'}
shape_file = '../shape/arrondissements-20131220-5m-shp/arrondissements-20131220-5m.shp'
lm = LayerMapping(Perimeter, shape_file, mapping, transaction_mode='autocommit')
lm.save(verbose=True)
