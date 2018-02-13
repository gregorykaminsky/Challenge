## INPUT ASSUMPTIONS:

input data must be located contained in files `input/itcont.txt`, `input/percentile.txt` <br />
Structure as described by FEC.

* LINE: splitting a line entry by '|' divider must yield an array of 21 entries, some of which may be empty. 
* NAME: consists of two parts (lastname, firstname) separated by a comma, neither lastname field nor firstname are empty
* ZIP_CODE: is either a five digit or nine digit number, no spaces in between, only numerical digits allowed
* TRANSACTION_DT: has to be a valid date, the  1776 <= year <= today, record cannot extend before United States was founded
* TRANSACTION_AMT: has to be convertible to a float and cannot be negative
* `percentile.txt` contains a single number entry, such that: `0 < entry < 100`

## STRUCTURE:
As defined in the README of the challenge. 
