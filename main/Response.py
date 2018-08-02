#!/usr/bin/python
#FileName: Response.py
#Author: Adivikolanu Teja Priyanka
#Purpose: builds the json response

#import statements
from flask import Flask
from flask.json import jsonify

#FunctionName: Build_Json_Response
#Purpose: builds the json response 
#Arguments: Accepts two argument on type string and int
#           1) msg - type string - message to be displayed in the response
#           2) code - type int - status code for the response.
#Return Value: Returns the response in json format


def Build_Json_Response(msg,code):
    response=jsonify(message=(str(msg)))
    response.status_code = code
    return response