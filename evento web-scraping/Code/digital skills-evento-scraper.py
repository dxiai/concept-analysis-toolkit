import bs4
import requests
import re
#import lxml

def no_stopwords(my_str):
    # define punctuation
    stopwords = 'anders,au,auch,auf,aus,ausser,ausserdem,außer,außerdem,b,bald,bei,beide,beiden,beim,beispiel,bekannt,bereits,besonders,besser,besten,bin,bis,bisher,bist,c,d,d.h,da,dabei,dadurch,dafür,dagegen,daher,dahin,dahinter,damals,damit,danach,daneben,dank,dann,daran,darauf,daraus,darf,darfst,darin,darum,darunter,darüber,das,dasein,daselbst,dass,dasselbe,davon,davor,dazu,dazwischen,daß,dein,deine,deinem,deinen,deiner,deines,dem,dementsprechend,demgegenüber,demgemäss,demgemäß,demselben,demzufolge,den,denen,denn,denselben,der,deren,derer,derjenige,derjenigen,dermassen,dermaßen,derselbe,derselben,des,deshalb,desselben,dessen,deswegen,dich,die,diejenige,diejenigen,dies,diese,dieselbe,dieselben,diesem,diesen,dieser,dieses,dir,doch,dort,drei,drin,dritte,dritten,dritter,drittes,du,durch,durchaus,durfte,durften,dürfen,dürft,e,eben,ebenso,ehrlich,ei,ei,,eigen,eigene,eigenen,eigener,eigenes,ein,einander,eine,einem,einen,einer,eines,einig,einige,einigem,einigen,einiger,einiges,einmal,eins,elf,en,ende,endlich,entweder,er,ernst,erst,erste,ersten,erster,erstes,es,etwa,etwas,euch,euer,eure,eurem,euren,eurer,eures,f,folgende,früher,fünf,fünfte,fünften,fünfter,fünftes,für,g,gab,ganz,ganze,ganzen,ganzer,ganzes,gar,gedurft,gegen,gegenüber,gehabt,gehen,geht,gekannt,gekonnt,gemacht,gemocht,gemusst,genug,gerade,gern,gesagt,geschweige,gewesen,gewollt,geworden,gibt,ging,gleich,gott,gross,grosse,grossen,grosser,grosses,groß,große,großen,großer,großes,gut,gute,guter,gutes,h,hab,habe,haben,habt,hast,hat,hatte,hatten,hattest,hattet,heisst,her,heute,hier,hin,hinter,hoch,hätte,hätten,i,ich,ihm,ihn,ihnen,ihr,ihre,ihrem,ihren,ihrer,ihres,im,immer,in,indem,infolgedessen,ins,irgend,ist,j,ja,jahr,jahre,jahren,je,jede,jedem,jeden,jeder,jedermann,jedermanns,jedes,jedoch,jemand,jemandem,jemanden,jene,jenem,jenen,jener,jenes,jetzt,k,kam,kann,kannst,kaum,kein,keine,keinem,keinen,keiner,keines,kleine,kleinen,kleiner,kleines,kommen,kommt,konnte,konnten,kurz,können,könnt,könnte,l,lang,lange,leicht,leide,lieber,los,m,machen,macht,machte,mag,magst,mahn,mal,man,manche,manchem,manchen,mancher,manches,mann,mehr,mein,meine,meinem,meinen,meiner,meines,mensch,menschen,mich,mir,mit,mittel,mochte,mochten,morgen,muss,musst,musste,mussten,muß,mußt,möchte,mögen,möglich,mögt,müssen,müsst,müßt,n,na,nach,nachdem,nahm,natürlich,neben,nein,neue,neuen,neun,neunte,neunten,neunter,neuntes,nicht,nichts,nie,niemand,niemandem,niemanden,noch,nun,nur,o,ob,oben,oder,offen,oft,ohne,ordnung,p,q,r,recht,rechte,rechten,rechter,rechtes,richtig,rund,s,sa,sache,sagt,sagte,sah,satt,schlecht,schluss,schon,sechs,sechste,sechsten,sechster,sechstes,sehr,sei,seid,seien,sein,seine,seinem,seinen,seiner,seines,seit,seitdem,selbst,sich,sie,sieben,siebente,siebenten,siebenter,siebentes,sind,so,solang,solche,solchem,solchen,solcher,solches,soll,sollen,sollst,sollt,sollte,sollten,sondern,sonst,soweit,sowie,später,startseite,statt,steht,suche,t,tag,tage,tagen,tat,teil,tel,tritt,trotzdem,tun ,u,uhr,um,und,und?,uns,unse,unsem,unsen,unser,unsere,unserer,unses,unter,v,vergangenen,viel,viele,vielem,vielen,vielleicht,vier,vierte,vierten,vierter,viertes,vom,von,vor,w,wahr?,wann,war,waren,warst,wart,warum,was,weg,wegen,weil,weit,weiter,weitere,weiteren,weiteres,welche,welchem,welchen,welcher,welches,wem,wen,wenig,wenige,weniger,weniges,wenigstens,wenn,wer,werde,werden,werdet,weshalb,wessen,wie,wieder,wieso,will,willst,wir,wird,wirklich,wirst,wissen,wo,woher,wohin,wohl,wollen,wollt,wollte,wollten,worden,wurde,wurden,während,währenddem,währenddessen,wäre,würde,würden,x,y,z,z.b,zehn,zehnte,zehnten,zehnter,zehntes,zeit,zu,zuerst,zugleich,zum,zunächst,zur,zurück,zusammen,zwanzig,zwar,zwei,zweite,zweiten,zweiter,zweites,zwischen,zwölf,über,überhaupt,übrigens,freilich,fürs'    
    # To take input from the user
    # my_str = input("Enter a string: ")
    
    # remove punctuation from the string
    no_stop = ""
    for word in my_str.split():
       if word.casefold() not in stopwords:
           no_stop = no_stop + word + ", "
    
    # display the unpunctuated string
   #print(no_stop + "\n")
    return no_stop    


