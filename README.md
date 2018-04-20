# falcon-js-fetch-boilerplate
Python's Falcon &amp; JS fetch

## JSON request and response example using Python web framework Falcon and JavaScript fetch

### Testing
``` 
pip install -r requirements.txt
cd api 
python _server.py
cd ../client
python -m SimpleHTTPServer
```
You are all done, go to http://127.0.0.1:8000


## Middleware Classes
### RequireJSON
If request method is POST or PUT:
```
Checks if request's content-type is 'application/json',
Check if client accepts json response
```
### JSONTranslator
```
Reads request's stream and loads in json
Dumps response in json
```

#### Built With
* [Falcon Framework](https://falconframework.org/) - The web framework used
* [JS fetch() & json()](https://developer.mozilla.org/en-US/docs/Web/API/Body/json) - Api caller

