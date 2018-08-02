#!/usr/bin/python
#FileName: Response.py
#Author: Adivikolanu Teja Priyanka
#Purpose: tests the fibonacci sequence generator app

#import statements
import unittest
from main.Fibonacci_Rest import app
from flask import json


class Testfibonacci(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    #verifies the response message when negative size is passed
    def test_negative_size_error_msg(self):
       res = self.client.get('/fibonacci/-1')
       data=json.loads(res.data)
       self.assertEqual('Invalid Size: Size must be a positive integer greater than 0', data['message'])

    #verifies the response status code when negative size is passed
    def test_negative_size_returns_400(self):
       res = self.client.get('/fibonacci/-1')
       self.assertEqual(res.status_code, 400)

    #verifies the response message when size is greater than the maximum limit
    def test_maxlimit_size_error_msg(self):
       res = self.client.get('/fibonacci/10001')
       data=json.loads(res.data)
       self.assertEqual('Size cannot be greater than 10000. Please pass a positive integer < 10000', data['message'])

    #verifies the response status code when size is greater than the maximum limit
    def test_maxlimit_size_returns_400(self):
       res = self.client.get('/fibonacci/10001')
       self.assertEqual(res.status_code, 400)

    #verifies the response message when a string is passed as size
    def test_string_as_size_error_msg(self):
       res = self.client.get('/fibonacci/abcd')
       data=json.loads(res.data)
       self.assertEqual('Invalid Size: Size must be a positive integer greater than 0', data['message'])

    #verifies the response status code when a string is passed as size
    def test_string_as_size_returns_400(self):
       res = self.client.get('/fibonacci/abcd')
       self.assertEqual(res.status_code, 400)

    #verifies the response message when the size is 0
    def test_zero_as_size_error_msg(self):
       res = self.client.get('/fibonacci/0')
       data=json.loads(res.data)
       self.assertEqual('Invalid Size: Size must be a positive integer greater than 0', data['message'])

    #verifies the response status code when the size is 0
    def test_zero_as_size_returns_400(self):
       res = self.client.get('/fibonacci/0')
       self.assertEqual(res.status_code, 400)

    #verifies if the response has 'size' number of fibonacci numbers when a valid size is passed
    def test_positive_int_as_size_responds_FibSeries_of_length_size(self):
       res = self.client.get('/fibonacci/13')
       data=json.loads(res.data)
       fib_list=data.get("message")
       self.assertEqual(len(fib_list.split()), 13)

    #verifies if the response has the expected result when a valid size is passed
    def test_positive_int_as_size_responds_FibSeries(self):
       res = self.client.get('/fibonacci/7')
       data=json.loads(res.data)
       self.assertEqual('[0, 1, 1, 2, 3, 5, 8]', data['message'])

    #verifies if the response status code is 200 when a valid size is passed
    def test_positive_int_as_size_returns_200(self):
       res = self.client.get('/fibonacci/10')
       self.assertEqual(res.status_code, 200)

    #verify if invalid methods generate an error
    def test_invalid_method_post_error_msg(self):
       res = self.client.post('/fibonacci/10')
       data=json.loads(res.data)
       self.assertEqual('The method is not allowed for the requested URL.', data['message'])

    #verify status code when invalid http method is called
    def test_invalid_method_post_returns_405(self):
       res = self.client.post('/fibonacci/10')
       self.assertEqual(res.status_code, 405)

    #verify page not found error when invalid url is given
    def test_page_not_found_error_msg(self):
       res = self.client.post('/fibonacci/10/abc')
       data=json.loads(res.data)
       self.assertEqual('Page not found', data['message'])

    #verify status code for page not found error when invalid url is given
    def test_page_not_found_returns_404(self):
       res = self.client.post('/fibonacci/10/abc')
       self.assertEqual(res.status_code, 404)

if __name__ == '__main__':
    unittest.main()
