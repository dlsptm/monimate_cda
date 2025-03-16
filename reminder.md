## List of packages
```
pip freeze > requirements.txt  
```


## Install all needed packages
```
 pip install -r requirements.txt
```

## Install migrate
```
 pip install migrate
```
###  database (only once)
```
 flask db init
```
###  migration
```
 flask db migrate
```

###  upgrade 
```
 flask db upgrade
```

## Test url via terminal 
### GET
```
curl http://127.0.0.1:5555/greet/ines
```
### Méthode personalisé
```
curl -X POST http://127.0.0.1:5555/greet/ines
```

## Tester avec info
### GET
```
curl -I http://127.0.0.1:5555/greet/ines
```
### Méthode personalisé
```
curl -X POST -I http://127.0.0.1:5555/greet/ines
```