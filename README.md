# ballxpit-gamepass-to-steam-save
# BALL x PIT Save Converter  
# BALL x PIT 存档转换工具

---

## 🇺🇸 English

### Description
This tool converts save files from the **Game Pass (XGP)** version of *BALL x PIT* to the **Steam** version.

It is based on the method described in this guide:  
https://steamcommunity.com/sharedfiles/filedetails/?id=3590175070  

Special thanks to the original author.

The logic follows the original guide, but replaces manual hex editing with automated code.

---

### How to Use

1. Run the program  
2. Select your Game Pass save file (`container.dat` or similar)  
3. A file named `meta1.yankai` will be generated in the same directory  
4. Replace the `meta1.yankai` file in your Steam save folder  

If you do not have a Python environment, download the `.exe` from the **Releases** page.

---

### Important Notes

- ⚠️ This tool does **NOT guarantee success in all cases**
- 💾 Always **backup your save files manually**
- ☁️ Disable **Steam Cloud synchronization** before replacing saves

---

### Game Pass Save Location
%appdata%..\Local\Packages\DevolverDigital.BallxPit_6kzv4j18v0c96\SystemAppData\wgs\


Steps:
1. Open the folder with a long random name  
2. Open its subfolder  
3. You should see two files  
4. Use the **larger file** (example: `C566B542A64C4C54AE63652C40AF3359`)

---

### Steam Save Location
%appdata%..\LocalLow\Kenny Sun\BALL x PIT\



---

## 🇨🇳 中文

### 项目说明
本工具用于将 *BALL x PIT* 的 **Game Pass（XGP）版本存档** 转换为 **Steam 版本存档**。

参考方案来自：  
https://steamcommunity.com/sharedfiles/filedetails/?id=3590175070  

感谢原作者提供的方法。

本工具实现逻辑与原教程一致，但将手动十六进制操作替换为自动化代码。

---

### 使用方法

1. 运行程序  
2. 选择 XGP 存档文件（如 `container.dat`）  
3. 程序会在同目录生成 `meta1.yankai`  
4. 将该文件替换到 Steam 存档目录  

如果没有 Python 环境，可以下载 **Releases 中的 exe 文件**。

---

### 注意事项

- ⚠️ 无法保证一定成功（不同版本可能存在差异）  
- 💾 使用前请**手动备份存档**  
- ☁️ 请先关闭 **Steam 云存档同步**  

---

### XGP 存档位置
%appdata%..\Local\Packages\DevolverDigital.BallxPit_6kzv4j18v0c96\SystemAppData\wgs\


步骤：

1. 打开名称很长的文件夹  
2. 再进入其中的子文件夹  
3. 会看到两个文件  
4. 选择**较大的那个文件**（例如：`C566B542A64C4C54AE63652C40AF3359`）

---

### Steam 存档位置
%appdata%..\LocalLow\Kenny Sun\BALL x PIT\


---

## ⭐ Disclaimer / 声明

This project is for learning and personal use only.  
Use at your own risk.

本项目仅用于学习与个人使用，风险自负。
