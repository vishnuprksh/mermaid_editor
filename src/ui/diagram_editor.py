import tkinter as tk
from tkinter import scrolledtext

class DiagramEditor(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        # Create scrolled text widget for diagram editing
        self.text_area = scrolledtext.ScrolledText(
            self, 
            wrap=tk.WORD, 
            width=60, 
            height=30, 
            font=("Courier", 10)
        )
        self.text_area.pack(fill=tk.BOTH, expand=True)
        
        # Syntax highlighting (basic implementation)
        self.text_area.tag_configure("keyword", foreground="blue")
        self.text_area.tag_configure("comment", foreground="green")
        
        # Bind events for syntax highlighting
        self.text_area.bind("<KeyRelease>", self._highlight_syntax)
    
    def _highlight_syntax(self, event=None):
        """Basic syntax highlighting for Mermaid"""
        content = self.text_area.get("1.0", tk.END)
        
        # Clear existing tags
        for tag in ["keyword", "comment"]:
            self.text_area.tag_remove(tag, "1.0", tk.END)
        
        # Highlight Mermaid keywords
        mermaid_keywords = [
            "graph", "flowchart", "subgraph", "end", 
            "classDiagram", "stateDiagram", "sequenceDiagram"
        ]
        
        for keyword in mermaid_keywords:
            start_index = "1.0"
            while True:
                start_index = self.text_area.search(keyword, start_index, tk.END)
                if not start_index:
                    break
                end_index = f"{start_index}+{len(keyword)}c"
                self.text_area.tag_add("keyword", start_index, end_index)
                start_index = end_index
    
    def get_text(self):
        """Get the current text from the editor"""
        return self.text_area.get("1.0", tk.END).strip()
    
    def set_text(self, text):
        """Set text in the editor"""
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert("1.0", text)
        self._highlight_syntax()
    
    def clear(self):
        """Clear the text area"""
        self.text_area.delete("1.0", tk.END)