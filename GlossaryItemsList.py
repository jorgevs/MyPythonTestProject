import requests
import csv
import io
import time

#POINTING TO LSCS PROD
url="http://xxx-xxxxxxxx.xxxxxxxx.com:1876/lscs/v1/document$?q=TeamSite/Templating/DCR/Type:=Static/Glossary&project=&start=0&max=3000&format=json"
#POINTING TO LSCS DEV
#url="http://xxx-xxxxxxxx.xxxxxxxx.com:1876/lscs/v1/document$?q=TeamSite/Templating/DCR/Type:=Static/Glossary&project=&start=0&max=3000&format=json"


# Do the HTTP get request (Verify is check SSL certificate)
response = requests.get(url, verify=True)

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()

data = response.json()
#print(data)
assets = data['results']['assets']
#print(assets)


# Writting a line in a file
timestr = time.strftime("%m%d%Y")
fileName = "glossaryList-" + timestr + ".csv"
myFile = open(fileName, 'wb')

# Create the CSV writer
output = io.StringIO()
writer = csv.writer(output, quoting=csv.QUOTE_NONNUMERIC)


# Add the headers to the writer
headers = ["META_ID", "ENDECA_ID", "TITLE", "DEFINITION", "ACTIVE", "CREATION_DATE", "LAST_MODIFIED_DATE", "PUBLISH_DATE"]
writer.writerow(headers)
print(output.getvalue())

# Process and add each record (row) to the writer
for asset in assets:
    metadata = asset['metadata']

    metaId = metadata.get('Property.Meta_id', "")
    endecaId = metadata.get('Property.Endeca_id', "")
    title = metadata.get('Property.Title', "")
    definition = metadata.get('Property.Definition', "")
    active = metadata.get('Property.Active', "")
    creationDate = metadata.get('TeamSite/Metadata/CreationDate', "")
    lastModifiedDate = metadata.get('LatestModifiedDate', "")
    publishDate = metadata.get('PublishDate', "")

    #print(metadata['Property.Meta_id'] + ", " + metadata['Property.Endeca_id'] + ", " + metadata['Property.Title'] + ", " + metadata['Property.Definition'] + ", " + metadata['Property.Active'] + ", " + metadata['TeamSite/Metadata/CreationDate'] + ", " + metadata['LatestModifiedDate'] + ", " + metadata['PublishDate'])
    #print(metaId + ", " + endecaId + ", " + title + ", " + definition + ", " + active + ", " + creationDate + ", " + lastModifiedDate + ", " + publishDate)
    #line = metaId + ", " + endecaId + ", " + title + ", " + definition + ", " + active + ", " + creationDate + ", " + lastModifiedDate + ", " + publishDate + "\n"
    #myFile.write(bytes(line, 'utf8'))

    row = [metaId, endecaId, title, definition, active, creationDate, lastModifiedDate, publishDate]
    writer.writerow(row)

# Writes the writer's info into the file
print(output.getvalue())
myFile.write(bytes(output.getvalue(), 'utf8'))

myFile.close()
