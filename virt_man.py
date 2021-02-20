# ouvrir la connexion avec
import libvirt
conn = libvirt.open('qemu:///system')

# fonctions


def Mach_list():
    for name in conn.listDefinedDomains():
        dom = conn.lookupByName(name)
        infos = dom.info()
        print '#############'
        print 'ID = %d' % dom.ID()
        print 'Nom = %s' % dom.name()
        print 'Etat = %d' % infos[0]
        print 'Max Memoire = %d' % infos[1]
        print 'Nombre de CPUsvirt = %d' % infos[3]
        print 'Temps CPU (en ns) = %d' % infos[2]


def launch_Mach():
    j = 0
    for name in conn.listDefinedDomains():
        dom = conn.lookupByName(name)
        print ') Nom = %s' % dom.name()
        j = j+1
    i = int(input("Entrer le num de la machine a demarer:: "))
    name = conn.listDefinedDomains()[i]
    VM = conn.lookupByName(name)
    VM.create()


def HP_name():
    pass


def shutdown_M():
    j = 0
    for name in conn.listDefinedDomains():
        dom = conn.lookupByName(name)
        print ') Nom = %s' % dom.name()
        j = j+1
    i = int(input("Entrer le num de la machine a demarer:: "))
    name = conn.listDefinedDomains()[i]
    VM = conn.lookupByName(name)
    # tester l'etat de la machine si elle est en cours d'exe
    # VM.create()


def IP_M():
    j = 0
    for name in conn.listDefinedDomains():
        dom = conn.lookupByName(name)
        print ') Nom = %s' % dom.name()
        j = j+1
    i = int(input("Entrer le num de la machine a demarer:: "))
    name = conn.listDefinedDomains()[i]
    VM = conn.lookupByName(name)
    # recuperr l'adresse IP de la machine
    # VM.create()


# interface
while(True):
    print '0) Nom de la machine hyperviseur '
    print '1) Lister les machines virtuelles '
    print '2) demarrer une machine'
    print '3) Arreter une machine'
    print "4) L'adresse IP d'une machine virtuelle donnee "
    print '5) Quitter'
    ch = int(raw_input("Votre choix ::"))
    # main
    if(ch == 0):
        HP_name()
    if(ch == 1):
        Mach_list()
    if(ch == 2):
        launch_Mach()
    if(ch == 3):
        shutdown_M()
    if(ch == 4):
        IP_M()
    if(ch == 5):
        conn.close()
        break
    if(ch > 5):
        print 'Wrong Input \n'
        continue