def no_punctuation(my_str):
        
    # define punctuation
   # punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    punctuations =  '''!()[]{};:'"\,<>./?@#$%^&*_~'''
    
    # To take input from the user
    # my_str = input("Enter a string: ")
    
    # remove punctuation from the string
    no_punct = ""
    for char in my_str:
       if char not in punctuations:
           no_punct = no_punct + char
    
    # display the unpunctuated string
  #  print(no_punct + "\n")
    return(no_punct)
    
    
def no_whiteSpaceAndEol(my_str):
     
    my_new_str = ""
    white_char = [9,10,13]
    
    for s in my_str:
        if ord(s) not in white_char:
            my_new_str  = my_new_str  + s
        elif ord(s) == 13:
            my_new_str  = my_new_str  + " "


    # strange way to replace '...' since a regular string replace did not work inside this function
    my_new_str = my_new_str[0:my_new_str.rfind("...")] + " " + my_new_str[my_new_str.rfind("...") + 3:len(my_new_str)]
    
    return(my_new_str)  



def vowels (my_str):
    # Program to count the number of each vowel in a string
    # string of vowels
    vowels = 'aeiou'
    
    # uncomment to take input from the user
    #ip_str = input("Enter a string: ")
    
    # make it suitable for caseless comparisions
    my_str = my_str.casefold()
    
    # make a dictionary with each vowel a key and value 0
    count = {}.fromkeys(vowels,0)
    
    # count the vowels
    for char in my_str:
       if char in count:
           count[char] += 1
    
    return(count)

    

def alphabetical_order(my_str):
    # Program to sort alphabetically the words form a string provided by the user
    
    # uncomment to take input from the user
    #my_str = input("Enter a string: ")
    
    # breakdown the string into a list of words
    words = my_str.split()
    
    # sort the list
    words.sort()
    
    # display the sorted words
    print("The sorted words are:")
    for word in words:
       print(word + ", ")
       
    print("\n")
    
    
    
