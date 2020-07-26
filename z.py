
print '''types of networking available
        1. connecting number of computers.
        2. connecting buildings/offices/factory in a city.
        3. connecting different cities.\n'''
num=input("Enter the option for networking as you like: ")
if num==1:
    computer=input("\nEnter number of computer for networking max(50): ")
    rang1=input("Enter your range for networking max(500): ")
    if (computer<=20 or rang1<=100):
        print "\nNetworking in these range are come in local area network (LAN)"
        print '''\nyou have two option in cabling.
                1. Twisted pair cable.
                2. Coaxial cable.
                
         If you want more speed and cheap then choose twisted pair cable otherwise coaxial cable.'''
        num1=input("Enter your option :")
        if (num1==1):
            print '''you are select  twisted pair cable which provide :-
                         (1). maximum segment length :- 100 meters
                         (2). supported bandwith :-
                                       a. 100 mbps for unshielded twisted pair(UTP)
                                       b. 500 mbps for shielded twisted pair(STP)
                         (3). cheapest cost.'''
        elif(num1==2):
           print '''you are select  coaxial cable which provide :-
                         (1). maximum segment length :- 185 meters (Thinnet) and 500 meters (Thicknet).
                         (2). supported bandwith 10 mbps.
                         (3). Thinnet coaxial cable is cheaper and Thicknet coaxial cable is at moderate cost. '''
        else:
               print "Invalid option"
        
    else:
        print '''\nNetworking in these range are  also come in local area network (LAN)
                   but it cause traffic signal'''
        print '''\nyou have two option in cabling.
                1. Twisted pair cable.
                2. Coaxial cable.
                
      That time you select coaxial cable for good cabling , if you want to cheaper cable than select Twisted pair cable'''
        num2=input("Enter your option : ")
        if num2==1:
            print '''you are select  twisted pair cable which provide :-
                         (1). maximum segment length :- 100 meters
                         (2). supported bandwith :-
                                       a. 100 mbps for unshielded twisted pair(UTP)
                                       b. 500 mbps for shielded twisted pair(STP)
                         (3). cheapest cost.


                        BUT TWISTED PAIR CABLE IS NOT RELIABLE  '''
        elif(num2==2):
            print '''you are select  coaxial cable which provide :-
                         (1). maximum segment length :- 185 meters (Thinnet) and 500 meters (Thicknet).
                         (2). supported bandwith 10 mbps.
                         (3). Thinnet coaxial cable is cheaper and Thicknet coaxial cable is at moderate cost. '''
        else:
               print "Invalid option"
            
    gd=raw_input("\npress enter for grtting topology.")
    print '''\n Topology of computers present for networking are following :-
                      (1). Star Topology            (2). Bus/Linear Topology
                      (3). Ring Topology            (4). Tree Topology
                      (5). Graph Topology        (6). Mesh Topology'''
    num3=input("\nenter your option to select  topology: ")
    if num3==1:
        print '''\nYou are select Star Topology.

                   The advantage of Star Topology are following :-
                   (1). Ease of service.
                   (2). One device per connection.
                   (3). Centralized control/prolem diagnosis.
                   (4). Simple access protocols.

                The disadvantage of Star Topology are following :-
                   (1). Long cable length
                   (2). Difficult to expand '''
    elif num3==2:
        print '''\nyou are select Bus/Linear  Topology.

                   The advantage of Bus/Linear Topology are following :-
                   (1). Short cable length and simple wiring layout.
                   (2). Resilient architecture
                   (3). Easy to extend.

                The disadvantage of Bus/Linear Topology are following :-
                   (1). Fault diagnosis is difficult.
                   (2). Repeater configuration.'''
    elif num3==3:
        print '''\nyou are select Ring Topology.

                   The advantage of Ring Topology are following :-
                   (1). Short cable length.
                   (2). suitable for optical fibres.
                   (3). No wiring closet space required.

                The disadvantage of Ring Topology are following :-
                   (1). Node failure cause network failure
                   (2). Network reconfiguration is difficult.'''
    elif num3==4:
        print '''\nyou are select Tree Topology.

                   The advantage of Tree Topology are following :-
                   (1). It have a hierarchical flow of data and control.
                   (2). It is a hybrid topology
                   (3). Short cable length 

                The disadvantage of  Topology are following :-
                   (1). Fault diagnosis is difficult.
                   (2). Repeater configuration.'''
    elif num3==5:
        print '''\nyou are select Graph Topology.

                   The advantage of Graph Topology are following :-
                   (1). Node are connected together in anarbitrary fashion.
                   (2). A link may or may not connected two or more node.
                   (3). there will be multiple link.'''
    elif(num3==6):
        print '''\nyou are select Mesh Topology.

                   The advantage of Mesh Topology are following :-
                   (1). Each node connected with more node.
                   (2). It is used in large internetworking environments.
                   (3). Communication is possible between two nodes.'''
    else:
               print "Invalid option"
    jg=raw_input("\npress enter for getting network devices.")
    print '''\nNetwork devices available for networking are following:-
                     (1). Hub            (2). Switch
                "Server is neccessary for all type of networking."'''
    num4=input("Enter your option to select network device: ")
    if num4==1:
         print '''You are selected  Hub for ---
                     (1). Connecting computer to computer together.
                     (2). It is used for spiliting signals.
                     (3). It is used in short range of computers.
     
               "Hub is not recover if it fail but it is cheaper and must be connected each computer with Hub"'''
    else:
          print  '''You are selected  Switch for ---
                     (1). Each connection get full bandwidth.
                     (2). It is also used for spiliting signals.
                     (3). It is  also used in short range of computers.

               Switch is recover after fails but it is expensve than Hub. '''
