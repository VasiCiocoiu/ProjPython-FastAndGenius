from tkinter import*
from random import*



def next(): #La définition choisit une question au hasard,supprime le texte inutile(le règlement),assigne et place les réponses à leur place et supprime la question de la liste
    txt=choice(Liste)
    Liste.remove(txt)
    Question.config(text=txt[0])
    Rep1.config(text=txt[1])
    Rep1.place(x=210,y=70)
    Rep2.config(text=txt[2])
    Rep2.place(x=210,y=105)
    Rep3.config(text=txt[3])
    Rep3.place(x=210,y=140)
    Rep4.config(text=txt[4])
    Rep4.place(x=210,y=175)

    boutonNext.config(text="Next")
    Regl.place_forget()
    Regl1.place_forget()
    Regl2.place_forget()
    Regl3.place_forget()
    Regl4.place_forget()
    result.place_forget()
    RepVr=txt[5]



    def repJ1A(event):#la définition vérifie si la réponse du joueur est correcte,supprime les réponses,montre quel joueur a répondu correctement et quelle a été la bonne réponse
        RepJ1=txt[1]
        if RepJ1==RepVr:
            Question.place_forget()
            Rep1.place_forget()
            Rep2.place_forget()
            Rep3.place_forget()
            Rep4.place_forget()
            frame.unbind("<a>")
            frame.unbind("<u>")
            result.config(text="Le joueur 1 a bien repondu =>"+txt[5])
            result.place(x=170,y=100)
            def testFunc():#la définition attribue au joueur qui a répondu correctement 10 points pour sa réponse et crée une zone graphique qui augmente en fonction de ses points
                global pointj1
                pointj1=pointj1+10
                j1p=str(pointj1)
                poinj1.config(text="Joueur1:"+j1p+" points")
                RectP1=repon.create_rectangle(100,370-3*pointj1,30,370,fill="orange")
            testFunc()
            if pointj1==70:#Vérifier si le joueur 1 a atteint 70 points  pour le déclarer vainqueur dans ce cas
                repon.destroy()
                Question.config(text="Win Joueur 1")
            elif pointj2==70:#Vérifier si le joueur 2 a atteint 70 points  pour le déclarer vainqueur dans ce cas
                repon.destroy()
                Question.config(text="Win Joueur 2")

