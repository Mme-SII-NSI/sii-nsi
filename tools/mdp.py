from random import *

def generation() :
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    id_lettre = randint(0, 25)
    id_chiffre = randint(0,9)
    mdp = alphabet[id_lettre] + str(id_chiffre) + alphabet[id_lettre]
    for i in range(2) :
        id_lettre = randint(0, 25)
        mdp += alphabet[id_lettre]
    for j in range(5) :
        id_chiffre = randint(0,9)
        mdp += str(id_chiffre)
    return mdp

liste_mdp = ['x1xxy54335', 'm7moh80089', 'g3gou89576', 'q9qtv60547', 'n8nru91134', 'g8gdx35360', 'j4jci29001', 'b6bzw04212', 'f9fcj82823', 'r0rpa28969', 'p0phi24687', 'y2ysu01501', 'c6cer00528', 'r6rud16688', 'z3zzu86595', 'z9zpk71681', 'u2uea85772', 'h9hfp02079', 'l5lnj69451', 'k8kuv19448', 'k2ktr41324', 'm6mtc55665', 'g8gdu86611', 'l7lvc18063', 'c7cdt74846', 'o9oue62006', 'd3dgk59013', 'l8los80794', 'q8qoh90055', 'q5qqu45610', 'w6wcv85297', 'z7zsl88822', 'x3xpl01648', 'h3hjq88729', 't5thw39297', 'a6aed25995', 'g6ggz88590', 'v0van80635', 'v7vkg04332', 'x6xot74271','m1mef11181', 'u8unb83300', 's9sen62363', 'e0ecc72199', 'i2igk88375', 't3tto93993', 't3tfb65318', 'w9weh62215', 'x6xvr41496', 't5tyv06683', 'z6zqz21381', 'i2ifw45847', 's9soe88025', 'e1elb64559', 'r7ryn33706', 'u5uvq94315', 'i5iyg84280', 'm1miq50193', 'c0cry53224', 't6trf35578', 'h4hwd34922', 
'q0qvk70292', 'j8jpy97028', 'f6ftb25895', 'b5bkm44631', 'h6hls06448', 'v7vic40911', 't0tab17055', 'l8lpj46298', 'j6jxa43507', 's5ssl87643', 'i5ivj08036', 'p0pxu76009', 'r1ren20591', 'a9aiu29874', 'b2bri38552', 'e4ewe07522', 'f5fvp99946', 'n3nfy32401', 'j7jex65053', 't4tff88908', 'p7pmh68098', 'r1rct13969', 't6tlj60981', 'i2ihc69280', 'p4pji30090', 'f2fjl37622', 'n6nsa13881', 'k0khq12027', 'q8qum64477', 'v7vur03002', 'n3neg64336', 'k1kbj48279', 'k5kci62125', 'e4edl53449', 'b2bca58638', 'f2frv17127', 'o9oab20862', 'e2evr02413', 'c7coa34069', 'x6xmt86968', 'r5ray10415', 'x2xsf06509', 'j7jsx75921', 'o1ovg73638', 'v4vvf30620']
for i in range(28) :
    mdp = generation()
    if mdp not in liste_mdp :
        liste_mdp.append(mdp)
print(liste_mdp)