# Retunrs a list of all course modules, listed in eventoweb
def getModuleList ():
    eventoweb_url = "https://eventoweb.zhaw.ch/"
    response = requests.get(eventoweb_url + 'EVT_Pages/SuchResultat.aspx?node=c594e3e5-cd9a-4204-9a61-de1e43ccb7b0&Tabkey=WebTab_ModuleSuchenZHAW&Print=true')
    eventoweb_html = bs4.BeautifulSoup(response.text,"lxml")
    course_div = eventoweb_html.find('div', attrs = {'id':'ctl00_WebPartManager1_ResultatAnzeigenWP1'}) # find the 'div' which is the indicator that the course list follows right-after"
    # find all course related block
    course_trs = course_div.find_all('tr')  
    
    # initialize the list th<t will contain all course URL"
    course_url_list = []  

    # iter<te over each course-block in order to extract its URL
    for course_tr in course_trs :  
        course_url = str(course_tr.find_all('a')[1:2]).split('\"')
        course_url = eventoweb_url+course_url[1][3:len(course_url[1])].replace('amp;',"")
        course_url_list.append(course_url)  # appending a found course URL to the course list
    return(course_url_list)
    
    
    
def saveModuleList (moduleList,file_path):
    f = open(file_path, "w")
#    f.write(" ".join(moduleList))
    f.write(moduleList)
    f.close()



def readModuleList (file_path):
    f = open(file_path, "r")
    return(f.read())
    


def filter_departement_n():
    
    dept = []
   
    for i in range(4730,7000):  # range for dept_n
        
        next_item = course_url_list[i]
#        print(next_item)
        
        # extracts the module header html details and parses the for the purpose of this app relevant details 
        single_course_html = get_online_module_details(next_item)
        #print(single_course_html)  
                
        # parse course heade and skills
        single_course_div = single_course_html.find('div', attrs = {'id':'ctl00_WebPartManager1_gwpctlModulDetail_ctlModulDetail_ctlModulDetail_dgrModulDetail'}) # find the 'div' which is the indicator that the course list follows right-after"
        #    print(single_course_div )
        
        single_course_label = single_course_div.find_all('div', attrs = {'class':'detail-label DetailDialog_FormLabel'}) # find the 'div' which is the indicator that the course list follows right-after"
        #print(single_course_label)
        
        single_course_header = single_course_div.find_all('div', attrs = {'class':'detail-content-bg DetailDialog_FormValue'}) # find the 'div' which is the indicator that the course list follows right-after"
        #print(single_course_header)
        
    
        if single_course_header[0].text[0:2]=="n.":
            dept.append(next_item)
            print(str(i) + ": taken: " + single_course_header[0].text)
        else:
            print(str(i) + ": not taken: " + single_course_header[0].text)
    
    return(dept)
    
#f = open("/Users/bajk/Desktop/dept_n.text", "w")
#f.write(" ".join(dept_n))
#f.close()


#*****************************************************************************
#course_url_list = getModuleList()
#print(course_url_list)

#saveModuleList (course_url_list,course_list_file_path)





#*****************************************************************************
#*****************************************************************************
def load_evento_file(course_list_file_path):
    # Once all Course secriptions are loaded 
    course_url_list = list(readModuleList (course_list_file_path).split(" "))
    print(course_url_list)  
    return course_url_list


#*****************************************************************************
def get_online_module_details(course_url_list):
    # Examine each single module
    eventoweb_course_div = "ctl00_WebPartManager1_gwpctlModulDetail_ctlModulDetail_ctlModulDetail_edbAnlassWebAnsicht" #619404"

#    course_url_list = "https://eventoweb.zhaw.ch/Evt_Pages/Brn_ModulDetailAZ.aspx?node=c594e3e5-cd9a-4204-9a61-de1e43ccb7b0&IDAnlass=575852"

    cul = course_url_list