#Toutes les définitions repJ1B,repJ1C.... ont le même rôle que la définition repJ1C

    def repJ1B(event):
        RepJ1=txt[2]
        if RepJ1==RepVr:
            Question.place_forget()
            Rep1.place_forget()
            Rep2.place_forget()
            Rep3.place_forget()
            Rep4.place_forget()
            frame.unbind("<z>")
            frame.unbind("<i>")
            result.config(text="Le joueur 1 a bien repondu =>"+txt[5])
            result.place(x=170,y=100)
            def testFunc():
                global pointj1
                pointj1=pointj1+10
                j1p=str(pointj1)
                poinj1.config(text="Joueur1:"+j1p+" points")
                RectP1=repon.create_rectangle(100,370-3*pointj1,30,370,fill="orange")
            testFunc()
            if pointj1==70:
                repon.destroy()
                Question.config(text="Win Joueur 1")
            elif pointj2==70:
                repon.destroy()
                Question.config(text="Win Joueur 2")


    def repJ1C(event):
        RepJ1=txt[3]
        if RepJ1==RepVr:
            Question.place_forget()
            Rep1.place_forget()
            Rep2.place_forget()
            Rep3.place_forget()
            Rep4.place_forget()
            frame.unbind("<e>")
            frame.unbind("<o>")
            result.config(text="Le joueur 1 a bien repondu =>"+txt[5])
            result.place(x=170,y=100)
            def testFunc():
                global pointj1
                pointj1=pointj1+10
                j1p=str(pointj1)
                poinj1.config(text="Joueur1:"+j1p+" points")
                RectP1=repon.create_rectangle(100,370-3*pointj1,30,370,fill="orange")
            testFunc()
            if pointj1==70:
                repon.destroy()
                Question.config(text="Win Joueur 1")
            elif pointj2==70:
                repon.destroy()
                Question.config(text="Win Joueur 2")


    def repJ1D(event):
        RepJ1=txt[4]
        if RepJ1==RepVr:
            Question.place_forget()
            Rep1.place_forget()
            Rep2.place_forget()
            Rep3.place_forget()
            Rep4.place_forget()
            frame.unbind("<p>")
            frame.unbind("<r>")
            result.config(text="Le joueur 1 a bien repondu =>"+txt[5])
            result.place(x=170,y=100)
            def testFunc():
                global pointj1
                pointj1=pointj1+10
                j1p=str(pointj1)
                poinj1.config(text="Joueur1:"+j1p+" points")
                RectP1=repon.create_rectangle(100,370-3*pointj1,30,370,fill="orange")
            testFunc()
            if pointj1==70:
                repon.destroy()
                Question.config(text="Win Joueur 1")
            elif pointj2==70:
                repon.destroy()
                Question.config(text="Win Joueur 2")


    def repJ2A(event):
        RepJ2=txt[1]
        if RepJ2==RepVr:
            Question.place_forget()
            Rep1.place_forget()
            Rep2.place_forget()
            Rep3.place_forget()
            Rep4.place_forget()
            frame.unbind("<a>")
            frame.unbind("<u>")
            result.config(text="Le joueur 2 a bien repondu =>"+txt[5])
            result.place(x=170,y=100)
            def testFunc():
                global pointj2
                pointj2=pointj2+10
                j2p=str(pointj2)
                poinj2.config(text="Joueur2:"+j2p+" points")
                RectP2=repon.create_rectangle(670,370-3*pointj2,600,370,fill="orange")
            testFunc()
            if pointj1==70:
                repon.destroy()
                Question.config(text="Win Joueur 1")
            elif pointj2==70:
                repon.destroy()
                Question.config(text="Win Joueur 2")


    def repJ2B(event):
        RepJ2=txt[2]
        if RepJ2==RepVr:
            Question.place_forget()
            Rep1.place_forget()
            Rep2.place_forget()
            Rep3.place_forget()
            Rep4.place_forget()
            frame.unbind("<z>")
            frame.unbind("<i>")
            result.config(text="Le joueur 2 a bien repondu =>"+txt[5])
            result.place(x=170,y=100)
            def testFunc():
                global pointj2
                pointj2=pointj2+10
                j2p=str(pointj2)
                poinj2.config(text="Joueur2:"+j2p+" points")
                RectP2=repon.create_rectangle(670,370-3*pointj2,600,370,fill="orange")
            testFunc()
            if pointj1==70:
                repon.destroy()
                Question.config(text="Win Joueur 1")
            elif pointj2==70:
                repon.destroy()
                Question.config(text="Win Joueur 2")



    def repJ2C(event):
        RepJ2=txt[3]
        if RepJ2==RepVr:
            Question.place_forget()
            Rep1.place_forget()
            Rep2.place_forget()
            Rep3.place_forget()
            Rep4.place_forget()
            frame.unbind("<e>")
            frame.unbind("<o>")
            result.config(text="Le joueur 2 a bien repondu =>"+txt[5])
            result.place(x=170,y=100)

            def testFunc():
                global pointj2
                pointj2=pointj2+10
                j2p=str(pointj2)
                poinj2.config(text="Joueur2:"+j2p+" points")
                RectP2=repon.create_rectangle(670,370-3*pointj2,600,370,fill="orange")
            testFunc()
            if pointj1==70:
                repon.destroy()
                Question.config(text="Win Joueur 1")
            elif pointj2==70:
                repon.destroy()
                Question.config(text="Win Joueur 2")


    def repJ2D(event):
        RepJ2=txt[4]
        if RepJ2==RepVr:
            Question.place_forget()
            Rep1.place_forget()
            Rep2.place_forget()
            Rep3.place_forget()
            Rep4.place_forget()
            frame.unbind("<r>")
            frame.unbind("<p>")
            result.config(text="Le joueur 2 a bien repondu =>"+txt[5])
            result.place(x=170,y=100)

            def testFunc():
                global pointj2
                pointj2=pointj2+10
                j2p=str(pointj2)
                poinj2.config(text="Joueur2:"+j2p+" points")
                RectP2=repon.create_rectangle(670,370-3*pointj2,600,370,fill="orange")
            testFunc()
            if pointj1==70:
                repon.destroy()
                Question.config(text="Win Joueur 1")
            elif pointj2==70:
                repon.destroy()
                Question.config(text="Win Joueur 2")



#Attribution des définitions aux touches associées
    frame = Frame(boy)


    frame.bind("<a>", repJ1A)
    frame.pack()
    frame.bind("<z>", repJ1B)
    frame.pack()
    frame.bind("<e>", repJ1C)
    frame.pack()
    frame.bind("<r>", repJ1D)
    frame.pack()
    frame.bind("<u>", repJ2A)
    frame.pack()
    frame.bind("<i>", repJ2B)
    frame.pack()
    frame.bind("<o>", repJ2C)
    frame.pack()
    frame.bind("<p>", repJ2D)
    frame.pack()



    frame.focus_set()


