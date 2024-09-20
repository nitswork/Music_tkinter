import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import webbrowser
from tkinter import Toplevel
from googleapiclient.discovery import build
log = 0
def show_login_page():
    login()
def show_home_page():
    global back_button
    if 'back_button' in globals():
        back_button.destroy()
    back_button = tk.Button(root, text='Back', command=show_login_page)
    back_button.pack(pady=20)

def login():
    for widget in root.winfo_children():
        widget.destroy()
    user_label = tk.Label(root, text='Username:', fg='black', bg='light pink')
    user_label.pack(pady=(20,5))
    user_label.config(font=('Arial',14))
    user_input = tk.Entry(root, width=35)
    user_input.pack(ipady=4, pady=(1,15))
            
    pass_label = tk.Label(root, text='Password:', fg='black', bg='light pink')
    pass_label.pack(pady=(20,5))
    pass_label.config(font=('Arial',14))
    pass_input = tk.Entry(root, width=35, show="*")
    pass_input.pack(ipady=4, pady=(1,15))
    
    btn = tk.Button(root, text='Login', bg='white', fg='blue', height=1, width=10, command=lambda: handle_log(user_input.get(), pass_input.get()))
    btn.pack(pady=(10,20))
    btn.config(font=('helvetica',15))

def signin_user(mail, passwrd):
    with open("credentials.txt", "a") as file:
        file.write(f"{mail},{passwrd}\n")
    show_home_page()

def signin():
    for widget in root.winfo_children():
        widget.destroy()
    user_label = tk.Label(root, text='Username:', fg='black', bg='light pink')
    user_label.pack(pady=(20,5))
    user_label.config(font=('Arial',14))
    user_input = tk.Entry(root, width=35)
    user_input.pack(ipady=4, pady=(1,15))
    
    pass_label = tk.Label(root, text='Password:', fg='black', bg='light pink')
    pass_label.pack(pady=(20,5))
    pass_label.config(font=('Arial',14))
    pass_input = tk.Entry(root, width=35, show="*")
    pass_input.pack(ipady=4, pady=(1,15))
    
    btn = tk.Button(root, text='Sign in', bg='white', fg='blue', height=1, width=10, command=lambda: signin_user(user_input.get(), pass_input.get()))
    btn.pack(pady=(10,20))
    btn.config(font=('helvetica',15))

