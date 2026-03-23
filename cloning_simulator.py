import requests
from requests.exceptions import RequestException
import tkinter as tk
from tkinter import messagebox
import Bio.Restriction as br

class Cloning():
    def __init__(self):
        
        self.screen = tk.Tk()
        self.screen.title('In Silico Restriction Cloning Simulator')
        self.screen.minsize(width = 600, height = 600)
        self.screen.config(bg = '#F5F0E8', padx = 20)
        self.screen.grid_columnconfigure(0, weight=1)
        self.screen.grid_columnconfigure(1, weight=1)
        
    def window(self):
        window_title = tk.Label(
            self.screen,
            text = 'In Silico Restriction Cloning Simulator',
            fg='#1B3A6B',
            bg = '#F5F0E8',
            font = ('Georgia', '22', 'bold')
            )
        window_title.grid(row=0, column=0, columnspan=2, pady=30)
        
    def DNA_label(self):
         DNA_label = tk.Label(
             self.screen,
             text = 'Write DNA Sequence\n (FASTA)',
             fg='#1a1a2a',
             bg = '#F5F0E8',
             font = ('Georgia', '10', 'bold'))
         DNA_label.grid(row  = 2, column = 0)
        
    def DNA_text_label(self):
        self.text_widget = tk.Text(
            self.screen,
            width = 40,
            height = 4,
            bg = '#FFFFFF',
            highlightthickness = 2,
            highlightbackground = '#1B3A6B',
            font = ('Georgia', '10')
            )
        self.text_widget.grid(row  = 2, column = 1)
      
    def plasmid_label(self):
         plasmid_label = tk.Label(
             self.screen,
             text = 'Write Plasmid Sequence\n (FASTA)',
             fg='#1a1a2a',
             bg = '#F5F0E8',
             font = ('Georgia', '10', 'bold'))
         plasmid_label.grid(row  = 3, column = 0, pady = 20)
         
    def plasmid_text_label(self):
        self.plasmid_text_widget = tk.Text(
            self.screen,
            width = 40,
            height = 4,
            bg = '#FFFFFF',
            highlightthickness = 2,
            highlightbackground = '#1B3A6B',
            font = ('Georgia', '10')
            )
        self.plasmid_text_widget.grid(row  = 3, column = 1, pady = 20)
        
    def restriction(self):
        self.enzymes_list = []
        for i in br.AllEnzymes:
            name = str(i)
            self.enzymes_list.append(name)
        self.enzymes_list.sort()
        
    def enzyme_label(self):
        label = tk.Label(
            self.screen,
            text = 'Write Restriction Enzyme',
            fg='#1a1a2a',
            bg = '#F5F0E8',
            font = ('Georgia', '10', 'bold'))
        label.grid(row  = 4, column = 0, pady = 20, sticky='e')
            
    def text_entry(self):
        self.string = tk.StringVar()
        self.string.trace_add('write', self.filter_enzymes)
        self.enzyme_input = tk.Entry(
            self.screen,
            width = 20,
            bg = '#FFFFFF',
            highlightthickness = 2,
            highlightbackground = '#1B3A6B',
            textvariable = self.string)
        self.enzyme_input.grid(row  = 4, column = 1, pady = 20)
        
    def listbox(self):
        self.listbox = tk.Listbox(
            self.screen,
            fg = '#1B3A6B',
            bg = '#FFFFFF',
            height = 6,
            width = 12,
            font = ('Georgia', '10', 'bold'))
        self.listbox.grid(row  = 5, column = 1)
        self.filter_enzymes()
        
    def filter_enzymes(self, *args):
        extracted_text = self.string.get().lower()
        self.listbox.delete(0, tk.END)
        for i in self.enzymes_list:
            if i.lower().startswith(extracted_text):
                self.listbox.insert(tk.END, i)
    
    def clean_sequence(self, seq):
        lines = seq.strip().splitlines()
        lines = [x for x in lines if not x.startswith('>')]
        return ''.join(lines).replace(' ', '').upper()
    
    def cloning_work(self):

        raw_DNA = self.text_widget.get('1.0', tk.END)
        raw_plasmid = self.plasmid_text_widget.get('1.0', tk.END)
        self.restriction_enzyme = self.enzyme_input.get()
        
        self.DNA = self.clean_sequence(raw_DNA)
        self.plasmid = self.clean_sequence(raw_plasmid)
        
        valid_sequence = {'A', 'T', 'G', 'C'}
        
        if self.DNA == '':
            messagebox.showerror(title= 'Error', message= 'Enter DNA FASTA sequence.')
            return
        if self.plasmid == '':
            messagebox.showerror(title= 'Error', message= 'Enter Plasmid sequence.')
            return
        if self.restriction_enzyme.strip() == '':
            messagebox.showerror(title= 'Error', message= 'Select a restriction enzyme.')
            return 
        
        if not set(self.DNA).issubset(valid_sequence):
            messagebox.showerror(title= 'Error', message= 'DNA sequence is incorrect!')
            return
        if not set(self.plasmid).issubset(valid_sequence):
            messagebox.showerror(title= 'Error', message= 'Plasmid sequence is incorrect!')
            return
        
        try:
            enzyme = getattr(br, self.restriction_enzyme)
            self.enzyme_site = enzyme.site
            
            if self.enzyme_site in self.DNA and self.enzyme_site in self.plasmid:
                DNA_fragments = self.DNA.split(self.enzyme_site)
                plasmid_fragments = self.plasmid.split(self.enzyme_site)
            else:
                messagebox.showerror(
                    title='Error',
                    message='Restriction site not found in both sequences!'
                    )
                return
                
            if len(DNA_fragments) > 2:
                messagebox.showerror(
                    title= 'Error',
                    message= 'Enzyme cuts DNA more than once. Choose different enzyme!'
                    )
                return
            if len(plasmid_fragments) > 2:
                messagebox.showerror(
                    title= 'Error',
                    message= 'Enzyme cuts plasmid more than once. Choose different enzyme!'
                    )
                return
            else:
                self.new_plasmid = plasmid_fragments[0] + self.enzyme_site + self.DNA + self.enzyme_site + plasmid_fragments[1]
            
        except AttributeError:
            messagebox.showerror(title= 'Error', message= 'Enzyme name is not correct!')
            return
        
        self.container()
        self.frame()
        self.results()
        self.visual_simulation()
    
    def container(self):
        self.container_frame = tk.Frame(self.screen, bg='#E8F4F0') 
        self.container_frame.grid(row=7, column=0, columnspan=2, pady=10)
            
        self.container_frame.grid_columnconfigure(0, weight=1)
        self.container_frame.grid_columnconfigure(1, weight=1)
        
    def frame(self):
        self.inner_frame = tk.Frame(
            self.container_frame,
            bg='#E8F4F0',
            highlightthickness = 2,
            highlightbackground = '#1B3A6B')
        self.inner_frame.grid(row=1, column=0, columnspan=2, sticky='n', pady=5)
        
    def results(self):
        DNA_length = len(self.DNA.strip())
        self.plasmid_length = len(self.plasmid.strip())
        self.cloned_plasmid = len(self.new_plasmid)
        cutting_enzyme = self.restriction_enzyme.strip()
        recognition_site = self.enzyme_site
        cloning_result = 'Successful'
        
        DNA_label_name = tk.Label(
            self.inner_frame,
            text = 'Insert DNA Length',
            fg='#8b0000',
            bg = '#E8F4F0',
            font = ('Georgia', '10', 'bold'))
                            
        DNA_label_name.grid(row = 1, column = 0, padx = 15, pady = 10)
        
        DNA_label = tk.Label(
            self.inner_frame,
            text = f'{DNA_length}',
            fg='#1a5c38',
            bg = '#E8F4F0',
            font = ('Georgia', '10', 'bold'))
                            
        DNA_label.grid(row = 1, column = 1, padx = 15, pady = 10)
        
        plasmid_label_name = tk.Label(
            self.inner_frame,
            text = 'Plasmid length',
            fg='#8b0000',
            bg = '#E8F4F0',
            font = ('Georgia', '10', 'bold'))
                            
        plasmid_label_name.grid(row = 2, column = 0, padx = 15, pady = 10)
        
        plasmid_label = tk.Label(
            self.inner_frame,
            text = f'{self.plasmid_length}',
            fg='#1a5c38',
            bg = '#E8F4F0',
            font = ('Georgia', '10', 'bold'))
                            
        plasmid_label.grid(row = 2, column = 1, padx = 15, pady = 10)
        
        recombinant_plasmid_label = tk.Label(
            self.inner_frame,
            text = 'Recombinant Plasmid Length',
            fg='#8b0000',
            bg = '#E8F4F0',
            font = ('Georgia', '10', 'bold'))
                            
        recombinant_plasmid_label.grid(row = 3, column = 0, padx = 15, pady = 10)
        
        recombinant_plasmid = tk.Label(
            self.inner_frame,
            text = f'{self.cloned_plasmid}',
            fg='#1a5c38',
            bg = '#E8F4F0',
            font = ('Georgia', '10', 'bold'))
                            
        recombinant_plasmid.grid(row = 3, column = 1, padx = 15, pady = 10)
               
        cutting_enzyme_label = tk.Label(
            self.inner_frame,
            text = 'Restriction enzyme',
            fg='#8b0000',
            bg = '#E8F4F0',
            font = ('Georgia', '10', 'bold'))
                            
        cutting_enzyme_label.grid(row = 4, column = 0, padx = 15, pady = 10)
        
        cutting_enzyme_name = tk.Label(
            self.inner_frame,
            text = f'{cutting_enzyme}',
            fg='#1a5c38',
            bg = '#E8F4F0',
            font = ('Georgia', '10', 'bold'))
                            
        cutting_enzyme_name.grid(row = 4, column = 1, padx = 15, pady = 10)
        
        recognition_site_label = tk.Label(
            self.inner_frame,
            text = 'Recognition site',
            fg='#8b0000',
            bg = '#E8F4F0',
            font = ('Georgia', '10', 'bold'))
                            
        recognition_site_label.grid(row = 5, column = 0, padx = 15, pady = 10)
        
        recognition_site_name = tk.Label(
            self.inner_frame,
            text = f'{recognition_site}',
            fg='#1a5c38',
            bg = '#E8F4F0',
            font = ('Georgia', '10', 'bold'))
                            
        recognition_site_name.grid(row = 5, column = 1, padx = 15, pady = 10)
        
        cloning_name = tk.Label(
            self.inner_frame,
            text = 'Cloning status',
            fg='#8b0000',
            bg = '#E8F4F0',
            font = ('Georgia', '10', 'bold'))
                            
        cloning_name.grid(row = 6, column = 0, padx = 15, pady = 10)
        
        cloning_label = tk.Label(
            self.inner_frame,
            text = f'{cloning_result}',
            fg='#1a5c38',
            bg = '#E8F4F0',
            font = ('Georgia', '10', 'bold'))
                            
        cloning_label.grid(row = 6, column = 1, padx = 15, pady = 10)
    
    def open_gel_window(self):
        self.gel_screen = tk.Toplevel(self.screen)
        self.gel_screen.title('Virtual Gel Visualization')    
        self.gel_screen.geometry('500x500')
        self.gel_screen.config(bg = '#F5F0E8')
        self.gel_screen.grid_columnconfigure(0, weight=1)
        self.gel_screen.grid_columnconfigure(1, weight=1)
        
        new_window_label = tk.Label(
            self.gel_screen,
            bg = '#F5F0E8',
            fg = '#1B3A6B',
            text = 'Virtual Gel Visualization',
            font = ('Georgia', '20', 'bold'))
        
        new_window_label.grid(row = 0, column = 0, columnspan=2, pady = 30)
        
        self.canva()
        
        max_value = max(self.plasmid_length, self.cloned_plasmid)
        reference = max_value * 1.2
        y_plasmid = 350 - ((self.plasmid_length/reference) * 350)
        y_cloned_plasmid = 350 - ((self.cloned_plasmid/reference) * 350)
        
        # Rectangle
        self.canvas.create_rectangle(62, y_plasmid, 112, y_plasmid + 10, fill='#50C878')
        self.canvas.create_rectangle(237, y_cloned_plasmid, 287, y_cloned_plasmid + 10, fill='#50C878')
        
        # Text
        self.canvas.create_text(87, y_plasmid - 15, text='Plasmid', fill='#ffffff')
        self.canvas.create_text(262, y_cloned_plasmid - 15, text='Recombinant', fill='#ffffff')
    
    def visual_simulation(self):
        button = tk.Button(
        self.inner_frame,
        text = 'View Virtual Gel',
        bg = '#1B3A6B',
        fg = '#FFFFFF',
        command = self.open_gel_window,
        font = ('Georgia', '10', 'bold'))
        
        button.grid(row = 7, column = 0, columnspan=2, pady = 30)
        
    def canva(self):
        self.canvas = tk.Canvas(
            self.gel_screen,
            width = 350,
            height = 350,
            highlightthickness = 0,
            bg = '#000000')
        self.canvas.grid(row = 1, column =0, columnspan=2, pady = 30)
    
    def button_creation(self):
        button = tk.Button(
            self.screen,
            text = 'Submit',
            bg = '#1B3A6B',
            fg = '#FFFFFF',
            command = self.cloning_work,
            font = ('Georgia', '10', 'bold'))
        button.grid(row = 6, column = 0, columnspan=2, pady = 30)
        
    def in_silico_cloning(self):
        self.window()
        self.DNA_label()
        self.DNA_text_label()
        self.plasmid_label()
        self.plasmid_text_label()
        self.restriction()
        self.enzyme_label()
        self.text_entry()
        self.listbox()
        self.button_creation()
        self.screen.mainloop()
