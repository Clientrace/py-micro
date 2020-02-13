# py-microservice-template
Serverless python template for microservice clean architecture

## Run Test
Run unit test using python unittest library and evaluate code coverage
```
coverage run -m unittest -v
```

## Coverage Report
Check code coverage report
```
coverage report -m
```

## API Documentation
### Installation
Install apidoc for writing in-line REST python documentation
```
npm install apidoc -g
```

### Generate Docu
Generate REST API Documentation
```
apidoc -i endpoint/ -f ".*\\.py$" -o apidoc
```


