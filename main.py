from googletrans import Translator
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import httpcore

#Translation of typed text
def translate():
    try:
        translator=Translator()
        if src_entry.get(1.0,'end-1c')=="":
            messagebox.showerror("Translate","Enter the text to translate")
        else:
            result=translator.translate(src_entry.get(1.0,'end-1c'),dest=dest_lang.get())
            dest_entry.insert('end',result.text)
    except httpcore._exceptions.ConnectError:
        messagebox.showerror("Translate","Internal server error")

#Clear text box
def clear():
    src_entry.delete(1.0,'end')
    dest_entry.delete(1.0,'end')

# GUI of application
if __name__ == "__main__":

    window=tk.Tk()
    window.geometry("700x400")
    window.title("Translate")
    window.configure(bg="white")
    window.iconbitmap("icon.ico")


    img=Image.open("Google-Translate.jpg")
    img=img.resize((400,70))
    img=ImageTk.PhotoImage(img)
    img_lab=tk.Label(window,image=img)
    img_lab.place(x=150,y=0)

    text=tk.StringVar()
    src_lang=ttk.Combobox(window,textvariable=text,width=31,font=("verdana Bold",10))
    src_lang['values']=("Auto Detect",)
    src_lang.current(0)
    src_lang.place(x=30,y=100)

    src_entry=tk.Text(window,font=("verdana Bold",10),width=33,height=12,relief="ridge",borderwidth=5)
    src_entry.place(x=28,y=130)


    dest_lang=ttk.Combobox(window,width=30,font=("verdana Bold",10))
    dest_lang['values']=(
                        "Afrikaans",
                        "Albanian",
                        "Amharic",
                        "Arabic",
                        "Armenian",
                        "Azerbaijani",
                        "Basque",
                        "Belarusian",
                        "Bengali",
                        "Bosnian",
                        "Bulgarian",
                        "Catalan",
                        "Cebuano",
                        "Chinese (Simplified)",
                        "Chinese (Traditional)",
                        "Corsican",
                        "Croatian",
                        "Czech",
                        "Danish",
                        "Dutch",
                        "English"	,
                        "Esperanto",
                        "Estonian",
                        "Finnish",
                        "French",
                        "Frisian",
                        "Galician",
                        "Georgian",
                        "German",
                        "Greek",
                        "Gujarati",
                        "Haitian Creole",
                        "Hausa",
                        "Hawaiian",
                        "Hebrew",
                        "Hindi",
                        "Hmong",
                        "Hungarian",
                        "Icelandic",
                        "Igbo",
                        "Indonesian",
                        "Irish",
                        "Italian",
                        "Japanese",
                        "Javanese",
                        "Kannada",
                        "Kazakh",
                        "Khmer",
                        "Kinyarwanda",
                        "Korean",
                        "Kurdish",
                        "Kyrgyz",
                        "Lao",
                        "Latin",
                        "Latvian",
                        "Lithuanian",
                        "Luxembourgish",
                        "Macedonian",
                        "Malagasy",
                        "Malay",
                        "Malayalam",
                        "Maltese",
                        "Maori",
                        "Marathi",
                        "Mongolian",
                        "Myanmar (Burmese)",
                        "Nepali",
                        "Norwegian",
                        "Odia (Oriya)",
                        "Pashto",
                        "Persian"	,
                        "Polish",
                        "Portuguese (Portugal, Brazil)",
                        "Punjabi",
                        "Romanian",
                        "Russian"	,
                        "Samoan",
                        "Scots Gaelic",
                        "Serbian"	,
                        "Sesotho"	,
                        "Shona"	,
                        "Sindhi"	,
                        "Sinhala (Sinhalese)"	,
                        "Slovak",
                        "Slovenian"	,
                        "Somali"	,
                        "Spanish"	,
                        "Sundanese"	,
                        "Swahili"	,
                        "Swedish"	,
                        "Tagalog (Filipino)	",
                        "Tajik"	,
                        "Tamil"	,
                        "Tatar"	,
                        "Telugu"	,
                        "Thai"	,
                        "Turkish"	,
                        "Turkmen"	,
                        "Ukrainian"	,
                        "Urdu"	,
                        "Uyghur"	,
                        "Uzbek"	,
                        "Vietnamese"	,
                        "Welsh"	,
                        "Xhosa"	,
                        "Yiddish"	,
                        "Yoruba"	,
                        "Zulu",
                        )



    dest_lang.current(0)
    dest_lang.place(x=352,y=100)


    l=tk.StringVar()
    dest_entry=tk.Text(window,font=("verdana Bold",10),width=31,height=12,relief="ridge",borderwidth=5)
    dest_entry.place(x=350,y=130)

    translate_but=tk.Button(window,text="Translate",width=15,font=("verdana Bold",12),relief="ridge",command=lambda:translate())
    translate_but.place(x=160,y=350)

    clear_but=tk.Button(window,text="Clear",width=15,font=("verdana Bold",12),relief="ridge",command=lambda:clear())
    clear_but.place(x=350,y=350)

    window.mainloop()


