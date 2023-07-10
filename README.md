# Web-scraping
Scrape a website and also analyse the residual from linear regression.

Behind the scenes, your program will
• fetch the web page at https://discoveratlanta.com/events/all/ • parse the result using BeautifulSoup and html.parser
• step through each article inspecting the dates of the events
• skip articles that do not contain the desired date
• for articles that have the desired date, note the title and the URL • make a dataframe with all the titles and URLs
• write the dataframe to an ExcelWriter
• resize the columns to be a reasonable width
• write it to the file named on the command line
You are putting data into only 2 columns – Don’t include the dataframe’s index in the excel file.