elif num==2:
     build=input("\nEnter number of building/offices/factory in a city you are connected max(10); ")
     range2=input("\nEnter your range of buildings in km(10 km); ")
     if (build<=6 and range2<=6):
          print "\nNetworking in these range are come in metropolitan area network (MAN)"
          print '''\nYou have two option in cabling.
                1. coaxial cable.
                2. optical fibers cable.
              If you want  cheaper cable  then choose coaxial cable. For better transmission speed choose optical fibers cable'''
          res1=input("Enter your option :")
          if (res1==1):
             print '''you are select  coaxial cable which provide :-
                         (1). Maximum segment length :- 185 meters (Thinnet) and 500 meters (Thicknet).
                         (2). Supported bandwith 10 mbps.
                         (3). Thinnet coaxial cable is cheaper and Thicknet coaxial cable is at moderate cost. '''
          elif(res1==2):
               print '''you are select  optical fibers cable which provide :-
                         (1). Maximum segment length :-2 km for multinode and 100 km for single node.
                         (2). Supported bandwith 100 mbps for multinode and 2 gbps for singlenode.
                         (3). Optical fibers cable is very expensive.'''
          else:
               print "invalid option."
     elif (build<=10 and range2>6):
          print "\nNetworking in these range are come in metropolitan area network (MAN)"       
          print '''\nYou have only  one  option in cabling.
                1. Multinode of Optical fibers cable.
          Multinode of Optical fibers cable is very hard and expensive.'''
     else:
          print "Range is more than 10 km. "
     gdl=raw_input("\npress enter for grtting topology.")
     print '''\n Topology of buildings/factory/offices present for networking are following :-
                      (1). Star Topology            (2). Bus/Linear Topology
                      (3). Ring Topology            (4). Tree Topology
                      (5). Graph Topology        (6). Mesh Topology'''
     res2=input("\nenter your option to select  topology: ")
     if res2==1:
        print '''\nYou are select Star Topology.

                   The advantage of Star Topology are following :-
                   (1). Ease of service.
                   (2). One device per connection.
                   (3). Centralized control/prolem diagnosis.
                   (4). Simple access protocols.

                The disadvantage of Star Topology are following :-
                   (1). Long cable length
                   (2). Difficult to expand '''
     elif res2==2:
        print '''\nyou are select Bus/Linear  Topology.

                   The advantage of Bus/Linear Topology are following :-
                   (1). Short cable length and simple wiring layout.
                   (2). Resilient architecture
                   (3). Easy to extend.

                The disadvantage of Bus/Linear Topology are following :-
                   (1). Fault diagnosis is difficult.
                   (2). Repeater configuration.'''
     elif res2==3:
        print '''\nyou are select Ring Topology.

                   The advantage of Ring Topology are following :-
                   (1). Short cable length.
                   (2). suitable for optical fibres.
                   (3). No wiring closet space required.

                The disadvantage of Ring Topology are following :-
                   (1). Node failure cause network failure
                   (2). Network reconfiguration is difficult.'''
     elif res2==4:
        print '''\nyou are select Tree Topology.

                   The advantage of Tree Topology are following :-
                   (1). It have a hierarchical flow of data and control.
                   (2). It is a hybrid topology
                   (3). Short cable length 

                The disadvantage of  Topology are following :-
                   (1). Fault diagnosis is difficult.
                   (2). Repeater configuration.'''
     elif res2==5:
        print '''\nyou are select Graph Topology.

                   The advantage of Graph Topology are following :-
                   (1). Node are connected together in anarbitrary fashion.
                   (2). A link may or may not connected two or more node.
                   (3). there will be multiple link.'''
     elif(res2==6):
        print '''\nyou are select Mesh Topology.

                   The advantage of Mesh Topology are following :-
                   (1). Each node connected with more node.
                   (2). It is used in large internetworking environments.
                   (3). Communication is possible between two nodes.'''
     else:
               print "Invalid option"
     jgh=raw_input("\npress enter for getting network devices.")
     print '''\nNetwork devices available for networking are following:-
                     (1).  Repeater           (2). Bridge         (3). Router
                "Server Hub and Switch are neccessary for all type of networking."'''
