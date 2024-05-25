Introduction
Error Log Monitor is a Python script that processes a log of error entries and performs certain queries on it.

Requirements
Python 3.6 or higher


Usage

First, create a file named input.txt in the same directory as script.py. In this file, provide the input in the following format:

Each line contains either an error log entry or a query.

An error log entry is of the form "timestamp;log_type;severity". For example: "1631079300;NETWORK;2.5".

A query can be one of the following types:

"2 log_type" - returns the stats for all entries of the given log_type.

"3 BEFORE timestamp" - returns the stats for all entries that occurred before the given timestamp.

"3 AFTER timestamp" - returns the stats for all entries that occurred after the given timestamp.

"4 log_type BEFORE timestamp" - returns the stats for all entries of the given log_type that occurred before the given timestamp.

"4 log_type AFTER timestamp" - returns the stats for all entries of the given log_type that occurred after the given timestamp.

Run the script using the command python script.py.

The script will process the input and create a file named output.txt in the same directory.

The output file will contain the results of each query, one per line.

Input.txt: 

1715744138011; INTERNAL_SERVER_ERROR; 23.72

1715744138012; INTERNAL_SERVER_ERROR; 10.17

INTERNAL_SERVER_ERROR

1715744138012; BAD_REQUEST; 15.22

1715744138013; INTERNAL_SERVER_ERROR; 23.72

BEFORE 1715744138011

AFTER 1715744138010

BAD_REQUEST

BEFORE INTERNAL_SERVER_ERROR 1715744138011

AFTER INTERNAL_SERVER_ERROR 1715744138010


Output.txt:

No output 

No output

Min: 10.17 , Max: 23.72 , Mean: 16.945 

No output

No output

Min: 0.0 , Max: 0.0 , Mean: 0.0

Min: 10.17, Max: 23.72, Mean: 18.2075

Min: 15.22, Max: 15.22, Mean: 15.22 

Min: 0.0 , Max: 0.0 , Mean: 0.0

Min: 10.17, Max: 23.72, Mean: 19.203333



Assumptions:
1. Timestamp will come in an ascending sorted way.
2. Log Type can be any utf-8 supported string with a maximum length of 100.
3. . Severity will be positive non zero floating-point number with no limit.


Expectations
1. Program need to be fast enough to handle al functionalities.
2. Severity results must need to be calculated with a precision of 10E-6. 3. Only use the standard libraries your programming language provides.
