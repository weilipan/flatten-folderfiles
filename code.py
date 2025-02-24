import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def select_source_folder():
    """讓使用者選擇來源資料夾"""
    folder = filedialog.askdirectory(title="選擇來源資料夾")
    if folder:
        source_var.set(folder)

def select_destination_folder():
    """讓使用者選擇目標資料夾"""
    folder = filedialog.askdirectory(title="選擇目標資料夾")
    if folder:
        destination_var.set(folder)

def copy_all_files():
    """複製來源資料夾內所有檔案（不包含子資料夾結構）到目標資料夾"""
    src_dir = source_var.get()
    dest_dir = destination_var.get()

    if not src_dir or not dest_dir:
        messagebox.showerror("錯誤", "請選擇來源與目標資料夾！")
        return

    if not os.path.exists(src_dir):
        messagebox.showerror("錯誤", f"來源資料夾不存在：{src_dir}")
        return

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    file_count = 0
    for root, _, files in os.walk(src_dir):
        for file in files:
            file_path = os.path.join(root, file)
            dest_file_path = os.path.join(dest_dir, file)

            shutil.copy2(file_path, dest_file_path)
            file_count += 1
            status_label.config(text=f"已複製 {file_count} 個檔案...")

    messagebox.showinfo("完成", f"檔案複製完成！共複製 {file_count} 個檔案。")
    status_label.config(text="檔案複製完成！")

# 建立 GUI 介面
root = tk.Tk()
root.title("檔案複製工具")
root.geometry("500x250")
root.resizable(False, False)

# 來源資料夾選擇
source_var = tk.StringVar()
tk.Label(root, text="來源資料夾：").pack(pady=5)
tk.Entry(root, textvariable=source_var, width=50).pack()
tk.Button(root, text="選擇資料夾", command=select_source_folder).pack(pady=5)

# 目標資料夾選擇
destination_var = tk.StringVar()
tk.Label(root, text="目標資料夾：").pack(pady=5)
tk.Entry(root, textvariable=destination_var, width=50).pack()
tk.Button(root, text="選擇資料夾", command=select_destination_folder).pack(pady=5)

# 開始複製按鈕
tk.Button(root, text="開始複製", command=copy_all_files, fg="white", bg="green").pack(pady=10)

# 狀態顯示
status_label = tk.Label(root, text="", fg="blue")
status_label.pack()

# 運行 GUI
root.mainloop()