elif num==3:
    city=input("\nEnter number of city you are connected max(10); ")
    range3=input("\nEnter your range of city in km(1000 km); ")
    if (city<=10 and range3<=1000):
          print "\nNetworking in these range are come in Wide Area Network (WAN)"
          print '''\nYou have three option in cabling.
                1. Micro wave.
                2. Radio wave.
                3. Satellite.
              If you want  cheaper way of cabling to connect city choose optical fibers cable. '''
          res3=input("Enter your option :")
          if (res3==1):
             print '''you are select Micro wave which provide :-
                         (1). It offer ease of communication.
                         (2). Microwave have the capability to communicate over oceans.
                         (3). It provide cheaper and digging trenches for laying cables. '''
          elif(res3==2):
               print '''you are select  Radio wave which provide :-
                         (1). It offer ease of communication over difficult terrain.
                         (2). It offers fredom from land acquisition rightsthat are required for laying ,
                                repairing the cables.
                         (3).  It provide cheaper and digging trenches for laying cables.'''
          elif(res3==3):
               print '''you are select  satellite which provide :-
                         (1). Area coverage through satellite transmission is quite large.
                         (2). The heavy usage of intercontinental trffic makes the satellite commercial
                                attractive.
                         (3). satellite can cover large area of Earth. '''
          else:
              print "Invalid option"
          jgha=raw_input("\npress enter for getting network devices.")
          print '''\nNetwork devices available for networking are following:-
                     (1).  Repeater           (2). Bridge
                     (3). Router                (4). Gateway
                "Server , Hub and Switch are neccessary for all type of networking."'''
          res4=input("Enter your option to select network device: ")
    if res4==1:
         print '''You are selected  Reapeter for ---
                     (1). It amplifies the signal for long distance transmission.
                     (2). It exceeds the maximum rated distance.
                     (3). It is used in long range of network.'''
     
    elif res4==2:
          print  '''You are selected  Bridge for ---
                     (1). Connects large networks without transfer of data.
                     (2). Data is not destined.'''
    elif res4==3:
          print  '''You are selected  Router for ---
                     (1). It is like Bridge but handle diffirently.
                     (2).  It is used in long range of network.
                     (3). It is a type of hardware.'''
    elif res4==4:
          print  '''You are selected  Gateway for ---
                     (1). It connect diffirent network like LAN-MAN and MAN-WAN.
                     (2).  It is a type of software.'''
    else:
        print "Invalid option."
          
                         

                
     
                
    

          
