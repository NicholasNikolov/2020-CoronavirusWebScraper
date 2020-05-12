# 2020-CoronavirusWebScraper
 I attempted to create a Covid-19 webscraper but unfortunately the site was too unexpectedly dynamic, releasing new changes to the table I was pulling from on a frequent basis. The latest April 09 update has made my code completely unusable. I will likely still explore a solution for practice, but sadly a lot of data collection will be lost.
 
 Ultimately, the project presented a valuable lesson. I learned to run scheduled Py Scripts as well as recognizing the need for versatility in web-scraping. Since HTML tables are presented as a series of <td> and <tr> tags, BeautifulSoup would naturally pull all results from the table. When Worldometers created a filterable table (filter by continent) it made it more difficult to capture data.
 
 For the future, I will be more cognizant of the HTML table format. Every row is represented with <tr> so I can produce a script that counts the number of entries in the first <tr> and can automatically adapt to changes in the number of columns by adding new values. Addtionally, I would need to consider methods to avoid counting duplicates. 

Project Progress: Closed [Project Failed - Discontinued]

Data Source: https://www.worldometers.info/coronavirus Note: Above data source is not a formatted source like other projects. The data was taken using a web scraper.

Question/Concerns?

Email me at Nikolovnickv@gmail.com

Thank you!
