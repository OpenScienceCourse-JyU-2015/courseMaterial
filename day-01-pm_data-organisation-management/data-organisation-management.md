Title: Data organisation and management
Date: 2016-11-10  
Summary: Introduction to data management with spreadsheets and databases

---

---

# Data organisation with spreadsheets

http://www.datacarpentry.org/spreadsheet-ecology-lesson/

---
## Background
In this lesson, we're going to talk about:
* Good data entry practices - formatting data tables in spreadsheets
* How to avoid common formatting mistakes
* Dates as data - **beware!**
* Basic quality control and data manipulation in spreadsheets
* Exporting data from spreadsheets

We will NOT teach you:
* How to do *statistics* in a spreadsheet
* How to do *plotting* in a spreadsheet
* How to *write code* in spreadsheet programs

Questions:
* How many people have used spreadsheets in their research?
* What kind of operations do you do in spreadsheets?
* Which ones do you think spreadsheets are good for?

## Problems with spreadsheets
Spreadsheets good for data entry, but used for much else
* Tables for publications
* Generating statistics
* Figures

Example:
* Accidentally sorted only a single column and not the rest of the data in the spreadsheet
* What have **you** accidentally done in spreadsheets?
	* As people answer, highlight some of these issues with spreadsheets

["Gene name errors are widespread in the scientific literature" Genome Biology 2016](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-016-1044-7)
* Septin 2 (SEPT2) -> 2<sup>nd</sup> September
* RIKEN identifiers converted to floating numbers, e.g. 2310009E13

## Data entry and cleaning

Keep track of your steps!

Keep raw data raw!

Structuring data:
* All variables in columns
* Each observation in its own row
* Don't combine multiple data in one cell
* Leave the raw data raw
* Export data in text- based format  

**columns = variables, rows = observations, cells = data**

