import tkinter as tk
import tkinter.messagebox as messagebox
import requests
import os
import base64
import tempfile
import webbrowser

class PreviewPanel(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        # Webview for Mermaid rendering
        self.webview = tk.Text(
            self, 
            width=60, 
            height=30, 
            wrap=tk.WORD
        )
        self.webview.pack(fill=tk.BOTH, expand=True)
        
        # Render button
        self.render_btn = tk.Button(
            self, 
            text="Render Diagram", 
            command=self._render_in_browser
        )
        self.render_btn.pack(fill=tk.X)
    
    def render_diagram(self, mermaid_code):
        """
        Render Mermaid diagram in a temporary HTML file
        
        Args:
            mermaid_code (str): Mermaid diagram syntax
        """
        try:
            # Create temporary HTML file for rendering
            with tempfile.NamedTemporaryFile(
                mode='w', 
                delete=False, 
                suffix='.html', 
                encoding='utf-8'
            ) as temp_file:
                html_content = f"""
                <!DOCTYPE html>
                <html>
                <head>
                    <meta charset="UTF-8">
                    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
                    <script>
                        mermaid.initialize({{ startOnLoad: true }});
                    </script>
                </head>
                <body>
                    <div class="mermaid">
                    {mermaid_code}
                    </div>
                </body>
                </html>
                """
                temp_file.write(html_content)
                self.temp_html_path = temp_file.name
            
            # Update text preview
            self.webview.delete("1.0", tk.END)
            self.webview.insert(tk.END, "Diagram ready for preview!")
        
        except Exception as e:
            messagebox.showerror("Rendering Error", str(e))
    
    def _render_in_browser(self):
        """Open the temporary HTML file in default web browser"""
        if hasattr(self, 'temp_html_path'):
            webbrowser.open(f'file://{self.temp_html_path}')
        else:
            messagebox.showinfo("Preview", "Generate a diagram first!")
    
    def clear(self):
        """Clear the preview panel"""
        self.webview.delete("1.0", tk.END)
        if hasattr(self, 'temp_html_path'):
            try:
                os.unlink(self.temp_html_path)
            except:
                pass