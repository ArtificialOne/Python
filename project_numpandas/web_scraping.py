import requests
from bs4 import BeautifulSoup
#HTML Tags enclose HTML Text ||| HTML Element is Root Element ||| Body Displayed in Webpage
#Same Level Tags are Siblings, Descendent/Child of Root
#<H3> Type 3 Heading, Larger, Bold Text ||| <P> Signifies Paragraph

#<a href="https://www.ibm.com"> IBM Webpage </a>
#<a = Tag ||| href = Attribute Name ||| https://www.ibm.com = Attribute Value
#<tr = Table Row Tag ||| <td = Table Cell Tag

html_balls="" #Website html data (i.e. Basketball players)
soup=BeautifulSoup(html_balls,'html5lib')

tag_object_title=soup.title
tag_object_h3=soup.h3
tag_child=tag_object_h3.b
tag_child.attrs #Attributes of tag_child
tag_child.string

parent_tag=tag_child.parent #Navigates up tree with parent
sibling_1=tag_object_h3.next_sibling #Navigates to sibling
sibling_2=sibling_1.next_sibling #Next sibling


html_pizza="" #Website html data (i.e. Pizza Places)
table=BeautifulSoup(html_pizza, 'html5lib')
table_rows=table.find_all(name='tr') 
first_row=table_rows[0]
for i,row in enumerate(table_rows):
    print("row",i)
    cells=row.find_all("td")

    for j,cell in enumerate(cells):
        print("column",j,"cell",cell)

##############################################################################

page=requests.get("http://URLHERE").text #DLs webpage
soup=BeautifulSoup(page,"html.parser") #Allows parsing of page
artists=soup.find_all('a')
for artist in artists:
    names=artist.contents[0]
    full_link=artist.get('href')
    print(names)
    print(full_link)