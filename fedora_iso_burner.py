from tkinter import *
from urllib.request import urlopen
import os
import requests

class fedorainstaller():
    def __init__(self):
        pass

    def burn(self,ufi, dsk, iso, folder):
        print("burning")
        dsk_path = '/dev/' + dsk
        iso_path = folder.get()+iso
        if ufi == 1:  # supports UEFI
            os.system(
                'pkexec bash -c "umount ' + dsk_path + ' ; ' + "mkfs.vfat -n 'fedora_disk' " + dsk_path + ' ; ' + "cp -r " + iso_path + " " + dsk_path + '"')
        else:  # burn the image (doesn't support UEFI)
            os.system('pkexec dd if=' + iso_path + ' of=' + dsk_path + ' bs=4M && sync')
        print("done burning")
    def find_disk(self):
        disks = (os.popen('lsblk -I 8 -d -o name,size').read()).split('\n')
        for i in range(len(disks)):
            disks[i] = list(disks[i].split('  '))
        disks = disks[1:-1]
        return disks

    def download(self,url, dst_file,T):
        print("downloading")
        content = urlopen(url).read()
        T.delete(1.0, END)
        T.insert(END, "Downloading.......")
        outfile = open(dst_file, "wb")
        outfile.write(content)
        outfile.close()
        T.delete(1.0, END)
        T.insert(END, "Downloading Complete")
        print("done downloading")

    def checksusm(self,nof,T):
        print("checksum")
        T.delete(1.0, END)
        T.insert(END, "Verifying checksum.........")
        response = requests.get("https://spins.fedoraproject.org/static/checksums/Fedora-Spins-31-1.9-x86_64-CHECKSUM")
        cont = response.content
        cont = str(cont, 'utf-8')
        x = cont.split('\n')
        cont_dict = {}
        x = x[4:17:2]
        for i in x:
            spin = i[i.find("(") + 1:(1 + i.find(")")) - 1]
            key = i[i.find('=') + 2:]
            cont_dict[spin] = key
        syskey = (os.popen('sha256sum ' + nof).read()).split()[0]
        T.delete(1.0, END)
        T.insert(END, 'Verified checksum')
        print("done checksum")
        return syskey == cont_dict[nof]


    def s_func(self,T,variable1,variable2,var,variable3):
        print("starting")
        variable1 = variable1.get()
        variable2 = variable2.get()
        if variable1 == 'KDE plasma desktop':
            self.download("https://download.fedoraproject.org/pub/fedora/linux/releases/31/Spins/x86_64/iso/Fedora-KDE-Live-x86_64-31-1.9.iso","Fedora-KDE-Live-x86_64-31-1.9.iso",T)
            if self.checksusm('Fedora-KDE-Live-x86_64-31-1.9.iso',T):
                dsk = variable2
                self.burn(var.get(), dsk, 'Fedora-KDE-Live-x86_64-31-1.9.iso',variable3)
            else:
                T.delete(1.0, END)
                T.insert(END, 'Checksum verification failed')
        if variable1 == 'XFCE desktop':
            self.download("https://download.fedoraproject.org/pub/fedora/linux/releases/31/Spins/x86_64/iso/Fedora-Xfce-Live-x86_64-31-1.9.iso","Fedora-Xfce-Live-x86_64-31-1.9.iso",T)
            if self.checksusm('Fedora-Xfce-Live-x86_64-31-1.9.iso',T):
                dsk = variable2
                self.burn(var.get(), dsk, 'Fedora-Xfce-Live-x86_64-31-1.9.iso',variable3)
            else:
                T.delete(1.0, END)
                T.insert(END, 'Checksum verification failed')
        if variable1 == 'LXQT desktop':
            self.download("https://download.fedoraproject.org/pub/fedora/linux/releases/31/Spins/x86_64/iso/Fedora-LXQt-Live-x86_64-31-1.9.iso","Fedora-LXQt-Live-x86_64-31-1.9.iso",T)
            if self.checksusm('Fedora-LXQt-Live-x86_64-31-1.9.iso',T):
                dsk = variable2
                self.burn(var.get(), dsk, 'Fedora-LXQt-Live-x86_64-31-1.9.iso',variable3)
            else:
                T.delete(1.0, END)
                T.insert(END, 'Checksum verification failed')
        if variable1 == 'MATE-Compiz Desktop':
            self.download("https://download.fedoraproject.org/pub/fedora/linux/releases/31/Spins/x86_64/iso/Fedora-MATE_Compiz-Live-x86_64-31-1.9.iso","Fedora-MATE_Compiz-Live-x86_64-31-1.9.iso",T)
            if self.checksusm('Fedora-MATE_Compiz-Live-x86_64-31-1.9.iso',T):
                dsk = variable2
                self.burn(var.get(), dsk, 'Fedora-MATE_Compiz-Live-x86_64-31-1.9.iso',variable3)
            else:
                T.delete(1.0, END)
                T.insert(END, 'Checksum verification failed')
        if variable1 == 'Cinnamon Desktop':
            self.download("https://download.fedoraproject.org/pub/fedora/linux/releases/31/Spins/x86_64/iso/Fedora-Cinnamon-Live-x86_64-31-1.9.iso","Fedora-Cinnamon-Live-x86_64-31-1.9.iso",T)
            if self.checksusm('Fedora-Cinnamon-Live-x86_64-31-1.9.iso',T):
                dsk = variable2
                self.burn(var.get(), dsk, 'Fedora-Cinnamon-Live-x86_64-31-1.9.iso',variable3)
            else:
                T.delete(1.0, END)
                T.insert(END, 'Checksum verification failed')
        if variable1 == 'LXDE Desktop':
            self.download("https://download.fedoraproject.org/pub/fedora/linux/releases/31/Spins/x86_64/iso/Fedora-LXDE-Live-x86_64-31-1.9.iso","Fedora-LXDE-Live-x86_64-31-1.9.iso",T)
            if self.checksusm('Fedora-LXDE-Live-x86_64-31-1.9.iso',T):
                dsk = variable2
                self.burn(var.get(), dsk, 'Fedora-LXDE-Live-x86_64-31-1.9.iso', variable3)
            else:
                T.delete(1.0, END)
                T.insert(END, 'Checksum verification failed')
        if variable1 == 'SoaS Desktop':
            self.download("https://download.fedoraproject.org/pub/fedora/linux/releases/31/Spins/x86_64/iso/Fedora-SoaS-Live-x86_64-31-1.9.iso","Fedora-SoaS-Live-x86_64-31-1.9.iso",T)
            if self.checksusm('Fedora-SoaS-Live-x86_64-31-1.9.iso',T):
                dsk = variable2
                self.burn(var.get(), dsk, 'Fedora-SoaS-Live-x86_64-31-1.9.iso', variable3)
            else:
                T.delete(1.0, END)
                T.insert(END, 'Checksum verification failed')

    def main(self):
        root = Tk()
        root.geometry("820x780+700+100")
        root.resizable(False, False)
        root.title("Fedora installer")

        wel=Label(root, text='Welcome to the fedora installer ')
        wel.config(font=('Ubuntu',36))
        wel.place(x=45, y=20)
        l = Label(root, text='_'*120)
        l.place(x=0,y=80)

        spin = Label(root, text='choose your fedora spin: ')
        spin.config(font=('Ubuntu', 22))
        spin.place(x=45, y=140)
        l = Label(root, text='_' * 120)
        l.place(x=0, y=200)

        OPTIONS1 = ['KDE plasma desktop', 'XFCE desktop', 'LXQT desktop', 'MATE-Compiz Desktop','Cinnamon Desktop',
                    'LXDE Desktop','SoaS Desktop']
        variable1 = StringVar(root)
        variable1.set(OPTIONS1[0])
        w1 = OptionMenu(root, variable1, *OPTIONS1)
        w1.place(x=400,y=145)
        w1.config(font=10)

        disk = Label(root, text='choose your USB disk: ')
        disk.config(font=('Ubuntu', 22))
        disk.place(x=45, y=250)
        l = Label(root, text='_' * 120)
        l.place(x=0, y=310)

        OPTIONS2 = ['choose disk']
        lst = self.find_disk()
        for i in lst:
            s = i[0]
            OPTIONS2.append(s)
        variable2 = StringVar(root)
        variable2.set(OPTIONS2[0])
        w2 = OptionMenu(root, variable2, *OPTIONS2)
        w2.place(x=400, y=255)
        w2.config(font=10)

        disk = Label(root, text='Does your system support UEFI :')
        disk.config(font=('Ubuntu', 20))
        disk.place(x=45, y=345)
        l = Label(root, text='_' * 120)
        l.place(x=0, y=420)

        var = IntVar(root)
        R1 = Radiobutton(root, text="Yes", variable=var, value=1, indicatoron=0, height=1, width=7, font=10)
        R1.place(x=225, y=395)
        R2 = Radiobutton(root, text="No", variable=var, value=0, indicatoron=0, height=1, width=7, font=10)
        R2.place(x=495, y=395)

        T = Text(root, height=7, width=102)
        T.place(x=0, y=650)

        pth = Label(root, text='enter path to this python file :')
        pth.config(font=('Ubuntu', 20))
        pth.place(x=20, y=480)
        variable3 = StringVar(root)
        textbox = Entry(root,textvariable=variable3, width=40)
        textbox.place(x=410,y=485)
        textbox.config(font=16)

        s = Button(root, text="Start", height=2, width=10, font=10,
                   command=lambda: self.s_func(T, variable1, variable2, var, variable3))
        s.place(x=410, y=600, anchor=CENTER)

        root.mainloop()


instance2 = fedorainstaller()
instance2.main()