RepJ1=[]
RepJ2=[]
pointj1=0
pointj2=0


#==================================================================Programme principal============================================================================================================================================================================
#Liste questions
Q1=("(7 + 3) + (20 + 17) : \n =___?  ?","A:52","B:50","C:47","D:45","C:47")
Q2=("25% des élèves de ma classe ont un chat. \n Il y a 28 élèves dans ma classe. \n Combien ont un chat ?","A:7","B:9","C:14","D: 12", "A:7")
Q3=("Lequel de ces mots est \n du genre féminin  ?","A:Tentacule","B:Echappatoire","C:Abysse","D:Eloge","B:Echappatoire")
Q4=("Les zèbres \n ont des rayures car ...","A:ça ventile","B:ça perturbe les prédateurs","C:c'est la nature","D:c'est dû à un mixage","D:c'est dû à un mixage")
Q5=("La résolution de l'oeil humain \n est de ... ","A:25 Mégaixels","B:63 Mégapixels","C:576 Mégapixels","D:1000 Mégapixels","C:576 Mégapixels")
Q6=("Où se situe la seconde Statue de la Liberté ?  ","A:Los Angeles","B:Las Vegas","C:New York","D:Paris","D:Paris")
Q7=("Le cardiologue : \n est le spécialiste ...  ","A:des pieds","B:du cerveau","C:des poumons","D:du coeur","D:du coeur")
Q8=("Le deuxième réseaux social : \n le plus utilisé est... ","A:Facebook","B:Snapchat","C:Youtube","D:Whatsapp","C:Youtube")
Q9=("La probabilité que vous aviez \n de venir au monde une fois que \n vos parents s'étaient déjà rencontré :","A:1/100","B:1/400 quadrillon","C:1/2","D:1/7 milliards","B:1/400 quadrillon")
Q10=("La date du premier Homme à avoir \n marché sur la Lune","A:1959","B:1966","C:1969","D:1970","C:1969")
Q11=("Quel animal pond \n le plus gros oeuf ?","A:l'autruche","B:la girafe","C:le dinosaure","D:la poule","A:l'autruche")
Q12=("L'objet le plus \n vendu au monde","A:vêtement Levi's","B:livre d'Harry Poter","C:téléphone","D:Coca-Cola","D:Coca-Cola")
Q13=("Combien y a-t-il de signes \n astrologiques chinois ?","A:12","B:10","C:6","D:18","A:12")
Q14=("L'objet le plus \n sale dans une maison","A:siège des toilettes","B:téléphone","C:argent","D:éponge","D:éponge")
Q15=("Quelle est la monnaie \n officielle de l'Australie ?","A:Livre australien","B:Dinar australien","C:Dollar australien","D:Kwanza","C:Dollar australien")
Q16=("Lequel de ces mots d'argtos \n ne désigne pas le travail ?  ?","A:Boulot","B:Gambille","C:Marnage","D:Taf","B:Gambille")
Q17=("Selon le dictionnaire, le mot bourdon\n ne désigne pas...","A:Une grosse cloche","B:Un bâton de pélerin","C:Une grande tristesse","D:Un avion de chasse","D:Un avion de chasse")
Q18=("Que ne désigne pas le mot fraise ?","A: Membrane intestinale","B: Collerette du XVIème siècle","C: Instrument de dentiste","D: Perle de forme évasée","D: Perle de forme évasée")
Q19=("Quelle race de chiens ne doit pas \n son nom à une zone géographique ?","A:Le chihuhua","B:Le yorkshire","C:Le terre neuve","D:Le barzoï","D:Le barzoï")
Q20=("Quel arbre produit la noix de pécan ?","A:Le macadamia","B: Le noisetier","C:Le pacanier","D:Le pécunier","C:Le pacanier")
Q21=("Lequel de ces noms communs n'est \n pas issu du nom d'une ville ?","A: Le damas","B: Le fez","C: Le labyrinthe","D: Le capharnaum","C: Le labyrinthe")
Q22=("Lequel de ces termes est spécifiquement \n utilisé dans le handball ?","A: Le nettoyage","B: Le bouton","C: Le chabala","D: L'aile de pigeon","C: Le chabala")
Q23=("Selon une superstition francaise,\n qu'est-il interdit de porter sur une scène de théâtre ?","A: Un habit vert","B: Un chapeau melon","C: Une jupe courte","D: Des dessous dentelles","A: Un habit vert")
Q24=("Quel pays a remporté la coupe du monde de football \n en 2014 ?","A:L'Argentine","B: L'Italie","C: Le Brésil	","D:L'Allemagne","D:L'Allemagne")
Q25=("En france, en quelle année la ceinture \n de sécurité est-elle devenue obligatoire à l'arrière ?","A:1980","B:1990","C:1995","D:2000","B:1990")
Q26=("Depuis le 1er janvier 2014, que doivent obligatoirement \n porter sur leur uniforme les policiers et les gendarmes","A: Un foulard","B: Leur numéro de téléphone","C: Une poche a stylos","D: Leur numéro matricule","D: Leur numéro matricule")
Q27=("Selon la tradition, quel fruit est commun a \n Guillaume Tell et à Isaac Newton ?","A: La pomme","B: La poire","C: La banane","D: L'orange","A: La pomme")
Q28=("Quel théorème est le plus ancien ?","A: Le théorème de fermat","B: Le théorème de thalès","C: Le théorème d'archimède","D:Le théorème d'L'euclide","B: Le théorème de thalès")
Q29=("Quel est le symbole chimique de l'argent ?","A: Ar","B: Ag","C: Al","D: Au","B: Ag")
Q30=("Quelle est la capitale \n de Wallis-et-Futuna ?","A:Melekeok","B:Mata-Utu","C:Marigot","D:Maseru","B:Mata-Utu")





