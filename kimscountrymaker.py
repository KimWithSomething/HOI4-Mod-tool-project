from tkinter import *
import os, shutil
import requests
import tkinter as tk
from PIL import Image, ImageTk


verison ="Beta V1.0.3 Leader's patch"
debugmode= True
xy = 0
finalAW=[]

def main():
    destory = None
    def filescreationY(nameoffolder,nameoffile,things):
        directory = './'+nameoffolder+''

        filename = nameoffile
        file_path = os.path.join(directory, filename)
        
        if not os.path.isdir(directory):
            os.mkdir(directory)
        file = open(file_path, "a")
        for items in things:
            file.writelines([items])
        try:
            file = open(file_path,encoding='utf-8-bom')
            file.close()
        except:
            print('failed set yml')
    def filescreation(nameoffolder,nameoffile,things):
        directory = './'+nameoffolder+''

        filename = nameoffile
        file_path = os.path.join(directory, filename)
        
        if not os.path.isdir(directory):
            os.mkdir(directory)
        file = open(file_path, "a")
        
        for items in things:

            file.writelines([items])
            
        file.close()
        print(file_path)

    def filescreationD(nameoffolder,nameoffile,link,list987):
        directory = './'+nameoffolder+''

        filename = nameoffile

        file_path = os.path.join(directory, filename)
        if not os.path.isdir(directory):
            os.mkdir(directory)
        url = link
        r = requests.get(url)
        
        open(file_path, 'wb').write(r.content)
        
        
        
        
        print(file_path)

        file = open(file_path, "a")
        file.writelines(list987)
        file.close()
        

    def filescreationDNolist(nameoffolder,nameoffile,link):
        directory = './'+nameoffolder+''

        filename = nameoffile

        file_path = os.path.join(directory, filename)
        if not os.path.isdir(directory):
            os.mkdir(directory)
        url = link
        r = requests.get(url)
        
        open(file_path, 'wb').write(r.content)
        

    def foldercreation(nameoffolder):
        directory = './'+nameoffolder+''
        if not os.path.isdir(directory):
            os.mkdir(directory)

    print('opening ' + verison)
    filescreationDNolist('','profile.ico','https://cdn.discordapp.com/attachments/870099462624780359/876629267298005022/profile.ico')



    def file(name,things):
        file = open(name + '.txt', "a")
            
        for items in things:
            file.writelines([items])
                
        file.close()

    def printproblems(name,varka,getname):
        
            varka = getname.get()
            print('getting ' + name)
            print( name + ': '+ varka )
            print('------------------------------')
            
    def printproblemslist(name,varka,getname):
        
            varka = getname.get()
            
            list3='getting ' + name
            list2=name + ': '+ varka 
            list1='------------------------------'
            finalAW.append(list3)
            finalAW.append(list2)
            finalAW.append(list1)
            finallist = [list3,list2,list1]
            print(finallist)

    root = Tk()
    root.title('country creation')
    

    def QuickLabelSP(NameOfLabel,x,y,textsays):
        NameOfLabel = Label(root, text= textsays)
        NameOfLabel.grid(row=x, column =y)


    def QuickEntry(EntryName,WidthSize,x,y):
        
        EntryName = Entry(root, width = WidthSize)
        EntryName.insert(0, '')
        EntryName.grid(row=x, column =y)

    
    def QuickButton(ButtonName2,txt2,CMD,x,y,):
        ButtonName2 = Button(root, text=txt2,command=CMD)
        ButtonName2.grid(row=x, column = y)
    
    def DEH(name):
        name.pack_forget()   
            
    def QuickButton2(ButtonName2,txt2,CMD,x,y,):
        ButtonName2 = Button(root, text=txt2,command=CMD)
        ButtonName2.grid(row=x, column = y)
        if destory == TRUE:
            ButtonName2.destroy()

    def CLICKEDCOUNTRY():

        

        def check19():
            
            yx=5
            xy=0

            
            for item in finalAW:
                xy += 1
                yx += 1
                item = Label(root, text= item)
                item.grid(row=xy+5, column = 9) 
                    
                checkButton.grid(row= yx + 1 ,column=  9)
            
            
        checkButton = Button(root,text='click for logs ',command= check19)
        checkButton.grid(row= x+ 5 ,column= y + 5)

        def createNHGS():
            #setting values and E
            print('getting country name')
            cmName = countryname23.get()
            print('country Name: ' + cmName)
            print('country name doned')
            print('------------------------------')
            
            
            print('getting TAG')
            cmTAG = TAGc.get()
            print('Country Tag: '+ cmTAG)
            print('tag doned')
            print('------------------------------')
            
            #party values
            
            print('getting democratic party value')
            cmD = partyDq.get()
            print('democratic party value = '+ cmD )
            print('------------------------------')
            
            print('getting Fascism party value')
            cmF = partyFq.get()
            print('Fascism party value = '+ cmF )
            print('------------------------------')
            

            print('getting Communism party value')
            cmC = partyCq.get()
            print('Communism party value = '+ cmC )
            print('------------------------------')
            
            print('getting neutrality party value')
            cmN = partyNq.get()
            print('neutrality party value = '+ cmN )
            print('------------------------------')
            
            print('getting ruling party value')
            cmRP = partyR.get()
            print('rulling party: '+ cmRP )
            print('------------------------------')

            print('getting reasrech slots')
            cmRS = RSl.get()
            print('reasrech slots : '+ cmRS )
            print('------------------------------')
            try:
                cmW = CWS.get()
                print('getting war support')
                print('war support: '+ cmW )
                print('------------------------------')
            except:
                print('error war')
                
            try:
                cmT = CTS.get()        
                print('getting stiabily support')
                print('stabil support: '+ cmT )
                print('------------------------------')
            except:
                print('error stab')
            
            cmS = STA3.get()        
            printproblems('state capital',cmS,STA3)
            
            cmR = RGB4.get()
            cmE= 'yes'
            printproblems('RGB color',cmR,RGB4)
            
            cmL = countrlea.get()
            printproblems('country leader name',cmL,countrlea)
            

            
            
            def fileSetup():
                print('well')
                    #,"non aligned -despotism", "non aligned -oligarchism", "non aligned -moderatism","non aligned -centrism"
                
                if leaderd.get() == 'democratic-conservatism':
                    cmlD = 'conservatism'
                    printproblems('country leader4 idea', cmlD,leaderd)
                if leaderd.get() == 'democratic-liberalism':
                    cmlD = 'liberalism'
                    printproblems('country leader4 idea', cmlD,leaderd)
                if leaderd.get() == 'democratic-socialism':
                    cmlD = 'socialism'
                    printproblems('country leader4 idea', cmlD,leaderd)
                    
            
                if leaderd.get() == 'facism-nazism':
                    cmlD = 'nazism'
                    printproblems('country leader4 idea', cmlD,leaderd)
                if leaderd.get() == 'facism-fascism':
                    cmlD = 'fascism'
                    printproblems('country leader4 idea', cmlD,leaderd)
                if leaderd.get() == 'facism-falangism':
                    cmlD = 'falangism'
                    printproblems('country leader4 idea', cmlD,leaderd)
                if leaderd.get() == 'facism-rexism':
                    cmlD = 'rexism'
                    printproblems('country leader4 idea', cmlD,leaderd)
                    
        
                if leaderd.get() == 'communism-marxism':
                    cmlD = 'marxism'
                    printproblems('country leader4 idea', cmlD,leaderd)
                if leaderd.get() == 'communism-leninism':
                    cmlD = 'leninism'
                    printproblems('country leader4 idea', cmlD,leaderd)
                if leaderd.get() == 'communism-stalinism':
                    cmlD = 'stalinism'
                    printproblems('country leader4 idea', cmlD,leaderd)
            
                if leaderd.get() == 'non aligned -despotism':
                    cmlD = 'despotism'
                    printproblems('country leader4 idea', cmlD,leaderd)
                if leaderd.get() == 'non aligned -oligarchism':
                    cmlD = 'oligarchism'
                    printproblems('country leader4 idea', cmlD,leaderd)
                if leaderd.get() == 'non aligned -moderatism':
                    cmlD = 'moderatism'
                    printproblems('country leader4 idea', cmlD,leaderd)
                if leaderd.get() == 'non aligned -centrism':
                    cmlD = 'centrism'
                    printproblems('country leader4 idea', cmlD,leaderd)
                          



                
            
                
                x = 0
                if x == 0:
                    ctxt = cmTAG + '= ' + '"' + 'countries/' + cmName + '.txt"'
                    
                    #setuping the color rgb 
                    cco1 = 'graphical_culture = southamerican_gfx'
                    cco2 = 'graphical_culture_2d = southamerican_2d'
                    cco3 = 'color = { ' + cmR +' }'

                    
                    #setuping up the color.txt file
                    cl1 = cmTAG + ' = {'
                    cl2 =' 	color = rgb { ' + cmR +' }'
                    cl3 = '	color_ui = rgb { '+ cmR + ' }'
                    cl4 = '}'
                    
                    #setuping the country leader
                    
                
                    
                    #Country settings preup
                    cc1 = 'capital = ' + cmS
                    cc2 = 'set_research_slots = ' + cmRS
                    cc3 = 'set_stability = ' + cmT
                    cc4 = 'set_war_support = ' + cmW
                    cc5 = 'set_technology = {'
                    cc6 = '}'
                    cc7 = '                        '
                    #poltics
                    cc8 = 'set_politics = {'
                    cc9 = '	ruling_party = ' + cmRP
                    cc10 ='	last_election = "1935.1.1"'
                    cc11 ='	election_frequency = 48'
                    cc12 ='	elections_allowed = ' + cmE
                    cc13 ='}'
                    #parties
                    cc14 ='set_popularities = {'
                    cc15 ='	democratic = ' + cmD
                    cc16 ='	fascism = ' + cmF
                    cc17 ='	communism = ' + cmC
                    cc18='	neutrality = ' + cmN
                    cc19='}'
                    #country leader
                    
                    cc20='create_country_leader = {'
                    cc21='	name = "' + cmL + '"'
                    cc23='	expire = "1965.1.1"'
                    
                    cc24='	ideology = ' + cmlD
                    cc25='	traits = { }'
                    cc26='	picture = "'+ cmL + '.dds"'
                    cc27='}'
                    
                    #_L_english.yml
                
                    yml1 = 'l_english:'
                    yml2 = cmTAG + ':0 "'+ cmName +'"'
                    yml3 = cmTAG + '_DEF:0 "'+ cmName +'"'
                    yml4 = cmTAG+ '_ADJ:0 "Citizen of '+ cmName +'"'

                    
                    ymlF = [yml1,"\n","\n",yml2,"\n",yml3,"\n",yml4,"\n",]
                    #country setup
                    ccF = ["\n",cc1,"\n",cc2,"\n",cc3,"\n",cc4,"\n",cc5,"\n",cc6,"\n",cc7,"\n","\n",cc8,"\n",cc9,"\n",cc10,"\n",cc11,"\n",cc12,"\n",cc13,"\n", "\n",cc14,"\n",cc15,"\n",cc16,"\n",cc17,"\n",cc18,"\n",cc19,"\n",cc20,"\n",cc21,"\n",cc23,"\n",cc24,"\n",cc25,"\n",cc26,"\n",cc27]
                    
                    #countries color setup
                    ccoF = ["\n",cco1,"\n" ,cco2, "\n" ,cco3]
                    clF = ["\n",cl1,"\n",cl2,"\n",cl3,"\n",cl4]

                    try:
                        ccoW29 = cmName + '.txt'
                        #adding the country color thingy to name.txt

                        foldercreation('common')
                        foldercreation('./common/countries')
                        LLO = './common/countries'
                        filescreation(LLO,ccoW29,ccoF)
                        
                        #adding the color to the color.txt
                        
                        cclWf = 'colors' + '.txt'
                        link243='https://cdn.discordapp.com/attachments/870099462624780359/870099501011075102/colors.txt'
                        filescreationD(LLO,cclWf,link243,clF)

                        
                        #getting country.txt to into aonfile
                        foldercreation('history')
                        foldercreation('./history/countries')
                        ccWF = cmTAG + ' - '+ cmName + '.txt'
                        LLO23 = './history/countries'
                        filescreation(LLO23,ccWF,ccF)
                        
                        #creating the country tag list
                        filetagname = cmTAG+ '_countries.txt'
                        tag0 = cmTAG+' = "countries/'+cmName+'.txt"'
                        tag1 = [tag0,"\n"]
                        foldercreation('./common/country_tags')
                        tag01 = './common/country_tags'
                        filescreation(tag01,filetagname,tag1)
                    except:
                        print('faoie')
                    
                    try:
                        # _I_english.yml stuff
                        foldercreation('./localisation')
                        
                        ymlname= cmName + '_countries_l_english.yml'

                        ymlfol = './localisation'
                        filescreationY(ymlfol,ymlname,ymlF)
                    except:
                        print('yml failed idk')
                        
                    # GFXX
                    #FLAGGGSSSSSS
                    
                    
                                            #democratic
                    try:
                        print('getting non agliened flags')
                        foldercreation('gfx')
                        foldercreation('./gfx/flags')
                        filescreationDNolist('./gfx/flags',str(cmTAG)+'.tga','https://cdn.discordapp.com/attachments/870099462624780359/875507248401621042/GAO.tga')
                        #medium
                        filescreationDNolist('./gfx/flags/medium',str(cmTAG)+'.tga','https://cdn.discordapp.com/attachments/870099462624780359/875507756566732831/GAO.tga')
                        #small 
                        filescreationDNolist('./gfx/flags/small',str(cmTAG)+'.tga','https://cdn.discordapp.com/attachments/870099462624780359/875507860270899259/GAO.tga')
                        print('doned downloading')
                    except:
                        print('non aliened flags download failed')
                    try:
                        print('getting communist flags')
                        filescreationDNolist('./gfx/flags',str(cmTAG)+'_communism.tga','https://cdn.discordapp.com/attachments/870099462624780359/875507680125530182/GAO_communism.tga')
                        filescreationDNolist('./gfx/flags/medium',str(cmTAG)+'_communism.tga','https://cdn.discordapp.com/attachments/870099462624780359/875507758038908979/GAO_communism.tga')
                        filescreationDNolist('./gfx/flags/small',str(cmTAG)+'_communism.tga','https://cdn.discordapp.com/attachments/870099462624780359/875507862737137664/GAO_communism.tga')
                        print('doned downloading')
                    except:
                        print('communist flags download failed')
                    try:
                        print('getting democratic flags')
                        filescreationDNolist('./gfx/flags',str(cmTAG)+'_democratic.tga','https://cdn.discordapp.com/attachments/870099462624780359/875507681962635354/GAO_democratic.tga')
                        filescreationDNolist('./gfx/flags/medium',str(cmTAG)+'_democratic.tga','https://cdn.discordapp.com/attachments/870099462624780359/875507758793904158/GAO_democratic.tga')
                        filescreationDNolist('./gfx/flags/small',str(cmTAG)+'_democratic.tga','https://cdn.discordapp.com/attachments/870099462624780359/875507867338276934/GAO_democratic.tga')
                        print('doned downloading')
                    except:
                        print('democratic flags download failed')
                    try:
                        print('getting fascism flags')
                        filescreationDNolist('./gfx/flags',str(cmTAG)+'_fascism.tga','https://cdn.discordapp.com/attachments/870099462624780359/875507678204547122/GAO_fascism.tga')
                        filescreationDNolist('./gfx/flags/medium',str(cmTAG)+'_fascism.tga','https://cdn.discordapp.com/attachments/870099462624780359/875507754968707112/GAO_fascism.tga')
                        filescreationDNolist('./gfx/flags/small',str(cmTAG)+'_fascism.tga','https://cdn.discordapp.com/attachments/870099462624780359/875507858941280316/GAO_fascism.tga')
                        print('doned downloading')
                    except:
                        print('fascism flags download failed')
                        
                        #leaders
                    try:
                        print('getting default leader .dd files')
                        foldercreation('./gfx/leaders')
                        filescreationDNolist('./gfx/leaders',str(cmL)+ '.dds','https://cdn.discordapp.com/attachments/870099462624780359/875918293536477195/portrait_spr_valentin_gonzalez.dds')
                        print('leader pics download done')
                    except:
                        print('leader download failed')

            fileSetup()
            try:
                print()
            except:
                print('failed for setup')


        #labels ------------------------------------------------------------

        countryname = Label(root, text='country name:')
        countryname.grid(row=x + 1, column = y + 1)
        
        leadername = Label(root, text='leader name:')
        leadername.grid(row=x + 1, column = y + 3)


        fuck = Label(root, text='the country tag:')
        fuck.grid(row=x + 2, column =y + 1)
        
        fuck = Label(root, text='leader ideology:')
        fuck.grid(row=x + 2, column =y + 3)
        
        
        

        leaderd= StringVar()
        leaderd.set('democratic-conservatism')
        
        

        drop = OptionMenu(root,leaderd,"democratic-conservatism", "democratic-liberalism","democratic-socialism","facism-nazism", "facism-fascism", "facism-falangism", "facism-rexism","communism-marxism", "communism-leninism", "communism-stalinism","non aligned -despotism", "non aligned -oligarchism", "non aligned -moderatism","non aligned -centrism")
        drop.grid(row=x + 3, column =y + 3)
        
        

        partyDq2 = Label(root, text='Time to setup the party values [ALL NUMBERS MUST EQUAL TO 100]')
        partyDq2.grid(row=x +3, column =y + 2)

        partyDq2 = Label(root, text='Enter a number for Democratic party:')
        partyDq2.grid(row=x +4, column =y + 1)

        partyFq2 = Label(root, text='Enter a number for Fascism party:')
        partyFq2.grid(row=x +5, column =y + 1)

        partyCq2 = Label(root, text='Enter a number for Communism party:')
        partyCq2.grid(row=x +6, column =y + 1)

        partyNq2 = Label(root, text='Enter a number for non-aligned party:')
        partyNq2.grid(row=x +7, column =y + 1)

        partyR2 = Label(root, text='ruling Party :[democratic,fascism , communism, neutrality ]:')
        partyR2.grid(row=x +8, column =y + 1)

        RS34 = Label(root, text='research slots:')
        RS34.grid(row=x +9, column =y + 1)


        warsupport3= Label(root, text='war support:')
        warsupport3.grid(row=x +10, column =y + 1)

        cosupport3= Label(root, text='country stability:')
        cosupport3.grid(row=x +11, column =y + 1)

        stateID2= Label(root, text='state capital id:')
        stateID2.grid(row=x +12, column =y + 1)

        stateIC2= Label(root, text='Country color [RGB ONLY!] id:')
        stateIC2.grid(row=x +13, column =y + 1)


        #entry------------------------------------------------CTS
        countryname23 = Entry(root, width ='10')
        countryname23.insert(0, 'No U empire')
        countryname23.grid(row=x+1, column =y + 2)


        TAGc = Entry(root, width ='10')
        TAGc.insert(0, 'GAO')
        TAGc.grid(row=x+ 2, column =y + 2)

        #party stuff
        partyDq = Entry(root, width ='10')
        partyDq.insert(0, '100')
        partyDq.grid(row=x +4, column =y + 2)


        partyFq = Entry(root, width ='10')
        partyFq.insert(0, '0')
        partyFq.grid(row=x +5, column =y + 2)

        partyCq = Entry(root, width ='10')
        partyCq.insert(0, '0')
        partyCq.grid(row=x +6, column =y + 2)

        partyNq = Entry(root, width ='10')
        partyNq.insert(0, '0')
        partyNq.grid(row=x +7, column =y + 2)

        partyR = Entry(root, width ='13')
        partyR.insert(0, 'democratic')
        partyR.grid(row=x +8, column =y + 2)
        #------------------------------------------------------------------CTS
        RSl = Entry(root, width ='13')
        RSl.insert(0, '2')
        RSl.grid(row=x +9, column =y + 2)


        CWS = Entry(root, width ='13')
        CWS.insert(0, '69')
        CWS.grid(row=x +10, column =y + 2)

        CTS = Entry(root, width ='13')
        CTS.insert(0, '67')
        CTS.grid(row=x +11, column =y + 2)

        STA3 = Entry(root, width ='10')
        STA3.insert(0, '567')
        STA3.grid(row=x +12, column =y + 2)


        RGB4 = Entry(root, width ='15')
        RGB4.insert(0, '345 456 656')
        RGB4.grid(row=x +13, column =y + 2)
        
        countrlea = Entry(root, width ='10')
        countrlea.insert(0, 'Osma WK')
        countrlea.grid(row=x +1, column =y + 4)
        




            
        def testclick():
                #               /x /y
            QuickLabelSP('Name',30,4,'hmm')
            printproblems('NAME','VAR',RGB4)
            QuickEntry('Test', '6',x + 40, y + 2)


        #buttons --------------------------------------------------------------RGB4
        myButton = Button(root, text="submit",command=createNHGS)
        myButton.grid(row=x + 20, column = y + 2)

    
    y = 4
    x = 5
    #button to active main country stuff
    QuickButton2('click','CountryMode',CLICKEDCOUNTRY,5,6)
    
    root.iconbitmap("profile.ico")
    root.geometry('1200x500')


    
    


    root.mainloop()

if __name__ == "__main__":
    main()

'''        QuickLabelSP('Name',30,4,'hmm')'''
'''        QuickEntry('EntryName','8',x,y)'''

'''
        QuickLabelSP('d',x + 3, y + 3 ,'|democratic-: conservatism, liberalism, socialism|')
        QuickLabelSP('df',x + 4, y + 3 ,'|facism-: nazism, fascism, falangism, rexism |')
        QuickLabelSP('dc',x + 5, y + 3 ,'|communism-: marxism, leninism, stalinism |')
        QuickLabelSP('dn',x + 6, y + 3 ,'|non aligned-: despotism, oligarchism, moderatism,centrism|')
        
    bg = PhotoImage(file='background.png')
    mlb= Label(root,image=bg)
    mlb.place(x=0,y=0,relwidth=1,relheight=1)     
'''
'''
    ico = Image.open('profile.ico')
    photo = ImageTk.PhotoImage('profile.png')
    root.wm_iconphoto(False, photo)
    
'''