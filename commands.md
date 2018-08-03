python3 manage.py dumpdata products.Product --format json --indent 4 > products/fixtures/products.json  --> creates fixtures to backup data for a particular model


python3 manage.py loaddata products/fixtures/products.json --> loads data from created fixtures