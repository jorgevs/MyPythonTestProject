import urllib
#import urllib2
import re

HTML_TAG = re.compile(r'<[^>]+>')
SPACES = re.compile(r'(&nbsp;)')
GREATER_THAN = re.compile(r'(&gt;)')
INDEX_OF = re.compile(r'(Index of)[ \w\-\/]*')
PARENT_DIR = re.compile(r'(Parent)[\w \-]*')
COLUMN_NAMES = re.compile(r'(NameLast)[\w ]*')
DATES = re.compile(r'[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9] [\w .:-]*')
EMPTY_NEW_LINES = re.compile(r'^[\s \t ]*')
EMPTY_SPACES = re.compile(r'[ ]*')

url = 'http://www.christianxxx.com/wp-content/uploads/'
#url = 'http://www.christianxxx.com/wp-content/uploads/2014/09/Pobre-so#U00f1ador.pdf'
user_agent = 'Mozilla 5.0 (Windows 7; Win64; x64)'

def remove_unnecessary_tags(text):
    text = HTML_TAG.sub('', text)
    text = SPACES.sub('', text)
    text = GREATER_THAN.sub('', text)
    text = INDEX_OF.sub('', text)
    text = PARENT_DIR.sub('', text)
    text = COLUMN_NAMES.sub('', text)
    text = DATES.sub('', text)
    text = EMPTY_NEW_LINES.sub('', text)
    text = EMPTY_SPACES.sub('', text)
    return text


def process_url(initial_url, initial_list):
    for element in initial_list:
        new_url = initial_url + element
        print(new_url)

        if str(new_url).endswith("/"):
            response = urllib.urlopen(new_url)
            data = response.read()

            # Remove HTML tags, new lines and other characters from the response
            clean_text = remove_unnecessary_tags(data)
            array_strings = clean_text.split("\n")

            # Remove empty elements from the list
            new_list = []
            for x in array_strings:
                if x != "":
                    new_list.append(x)

            print(new_list)
            process_url(new_url, new_list)
        else:
            if str(new_url).endswith(".pdf"):
                print("Save file")

                # Replace the '#' character from the filename and from the url
                # file_name = "Pobre-so#U00f1ador.pdf" #str(element)
                file_name = str(element)
                file_name = file_name.replace('#U00f1', 'n')

                pdf_url = str(new_url)
                pdf_url = pdf_url.replace('#', '%23')


                response = urllib.urlopen(pdf_url)
                data = response.read()

                # use of 'wb'. Pdf files are binary files so you need the 'b'
                file_ = open("D:\\GuitarPdfs\\" + file_name, 'wb')
                file_.write(data)
                file_.close()


def main():
    initial_url = url
    initial_list = ['']
    process_url(initial_url, initial_list)


main()

# print("downloading with urllib")
# urllib.urlretrieve(url, "code.zip")


# with open("code2.zip", "wb") as code:
#     code.write(f.read())

# print("downloading with requests")
# r = requests.get(url)
# with open("code3.zip", "wb") as code:
#     code.write(r.content)
