import os 
import getpass

os.system("tput setaf 3")
print("\n\t\t******************AutoPY Welcomes You!!*******************")
os.system("tput setaf 7")
print("\n\t------------------------------------------------------------------------------------------------------")

passwd = getpass.getpass("Enter your password : ")

if passwd == "onkar":
    print("\n\t\t-----------------> you have sucessfully logged in <--------------------------")
else:
    print("Wrong password")
    exit()

os.system("tput setaf 3")
print("\n\n\t 1)-> Linux Automation   2)-> Hadoop Automation  3)-> AWS Cloud Automation   4)-> Docker Automation")
os.system("tput setaf 7")
r = input("\n\t\tWhich Automation Would You Like To Choose ?: ----> ")

if int(r) == 1:
 ws = input("\n\t\t\tSelect Your Workspace(Local/Remote) : ")

 os.system("tput setaf 3")
 print("\n\t--------------**-------------------Linux Automation Console--------------------**---------------")
 os.system("tput setaf 7")
 if ws == "Remote":
      ip = input("\n\t\t\tEnter Remote IP: ")
 while True:
       print("\n\n************************************** Menu List ************************************************")
       print("""
\n\t\t
Press 1: Show Date
press 2: Show Calender
press 3: Run any Linux Command
press 4: Create Logical Partiton
press 5: Mount The LVM Partition
press 6: Extend / Decrease the Size of Logical Volume
press 7: Add Hard Disks To Volume Group Dynamically 
press 8: Configure A Web Server
press 9: Capture Data Packets
press 10: Exit
""")
  
       ch = input("\n\t\t\t\tEnter your choice: ")
       print("\n\t-----------------------------------------------------------------------------------")


       if ws == "Local":

            if int(ch) == 1:
                print("\n\t\t\tShowing the Date")
                print("---------------------------------------------------------------------------------")
                os.system('date')
            elif int(ch) == 2:
                print("\n\t\t\tShowing the Calender")
                print("---------------------------------------------------------------------------------")
                os.system('cal')
            elif int(ch) == 3:
                cmd = input("Enter your Linux Command :")
                os.system('sudo {}'.format(cmd))
            elif int(ch) == 4:    
                dev = input("\t\t\t\tEnter Your Device Name : ")
                os.system('pvcreate {}'.format(dev))
                print("\t\t\tSucessfully Created pv : {}".format(dev))
                os.system('pvdisplay {}'.format(dev))
                print("------------------------------------------------------")
                vg = input("\t\t\t\tEnter The Name of Volume Group : ")
                os.system('vgcreate {}  {}'.format(vg , dev))
                os.system('vgdisplay {}'.format(vg))
                print("------------------------------------------------------")
                lv = input("\t\t\t\tEnter Your Logical Volume Name : ")
                sz = input("\t\t\t\tEnter the Size of Partition you want : ")
                os.system('lvcreate --size {} --name {} {}'.format(sz , lv ,vg))
                os.system("lvdisplay {}/{}".format(vg ,lv))
                print("------------------------------------------------------")
                os.system('mkfs.ext4 /dev/{}/{}'.format(vg , lv))
                print("\t\t\tLogical Volume Sucessfully Formatted ..")
            elif int(ch) == 5:
                fold = input("\t\tEnter your folder Name which you want to mount on LVM Parition : ")
                vg = input("\t\tEnter Volume Group Name : ")
                lv = input("\t\tEnter Logical Volume Name : ")
                os.system("mount /dev/{}/{}  {}".format(vg , lv , fold))
                print("\t\t\tSucessfully Mounted the LVM Partiton ..")
                os.system('df -hT')
            elif int(ch) == 6:
                ex = input("\n\tDo you want to extend/reduce the Size of LVM? : ")
                if ex == "extend":
                    ex = input("\n\t\tHow much you want to extend? : ")
                    vg = input("\t\tEnter Your Volume Group Name : ")
                    lv = input("\t\tEnter Your Logical Volume Name : ")
                    os.system('ssh {} lvextend --size {} /dev/{}/{}'.format(ip , ex , vg , lv))
                    print("\t\t\tSucessfully Extended the Size of LVM Partition ")
                    os.system('ssh {} resize2fs  /dev/{}/{}'.format(ip , vg ,lv))
                    os.system('ssh {} df -hT'.format(ip))
                    os.system('df -hT')
                elif ex == "reduce":
                    ex = input("\n\t\tHow much you want to reduce? : ")
                    vg = input("\t\tEnter Your Volume Group Name : ")
                    lv = input("\t\tEnter Your Logical Volume Name : ")
                    os.system('ssh {} lvreduce --size {} /dev/{}/{}'.format(ip , ex , vg , lv))
                    print("\t\t\tSucessfully reduced the Size of LVM Partition ")
                    os.system('ssh {} resize2fs  /dev/{}/{}'.format(ip , vg ,lv))
                    os.system('ssh {} df -hT'.format(ip))
                    os.system('df -hT') 

            elif int(ch) == 7:
                nw = input("\t\tEnter the Name of Device you want to Add in Volume Group (LVM) : ")
                vg = input("\t\tEnter Volume Group Name : ")
                os.system('vgextend {} {}'.format(vg , nw))
                print("\t\tDynamically Added Extra Storage or Volume in LVM")
                print("-------------------------------------------------------------------")
                os.system('vgdisplay {}'.format(vg))

            elif int(ch) == 8:
                os.system('yum install httpd -y')
                os.system('setenforce 0')
                os.system('systemctl start httpd')


            elif int(ch) == 9:
                nn = input("\t\tEnter Your System Network Card Name : ")
                ok = input("\t\tEnter Type of Protocol : ")
                pn = input("\t\tEnter Port Number from which Data Packets are coming : ")
                os.system('tcpdump -i {} {} port {} -n -X'.format(nn , ok , pn))
     
            elif int(ch) == 10:
                break


       elif ws == "Remote":
            

            if int(ch) == 1:
                print("\n\t\t\tShowing the Date")
                print("---------------------------------------------------------------------------------")
                os.system('ssh {} date'.format(ip))
            elif int(ch) == 2:
                print("\n\t\t\tShowing thr Calender")
                print("---------------------------------------------------------------------------------")
                os.system('ssh {} cal'.format(ip))
            elif int(ch) == 3:
                cmd = input("Enter your Linux Command :")
                os.system('ssh {} sudo {}'.format(ip , cmd))

            elif int(ch) == 4:
                dev = input("\t\t\t\tEnter Your Device Name : ")
                os.system('ssh {} pvcreate {}'.format(ip , dev))
                print("\t\t\tSucessfully Created pv : {}".format(dev))
                os.system('ssh {} pvdisplay {}'.format(ip , dev))
                print("------------------------------------------------------")
                vg = input("\t\t\t\tEnter The Name of Volume Group : ")
                os.system('ssh {} vgcreate {}  {}'.format(ip , vg , dev))
                os.system('ssh {} vgdisplay {}'.format(ip , vg))
                print("------------------------------------------------------")
                lv = input("\t\t\t\tEnter Your Logical Volume Name : ")
                sz = input("\t\t\t\tEnter the Size of Partition you want : ")
                os.system('ssh {} lvcreate --size {} --name {} {}'.format(ip , sz , lv ,vg))
                os.system("ssh {} lvdisplay {}/{}".format(ip , vg ,lv))
                print("------------------------------------------------------")
                os.system('ssh {} mkfs.ext4 /dev/{}/{}'.format(ip ,vg , lv))
                print("\t\t\tLogical Volume Sucessfully Formatted ..")
            elif int(ch) == 5:
                fold = input("\t\tEnter your folder Name which you want to mount on LVM Parition : ")
                vg = input("\t\tEnter Volume Group Name : ")
                lv = input("\t\tEnter Logical Volume Name : ")
                os.system("ssh {} mount /dev/{}/{}  {}".format(ip , vg , lv , fold))
                print("\t\t\tSucessfully Mounted the LVM Partiton ..")
                os.system('ssh {} df -hT'.format(ip))
            elif int(ch) == 6:
                ex = input("\n\tDo you want to extend/reduce the Size of LVM? : ")
                if ex == "extend":
                    ex = input("\n\t\tHow much you want to extend? : ")
                    vg = input("\t\tEnter Your Volume Group Name : ")
                    lv = input("\t\tEnter Your Logical Volume Name : ")
                    os.system('ssh {} lvextend --size {} /dev/{}/{}'.format(ip , ex , vg , lv))
                    print("\t\t\tSucessfully Extended the Size of LVM Partition ")
                    os.system('ssh {} resize2fs  /dev/{}/{}'.format(ip , vg ,lv))
                    os.system('ssh {} df -hT'.format(ip))
                    os.system('ssh {} df -hT'.format(ip))
                elif ex == "reduce":
                    ex = input("\n\t\tHow much you want to reduce? : ")
                    vg = input("\t\tEnter Your Volume Group Name : ")
                    lv = input("\t\tEnter Your Logical Volume Name : ")
                    os.system('ssh {} lvreduce --size {} /dev/{}/{}'.format(ip , ex , vg , lv))
                    print("\t\t\tSucessfully Reduced the Size of LVM Partition ")
                    os.system('ssh {} resize2fs  /dev/{}/{}'.format(ip , vg ,lv))
                    os.system('ssh {} df -hT'.format(ip))
                    os.system('ssh {} df -hT'.format(ip))
            elif int(ch) == 7:
                nw = input("\t\tEnter the Name of Device you want to Add in Volume Group (LVM) : ")
                vg = input("\t\tEnter Volume Group Name : ")
                os.system('ssh {} vgextend {} {}'.format(ip , vg , nw))
                print("\t\tDynamically Added Extra Storage or Volume in LVM")
                print("-------------------------------------------------------------------")
                os.system('ssh {} vgdisplay {}'.format(ip , vg))

            elif int(ch) == 8:
                os.system('ssh {} yum install httpd -y'.format(ip))
                os.system('ssh {} setenforce 0'.format(ip))
            
            
            elif int(ch) == 9:
                nn = input("\t\tEnter Your System Network Card Name : ")
                ok = input("\t\tEnter Type of Protocol : ")
                pn = input("\t\tEnter Port Number from which Data Packets are coming : ")
                os.system('tcpdump -i {} {} port {} -n -X'.format(nn , ok , pn))
            
       elif int(ch) == 10:
           break
    
              


