import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from src.ui.diagram_editor import DiagramEditor
from src.ui.preview_panel import PreviewPanel
from src.ai.openai_client import OpenAIClient
from src.utils.file_handler import FileHandler

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Mermaid Diagram Editor")
        self.root.geometry("1200x800")
        
        # AI Client
        self.ai_client = OpenAIClient()
        
        # Create UI Components
        self._create_menu()
        self._create_layout()
    
    def _create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File Menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_diagram)
        file_menu.add_command(label="Open", command=self.open_diagram)
        file_menu.add_command(label="Save", command=self.save_diagram)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        # AI Menu
        ai_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="AI", menu=ai_menu)
        ai_menu.add_command(label="Generate Diagram", command=self.generate_ai_diagram)
    
    def _create_layout(self):
        # Main container
        main_container = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        main_container.pack(fill=tk.BOTH, expand=True)
        
        # Diagram Editor
        self.diagram_editor = DiagramEditor(main_container)
        main_container.add(self.diagram_editor)
        
        # Preview Panel
        self.preview_panel = PreviewPanel(main_container)
        main_container.add(self.preview_panel)
    
    def generate_ai_diagram(self):
        # Prompt user for diagram description
        prompt = tk.simpledialog.askstring("AI Diagram Generator", "Describe the diagram you want to create:")
        if prompt:
            try:
                diagram_code = self.ai_client.generate_mermaid_diagram(prompt)
                self.diagram_editor.set_text(diagram_code)
                self.preview_panel.render_diagram(diagram_code)
            except Exception as e:
                messagebox.showerror("AI Generation Error", str(e))
    
    def new_diagram(self):
        self.diagram_editor.clear()
        self.preview_panel.clear()
    
    def open_diagram(self):
        filepath = filedialog.askopenfilename(
            defaultextension=".mmd",
            filetypes=[("Mermaid Files", "*.mmd"), ("All Files", "*.*")]
        )
        if filepath:
            content = FileHandler.read_file(filepath)
            self.diagram_editor.set_text(content)
            self.preview_panel.render_diagram(content)
    
    def save_diagram(self):
        filepath = filedialog.asksaveasfilename(
            defaultextension=".mmd",
            filetypes=[("Mermaid Files", "*.mmd"), ("All Files", "*.*")]
        )
        if filepath:
            content = self.diagram_editor.get_text()
            FileHandler.save_file(filepath, content)