Liste=[Q1,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10,Q11,Q12,Q13,Q14,Q15,Q16,Q17,Q18,Q19,Q20,Q21,Q22,Q23,Q24,Q25,Q26,Q27,Q28,Q29,Q30]


#Creation zone graphique
boy=Tk()
boy.title(" Fast&Genius!")
boy.config(width=1000, height=500, bg="#4682B4")

Question=Label(boy,text="BONJOUR ,\n VOUS VOULEZ COMMENCER?",fg="black",bg="#4682B4")
Question.pack(side="top")
Question.config(font=("verdana",20,"bold"))


repon=Canvas(boy,bg="#ADFF2F")
repon.config(width=700,height=400)
repon.pack()

boutonNext=Button(repon, text='Start', width=10, height=2, command=next)
boutonNext.place(x=300,y=310)

result=Label(repon,fg="black",bg="#ADFF2F")
result.config(font=("Arial",15,"bold"))



Regl=Label(repon,text="Avant d’appuyer sur Start\nlisez attentivement les instructions.",fg="black",bg="#ADFF2F")
Regl.place(x=180,y=20)
Regl.config(font=("Arial",15,"bold"))

poinj1=Label(repon,fg="black",bg="#ADFF2F")
poinj1.place(x=5,y=380)
poinj1.config(font=("Arial",10,"bold"))



poinj2=Label(repon,fg="black",bg="#ADFF2F")
poinj2.place(x=585,y=380)
poinj2.config(font=("Arial",10,"bold"))



Regl1=Label(repon,text="Le jeu s'arrête lorsque l'un des deux joueurs \n atteint le score de 70 points. ",fg="black",bg="#ADFF2F")
Regl1.place(x=200,y=80)
Regl1.config(font=("Arial",10,"bold"))


Regl2=Label(repon,text="Clavier Joueur 2:\n \n Reponse A : Touche U\nReponse B : Touche I\n Reponse C : Touche O\n Reponse D : Touche P",fg="black",bg="#ADFF2F")
Regl2.place(x=510,y=250)
Regl2.config(font=("Arial",10,"bold"))

Regl3=Label(repon,text="Clavier Joueur 1:\n \n Reponse A : Touche A\nReponse B : Touche Z\n Reponse C : Touche E\n Reponse D : Touche R",fg="black",bg="#ADFF2F")
Regl3.place(x=10,y=250)
Regl3.config(font=("Arial",10,"bold"))

Regl4=Label(repon,text="!!!ATTENTION!!! : \n Nous avons une liste de 30 questions de différents domaines.\n Mais en raison d'une erreur inconnue,\n certaines questions ne répondent pas aux commandes. \n Après chaque réponse correcte, appuyez sur Next pour passer à la question suivante \n Même si les 2 joueurs ont mal répondu, cliquez sur Next.",fg="black",bg="#ADFF2F")
Regl4.place(x=10,y=130)
Regl4.config(font=("Arial",13,"bold"))



Rep1=Label(repon,fg="black",bg="#ADFF2F")
Rep1.config(font=("verdana",20,"bold"))


Rep2=Label(repon,fg="black",bg="#ADFF2F")
Rep2.config(font=("verdana",20,"bold"))


Rep3=Label(repon,fg="black",bg="#ADFF2F")
Rep3.config(font=("verdana",20,"bold"))

Rep4=Label(repon,fg="black",bg="#ADFF2F")
Rep4.config(font=("verdana",20,"bold"))




boy.mainloop()



