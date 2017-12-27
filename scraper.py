from bs4 import BeautifulSoup
from datetime import datetime
import requests, re
import pandas as pd

def findParties(textblocks):
    partyAffiliation = []
    for i, block in enumerate(textblocks):
        try:
            partydiv = block.find("p", { "class" : "partytag" }).contents[0]
            party = str(partydiv.text)
        except:
            if (i+1) <  len(textblocks):
                party = "None"
            else:
                return partyAffiliation
        finally:
            partyAffiliation.append(party)
    return partyAffiliation

def findStatements(textblocks):
    statementText = []
    try:
        for block in textblocks:
            statementdiv = block.find("div", { "class" : "text" })
            statement = ''
            for lines in statementdiv.findAll('p'):
                statement = statement + str(lines.text)
            statementText.append(statement)
    except:
        return statementText
    finally:
        return statementText

def findPrevious(statementText):
    previousStatement = []
    for i, text in enumerate(statementText):
        if i == 0:
            previousStatement.append("None")
        else:
            previousStatement.append(statementText[i - 1])

    return previousStatement

def getHTML(url):
    r = requests.get(url)
    data = r.text
    return data


def getDates(year):
    url = str('https://openparliament.ca/debates/') + str(year)
    soup = BeautifulSoup(getHTML(url), 'lxml')
    soup.prettify()
    dates =[]

    dateblocks = soup.findAll("div", { "class" : "column column-block" })

    for block in dateblocks:
        date = block.find('a').text
        date = date[:-2]
        d = datetime.strptime(date, '%B %d').strftime('%m-%d')
        dates.append(d)


    return dates


for year in range(1994, 2018):
    dates = getDates(year)
    data = pd.DataFrame(columns=[ 'Date', 'Party', 'Statement', 'Previous Statement'])

    temp = getYearData(dates)


    for day in dates:
        url = str('https://openparliament.ca/debates/2017/' + day[0:2] + '/' + day[3:5] + '/?singlepage=1')

        soup = BeautifulSoup(getHTML(url), 'lxml')
        soup.prettify()

        partyblocks = soup.findAll("div", { "class" : "l-ctx-col" })
        statementblocks = soup.findAll("div", { "class" : "text-col" })

        partyAffiliation = findParties(partyblocks)
        statementText = findStatements(statementblocks)
        previousText = findPrevious(statementText)
        dateoOfStatement = str(year) + '-' + day
        temp = pd.DataFrame({'Date': dateoOfStatement, 'Party' : partyAffiliation, 'Statement': statementText, 'Previous Statement': previousText})
        data = pd.concat([temp, data])

    data.to_csv('data' + str(year) + '.csv',encoding='utf-8', index=False)