Not like this:  
![](http://www.datacarpentry.org/spreadsheet-ecology-lesson/fig/multiple-info.png)

But like this:  
![](http://www.datacarpentry.org/spreadsheet-ecology-lesson/fig/single-info.png)

Excellent (R) reference: Hadley Wickham, *Tidy Data*, Vol. 59, Issue 10, Sep 2014, Journal of Statistical Software. <http://www.jstatsoft.org/v59/i10>.

Exercise:
* Download and open data: https://ndownloader.figshare.com/files/2252083
* Two field assistants conducted the surveys, one in 2013 and one in 2014, and they both kept track of the data in their own way. Now you're the person in charge of this project and you want to be able to start doing statistics with the data.
* With the person next to you clean the data and put them all in one spreadsheet **(15 minutes)**
	* Create a new file or tab
	* **Don't modify the original data!**

## Formatting problems
Multiple tables
* http://www.datacarpentry.org/spreadsheet-ecology-lesson/fig/2_datasheet_example.jpg
* Remember: row = observation!
* Column names repeated many times

Multiple tabs
* If e.g. each day is a separate tab you might introduce inconsistencies between tabs
* Need to combine everything before analysing – extra step
* Instead, could just add new column

Not filling zeros
* To a human zero and an empty cell might be similar
* To a computer zero is a number and empty is disregarded

Bad null values
* Don't use numerical values for null! (e.g. -999)
* http://www.datacarpentry.org/spreadsheet-ecology-lesson/fig/3_white_table_1.jpg

Using formatting to convey information
* http://www.datacarpentry.org/spreadsheet-ecology-lesson/fig/formatting.png
* http://www.datacarpentry.org/spreadsheet-ecology-lesson/fig/good_formatting.png

Prettifying data with formatting
* E.g. merging cells – NO!

Commenting cells

More than one piece of info / cell
* Don't include units in cells
* Don't write e.g. 1M, 1F

Field name problems
* Avoid spaces, numbers and special characters
* Spaces and special characters can be misinterpreted by parsers
* Underscores and CamelCase are good options

Special characters in data
* Avoid copying special characters such as newlines, tabs, quotation marks etc.
* Treat cells as simple web forms – only text and spaces

Inclusion of metadata in tables
* See above
* Save metadata as separate file in same directory

## Dates as data
Dates usually stored in one column
* Not a good idea due to storing and handling problems (show example in messy data spreadsheet)
* Instead, store as separate columns: day, month, year or year, day-of-year
* NOTE: 1899-12-31 (1904 default for mac) be careful when exporting dates from Excel!
* http://www.datacarpentry.org/spreadsheet-ecology-lesson/fig/5_excel_dates_1.jpg

Excel stores dates as integers
* Counts number of days since 1899-12-31
* This makes adding and subtracting dates easy
* Be aware of this! Other programs might interpret this differently

Best practices:
* Day, month, year
	* http://www.datacarpentry.org/spreadsheet-ecology-lesson/fig/6_excel_dates_2.jpg
	* Eliminate chances of ambiguity
* Year, day-of-year
	* Easy to incorporate year as a factor, easy to calculate passage of time within year
	* How? http://www.datacarpentry.org/spreadsheet-ecology-lesson/fig/7_excel_dates_3.jpg

## Quality assurance
*Before* entering data
* Use “Data validation” or “Validity”
* Can also limit options that with drop-down list

## Quality control
*After* entering data
* Save original data with formulas
* Save new file WITHOUT formulas (moving cells can cause problems)
* Create ReadMe file tracking your manipulations

Sorting can be used to get bad values to top of bottom of column  
Conditional formatting

## Exporting data
Don't export as xls/xlsx
* Propriety format

Use universal, open, static format
* CSV
* Tab-delimited

A note on cross-platform interoperability
* Most coding and statistical environments use UNIX-style line endings (\\n)
* Windows uses its own ending (\\r\\n)
* Can be problematic when shifting data between Windows and Mac/Unix
* Can be fixed with Git (http://nicercode.github.io/blog/2013-04-30-excel-and-line-endings)
* or a small helper application(http://dos2unix.sourceforge.net/)

## Caveats of popular data and file formats
Be careful if your data contains commas as values!
* E.g. http://www.datacarpentry.org/spreadsheet-ecology-lesson/06-data-formats-caveats.html

What can you do?
* Avoid commas
* Put values in quotation marks
* Change regional settings
* Use different delimiter (Excel uses semicolons)
* Write a script (this course will help you do that!)

---

# Data management with SQL

<http://www.datacarpentry.org/sql-ecology-lesson/>

## Introduction to SQL
What we will learn:
* Subsetting
* Grouping subsets
* Performing calculations
* Combining data

This will be done in a **reproducible** fashion, **without** modifying the original data

## Basic queries
The data:
* https://figshare.com/articles/Portal_Project_Teaching_Database/1314459
* Time series for small mammal community in southern Arizona
* Studying impact of rodents and ants on plant community for almost 40 years
* 24 plots with different experimental manupulations
* Simplified version of original dataset, which has been used inover 100 publications: http://esapubs.org/archive/ecol/E090/118/

Challenge:
* What info contained in each file?
* What information can I learn about Dipodomys species in the 2000s, over time?
* What is the average weight of each species, per year?

What would I need to answer these questions? Which files have the data? What operations would I need to perform if I were doing this by hand?

We will need to:
* Select subsets of the data
* Group the subsets
* Do calculations on the data
* Combine data across spreadsheets

Whey relational databases?
* Data separate from analysis
* Fast even with large datasets
* Improved data quality (type constraints, forms in some applications)
* Relational database query concepts used in R and Python

Database management systems
* SQLite
* MySQL
* PostgreSQL
* MS Access
* FIlemaker Pro

[Let's start](http://www.datacarpentry.org/sql-ecology-lesson/00-sql-introduction.html#relational-databases)

[Basic queries](http://www.datacarpentry.org/sql-ecology-lesson/01-sql-basic-queries.html)

## Aggregation

[Aggregating data](http://www.datacarpentry.org/sql-ecology-lesson/02-sql-aggregation.html)

## Joins and aliases

[Joins and aliases](http://www.datacarpentry.org/sql-ecology-lesson/03-sql-joins-aliases.html)

---