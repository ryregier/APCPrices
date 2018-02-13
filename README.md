# APCPrices

This is a JSON file of Article Processing Charges (APC) and other journal information. Currently it has 20,347 journals. 16,635 of those journals have APC information.

Data was obtained from:
* [The Directory of Open Access Journals](https://doaj.org/faq#metadata) [dataset](https://github.com/FlourishOA/Data) 
* [Flourish OA](http://flourishoa.org/)
* [Elsevier's journal pricing list](https://www.elsevier.com/about/our-business/policies/pricing)
* [Wiley's journal pricing list](https://authorservices.wiley.com/author-resources/Journal-Authors/licensing-open-access/open-access/article-publication-charges.html)

Flourish did a lot of heavy lifting here to get this data for Hybrid Journals. I am mostly just coasting on all their hard work!

Data was exported in csv files (In the (Data folder)[https://github.com/ryregier/APCPrices/tree/master/Data])and deduped and cleaned to be added to the APCPrices JSON file. Code for the deduping and cleaning can be found in the (Data and clean-up code folder)[https://github.com/ryregier/APCPrices/tree/master/Data%20clean-up%20and%20code]

The format of the JSON file looks like:

Data was pulled from the DOAJ and Flourish csv files and cleaned and deduped. The result is the massive JSON file that is attached named APCPrices. It has approximately 17000 journals in it and 10401 of those journals currently have APC prices. (I'm working on adding more APC prices)

You can get a readable preview of the format of the JSON data in (Examplefile_APCPrices)[https://github.com/ryregier/APCPrices/blob/master/Examplefile_APCPrices].

Data is still a bit messy. There's a problem with unicode and how some characters appear that I'm trying to fix.

