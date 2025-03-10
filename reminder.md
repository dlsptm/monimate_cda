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



INSERT INTO public."user" (id, email, username, password, active, role, created_at, last_active) VALUES ('44060963-dae2-44a7-aeef-26ef59e1cf92', 'dlsptm6981@gmail.com', 'dlsptm', 'password', true, '"[\"ROLE_ADMIN\"]"', '2024-12-22 17:32:47.537226', null);
INSERT INTO public."user" (id, email, username, password, active, role, created_at, last_active) VALUES ('33b368e7-5a05-403c-b1f5-559885bdd854', 'inesberber92@gmail.com', 'inespereeyt', '2432622431322447324e493241387a57684b33746a675a4b557746452e376d574f4271733131716a2e7333304b7365586b5041443749314772373843', false, '"[\"ROLE_USER\"]"', '2024-12-23 18:54:00.643835', null);
