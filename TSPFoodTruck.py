"""
A program that takes the attached list of kiosks and their coordinates
as input and outputs routes for 2 delivery drivers that start and end
at our kitchen on Lake and Racine Ave (41.8851024,-87.6618988). These
routes should be optimized for the shortest length. Feel free to use
any technology or language, but the routing code should be yours. Feel
free to make other assumptions.

"""
import csv
import json
import sys


def fetchDestinationPoints(filename):
        reader = csv.reader(open(filename))
        dictlatLong = {}
        for row in reader:
                dictlatLong[row[0]] = [row[2]] + [row[3]]
        del dictlatLong['name']
        return dictlatLong



def fetchDirections(org, dest):
        aList = list()
        a = len(directions['routes'])
        if a == 1:
                print("For the driver there is only one route available, As there is no alternate path.")
                for step in directions['routes'][0]['legs'][0]['steps']:
                        print(BeautifulSoup(step['html_instructions'],"html.parser").text)


        elif a > 1:
                for distance in range(a):
                        dist = directions['routes'][distance]['legs'][0]['distance']['text']
                        aList.append(dist.split(" ")[0])
                minIndex, secondMinIndex =  findIndex(aList)
                print("The route for the first driver is ")
                for step in directions['routes'][minIndex]['legs'][0]['steps']:
                        print(BeautifulSoup(step['html_instructions'],"html.parser").text)
                print("\n\nThe route for the second driver is ")
                for step in directions['routes'][secondMinIndex]['legs'][0]['steps']:
                        print(BeautifulSoup(step['html_instructions'],"html.parser").text)

        else:
                print("No path between given source and destination")




DestCoordDict = fetchDestinationPoints("Kiosk Coords.csv")

fetchDirections("41.871103,-87.6745017", "41.8851024,-87.6618988")
#termprint("\n\n\n\n\n\n\n")
fetchDirections("41.8851024,-87.6618988","41.871103,-87.6745017")
