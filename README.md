## Create a virtual enviroment
```
python -m venv env
```
 Should create a folder called `env`


## Activate virtual enviroment (bash)
```
source ./env/Scripts/activate
```

## Exit from virtual enviroment (bash)
```
deactivate
```

## Install a package
```
pip install python-dateutil
```

## Uninstall a package
```
pip uninstall python-dateutil
```

## List all dependencies
```
pip freeze
```

## Create file with all dependencies 
```
pip freeze > requirements.txt
```

## Install dependencies from requirements file
```
pip install -r requirements.txt
```

## Uninstall all dependencies from requirements file
```
pip uninstall -r requirements.txt -y
```


## Install specific version
```
pip install python-dateutil===1.4
```

## Update a package
```
pip install <name of package> --upgrade
```

