# Homework-4-Regex
Wrote small programs to find data type of an input, all pdf files in list, emails on webpage, and happiness text rater


Notes:

Email scraper:        
-Outputs any email addresses that look like “xxx@xxx.xxx.xxx” with any number of dots after the @-sign on this page. Function gets around tricks people use to hide their email addresses, such as
     hangjie@math.ucla.edu
     hangjie AT math DOT ucla DOT edu
     hangjie at math dot ucla dot edu
     hangjie[AT]ucla[DOT]edu
     hangjie[at]ucla[dot]edu
     

Happiness Rater:      
-Wrote a function happiness(text) that uses the Dodds et al happiness dictionary [1] to rate the happiness of a piece of english text (input as a single string). The happiness score is the average score over all words in the text that appear in the dictionary.


References
[1] Peter Sheridan Dodds, Kameron Decker Harris, Isabel M Kloumann, Catherine A Bliss, and Christopher M Danforth. Temporal patterns of happiness and information in a global social network: Hedonometrics and twitter. PloS one, 6(12):e26752, 2011.

