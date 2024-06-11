import os
import json
import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import filedialog, messagebox

def process_json(input_file, output_dir):
    # Define the new mapping of speaker to color
    color_mapping = {
        'SPEAKER_00': '#ff6b06',
        'SPEAKER_01': '#ff0000',
        'SPEAKER_02': '#ffff00',
        'SPEAKER_03': '#0873d5',
        'SPEAKER_04': '#e34282',
        'SPEAKER_05': '#632466'
    }

    # Read the JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Create the root element
    root = ET.Element('captions', {
        'title': '',
        'case-number': '',
        'transcribed-by': '',
        'translator': '',
        'description': '',
        'client': ''
    })

    # Extract segments and create caption elements
    for i, segment in enumerate(data['segments'], start=1):
        begin = str(segment['start'])
        end = str(segment['end'])
        text = segment['text']
        speaker = segment.get('speaker', 'unknown')
        
        # Determine the color based on the speaker
        color = color_mapping.get(speaker, '#FFFFFF')
        
        # Create the caption element
        caption = ET.SubElement(root, 'caption', {
            'begin': begin,
            'end': end,
            'id': str(i + 1),
            'text': text,
            'actor': speaker,
            'color': color
        })

    # Create a new XML tree with the root element
    tree = ET.ElementTree(root)

    # Define the output file path
    output_file = os.path.join(output_dir, 'output.captions')
    
    # Write the tree to a file with .captions extension
    tree.write(output_file, encoding='UTF-8', xml_declaration=True)

    # Pretty print the XML (optional)
    import xml.dom.minidom

    xmlstr = ET.tostring(root, encoding='utf-8', method='xml')
    parsed = xml.dom.minidom.parseString(xmlstr)
    pretty_xml_as_string = parsed.toprettyxml()

    # Write the pretty-printed XML to the .captions file
    pretty_output_file = os.path.join(output_dir, 'output_pretty.captions')
    with open(pretty_output_file, 'w') as f:
        f.write(pretty_xml_as_string)

    print(f'Caption files have been created successfully: {output_file}, {pretty_output_file}')
    messagebox.showinfo("Success", f"Caption files have been created successfully:\n{output_file}\n{pretty_output_file}")

def select_input_file():
    input_file = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if input_file:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, input_file)
        output_dir = os.path.dirname(input_file)
        output_entry.delete(0, tk.END)
        output_entry.insert(0, output_dir)

def select_output_dir():
    output_dir = filedialog.askdirectory()
    if output_dir:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, output_dir)

def start_processing():
    input_file = input_entry.get()
    output_dir = output_entry.get()
    if not input_file or not os.path.exists(input_file):
        messagebox.showerror("Error", "Please select a valid input JSON file.")
        return
    if not output_dir or not os.path.isdir(output_dir):
        messagebox.showerror("Error", "Please select a valid output directory.")
        return
    process_json(input_file, output_dir)

# Create the main Tkinter window
root = tk.Tk()
root.title("JSON to Captions Converter")

# Create and place widgets
tk.Label(root, text="Input JSON file:").grid(row=0, column=0, padx=10, pady=10)
input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Select File", command=select_input_file).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Output Directory:").grid(row=1, column=0, padx=10, pady=10)
output_entry = tk.Entry(root, width=50)
output_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Select Directory", command=select_output_dir).grid(row=1, column=2, padx=10, pady=10)

tk.Button(root, text="Start Processing", command=start_processing).grid(row=2, columnspan=3, padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
