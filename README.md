# APCPrices

This is A JSON file of APCs and other journal information. Data was obtained from [The Directory of Open Access Journals](https://doaj.org/faq#metadata) and the [dataset](https://github.com/FlourishOA/Data) from the amazing people behind [Flourish OA](http://flourishoa.org/). Flourish did a lot of heavy lifting here to get this data for Hybrid Journals. I am mostly just coasting on all their hard work!

Data was pulled from the DOAJ and Flourish csv files and cleaned and deduped. The result is the massive JSON file that is attached named APCPrices. It has approximately 17000 journals in it and 10401 of those journals currently have APC prices. (I'm working on adding more APC prices)

The format looks as such:

{
"Journal Title": "Current Therapeutic Research", 
"OA_Type": "Gold", 
"ISSN": ["0011-393X", "1879-0313"], 
"APC": "Yes", 
"APC Price": 1200, 
"Currency": "USD", 
"Source of APC": "DOAJ", 
"Publisher": "Elsevier", 
"Last_update": "10/02/2018"
}

