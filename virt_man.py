# ouvrir la connexion avec
import libvirt
conn = libvirt.open('qemu:///system')

# fonctions


def Mach_list():
    domains = conn.listAllDomains(0)
    for dom in domains:
        infos = dom.info()
        print '#############'
        id = dom.ID()
        if id == -1:
            print"le domain n'est pas en cours d'execution donc il n'a pas d'ID."
        else:
            print 'The ID = %s' % str(id)
        print 'Nom = %s' % dom.name()
        etat = State(infos[0])
        print 'Etat = %s' % etat
        print 'Max Memoire = %d' % infos[1]
        print 'Nombre de CPUsvirt = %d' % infos[3]
        print 'Temps CPU (en ns) = %d' % infos[2]
    print'******************'


def launch_Mach():
    j = 0
    domains = conn.listAllDomains(0)
    for dom in domains:
        name = dom.name()
        print '{}) Nom = {}'.format(str(j), dom.name())
        j = j+1
    i = int(input("Entrer le num de la machine a demarer:: "))
    VM = domains[i]
    VM.create()


def HP_name():
    print "Le nom de l'hyperviseur est %s" % conn.getHostname()


def shutdown_M():
    j = 0
    domains = conn.listAllDomains(0)
    for dom in domains:
        name = dom.name()
        print '{}) Nom = {}'.format(str(j), dom.name())
        j = j+1
    i = int(input("Entrer le num de la machine a Arreter:: "))
    VM = domains[i]
    # tester l'etat de la machine si elle est en cours d'exe
    state = dom.info()[0]
    if state == libvirt.VIR_DOMAIN_RUNNING:
        VM.destroy()
        print "Arret de VM : %s" % VM.name()
    else:
        print "VM n'est pas en cours d'execution"


def IP_M():
    j = 0
    domains = conn.listAllDomains(0)
    for dom in domains:
        print '{}) Nom = {}'.format(str(j), dom.name())
        j = j+1
    i = int(input(
        "Entrer le numero de la machine que vous voulez obtenir les informations IP:: "))
    VM = domains[i]
    if VM.info()[0] == libvirt.VIR_DOMAIN_RUNNING:
        try:
            ifaces = dom.interfaceAddresses(
                libvirt.VIR_DOMAIN_INTERFACE_ADDRESSES_SRC_AGENT, 0)
        except libvirt.libvirtError as e:
            print str(e)
            return 0
        print("The interface IP addresses:")
        for (name, val) in ifaces.iteritems():
            if val['addrs']:
                for ipaddr in val['addrs']:
                    if ipaddr['type'] == libvirt.VIR_IP_ADDR_TYPE_IPV4:
                        print(ipaddr['addr'] + " VIR_IP_ADDR_TYPE_IPV4")
                    elif ipaddr['type'] == libvirt.VIR_IP_ADDR_TYPE_IPV6:
                        print(ipaddr['addr'] + " VIR_IP_ADDR_TYPE_IPV6")


def State(state):
    if state == libvirt.VIR_DOMAIN_NOSTATE:
        return 'NOSTATE'
    elif state == libvirt.VIR_DOMAIN_RUNNING:
        return 'RUNNING'
    elif state == libvirt.VIR_DOMAIN_BLOCKED:
        return 'BLOCKED'
    elif state == libvirt.VIR_DOMAIN_PAUSED:
        return 'PAUSED'
    elif state == libvirt.VIR_DOMAIN_SHUTDOWN:
        return 'SHUTDOWN'
    elif state == libvirt.VIR_DOMAIN_SHUTOFF:
        return 'SHUTOFF'


# interface
while(True):
    print'<<<<<<<<<<<<<<<<<<< VM Manager >>>>>>>>>>>>>>>>>>>>>>>>>>>>\n'
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
    elif(ch == 1):
        Mach_list()
    elif(ch == 2):
        launch_Mach()
    elif(ch == 3):
        shutdown_M()
    elif(ch == 4):
        IP_M()
    elif(ch == 5):
        conn.close()
        break
    elif(ch > 5):
        print 'Wrong Input \n'
        continue
