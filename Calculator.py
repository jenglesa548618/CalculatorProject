import tkinter as tk
from tkinter import font

class calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ Calculator ✨")
        self.root.geometry("450x620")
        self.root.configure(bg="#0f0f1e")
        self.root.resizable(True, True)
        
        # Set window icon and appearance
        self.root.attributes('-alpha', 1.0)
        
        self.expression = ""
        self.setup_ui()
        
    def setup_ui(self):
        # Header frame
        header_frame = tk.Frame(self.root, bg="#1a1a2e", height=60)
        header_frame.pack(fill="x", padx=0, pady=0)
        
        header_label = tk.Label(
            header_frame,
            text="Calculator",
            font=("Segoe UI", 24, "bold"),
            bg="#1a1a2e",
            fg="#00d4ff"
        )
        header_label.pack(pady=12)
        
        # Main container
        main_frame = tk.Frame(self.root, bg="#0f0f1e")
        main_frame.pack(fill="both", expand=True, padx=15, pady=15)
        
        # Display with shadow effect
        display_shadow = tk.Frame(main_frame, bg="#00d4ff", highlightthickness=0)
        display_shadow.pack(fill="x", pady=(0, 8))
        
        display_font = font.Font(family="Segoe UI", size=26, weight="bold")
        self.display = tk.Entry(
            display_shadow,
            font=display_font,
            borderwidth=0,
            relief="flat",
            justify="right",
            bg="#1a1a2e",
            fg="#00ff88",
            insertbackground="#00ff88",
            highlightthickness=0
        )
        self.display.pack(ipady=18, ipadx=10, fill="both")
        
        # Button frame
        button_frame = tk.Frame(main_frame, bg="#0f0f1e")
        button_frame.pack(fill="both", expand=True, pady=10)
        
        buttons = [
            ["7", "8", "9", "÷"],
            ["4", "5", "6", "×"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["C", "←", "√", "%"]
        ]
        
        button_font = font.Font(family="Segoe UI", size=16, weight="bold")
        
        for row in buttons:
            row_frame = tk.Frame(button_frame, bg="#0f0f1e")
            row_frame.pack(fill="both", expand=True, pady=4)
            
            for btn_text in row:
                self.create_styled_button(
                    row_frame, 
                    btn_text, 
                    button_font
                )
    
    def create_styled_button(self, parent, text, font_obj):
        # Determine button color
        if text in ["C", "←"]:
            bg_color = "#ff006e"
            hover_color = "#ff3b8f"
        elif text == "=":
            bg_color = "#00ff88"
            hover_color = "#33ffaa"
            fg_color = "#0f0f1e"
            hover_fg = "#0f0f1e"
        elif text in ["÷", "×", "-", "+"]:
            bg_color = "#00d4ff"
            hover_color = "#33e5ff"
            fg_color = "#0f0f1e"
            hover_fg = "#0f0f1e"
        elif text in ["√", "%"]:
            bg_color = "#a100f2"
            hover_color = "#c233ff"
        else:
            bg_color = "#1a1a2e"
            hover_color = "#2a2a4e"
        
        if text != "=":
            fg_color = "#ffffff"
            hover_fg = "#ffffff"
        
        btn = tk.Button(
            parent,
            text=text,
            font=font_obj,
            command=lambda x=text: self.on_button_click(x),
            bg=bg_color,
            fg=fg_color,
            activebackground=hover_color,
            activeforeground=hover_fg,
            relief="flat",
            bd=0,
            highlightthickness=0,
            cursor="hand2"
        )
        btn.pack(side="left", fill="both", expand=True, padx=3)
    
    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "←":
            self.expression = self.expression[:-1]
        elif char == "=":
            try:
                # Replace display symbols with Python operators
                calc_expr = self.expression.replace("÷", "/").replace("×", "*")
                result = eval(calc_expr)
                self.expression = str(result)
            except:
                self.expression = "Error"
        elif char == "√":
            try:
                result = float(self.expression) ** 0.5
                self.expression = str(result)
            except:
                self.expression = "Error"
        elif char == "%":
            try:
                result = float(self.expression) / 100
                self.expression = str(result)
            except:
                self.expression = "Error"
        else:
            self.expression += str(char)
        
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = calculator(root)
    root.mainloop()