#    print(cul)
    cul_split = cul.rfind("=")
    cul_len = len(cul)
    
    eventoweb_course_address = eventoweb_course_div + cul[cul_split + 1:cul_len-1]
    eventoweb_course_container = eventoweb_course_address + 'slc_container'
    
    
    eventoweb_course_tag = requests.get(cul)
    #print(eventoweb_course_tag)
    
    single_course_html = bs4.BeautifulSoup(eventoweb_course_tag.text,"lxml")
    #print(single_course_html)
    
    return single_course_html


#*****************************************************************************
def parse_module_header_info(single_course_html):
    # parse course heade and skills
    single_course_div = single_course_html.find('div', attrs = {'id':'ctl00_WebPartManager1_gwpctlModulDetail_ctlModulDetail_ctlModulDetail_dgrModulDetail'}) # find the 'div' which is the indicator that the course list follows right-after"
    print(single_course_div )
    
    single_course_label = single_course_div.find_all('div', attrs = {'class':'detail-label DetailDialog_FormLabel'}) # find the 'div' which is the indicator that the course list follows right-after"
    print(single_course_label)
    
    single_course_header = single_course_div.find_all('div', attrs = {'class':'detail-content-bg DetailDialog_FormValue'}) # find the 'div' which is the indicator that the course list follows right-after"
    print(single_course_header)
    
    # extract the module and course META data and store it for a later concatenation in the list course_header_info 
 
#    module_header = []
#    k = 0
#    
#    for i in [4,3,3]:
#        course_header_list = []
#        
#        for j in range(k,k+i):
#            course_header_item_list = []
#            course_header_item_list.append(single_course_label[j].text)
#            course_header_item_list.append(single_course_header[j].text)
#            course_header_list.append(course_header_item_list)
#        
#        k = k + i
#        module_header.append(course_header_list)
#        
#    return module_header      


#*****************************************************************************
def parse_module_course_details(next_item):
    # extracts the module header html details and parses the for the purpose of this app relevant details 
    single_course_html = get_online_module_details(next_item)
#    print(single_course_html)  

    # parse course heade and skills
    single_course_div = single_course_html.find('div', attrs = {'id':'ctl00_WebPartManager1_gwpctlModulDetail_ctlModulDetail_ctlModulDetail_dgrModulDetail'}) # find the 'div' which is the indicator that the course list follows right-after"
#    print(single_course_div )

    # find the 'div' which is the indicator that the course list follows right-after"
    single_course_tr_list = single_course_div.find_all('tr')  
#    print(single_course_tr_list)
    
    # create and initialize a module specific dataset variable to temporarely store a list of related courses containing name and skills to achieve 
    tmp_dataset_skills = []
    single_course_content_concat = ""
    
    for tr in single_course_tr_list:
        #
        tmp_dataset_skills = []
        #
        tmp_dataset_skills.append(next_item)
        #
        single_course_label = str(tr.find('td', attrs = {'class':'detail-label DetailDialog_FormLabelCell'}))
#        print(single_course_label)
        
        if re.compile('|'.join(search_list),re.IGNORECASE).search(single_course_label):            
            single_course_name = (single_course_html.find('div', attrs = {'class':"detail-content-bg DetailDialog_FormValue"})).text # find the 'div' which is the indicator that the course list follows right-after"  
#            print(single_course_name)
            
            tmp_dataset_skills.append(single_course_name)
            #
            single_course_content_raw = tr.find('td', attrs = {'detail-content-bg DetailDialog_FormValueCell'})
#            print(single_course_content_raw)
            
            single_course_content_concat = ""
            single_course_content_text = ""
            
            for li in single_course_content_raw:
                single_course_content_concat = single_course_content_concat + (str(li).replace("ul>","").replace("li>","").replace("</","").replace("<","").rstrip() + " ").lstrip()
                
#            print(single_course_content_concat)
            
            single_course_content_text = single_course_content_text + no_whiteSpaceAndEol(single_course_content_concat)
