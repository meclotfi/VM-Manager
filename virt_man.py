importlibvirt
conn = libvirt.open("qemu:///system")
# interface
print '0) Nom de la machine hyperviseur \n'
print '1) Lister les machines virtuelles \n'
print '2) démarrer une machine [donne un autre menu de choix de la machine à démarrer]\n'
print '3) Arrêter une machine [donne un autre menu de choix de la machine à arrêter]\n'
print '4) L’adresse IP d’une machine virtuelle donnée [donne un autre menu de choix]'
print '5) Quitter'
ch = int(raw_input("Votre choix ::"))


def Hp_name():
    pass


def Mach_list():
    for id in conn.listDomainsID():
        dom = conn.lookupByID(id)
        infos = dom.info()
        print 'ID = %d' % id
        print 'Nom = %s' % dom.name()
        print 'Etat = %d' % infos[0]
        print 'Max Memoire = %d' % infos[1]
        print 'Nombre de CPUsvirt = %d' % infos[3]
        print 'Temps CPU (en ns) = %d' % infos[2]


def launch_Mach(name):
    VM = premier_conn.lookupByName(name)
    VM.create()


def choix_Mach():
    for (i, name) in enumerate(conn.listDefinedDomains()):
        print '%d) %s' % i, name


"""
for id in conn.listDomainsID():
dom = conn.lookupByID(id)
infos = dom.info()
print 'ID = %d' % id
print 'Nom = %s' % dom.name()
print 'Etat = %d' % infos[0]
print 'Max Memoire = %d' % infos[1]
print 'Nombre de CPUsvirt = %d' % infos[3]
print 'Temps CPU (en ns) = %d' % infos[2]
print ' '
"""
