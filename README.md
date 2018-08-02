# fibonacci-sequence-api

To install the requirements:
    pip install -r requirements.txt

Asumptions:
    The service will return [0] if the size is 1
    The service will return [0, 1] if the size is 2
    The maximum limit is 10000
    all the commands in this file are based on pwd being the project folder fibonacci-sequence-api

Logfile:
    Logfile will be stored in below location.
    fibonacci-sequence-api/Fibonacci.log

To run the application:
    python main/Fibonacci_Rest.py

To run the testcases:
    python -m pytest tests/test_Fibonacci.py
    
To test in your browser:
    http://localhost:5000/fibonacci/<size>
    example, http://localhost:5000/fibonacci/10

To test using curl command:
    curl -i -X GET "http://localhost:5000/fibonacci/10"

    invalid path with negative number or 0- returns 400
    curl -i -X GET "http://localhost:5000/fibonacci/-10"

    invalid http method - returns 405
    curl -i -X POST "http://localhost:5000/fibonacci/100"

    invalid path - returns 404
    curl -i -X GET "http://localhost:5000/fibonacci/abcd/abcd"
    
To test using POSTMAN:
curl -X GET \
  http://127.0.0.1:5000/fibonacci/12 \
  -H 'Accept: application/json' \
  -H 'Cache-Control: no-cache' \
  -H 'Postman-Token: 89b46c52-e5cb-4ba9-96a1-e7a208fdd801'

Cloud:
To test using cloud URI :
curl -X GET \
  https://priyanka-fibonacci.cfapps.io/fibonacci/122 \
  -H 'Accept: application/json' \
  -H 'Cache-Control: no-cache' \
  -H 'Postman-Token: a2868b8e-bd79-4ca9-bd14-a180eceb8c90'
  
To deploy app on pivotal cloud foundary:
    cf push fibonacci  