#            print(single_course_content_text)
            
            single_course_content_text = no_stopwords(no_punctuation(single_course_content_text)).split(" ")
#            print(single_course_content_text)
#            #
            tmp_dataset_skills.append(single_course_content_text) 
            #
            course_dataset_skills.append(tmp_dataset_skills)
        else:
            tmp_dataset_skills = []
            
    return tmp_dataset_skills



# START MAIN
# ***********************************************************************************************************************
    
# variable initialisation
course_list_file_path = "/Users/bajk/Desktop/DigitalSkills/CourseListDeptN_bereinigt.txt"
course_url_list = []

module = []

# assigns the local file image of the evento course urls's to the variable course_url_list 
course_url_list = str(load_evento_file(course_list_file_path))
#course_url_list = load_evento_file(course_list_file_path)

course_url_list = list(course_url_list.split(","))
#print(len(course_url_list))

    
header = []
tmp = []
course_dataset_skills =[]
search_list = ['lernziele', 'zu erreichende kompetenzen']

#print(str(len(course_url_list)))
for i in range(1,len(course_url_list)):  # range for dept_n    
#for i in range(0,3):  # range for dept_n
    print(str(i))
    next_item = course_url_list[i][3:-1] #cleaning pre- and post chars
#    print(next_item)
    if parse_module_course_details(next_item) != []:
        course_dataset_skills += course_dataset_skills

print(course_dataset_skills)
saveModuleList (str(course_dataset_skills),"/Users/bajk/Desktop/DigitalSkills/CourseListDeptN_655_tot.txt")

#=================================================================


    course_dataset_skills = parse_module_course_details(single_course_html)
    print(course_dataset_skills)  
            
      single_course_label = single_course_div.find_all('div', attrs = {'class':'detail-label DetailDialog_FormLabel'}) # find the 'div' which is the indicator that the course list follows right-after"
    #print(single_course_label)
    
    single_course_header = single_course_div.find_all('div', attrs = {'class':'detail-content-bg DetailDialog_FormValue'}) # find the 'div' which is the indicator that the course list follows right-after"
    #print(single_course_header)  
       
    #print(single_course_label[0])
    #print(single_course_header[0].text)
    label = []
    
    for j in range(0,len(single_course_label)):
        label.append(single_course_label[j].text)
        label.append(single_course_header[j].text)
    
    header.append(label)
    print(header)

    print("\n")
    
    #    module_header = []
#    k = 0
#    
#    for i in [4,3,3]:
#        course_header_list = []
#        
#        for j in range(k,k+i):
#            course_header_item_list = []
#            course_header_item_list.append(single_course_label[j].text)
#            course_header_item_list.append(single_course_header[j].text)
#            course_header_list.append(course_header_item_list)
#        
#        k = k + i
#        module_header.append(course_header_list)
    
 #""""""""""""""""""""""""""""""""""""""""""   
    

#=======================================
    
    
module_header = parse_module_header_info(single_course_html)
print(module_header)

# extract the course related skills out of the module details
course_dataset_skills = parse_module_course_details(single_course_html)

#temporarely used for cancatenating parsed elements
module_course = []

# in a first step add module header details to the list
if len(module_header) > 0 :
    module.append(module_header.pop(0))

# appending the list of all course related and relevant elements.
while len(module_header) > 0:
    module_course = module_header.pop(0)
    module_course.append(course_dataset_skills.pop(0))
    module.append(module_course)
    
print(module)



#*****************************************************************************
#parse course name
eventoweb_course_container = eventoweb_course_address + 'slc_container'
print(eventoweb_course_container)

single_course_name = (single_course_html.find('div', attrs = {'class':"detail-content-bg DetailDialog_FormValue"})).text # find the 'div' which is the indicator that the course list follows right-after"
print(single_course_name)

#*****************************************************************************
course_dataset = []
course_dataset.append(single_course_name)
course_dataset.append(single_course_skill_list)
print(course_dataset)