elif int(r) == 2:
 os.system("tput setaf 3")
 print("\n\t--------------**------------------Hadoop Automation Console---------------------**----------")
 os.system("tput setaf 7")
 while True:
       print("\n\n************************************** Menu List ************************************************")
       print("""
\n\t\t
Press 1: Install Hadoop Requirements
press 2: Configure Name Node
press 3: Configure Data Node
press 4: Configure Hadoop Client
press 5: Limit The Data Node Storage
press 6: Upload Data To Hadoop Cluster
press 7: Read Client Data from Hadoop Cluster
press 8: Delete Client Data
press 9: Stop Name Node
press 10: Stop Data Node
press 11: Exit
""")
       ch = input("\n\t\t\t\tEnter your choice : ") 
       print("\n\t-----------------------------------------------------------------------------------")

       if int(ch) == 1:
           os.system('rpm -ivh /root/jdk-8u171-linux-x64.rpm')
           os.system('rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm  --force')
           print("\n\tHadoop Requirements Sucessfully Installed In Name Node")
           print("\n\t---------------------------------------------------------------------")
           ab = input("Enter Your Data Node IP :")
           os.system('ssh {} rpm -ivh jdk-8u171-linux-x64.rpm'.format(ab))
           os.system('ssh {} rpm -ivh  hadoop-1.2.1-1.x86_64.rpm  --force'.format(ab))
           print("\n\tHadoop Requirements Sucessfully Installed In Data Node")
           print("\n\t---------------------------------------------------------------------")
           bb = input("Enter Your Client Node IP :")
           os.system('ssh {} rpm -ivh jdk-8u171-linux-x64.rpm'.format(bb))
           os.system('ssh {} rpm -ivh  hadoop-1.2.1-1.x86_64.rpm  --force'.format(bb))
           print("\n\tHadoop Requirements Sucessfully Installed In Client Node")
           print("\n\t---------------------------------------------------------------------")
           
       elif int(ch) == 2:
           dir = input("\n\t\tEnter your Name Node directory name : ")
           print("\t\t\t\tConfiguring hdfs-site.xml file ............")
           os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/hdfs-site.xml")
           os.system("echo -e '\n<!-- Put site-specific property overrides in this file. -->' >> /root/hdfs-site.xml")
           os.system('echo -e "\n<configuration>" >> /root/hdfs-site.xml')
           os.system('echo -e "\n<property>" >> /root/hdfs-site.xml')
           os.system('echo -e "<name>dfs.name.dir</name>" >> /root/hdfs-site.xml')
           os.system('echo -e "<value>{}</value>" >> /root/hdfs-site.xml'.format(dir))
           os.system('echo -e "</property>" >> /root/hdfs-site.xml')
           os.system('echo -e "\n</configuration>" >> /root/hdfs-site.xml')
           os.system('rm -rf /etc/hadoop/hdfs-site.xml')
           os.system('cp  /root/hdfs-site.xml  /etc/hadoop')
           os.system('rm -rf /root/hdfs-site.xml')
           print("\n\tFormatting the Name Node ..............................")
           print()
           os.system('hadoop namenode -format')
           print()
           print()
           nip = input("Enter Name Node IP :")
           print("\t\t\t\tConfiguring core-site.xml file ...........")
           os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/core-site.xml")
           os.system('echo -e "\n<!-- Put site-specific property overrides in this file. -->" >> /root/core-site.xml')
           os.system('echo -e "\n<configuration>" >> /root/core-site.xml')
           os.system('echo -e "\n<property>" >> /root/core-site.xml')
           os.system('echo -e "<name>fs.default.name</name>" >> /root/core-site.xml')
           os.system('echo -e "<value>hdfs://{}:9001</value>" >> /root/core-site.xml'.format(nip))
           os.system('echo -e "</property>" >> /root/core-site.xml')
           os.system('echo -e "\n</configuration>" >> /root/core-site.xml')
           os.system('rm -rf /etc/hadoop/core-site.xml')
           os.system('cp  /root/core-site.xml  /etc/hadoop')
           os.system('rm -rf /root/core-site.xml')
           print("\n\t--------------------------------------------------------------")
           print("\n\t Starting Hadoop Name Node Services .............................")
           os.system('hadoop-daemon.sh start namenode') 
           os.system('jps')

       elif int(ch) == 3:
           dip = input("\t\tEnter Data Node IP : ")
           dio = input("\t\tEnter your Data Node directory name : ")
           print("\t\t\t\tConfiguring hdfs-site.xml file ............")
           os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/hdfs-site.xml")
           os.system("echo -e '\n<!-- Put site-specific property overrides in this file. -->' >> /root/hdfs-site.xml")
           os.system('echo -e "\n<configuration>" >> /root/hdfs-site.xml')
           os.system('echo -e "\n<property>" >> /root/hdfs-site.xml')
           os.system('echo -e "<name>dfs.data.dir</name>" >> /root/hdfs-site.xml')
           os.system('echo -e "<value>{}</value>" >> /root/hdfs-site.xml'.format(dio))
           os.system('echo -e "</property>" >> /root/hdfs-site.xml')
           os.system('echo -e "\n</configuration>" >> /root/hdfs-site.xml')
           os.system('scp  /root/hdfs-site.xml  {}:/etc/hadoop'.format(dip))
           os.system('rm -rf /root/hdfs-site.xml')
           niq = input("Enter Name Node IP :")
           print("\t\t\t\tConfiguring core-site.xml file ...........")
           os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/core-site.xml")
           os.system('echo -e "\n<!-- Put site-specific property overrides in this file. -->" >> /root/core-site.xml')
           os.system('echo -e "\n<configuration>" >> /root/core-site.xml')
           os.system('echo -e "\n<property>" >> /root/core-site.xml')
           os.system('echo -e "<name>fs.default.name</name>" >> /root/core-site.xml')
           os.system('echo -e "<value>hdfs://{}:9001</value>" >> /root/core-site.xml'.format(niq))
           os.system('echo -e "</property>" >> /root/core-site.xml')
           os.system('echo -e "\n</configuration>" >> /root/core-site.xml')
           os.system('scp  /root/core-site.xml  {}:/etc/hadoop'.format(dip))
           os.system('rm -rf /root/core-site.xml')
           print("\n\t--------------------------------------------------------------")
           print("\n\t Starting Hadoop Data Node Services .............................")
           os.system('ssh {} hadoop-daemon.sh start datanode'.format(dip))
           os.system('ssh {} jps'.format(dip))
           print("\n\t--------------------------------------------------------------")
           print("\n\t Showing Hadoop Cluster Report ..............................")
           os.system('ssh {} hadoop dfsadmin -report'.format(dip))

      
       elif int(ch) == 4:
           yu = input("Enter Name Node IP : ")
           print("\t\t\t\tConfiguring core-site.xml file ...........")
           ip = input("\n\t\tEnter Client IP : ")
           os.system("echo -e '<?xml version=\"1.0\"?> \n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>' > /root/core-site.xml")
           os.system('echo -e "\n<!-- Put site-specific property overrides in this file. -->" >> /root/core-site.xml')
           os.system('echo -e "\n<configuration>" >> /root/core-site.xml')
           os.system('echo -e "\n<property>" >> /root/core-site.xml')
           os.system('echo -e "<name>fs.default.name</name>" >> /root/core-site.xml')
           os.system('echo -e "<value>hdfs://{}:9001</value>" >> /root/core-site.xml'.format(yu))
           os.system('echo -e "</property>" >> /root/core-site.xml')
           os.system('echo -e "\n</configuration>" >> /root/core-site.xml')
           os.system('scp  /root/core-site.xml  {}:/etc/hadoop'.format(ip))
           print("\t\tHadoop Client Sucessfully Configured.........")

       elif int(ch) == 5:
           ip = input("\n\tEnter Data Node IP : ")
           si = input("\n\tDo You want to extend/reduce Data Node Storage? : ")
           if si == "extend":
               os.system('ssh {} df -hT'.format(ip))
               ex = input("\n\t\tHow much you want to extend? : ")
               vg = input("\t\tEnter Your Volume Group Name : ")
               lv = input("\t\tEnter Your Logical Volume Name : ")
               os.system('ssh {} lvextend --size {} /dev/{}/{}'.format(ip , ex , vg , lv))
               print("\t\t\tSucessfully Extended the  Data Node Storage ")
               os.system('ssh {} resize2fs  /dev/{}/{}'.format(ip , vg ,lv))
               print("------------------------------------------------------------")
               os.system('ssh {} df -hT'.format(ip))
           elif si == "reduce":
               os.system('ssh {} df -hT'.format(ip))
               ex = input("\n\t\tHow much you want to reduce? : ")
               vg = input("\t\tEnter Your Volume Group Name : ")
               lv = input("\t\tEnter Your Logical Volume Name : ")
               os.system('ssh {} lvextend --size {} /dev/{}/{}'.format(ip , ex , vg , lv))
               print("\t\t\tSucessfully Reduced Data Node Storage ")
               os.system('ssh {} resize2fs  /dev/{}/{}'.format(ip , vg ,lv))
               print("------------------------------------------------------------")
               os.system('ssh {} df -hT'.format(ip))
       
       elif int(ch) == 6:
           ci = input("\t\tEnter Client IP : ")
           fiz = input("\t\tEnter The Name of File You want to upload on Hadoop Cluster : ")
           os.system('ssh {} hadoop fs -put {} /'.format(ci , fiz))
           print("\t\t\tFile Sucessfully Uploaded .......................")
           os.system('ssh {} hadoop fs -ls /'.format(ci))
       
       elif int(ch) == 7:
           co = input("\t\tEnter Client IP : ")
           fii = input("\t\tEnter Your File Name : ")
           os.system('ssh {} hadoop fs -cat /{}'.format(co , fii))

       elif int(ch) == 8:
           ty = input("\t\tEnter Client IP : ")
           foi = input("\t\tEnter Your File Name : ")
           os.system('ssh {} hadoop fs -rm /{}'.format(ty , foi))
           print("\t\tSucessfully Deleted File {} ".format(foi))
       
       elif int(ch) == 9:
           os.system('hadoop-daemon.sh stop namenode')
           os.system('jps')

       elif int(ch) == 10:
           ip = input("\n\tEnter Data Node IP : ")
           os.system('ssh {} hadoop-daemon.sh stop datanode'.format(ip))
           os.system('ssh {} jps'.format(ip))
       
       elif int(ch) == 11:
           break