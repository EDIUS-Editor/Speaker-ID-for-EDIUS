import tkinter as tk
from tkinter import filedialog, messagebox
import os

def select_audio_file():
    file_path = filedialog.askopenfilename(
        title="Select File to Transcribe",
        filetypes=(("Audio Files", "*.mp3;*.mp4;*.m4a;*.mpeg;*.mpga;*.wav;*.webm"),)
    )
    if file_path:
        audio_file_var.set(file_path)
        # Set default output directory to the same as the audio file directory
        output_dir_var.set(os.path.dirname(file_path))

def select_token_file():
    file_path = filedialog.askopenfilename(
        title="Select Hugging Face Token File",
        filetypes=(("Text Files", "*.txt"),)
    )
    if file_path:
        token_file_var.set(file_path)

def select_output_dir():
    directory = filedialog.askdirectory(title="Select Output Directory")
    if directory:
        output_dir_var.set(directory)

def run_whisperx():
    if not audio_file_var.get() or not token_file_var.get() or not output_dir_var.get():
        messagebox.showerror("Error", "Ensure you have selected an audio file, a token file, and an output directory.")
        return

    with open(token_file_var.get(), 'r') as f:
        hf_token = f.read().strip()

    command = f"whisperx \"{audio_file_var.get()}\" --model {model_var.get()}"
    command += f" --output_dir \"{output_dir_var.get()}\""
    command += f" --hf_token {hf_token}"
    command += " --diarize"
    command += f" --language {language_var.get()}"
    command += f" --compute_type {compute_type_var.get()}"

    command += f" --batch_size {batch_size_var.get()}"

    os.system(f"cmd.exe /c {command}")
    os.startfile(output_dir_var.get())
    messagebox.showinfo("Info", "FINISHED")
    root.quit()

# Initialize GUI
root = tk.Tk()
root.title("WhisperX GUI")

# Variables
audio_file_var = tk.StringVar()
token_file_var = tk.StringVar()
output_dir_var = tk.StringVar()
model_var = tk.StringVar(value="small")
compute_type_var = tk.StringVar(value="int8")
batch_size_var = tk.StringVar(value="4")
language_var = tk.StringVar(value="en")

# GUI Layout
tk.Label(root, text="Select Audio File").grid(row=0, column=0, padx=10, pady=5, sticky="w")
tk.Entry(root, textvariable=audio_file_var, width=50).grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=select_audio_file).grid(row=0, column=2, padx=10, pady=5)

tk.Label(root, text="Select Token File").grid(row=1, column=0, padx=10, pady=5, sticky="w")
tk.Entry(root, textvariable=token_file_var, width=50).grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=select_token_file).grid(row=1, column=2, padx=10, pady=5)

tk.Label(root, text="Model Type").grid(row=2, column=0, padx=10, pady=5, sticky="w")
tk.OptionMenu(root, model_var, "large", "medium", "small", "base", "tiny", "tiny.en").grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Compute type for computation").grid(row=3, column=0, padx=10, pady=5, sticky="w")
tk.OptionMenu(root, compute_type_var, "float16", "float32", "int8").grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Batch Size").grid(row=4, column=0, padx=10, pady=5, sticky="w")
tk.OptionMenu(root, batch_size_var, "4", "8", "16").grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Language").grid(row=5, column=0, padx=10, pady=5, sticky="w")
tk.OptionMenu(root, language_var, 
              "af","am","ar","as","az","ba","be","bg","bn","bo","br","bs","ca","cs","cy","da","de","el","en","es","et","eu",
              "fa","fi","fo","fr","gl","gu","ha","haw","he","hi","hr","ht","hu","hy","id","is","it","ja","jw","ka","kk","km",
              "kn","ko","la","lb","ln","lo","lt","lv","mg","mi","mk","ml","mn","mr","ms","mt","my","ne","nl","nn","no","oc",
              "pa","pl","ps","pt","ro","ru","sa","sd","si","sk","sl","sn","so","sq","sr","su","sv","sw","ta","te","tg","th",
              "tk","tl","tr","tt","uk","ur","uz","vi","yi","yo","yue","zh","Afrikaans","Albanian","Amharic","Arabic","Armenian",
              "Assamese","Azerbaijani","Bashkir","Basque","Belarusian","Bengali","Bosnian","Breton","Bulgarian","Burmese",
              "Cantonese","Castilian","Catalan","Chinese","Croatian","Czech","Danish","Dutch","English","Estonian","Faroese",
              "Finnish","Flemish","French","Galician","Georgian","German","Greek","Gujarati","Haitian","Haitian Creole",
              "Hausa","Hawaiian","Hebrew","Hindi","Hungarian","Icelandic","Indonesian","Italian","Japanese","Javanese",
              "Kannada","Kazakh","Khmer","Korean","Lao","Latin","Latvian","Letzeburgesch","Lingala","Lithuanian",
              "Luxembourgish","Macedonian","Malagasy","Malay","Malayalam","Maltese","Maori","Marathi","Moldavian",
              "Moldovan","Mongolian","Myanmar","Nepali","Norwegian","Nynorsk","Occitan","Panjabi","Pashto","Persian",
              "Polish","Portuguese","Punjabi","Pushto","Romanian","Russian","Sanskrit","Serbian","Shona","Sindhi",
              "Sinhala","Sinhalese","Slovak","Slovenian","Somali","Spanish","Sundanese","Swahili","Swedish","Tagalog",
              "Tajik","Tamil","Tatar","Telugu","Thai","Tibetan","Turkish","Turkmen","Ukrainian","Urdu","Uzbek","Valencian",
              "Vietnamese","Welsh","Yiddish","Yoruba").grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Select Output Directory").grid(row=6, column=0, padx=10, pady=5, sticky="w")
tk.Entry(root, textvariable=output_dir_var, width=50).grid(row=6, column=1, padx=10, pady=5)
tk.Button(root, text="Browse", command=select_output_dir).grid(row=6, column=2, padx=10, pady=5)

tk.Button(root, text="Run", command=run_whisperx).grid(row=7, column=0, padx=10, pady=20)
tk.Button(root, text="Cancel", command=root.quit).grid(row=7, column=1, padx=10, pady=20)

root.mainloop()
