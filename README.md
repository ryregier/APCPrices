# APCPrices

This is a JSON file of Article Processing Charges (APC) and other journal information. Currently it has 21,093 journals. 17,397 journals have APC information. Of the 17,397 journals with pricing information:
* 5,758 are Hybrid and 11,639 are Gold
* 8,217 of the Gold journals have no APC (i.e. they charge $0)

Let me know if you find this dataset useful and I will try to keep it updated. Also, if you know any other sources where I can mass collect APC data, that would also be much appreciated!

Data was obtained from:
* [The Directory of Open Access Journals](https://doaj.org/faq#metadata) [dataset](https://github.com/FlourishOA/Data) - 11,100 journals
* [Flourish OA](http://flourishoa.org/) - 13,150 journals
* [Elsevier's journal pricing list](https://www.elsevier.com/about/our-business/policies/pricing) - 2,511 journals
* [Wiley's journal pricing list](https://authorservices.wiley.com/author-resources/Journal-Authors/licensing-open-access/open-access/article-publication-charges.html) - 1,458 journals
* [2015-2017 APC Averages from the OpenAPC dataset](https://treemaps.intact-project.org/apcdata/openapc/) - 2,452 journals

**Please Note** that there was a lot overlap between these providers. The Publisher lists were used as the primary source of info followed by DOAJ, Flourish, and then the Open APC averages.

Flourish did a lot of heavy lifting here to get this data for Hybrid Journals. I am mostly just coasting on all their hard work!

Data was exported in csv files located in the [Data folder](https://github.com/ryregier/APCPrices/tree/master/Data) and deduped and cleaned to be added to the APCPrices JSON file. Code for the deduping and cleaning can be found in the [Data and clean-up code folder](https://github.com/ryregier/APCPrices/tree/master/Data%20clean-up%20and%20code)

You can get a readable preview of the format of the JSON data in [Examplefile_APCPrices](https://github.com/ryregier/APCPrices/blob/master/Examplefile_APCPrices).

Data is still a bit messy. There's a problem with unicode and how some characters appear that I'm trying to fix.

