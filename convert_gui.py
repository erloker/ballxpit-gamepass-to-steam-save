import os
import tkinter as tk
from tkinter import filedialog, messagebox

# ===== pattern（保持你原来的）=====
START_PATTERN = bytes.fromhex(
    "02 2F 00 00 00 00 01 1D 00 00 00 4D 00 65 00 74 00 61 00 53 00 61 00 76 00 65 00 44 00 61 00 74 00 61"
)

END_PATTERN = bytes.fromhex(
    "4E 00 75 00 6D 00 42 00 6F 00 73 00 73 00 42 00 6C 00 75 00 65 00 70 00 72 00 69 00 6E 00 74 00 73 00 44 00 72 00 6F 00 70 00 70 00 65 00 64 00 00 00 00 00 05"
)

def convert_file(input_path):
    with open(input_path, "rb") as f:
        data = f.read()

    start = data.find(START_PATTERN)
    end = data.find(END_PATTERN, start)

    if start == -1 or end == -1:
        messagebox.showerror("失败", "❌ 没找到标记（版本可能不匹配）")
        return

    end += len(END_PATTERN)
    chunk = data[start:end]

    output_path = os.path.join(
        os.path.dirname(input_path),
        "meta1.yankai"
    )

    with open(output_path, "wb") as f:
        f.write(chunk)

    messagebox.showinfo(
        "成功",
        f"✅ 已导出:\n{output_path}\n\n大小: {len(chunk)} bytes"
    )

def select_file():
    path = filedialog.askopenfilename(
        title="选择 Game Pass 存档文件",
        filetypes=[("All Files", "*.*")]
    )
    if path:
        convert_file(path)

# ===== GUI =====
root = tk.Tk()
root.title("BALL x PIT 存档转换工具")
root.geometry("400x150")

label = tk.Label(root, text="选择 container.dat 文件进行转换")
label.pack(pady=20)

btn = tk.Button(root, text="选择文件并转换", command=select_file, height=2)
btn.pack()

note = tk.Label(root, text="输出文件会在同目录生成 meta1.yankai", fg="gray")
note.pack(pady=10)

root.mainloop()
