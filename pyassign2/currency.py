#!/usr/bin/env python3

"""Module for currency exchange

This module provides several string parsing functions to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange.

__author__ = "Xiangtao Hu"
__pkuid__  = "1700011768"
__email__  = "white_emperor@pku.edu.cn"
"""

def before_space(s):
    """Returns: Substring of s; up to, but not including, the first space 
    Parameter s: the string to slice
    Precondition: s has at least one space in it 
    """
    place_of_space=s.find(" ")
    return s[:place_of_space]

def after_space(s):
    """Returns: Substring of s after the first space 
    Parameter s: the string to slice
    Precondition: s has at least one space in it 
    """
    place_of_space=s.find(" ")
    return s[(place_of_space+1):]

def first_inside_quotes(s):
    """Returns: The first substring of s between two (double) quote characters 
    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters inside.
    """
    x1=s.find('"')
    x2=s[(x1+1):].find('"')
    return s[(x1+1):x2]

def get_from(json):
    """Returns: The FROM value in the response to a currency query. 
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query 
    """
    x=json.find(":")
    return first_inside_quotes(json[x:])

def get_to(json):
    """Returns: The TO value in the response to a currency query. 
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query
    """ 
    x1=json.find(":")
    x2=json[(x1+1):].find(":")+x1+1
    return first_inside_quotes(json[x2:])

def has_error(json):
    """Returns: True if the query has an error; False otherwise.
    Parameter json: a json string to parse
    Precondition: json is the response to a currency query 
    """
    return "false" in json

def currency_response(currency_from,currency_to,amount_from):
    """Returns: a JSON string that is a response to a currency query.
    
    A currency query converts amount_from money in currency currency_from 
    to the currency currency_to. The response should be a string of the form
    
        '{"from":"<old-amt>","to":"<new-amt>","success":true, "error":""}'
    
    where the values old-amount and new-amount contain the value and name 
    for the original and new currencies. If the query is invalid, both 
    old-amount and new-amount will be empty, while "success" will be followed 
    by the value false.
    
    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string
    
    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string
    
    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    from urllib.request import urlopen
    doc=urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+currency_from+'&to='+currency_to+'&amt='+str(amount_from))
    docstr=doc.read()
    doc.close()
    return docstr.decode('ascii')

def is_currency(currency):
    """Returns: True if currency is a valid (3 letter code for a) currency. 
    It returns False otherwise.

    Parameter currency: the currency code to verify
    Precondition: currency is a string."""
    json=currency_response(currency,currency,2.5)
    return not has_error(json)

def exchange(currency_from,currency_to,amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code
    
    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code
    
    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    json=currency_response(currency_from,currency_to,amount_from)
    s=get_to(json)
    return float(before_space(s))

def main():
    """main module
    """
    currency_from=input("The old currency\n")
    currency_to=input("The new currency\n")
    amount_from=float(input("The amount of the old currency\n"))
    print(exchange(currency_from,currency_to,amount_from))

if __name__ == '__main__':
    main()

"""Below are the test function module for the project
"""

def test_before_space():
    """Used to test whether the before_space function works
    """
    test1=" test1"
    if before_space(test1)=="":
        pass
    else:
        return False
    test2="   "
    if before_space(test2)=="":
        pass
    else:
        return False

def test_after_space():
    """Used to test whether the after_space function works
    """
    test1="test1 "
    if after_space(test1)=="":
        pass
    else:
        return False
    test2="   "
    if after_space(test2)=="  ":
        pass
    else:
        return False

def test_A():
    """The testing function for part A
    """
    test_before_space()
    test_after_space()

def test_first_inside_quotes():
    """Used to test whether the first_inside_quotes function works
    """
    test1='  "" test1 '
    if first_inside_quotes(test1)=="":
        pass
    else:
        return False

def test_get_from():
    """Used to test whether the get_from function works
    """
    test1='"from" : "2.5 United States Dollars", "to" : "2.0952375 Euros", "success" : true, "error" : ""' 
    if get_from(test1)=="2.5 United States Dollars":
        pass
    else:
        return False

def test_get_to():
    """Used to test whether the get_to function works
    """
    test1='"from" : "2.5 United States Dollars", "to" : "2.0952375 Euros", "success" : true, "error" : "" '
    if get_to(test1)=="2.0952375 Euros":
        pass
    else:
        return False

def test_has_error():
    """Used to test whether the has_error function works
    """
    test1='"from" : "", "to" : "", "success" : false, "error" : "Exchange currency code is invalid."'
    if has_error(test1):
        pass
    else:
        return False

def test_B():
    """The test function for part B
    """
    test_first_inside_quotes()
    test_get_from()
    test_get_to()
    test_has_error()

def test_currency_response():
    """Used to test whether the currency_response function works
    """
    test1='{ "from" : "2.5 United States Dollars", "to" : "2.0952375 Euros", "success" : true, "error" : "" }'
    if currency_response("USD","EUR",2.5)==test1:
        pass
    else:
        return False

def test_C():
    """The test function for part C
    """
    test_currency_response()

def test_is_currency():
    """Used to test whether the is_currency function works
    """
    test1="USD"
    if is_currency(test1):
        pass
    else:
        return False
    test2="AAA"
    if not is_currency(test2):
        pass
    else:
        return False

def test_exchange():
    """Used to test whether the exchange function works
    """
    test1=2.0952375
    if exchange("USD","EUR",2.5)==test1:
        pass
    else:
        return False

def test_D():
    """The test function for part D
    """
    test_is_currency()
    test_exchange()

def test():
    """The test function for the project
    """
    test_A()
    test_B()
    test_C()
    test_D()
    return True
