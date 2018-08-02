#!/usr/bin/python

#FileName: Fibonacci_Rest.py
#Author: Adivikolanu Teja Priyanka
#Purpose: creating a RESTful service for generating the fibonacci numbers

#import statements
import os
import GenerateFibonacci
import Response
from flask import Flask, json
from flask_restful import Api, Resource

#Creating the Flask app
app = Flask(__name__)

api=Api(app)
app.logger.info('Created flask app')


class Fibonacci_Series(Resource):

	#implementing the get method
	def get(self, Size):
		app.logger.info('size is %d', Size)
		if Size <= 0:		#checking for negative or 0 Size and responding with appropriate error message and status code
			app.logger.error('Invalid Size: Size must be a positive integer greater than 0 - status code 400')
			return Response.Build_Json_Response('Invalid Size: Size must be a positive integer greater than 0',400)
		elif Size >10000:	# checking the max limit of size and responding with appropriate error message and status code
			app.logger.error('Size cannot be greater than 10000. Please pass a positive integer < 10000 - status code 400')
			return Response.Build_Json_Response('Size cannot be greater than 10000. Please pass a positive integer < 10000',400)
		else: 				#generating the fibonacci sequence if size is valid
			fib=str(GenerateFibonacci.Generate_Fibonacci(Size))
			res=Response.Build_Json_Response(fib,200)
			app.logger.info("generated fibonacci sequence %s - status code %d" , fib,res.status_code )
			return res

#defining the url		
api.add_resource(Fibonacci_Series,"/fibonacci/<int:Size>")

#handling invalid paths
@app.route('/fibonacci/<invalid_path>')
def handle_invalid_path(invalid_path):
	app.logger.info('size is %s', invalid_path)
	app.logger.error('Invalid Size: Size must be a positive integer greater than 0 - status code 400')
	return Response.Build_Json_Response('Invalid Size: Size must be a positive integer greater than 0',400)

#handling page not found exception
@app.errorhandler(404)
def page_not_found(e):
	app.logger.exception('exception generated - Page not found - status code 404')
	return Response.Build_Json_Response('Page not found',404)

#handling invalid method exception
@app.errorhandler(405)
def method_not_allowed(e):
	app.logger.exception('exception generated - The method is not allowed for the requested URL. - status code 405')
	return Response.Build_Json_Response('The method is not allowed for the requested URL.',405)

#unhandled exceptions
@app.errorhandler(Exception)
def Unhandled_Exceptions(e):
	app.logger.exception('exception generated - %s - status code 500', str(e) )
	return Response.Build_Json_Response(str(e),500)

#starting the app	
if __name__ == '__main__':
	app.run()