def check_file(mail, passwrd):
    with open("credentials.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(",")
            if mail == stored_username and passwrd == stored_password:
                return True
    return False

def handle_log(mail, passwrd):
    if check_file(mail, passwrd):
        messagebox.showinfo("Login Successful", "You are successfully logged in.")
        log = 1
        for widget in root.winfo_children():
                if widget == btn_log:
                    widget.destroy()
        if log == 1:
            btn2=tk.Button(root, text='Next',bg='white',fg='blue',height=1,width=10,command=nxt_pge)
            btn2.pack(pady=(10,20))
            btn2.config(font=('helvetica',15))

    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def nxt_pge():
    global combobox
    new_window =tk.Toplevel(root)
    new_window.title("Login")
    new_window.geometry("600x700")
    new_window.configure(background='sky blue')
   
    text_label = tk.Label(new_window, text='Choose your Music Type:',fg='white',bg='light pink')
    text_label.pack(pady=(15,15))
    text_label.config(font=('verdana',20))

  
    def show_back_button(new_window):
            back_button_2 = tk.Button(new_window, text='Back', command=show_login_page)
            back_button_2.pack(pady=20)

    def sad_pop():
        for widget in new_window.winfo_children():
                widget.destroy()
        txt_lab=tk.Label(new_window,text='Top Songs:',fg='white',bg='black')
        txt_lab.pack(pady=(15,15))
        txt_lab.config(font=('Bold',20))
        def open_link(url):
            webbrowser.open(url)
        def create_link(new_window,url):
            link_label = tk.Label(new_window, text="1.What was I made for?: Billie Eilish",bg='black',fg="white",cursor="hand2",height=3,width=30)
            link_label.bind("<Button-1>", lambda event: open_link(url))
            return link_label
        link_url = "https://www.youtube.com/watch?v=cW8VLC9nnTo&list=RDcW8VLC9nnTo&start_radio=1"
        link_label = create_link(new_window, link_url)
        link_label.pack(padx=10, pady=10)
        link_label.config(font=('Bold',18))

        def open(url):
            webbrowser.open(url)
        def create(new_window,url):
            link_label2 = tk.Label(new_window, text="2.Can't catch me now : Olivia Rodrigo",bg='black',fg="white",cursor="hand2",height=3,width=30)
            link_label2.bind("<Button-1>", lambda event: open(url))
            return link_label2
        link_url = "https://www.youtube.com/watch?v=GlM6lcFbLSg&list=PLgzTt0k8mXzHcKebL8d0uYHfawiARhQja&index=3"
        link_label2 = create(new_window, link_url)
        link_label2.pack(padx=10, pady=10)
        link_label2.config(font=('Bold',18))

        def link(url):
            webbrowser.open(url)
        def crt_link(new_window,url):
            lnk_label = tk.Label(new_window, text="3.Heartbreak Anniversary: Giveon",bg='black',fg="white",cursor="hand2",height=3,width=30)
            lnk_label.bind("<Button-1>", lambda event: link(url))
            return lnk_label
        lnk_url = "https://www.youtube.com/watch?v=uWRlisQu4fo"
        lnk_label = crt_link(new_window, lnk_url)
        lnk_label.pack(padx=10, pady=10)
        lnk_label.config(font=('Bold',18))

        def opn_lnk(url):
            webbrowser.open(url)
        def create_lnk(new_window,url):
            link_labl = tk.Label(new_window, text="4.Oh Cecilia (Breaking My Heart): The Vamps",bg='black',fg="white",cursor="hand2",height=2,width=70)
            link_labl.bind("<Button-1>", lambda event: opn_lnk(url))
            return link_labl
        link_url = "https://www.youtube.com/watch?v=COwkCW38J54"
        link_labl = create_lnk(new_window, link_url)
        link_labl.pack(padx=10, pady=10)
        link_labl.config(font=('Bold',18))

        def openlink(url):
            webbrowser.open(url)
        def create_lk(new_window,url):
            lk_label = tk.Label(new_window, text="5.I'll Be Waiting: Cian Ducrot",bg='black',fg="white",cursor="hand2",height=3,width=30)
            lk_label.bind("<Button-1>", lambda event: openlink(url))
            return lk_label
        lk_url = "https://www.youtube.com/watch?v=qKvlU2n1nso"
        lk_label = create_lk(new_window, lk_url)
        lk_label.pack(padx=10, pady=10)
        lk_label.config(font=('Bold',18))
        show_back_button(new_window)
        
    def rom_pop():
        for widget in new_window.winfo_children():
                widget.destroy()
        txt_lab=tk.Label(new_window,text='Top Songs:',fg='white',bg='black')
        txt_lab.pack(pady=(15,15))
        txt_lab.config(font=('Bold',20))
        def open_link(url):
            webbrowser.open(url)
        def create_link(new_window,url):
            link_label = tk.Label(new_window, text="1.Steal The Show",bg='black',fg="white",cursor="hand2",height=3,width=30)
            link_label.bind("<Button-1>", lambda event: open_link(url))
            return link_label
        linkurl = "https://www.youtube.com/watch?v=DwuJeGYlYyw&list=RDDwuJeGYlYyw&start_radio=1"
        link_label = create_link(new_window, linkurl)
        link_label.pack(padx=10, pady=10)
        link_label.config(font=('Bold',18))

        def open(url):
            webbrowser.open(url)
        def create(new_window,url):
            link_label2 = tk.Label(new_window, text="2.Like Me Better",bg='black',fg="white",cursor="hand2",height=3,width=30)
            link_label2.bind("<Button-1>", lambda event: open(url))
            return link_label2
        linnk_url = "https://www.youtube.com/watch?v=BcqxLCWn-CE&list=PLgzTt0k8mXzE6H9DDgiY7Pd8pKZteis48&index=12"
        link_label2 = create(new_window, linnk_url)
        link_label2.pack(padx=10, pady=10)
        link_label2.config(font=('Bold',18))

        def link(url):
            webbrowser.open(url)
        def crt_link(new_window,url):
            lnk_label = tk.Label(new_window, text="3.What Makes You Beautiful",bg='black',fg="white",cursor="hand2",height=3,width=70)
            lnk_label.bind("<Button-1>", lambda event: link(url))
            return lnk_label
        lnk_url = "https://www.youtube.com/watch?v=QJO3ROT-A4E&list=PLgzTt0k8mXzE6H9DDgiY7Pd8pKZteis48&index=32"
        lnk_label = crt_link(new_window, lnk_url)
        lnk_label.pack(padx=10, pady=10)
        lnk_label.config(font=('Bold',18))

        def opn_lnk(url):
            webbrowser.open(url)
        def create_lnk(new_window,url):
            link_labl = tk.Label(new_window, text="4.Make You Mine",bg='black',fg="white",cursor="hand2",height=3,width=30)
            link_labl.bind("<Button-1>", lambda event: opn_lnk(url))
            return link_labl
        lin_url = "https://www.youtube.com/watch?v=nLnp0tpZ0ok"
        link_labl = create_lnk(new_window, lin_url)
        link_labl.pack(padx=10, pady=10)
        link_labl.config(font=('Bold',18))

        def openlink(url):
            webbrowser.open(url)
        def create_lk(new_window,url):
            lk_label = tk.Label(new_window, text="5.Here With Me",bg='black',fg="white",cursor="hand2",height=3,width=30)
            lk_label.bind("<Button-1>", lambda event: openlink(url))
            return lk_label
        lk_url = "https://www.youtube.com/watch?v=Ip6cw8gfHHI&list=PLgzTt0k8mXzE6H9DDgiY7Pd8pKZteis48"
        lk_label = create_lk(new_window, lk_url)
        lk_label.pack(padx=10, pady=10)
        lk_label.config(font=('Bold',18))

        def openlink(url):
            webbrowser.open(url)
        def create_lk(new_window,url):
            lk_label = tk.Label(new_window, text="6.Give me Everything.",bg='black',fg="white",cursor="hand2",height=3,width=30)
            lk_label.bind("<Button-1>", lambda event: openlink(url))
            return lk_label
        lk_url = "https://www.youtube.com/watch?v=EPo5wWmKEaI"
        lk_label = create_lk(new_window, lk_url)
        lk_label.pack(padx=10, pady=10)
        lk_label.config(font=('Bold',18))
        show_back_button(new_window)

    def fit_pop():
        for widget in new_window.winfo_children():
                widget.destroy()
        txt_lab=tk.Label(new_window,text='Top Songs:',fg='white',bg='black')
        txt_lab.pack(pady=(15,15))
        txt_lab.config(font=('Bold',20))
        def open_link(url):
            webbrowser.open(url)
        def create_link(new_window,url):
            link_label = tk.Label(new_window, text="1.Believer: Imagine Dragons",bg='black',fg="white",cursor="hand2",height=3,width=30)
            link_label.bind("<Button-1>", lambda event: open_link(url))
            return link_label
        link_url = "https://www.youtube.com/watch?v=7wtfhZwyrcc"
        link_label = create_link(new_window, link_url)
        link_label.pack(padx=10, pady=10)
        link_label.config(font=('Bold',18))

        def open(url):
            webbrowser.open(url)
        def create(new_window,url):
            link_label2 = tk.Label(new_window, text="2.Vem Dancar Kuduro: Lucenzo(ft.Big Ali)",bg='black',fg="white",cursor="hand2",height=3,width=70)
            link_label2.bind("<Button-1>", lambda event: open(url))
            return link_label2
        lik_url = "https://www.youtube.com/watch?v=uv9CjsQNtf4"
        link_label2 = create(new_window, lik_url)
        link_label2.pack(padx=10, pady=10)
        link_label2.config(font=('Bold',18))

        def link(url):
            webbrowser.open(url)
        def crt_link(new_window,url):
            lnk_label = tk.Label(new_window, text="3.GDFR: Flo Rida",bg='black',fg="white",cursor="hand2",height=3,width=70)
            lnk_label.bind("<Button-1>", lambda event: link(url))
            return lnk_label
        lnk_url = "https://www.youtube.com/watch?v=Ob3Ky7qU9ZE"
        lnk_label = crt_link(new_window, lnk_url)
        lnk_label.pack(padx=10, pady=10)
        lnk_label.config(font=('Bold',18))

        def opn_lnk(url):
            webbrowser.open(url)
        def create_lnk(new_window,url):
            link_labl = tk.Label(new_window, text="4.Animals: Maroon 5",bg='black',fg="white",cursor="hand2",height=3,width=70)
            link_labl.bind("<Button-1>", lambda event: opn_lnk(url))
            return link_labl
        link_url = "https://www.youtube.com/watch?v=qpgTC9MDx1o"
        link_labl = create_lnk(new_window, link_url)
        link_labl.pack(padx=10, pady=10)
        link_labl.config(font=('Bold',18))

        def openlink(url):
            webbrowser.open(url)
        def create_lk(new_window,url):
            lk_label = tk.Label(new_window, text="5.Another Round: (feat. Mohombi & Pitbull) ",bg='black',fg="white",cursor="hand2",height=3,width=70)
            lk_label.bind("<Button-1>", lambda event: openlink(url))
            return lk_label
        lk_url = "https://www.youtube.com/watch?v=vBzKqfKXw2c"
        lk_label = create_lk(new_window, lk_url)
        lk_label.pack(padx=10, pady=10)
        lk_label.config(font=('Bold',18))
        show_back_button(new_window)

    def dance_pop():
        for widget in new_window.winfo_children():
                widget.destroy()
        txt_lab=tk.Label(new_window,text='Top Songs:',fg='white',bg='black')
        txt_lab.pack(pady=(15,15))
        txt_lab.config(font=('Bold',20))
        def open_link(url):
            webbrowser.open(url)
        def create_link(new_window,url):
            link_label = tk.Label(new_window, text="1.Taki Taki: DJ Snake,(ft. Selena Gomez, Ozuna, Cardi B)",bg='black',fg="white",cursor="hand2",height=3,width=70)
            link_label.bind("<Button-1>", lambda event: open_link(url))
            return link_label
        link_url = "https://www.youtube.com/watch?v=ixkoVwKQaJg"
        link_label = create_link(new_window, link_url)
        link_label.pack(padx=10, pady=10)
        link_label.config(font=('Bold',18))

        def open(url):
            webbrowser.open(url)
        def create(new_window,url):
            link_label2 = tk.Label(new_window, text="2.Calm Down: Rema(ft.Selena Gomez)",bg='black',fg="white",cursor="hand2",height=3,width=70)
            link_label2.bind("<Button-1>", lambda event: open(url))
            return link_label2
        lk_url = "https://www.youtube.com/watch?v=WcIcVapfqXw"
        link_label2 = create(new_window, lk_url)
        link_label2.pack(padx=10, pady=10)
        link_label2.config(font=('Bold',18))

        def link(url):
            webbrowser.open(url)
        def crt_link(new_window,url):
            lnk_label = tk.Label(new_window, text="3.Shape of You: Ed Sheeran",bg='black',fg="white",cursor="hand2",height=3,width=70)
            lnk_label.bind("<Button-1>", lambda event: link(url))
            return lnk_label
        lnk_url = "https://www.youtube.com/watch?v=JGwWNGJdvx8"
        lnk_label = crt_link(new_window, lnk_url)
        lnk_label.pack(padx=10, pady=10)
        lnk_label.config(font=('Bold',18))

        def opn_lnk(url):
            webbrowser.open(url)
        def create_lnk(new_window,url):
            link_labl = tk.Label(new_window, text="4.Go Down Deh: Spice, Sean Paul, Shaggy ",bg='black',fg="white",cursor="hand2",height=3,width=70)
            link_labl.bind("<Button-1>", lambda event: opn_lnk(url))
            return link_labl
        link_url = "https://www.youtube.com/watch?v=8v1WUh1kgBw"
        link_labl = create_lnk(new_window, link_url)
        link_labl.pack(padx=10, pady=10)
        link_labl.config(font=('Bold',18))

        def openlink(url):
            webbrowser.open(url)
        def create_lk(new_window,url):
            lk_label = tk.Label(new_window, text="5.Colors: Jason Derulo",bg='black',fg="white",cursor="hand2",height=3,width=30)
            lk_label.bind("<Button-1>", lambda event: openlink(url))
            return lk_label
        lik_url = "https://www.youtube.com/watch?v=p6E9R9qv1No"
        lk_label = create_lk(new_window, lik_url)
        lk_label.pack(padx=10, pady=10)
        lk_label.config(font=('Bold',18))
        show_back_button(new_window)

    def clas_bol():
        for widget in new_window.winfo_children():
                widget.destroy()
        txt_lab=tk.Label(new_window,text='Top Songs:',fg='white',bg='black')
        txt_lab.pack(pady=(15,15))
        txt_lab.config(font=('Bold',20))
        def open_link(url):
            webbrowser.open(url)
        def create_link(new_window,url):
            link_label = tk.Label(new_window, text="1.Kajra Re: Alisha Chinai, Shankar Mahadevan, Javed Ali ",bg='black',fg="white",cursor="hand2",height=3,width=70)
            link_label.bind("<Button-1>", lambda event: open_link(url))
            return link_label
        link_url = "https://www.youtube.com/watch?v=4dsFQFCvVGU"
        link_label = create_link(new_window, link_url)
        link_label.pack(padx=10, pady=10)
        link_label.config(font=('Bold',18))

        def open(url):
            webbrowser.open(url)
        def create(new_window,url):
            link_label2 = tk.Label(new_window, text="2.Mere Sapno Ki Rani: Kishore Kumar & Rajesh Khanna",bg='black',fg="white",cursor="hand2",height=3,width=70)
            link_label2.bind("<Button-1>", lambda event: open(url))
            return link_label2
        lik_url = "https://www.youtube.com/watch?v=po6kjouyxXg"
        link_label2 = create(new_window, lik_url)
        link_label2.pack(padx=10, pady=10)
        link_label2.config(font=('Bold',18))

        def link(url):
            webbrowser.open(url)
        def crt_link(new_window,url):
            lnk_label = tk.Label(new_window, text="3.O mere Dil ke Chain: Kishore Kumar",bg='black',fg="white",cursor="hand2",height=3,width=70)
            lnk_label.bind("<Button-1>", lambda event: link(url))
            return lnk_label
        lnk_url = "https://www.youtube.com/watch?v=FFbc-jXkADs"
        lnk_label = crt_link(new_window, lnk_url)
        lnk_label.pack(padx=10, pady=10)
        lnk_label.config(font=('Bold',18))

        def opn_lnk(url):
            webbrowser.open(url)
        def create_lnk(new_window,url):
            link_labl = tk.Label(new_window, text="4.Roop Tera Mastana :Kishore Kumar",bg='black',fg="white",cursor="hand2",height=2,width=70)
            link_labl.bind("<Button-1>", lambda event: opn_lnk(url))
            return link_labl
        lin_url = "https://www.youtube.com/watch?v=dyEdcOhxJNQ"
        link_labl = create_lnk(new_window, lin_url)
        link_labl.pack(padx=10, pady=10)
        link_labl.config(font=('Bold',18))

        def openlink(url):
            webbrowser.open(url)
        def create_lk(new_window,url):
            lk_label = tk.Label(new_window, text="5.Badan Pe Sitare Lapete Huye: Mohammad Rafi ",bg='black',fg="white",cursor="hand2",height=3,width=70)
            lk_label.bind("<Button-1>", lambda event: openlink(url))
            return lk_label
        lk_url = "https://www.youtube.com/watch?v=MkABeVCv4lw"
        lk_label = create_lk(new_window, lk_url)
        lk_label.pack(padx=10, pady=10)
        lk_label.config(font=('Bold',18))
        show_back_button(new_window)

    def clas_hol():
        for widget in new_window.winfo_children():
                widget.destroy()
        txt_lab=tk.Label(new_window,text='Top Songs:',fg='white',bg='black')
        txt_lab.pack(pady=(15,15))
        txt_lab.config(font=('Bold',20))
        def open_link(url):
            webbrowser.open(url)
        def create_link(new_window,url):
            link_label = tk.Label(new_window, text="1.Dangerous: Michael Jackson",bg='black',fg="white",cursor="hand2",height=3,width=30)
            link_label.bind("<Button-1>", lambda event: open_link(url))
            return link_label
        link_url = "https://www.youtube.com/watch?v=oughF5hIV3E"
        link_label = create_link(new_window, link_url)
        link_label.pack(padx=10, pady=10)
        link_label.config(font=('Bold',18))

        def open(url):
            webbrowser.open(url)
        def create(new_window,url):
            link_label2 = tk.Label(new_window, text="2.My Heart will go on: Celine Dion",bg='black',fg="white",cursor="hand2",height=3,width=70)
            link_label2.bind("<Button-1>", lambda event: open(url))
            return link_label2
        linkurl = "https://www.youtube.com/watch?v=F2RnxZnubCM"
        link_label2 = create(new_window, linkurl)
        link_label2.pack(padx=10, pady=10)
        link_label2.config(font=('Bold',18))

        def link(url):
            webbrowser.open(url)
        def crt_link(new_window,url):
            lnk_label = tk.Label(new_window, text="3.I Can't Help Falling In Love with you:Elvis Presley",bg='black',fg="white",cursor="hand2",height=3,width=70)
            lnk_label.bind("<Button-1>", lambda event: link(url))
            return lnk_label
        lnk_url = "https://www.youtube.com/watch?v=MqazV4hbu8E"
        lnk_label = crt_link(new_window, lnk_url)
        lnk_label.pack(padx=10, pady=10)
        lnk_label.config(font=('Bold',18))

        def opn_lnk(url):
            webbrowser.open(url)
        def create_lnk(new_window,url):
            link_labl = tk.Label(new_window, text="4.(Everything I Do) I Do It For You:Bryan Adams",bg='black',fg="white",cursor="hand2",height=2,width=70)
            link_labl.bind("<Button-1>", lambda event: opn_lnk(url))
            return link_labl
        linnk_url = "https://www.youtube.com/watch?v=Y0pdQU87dc8&list=PLYVjGTi85afou-GAHkhC6OgU7Merg0G0B&index=16"
        link_labl = create_lnk(new_window, linnk_url)
        link_labl.pack(padx=10, pady=10)
        link_labl.config(font=('Bold',18))

        def openlink(url):
            webbrowser.open(url)
        def create_lk(new_window,url):
            lk_label = tk.Label(new_window, text="5.Dessert Rose:Sting",bg='black',fg="white",cursor="hand2",height=3,width=30)
            lk_label.bind("<Button-1>", lambda event: openlink(url))
            return lk_label
        lk_url = "https://www.youtube.com/watch?v=C3lWwBslWqg"
        lk_label = create_lk(new_window, lk_url)
        lk_label.pack(padx=10, pady=10)
        lk_label.config(font=('Bold',18))
        show_back_button(new_window)

    def ghazals():
        for widget in new_window.winfo_children():
                widget.destroy()
        txt_lab=tk.Label(new_window,text='Top Songs:',fg='white',bg='black')
        txt_lab.pack(pady=(15,15))
        txt_lab.config(font=('Bold',20))
        def open_link(url):
            webbrowser.open(url)
        def create_link(new_window,url):
            link_label = tk.Label(new_window, text="1.Ye Jo Halka Halka:Nusrat Fateh Ali Khan",bg='black',fg="white",cursor="hand2",height=3,width=30)
            link_label.bind("<Button-1>", lambda event: open_link(url))
            return link_label
        link_url = "https://www.youtube.com/watch?v=3R1eUfVxOGI"
        link_label = create_link(new_window, link_url)
        link_label.pack(padx=10, pady=10)
        link_label.config(font=('Bold',18))

        def open(url):
            webbrowser.open(url)
        def create(new_window,url):
            link_label2 = tk.Label(new_window, text="2.Tum Ko Dekha To Yeh Khayal Aaya: Jagjit singh",bg='black',fg="white",cursor="hand2",height=3,width=70)
            link_label2.bind("<Button-1>", lambda event: open(url))
            return link_label2
        linkurl = "https://www.youtube.com/watch?v=Jc9PBgHwdII&list=TLPQMjAwNDIwMjSRnBJ-dqX5NQ&index"
        link_label2 = create(new_window, linkurl)
        link_label2.pack(padx=10, pady=10)
        link_label2.config(font=('Bold',18))

        def link(url):
            webbrowser.open(url)
        def crt_link(new_window,url):
            lnk_label = tk.Label(new_window, text="3.Ek Pyar Ka Nagma Hai:Jagjit singh",bg='black',fg="white",cursor="hand2",height=3,width=70)
            lnk_label.bind("<Button-1>", lambda event: link(url))
            return lnk_label
        lnk_url = "https://www.youtube.com/watch?v=FH1IkSLGZ48"
        lnk_label = crt_link(new_window, lnk_url)
        lnk_label.pack(padx=10, pady=10)
        lnk_label.config(font=('Bold',18))

        def opn_lnk(url):
            webbrowser.open(url)
        def create_lnk(new_window,url):
            link_labl = tk.Label(new_window, text="4.Woh Humsafar Tha:Abida Praveen",bg='black',fg="white",cursor="hand2",height=2,width=70)
            link_labl.bind("<Button-1>", lambda event: opn_lnk(url))
            return link_labl
        linnk_url = "https://www.youtube.com/watch?v=RfDEtYP8WhY"
        link_labl = create_lnk(new_window, linnk_url)
        link_labl.pack(padx=10, pady=10)
        link_labl.config(font=('Bold',18))

        def openlink(url):
            webbrowser.open(url)
        def create_lk(new_window,url):
            lk_label = tk.Label(new_window, text="5.Main Nashe Mein Hun: Jagjit Singh",bg='black',fg="white",cursor="hand2",height=3,width=30)
            lk_label.bind("<Button-1>", lambda event: openlink(url))
            return lk_label
        lk_url = "https://www.youtube.com/watch?v=w5d_RifBorE"
        lk_label = create_lk(new_window, lk_url)
        lk_label.pack(padx=10, pady=10)
        lk_label.config(font=('Bold',18)) 
        show_back_button(new_window)

    def sad_bol():
        for widget in new_window.winfo_children():
                widget.destroy()
        txt_lab=tk.Label(new_window,text='Top Songs:',fg='white',bg='black')
        txt_lab.pack(pady=(15,15))
        txt_lab.config(font=('Bold',20))
        def open_link(url):
            webbrowser.open(url)
        def create_link(new_window,url):
            link_label = tk.Label(new_window, text="1.Tujhe bhula diya",bg='black',fg="white",cursor="hand2",height=3,width=30)
            link_label.bind("<Button-1>", lambda event: open_link(url))
            return link_label
        link_url = "https://www.youtube.com/watch?v=-Hb2DeHvvEghttps://www.youtube.com/watch?v=-Hb2DeHvvEg"
        link_label = create_link(new_window, link_url)
        link_label.pack(padx=10, pady=10)
        link_label.config(font=('Bold',18))

        def open(url):
            webbrowser.open(url)
        def create(new_window,url):
            link_label2 = tk.Label(new_window, text="2.Agar tum saath ho",bg='black',fg="white",cursor="hand2",height=3,width=70)
            link_label2.bind("<Button-1>", lambda event: open(url))
            return link_label2
        linkurl = "https://www.youtube.com/watch?v=sK7riqg2mr4"
        link_label2 = create(new_window, linkurl)
        link_label2.pack(padx=10, pady=10)
        link_label2.config(font=('Bold',18))

        def link(url):
            webbrowser.open(url)
        def crt_link(new_window,url):
            lnk_label = tk.Label(new_window, text="3.Abhi Mujh Mein Kahin",bg='black',fg="white",cursor="hand2",height=3,width=70)
            lnk_label.bind("<Button-1>", lambda event: link(url))
            return lnk_label
        lnk_url = "https://www.youtube.com/watch?v=dTu5dTEzVM4"
        lnk_label = crt_link(new_window, lnk_url)
        lnk_label.pack(padx=10, pady=10)
        lnk_label.config(font=('Bold',18))

        def opn_lnk(url):
            webbrowser.open(url)
        def create_lnk(new_window,url):
            link_labl = tk.Label(new_window, text="4.Ghalat Fehmi",bg='black',fg="white",cursor="hand2",height=2,width=70)
            link_labl.bind("<Button-1>", lambda event: opn_lnk(url))
            return link_labl
        linnk_url = "https://www.youtube.com/watch?v=0Np37l4ykRE"
        link_labl = create_lnk(new_window, linnk_url)
        link_labl.pack(padx=10, pady=10)
        link_labl.config(font=('Bold',18))

        def openlink(url):
            webbrowser.open(url)
        def create_lk(new_window,url):
            lk_label = tk.Label(new_window, text="5.Kun Faya Kun",bg='black',fg="white",cursor="hand2",height=3,width=30)
            lk_label.bind("<Button-1>", lambda event: openlink(url))
            return lk_label
        lk_url = "https://www.youtube.com/watch?v=T94PHkuydcw"
        lk_label = create_lk(new_window, lk_url)
        lk_label.pack(padx=10, pady=10)
        lk_label.config(font=('Bold',18)) 
        show_back_button(new_window)

    def rom_bol():
        for widget in new_window.winfo_children():
                widget.destroy()
        txt_lab=tk.Label(new_window,text='Top Songs:',fg='white',bg='black')
        txt_lab.pack(pady=(15,15))
        txt_lab.config(font=('Bold',20))
        def open_link(url):
            webbrowser.open(url)
        def create_link(new_window,url):
            link_label = tk.Label(new_window, text="1.  Peheli Dafa: Atif Aslam",bg='black',fg="white",cursor="hand2",height=3,width=30)
            link_label.bind("<Button-1>", lambda event: open_link(url))
            return link_label
        link_url = "https://www.youtube.com/watch?v=SxTYjptEzZs"
        link_label = create_link(new_window, link_url)
        link_label.pack(padx=10, pady=10)
        link_label.config(font=('Bold',18))

        def open(url):
            webbrowser.open(url)
        def create(new_window,url):
            link_label2 = tk.Label(new_window, text="2.Tere Liye:Atif Aslam",bg='black',fg="white",cursor="hand2",height=3,width=70)
            link_label2.bind("<Button-1>", lambda event: open(url))
            return link_label2
        linkurl = "https://www.youtube.com/watch?v=X7L4wvljHhM"
        link_label2 = create(new_window, linkurl)
        link_label2.pack(padx=10, pady=10)
        link_label2.config(font=('Bold',18))

        def link(url):
            webbrowser.open(url)
        def crt_link(new_window,url):
            lnk_label = tk.Label(new_window, text="3.Pehli Nazar Mein: Atif Aslam",bg='black',fg="white",cursor="hand2",height=3,width=70)
            lnk_label.bind("<Button-1>", lambda event: link(url))
            return lnk_label
        lnk_url = "https://www.youtube.com/watch?v=BadBAMnPX0I"
        lnk_label = crt_link(new_window, lnk_url)
        lnk_label.pack(padx=10, pady=10)
        lnk_label.config(font=('Bold',18))

        def opn_lnk(url):
            webbrowser.open(url)
        def create_lnk(new_window,url):
            link_labl = tk.Label(new_window, text="4.GF BF:  T-Series",bg='black',fg="white",cursor="hand2",height=2,width=70)
            link_labl.bind("<Button-1>", lambda event: opn_lnk(url))
            return link_labl
        linnk_url = "https://www.youtube.com/watch?v=6CVVd9RB7CI"
        link_labl = create_lnk(new_window, linnk_url)
        link_labl.pack(padx=10, pady=10)
        link_labl.config(font=('Bold',18))

        def openlink(url):
            webbrowser.open(url)
        def create_lk(new_window,url):
            lk_label = tk.Label(new_window, text="5.Tere Sang Yaara: Arko ft. Atif Aslam",bg='black',fg="white",cursor="hand2",height=3,width=30)
            lk_label.bind("<Button-1>", lambda event: openlink(url))
            return lk_label
        lk_url = "https://www.youtube.com/watch?v=gIOea2pgfIo"
        lk_label = create_lk(new_window, lk_url)
        lk_label.pack(padx=10, pady=10)
        lk_label.config(font=('Bold',18)) 

        def openlink(url):
            webbrowser.open(url)
        def create_lk(new_window,url):
            lk_label = tk.Label(new_window, text="6.Pehela Nasha:Udit Narayan,Sadhana",bg='black',fg="white",cursor="hand2",height=3,width=30)
            lk_label.bind("<Button-1>", lambda event: openlink(url))
            return lk_label
        lk_url = "https://www.youtube.com/watch?v=SBfPs-PMGTA"
        lk_label = create_lk(new_window, lk_url)
        lk_label.pack(padx=10, pady=10)
        lk_label.config(font=('Bold',18)) 
        show_back_button(new_window)

    def sad_pnj():
        for widget in new_window.winfo_children():
                widget.destroy()
        txt_lab=tk.Label(new_window,text='Top Songs:',fg='white',bg='black')
        txt_lab.pack(pady=(15,15))
        txt_lab.config(font=('Bold',20))
        def open_link(url):
            webbrowser.open(url)
        def create_link(new_window,url):
            link_label = tk.Label(new_window, text="1.Yaar Mod Do",bg='black',fg="white",cursor="hand2",height=3,width=30)
            link_label.bind("<Button-1>", lambda event: open_link(url))
            return link_label
        link_url = "https://www.youtube.com/watch?v=dGwau9Vcc0o"
        link_label = create_link(new_window, link_url)
        link_label.pack(padx=10, pady=10)
        link_label.config(font=('Bold',18))

        def open(url):
            webbrowser.open(url)
        def create(new_window,url):
            link_label2 = tk.Label(new_window, text="2.Qismat:Ammy Virk, Sargun Mehta, Jaani ",bg='black',fg="white",cursor="hand2",height=3,width=70)
            link_label2.bind("<Button-1>", lambda event: open(url))
            return link_label2
        linkurl = "https://www.youtube.com/watch?v=9xVp8m0fJSg"
        link_label2 = create(new_window, linkurl)
        link_label2.pack(padx=10, pady=10)
        link_label2.config(font=('Bold',18))

        def link(url):
            webbrowser.open(url)
        def crt_link(new_window,url):
            lnk_label = tk.Label(new_window, text="3.Mann Bharaya",bg='black',fg="white",cursor="hand2",height=3,width=70)
            lnk_label.bind("<Button-1>", lambda event: link(url))
            return lnk_label
        lnk_url = "https://www.youtube.com/watch?v=YrUqw7uspKg"
        lnk_label = crt_link(new_window, lnk_url)
        lnk_label.pack(padx=10, pady=10)
        lnk_label.config(font=('Bold',18))

        def opn_lnk(url):
            webbrowser.open(url)
        def create_lnk(new_window,url):
            link_labl = tk.Label(new_window, text="4.Titliaan: Harry Sandhu, Sargun Mehta",bg='black',fg="white",cursor="hand2",height=2,width=70)
            link_labl.bind("<Button-1>", lambda event: opn_lnk(url))
            return link_labl
        linnk_url = "https://www.youtube.com/watch?v=YPohR_9v6HA"
        link_labl = create_lnk(new_window, linnk_url)
        link_labl.pack(padx=10, pady=10)
        link_labl.config(font=('Bold',18))

        def openlink(url):
            webbrowser.open(url)
        def create_lk(new_window,url):
            lk_label = tk.Label(new_window, text="5.Salooq:MOH, B Praak, Jaani",bg='black',fg="white",cursor="hand2",height=3,width=30)
            lk_label.bind("<Button-1>", lambda event: openlink(url))
            return lk_label
        lk_url = "https://www.youtube.com/watch?v=eF0Qos8NnSA"
        lk_label = create_lk(new_window, lk_url)
        lk_label.pack(padx=10, pady=10)
        lk_label.config(font=('Bold',18)) 
        show_back_button(new_window)

    def rom_pnj():
        for widget in new_window.winfo_children():
                widget.destroy()
        txt_lab=tk.Label(new_window,text='Top Songs:',fg='white',bg='black')
        txt_lab.pack(pady=(15,15))
        txt_lab.config(font=('Bold',20))
        def open_link(url):
            webbrowser.open(url)
        def create_link(new_window,url):
            link_label = tk.Label(new_window, text="1.Waalian:Harnoor",bg='black',fg="white",cursor="hand2",height=3,width=30)
            link_label.bind("<Button-1>", lambda event: open_link(url))
            return link_label
        link_url = "https://www.youtube.com/watch?v=rCoPr8UwRMc"
        link_label = create_link(new_window, link_url)
        link_label.pack(padx=10, pady=10)
        link_label.config(font=('Bold',18))

        def open(url):
            webbrowser.open(url)
        def create(new_window,url):
            link_label2 = tk.Label(new_window, text="2.Moonlight:Harnoor",bg='black',fg="white",cursor="hand2",height=3,width=70)
            link_label2.bind("<Button-1>", lambda event: open(url))
            return link_label2
        linkurl = "https://www.youtube.com/watch?v=TUawyJn7dws"
        link_label2 = create(new_window, linkurl)
        link_label2.pack(padx=10, pady=10)
        link_label2.config(font=('Bold',18))

        def link(url):
            webbrowser.open(url)
        def crt_link(new_window,url):
            lnk_label = tk.Label(new_window, text="3.SAKHIYAAN:Maninder Buttar",bg='black',fg="white",cursor="hand2",height=3,width=70)
            lnk_label.bind("<Button-1>", lambda event: link(url))
            return lnk_label
        lnk_url = "https://www.youtube.com/watch?v=S-ezhTXPVGU"
        lnk_label = crt_link(new_window, lnk_url)
        lnk_label.pack(padx=10, pady=10)
        lnk_label.config(font=('Bold',18))

        def opn_lnk(url):
            webbrowser.open(url)
        def create_lnk(new_window,url):
            link_labl = tk.Label(new_window, text="4.Laal Bindi-Akull",bg='black',fg="white",cursor="hand2",height=2,width=70)
            link_labl.bind("<Button-1>", lambda event: opn_lnk(url))
            return link_labl
        linnk_url = "https://www.youtube.com/watch?v=PAW_Gd3QVww"
        link_labl = create_lnk(new_window, linnk_url)
        link_labl.pack(padx=10, pady=10)
        link_labl.config(font=('Bold',18))

        def openlink(url):
            webbrowser.open(url)
        def create_lk(new_window,url):
            lk_label = tk.Label(new_window, text="5.Mere Wala Sardar:Jugraj Sandhu ",bg='black',fg="white",cursor="hand2",height=3,width=30)
            lk_label.bind("<Button-1>", lambda event: openlink(url))
            return lk_label
        lk_url = "https://www.youtube.com/watch?v=3dW6hTdyYSA"
        lk_label = create_lk(new_window, lk_url)
        lk_label.pack(padx=10, pady=10)
        lk_label.config(font=('Bold',18))     

    def on_selection(event):
        selected_item = combobox.get()
        for widget in new_window.winfo_children():
            if widget != combobox:
                widget.destroy()

        if selected_item == 'Pop':
            sad=tk.Button(new_window, text='Sad',bg='white',fg='black',height=1,width=10, command= sad_pop)
            sad.pack(pady=(10,20))
            sad.config(font=('helvetica',15))

            rom=tk.Button(new_window, text='Romantic',bg='white',fg='black',height=1,width=10,command= rom_pop)
            rom.pack(pady=(10,20))
            rom.config(font=('helvetica',15))

            fit=tk.Button(new_window, text='Fitness',bg='white',fg='black',height=1,width=10,command=fit_pop)
            fit.pack(pady=(10,20))
            fit.config(font=('helvetica',15))

            dnc=tk.Button(new_window, text='Dance',bg='white',fg='black',height=1,width=10,command=dance_pop)
            dnc.pack(pady=(10,20))
            dnc.config(font=('helvetica',15))
        
        elif selected_item == 'Classic':
            bol=tk.Button(new_window, text='Old Bollywood',bg='white',fg='black',height=1,width=15,command=clas_bol)
            bol.pack(pady=(10,20))
            bol.config(font=('helvetica',15))

            hol=tk.Button(new_window, text='90s Hollywood',bg='white',fg='black',height=1,width=18,command=clas_hol)
            hol.pack(pady=(10,20))
            hol.config(font=('helvetica',15))

            gaz=tk.Button(new_window, text='Ghazals',bg='white',fg='black',height=1,width=10,command=ghazals)
            gaz.pack(pady=(10,20))
            gaz.config(font=('helvetica',15))

        elif selected_item == 'Bollywood':
            sad2=tk.Button(new_window, text='Sad',bg='white',fg='black',height=1,width=10,command=sad_bol)
            sad2.pack(pady=(10,20))
            sad2.config(font=('helvetica',15))

            rom2=tk.Button(new_window, text='Romantic',bg='white',fg='black',height=1,width=10,command=rom_bol)
            rom2.pack(pady=(10,20))
            rom2.config(font=('helvetica',15))

        elif selected_item == 'Punjabi':
            sad3=tk.Button(new_window, text='Sad',bg='white',fg='black',height=1,width=10,command=sad_pnj)
            sad3.pack(pady=(10,20))
            sad3.config(font=('helvetica',15))

            rom3=tk.Button(new_window, text='Romantic',bg='white',fg='black',height=1,width=10,command=rom_pnj)
            rom3.pack(pady=(10,20))
            rom3.config(font=('helvetica',15))

    options = ["Pop", "Classic", "Bollywood","Punjabi"]
    combobox = ttk.Combobox(new_window, values=options, height='8',width='40')
    combobox.set("Choose:")
    combobox.pack(pady=(40,80))
    combobox.bind("<<ComboboxSelected>>",on_selection)

    entry_label = tk.Label(new_window, text='Enter your favorite song:', fg='white', bg='light pink')
    entry_label.pack(pady=(15, 5))
    entry_label.config(font=('verdana', 14))

    API_KEY = 'AIzaSyDcasE3yC-wLFSPEZE0y6nzoQWa7j2G6cc' # api key 

    def search_youtube(query):
        youtube = build('youtube', 'v3', developerKey=API_KEY)
        request = youtube.search().list(
            q=query,
            part='snippet',
            maxResults=5  
        )
        response = request.execute()
        print(response['items'])
        return response['items']

    def display_songs(song_name):
        results = search_youtube(song_name)
        new_window = Toplevel(root)
        for result in results:
            title = result['snippet']['title']
            video_id = result['id']['videoId']
            link = f"https://www.youtube.com/watch?v={video_id}"  

            # Display title and link
            title_label = tk.Label(new_window, text=title)
            title_label.pack()
            link_label = tk.Label(new_window, text=link, fg="blue", cursor="hand2")
            link_label.pack()
            link_label.bind("<Button-1>", lambda e: webbrowser.open_new(link))  

    def on_enter(event):
        song_name = entry_input.get()
        display_songs(song_name)
            
    entry_input = tk.Entry(new_window, width=35)
    entry_input.pack(ipady=4, pady=(1, 15))
    entry_input.bind("<Return>", on_enter)


root = tk.Tk()
root.title("Welcome")
root.geometry("500x700")
root.configure(background='light pink')

img= ImageTk.PhotoImage(Image.open("D:\Desktop\Project Python\music\musicano1.png"))
img_label= tk.Label(root,image=img)
img_label.pack(pady=(10,10))

text_lab = tk.Label(root, text='Musicano Welcomes You!', fg='white', bg='light pink')
text_lab.pack(pady=(15,15))
text_lab.config(font=('Bold',20))

btn_log = tk.Button(root, text='Login', bg='white', fg='blue', height=1, width=10, command=login)
btn_log.pack(pady=(10,20))
btn_log.config(font=('helvetica',15))

btn_sign = tk.Button(root, text='Sign Up', bg='white', fg='blue', height=1, width=10, command=signin)
btn_sign.pack(pady=(10,20))
btn_sign.config(font=('helvetica',15))

root.mainloop()