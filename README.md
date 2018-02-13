# APCPrices

This is a JSON file of Article Processing Charges (APC) and other journal information. Currently it has 20,347 journals. 16,635 of those journals have APC information.

Data was obtained from:
* [The Directory of Open Access Journals](https://doaj.org/faq#metadata) [dataset](https://github.com/FlourishOA/Data) 
* [Flourish OA](http://flourishoa.org/)
* [Elsevier's journal pricing list](https://www.elsevier.com/about/our-business/policies/pricing)
* [Wiley's journal pricing list](https://authorservices.wiley.com/author-resources/Journal-Authors/licensing-open-access/open-access/article-publication-charges.html)

Flourish did a lot of heavy lifting here to get this data for Hybrid Journals. I am mostly just coasting on all their hard work!

Data was exported in csv files located in the [Data folder](https://github.com/ryregier/APCPrices/tree/master/Data) and deduped and cleaned to be added to the APCPrices JSON file. Code for the deduping and cleaning can be found in the [Data and clean-up code folder](https://github.com/ryregier/APCPrices/tree/master/Data%20clean-up%20and%20code)

You can get a readable preview of the format of the JSON data in [Examplefile_APCPrices](https://github.com/ryregier/APCPrices/blob/master/Examplefile_APCPrices).

Data is still a bit messy. There's a problem with unicode and how some characters appear that I'm trying to fix.

