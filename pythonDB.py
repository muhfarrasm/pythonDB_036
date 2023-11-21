import sqlite3
import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menambahkan data ke database
def tambah_data():
    try:
        nama = entry_nama.get()
        nilai_biologi = int(entry_biologi.get())
        nilai_fisika = int(entry_fisika.get())
        nilai_inggris = int(entry_inggris.get())

        # Menentukan prediksi fakultas
        if nilai_biologi > nilai_fisika and nilai_biologi > nilai_inggris:
            prediksi = 'Kedokteran'
        elif nilai_fisika > nilai_biologi and nilai_fisika > nilai_inggris:
            prediksi = 'Teknik'
        elif nilai_inggris > nilai_biologi and nilai_inggris > nilai_fisika:
            prediksi = 'Bahasa'
        else:
            prediksi = 'Tidak Dapat Diprediksi'

        # Menyimpan data ke database
        conn = sqlite3.connect('datamurid.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS nilai_siswa (
                            nama_siswa TEXT,
                            biologi INTEGER,
                            fisika INTEGER,
                            inggris INTEGER,
                            prediksi_Prodi TEXT
                        )''')
        cursor.execute("INSERT INTO nilai_siswa VALUES (?, ?, ?, ?, ?)",
                       (nama, nilai_biologi, nilai_fisika, nilai_inggris, prediksi))
        conn.commit()
        conn.close()
        
        
        # Menampilkan message box dengan prediksi
        messagebox.showinfo("Success", "Prediksi Fakultas: {}".format(prediksi))
    except sqlite3.Error as e:
        messagebox.showerror("Error", ": {}".format(prediksi))


# Membuat GUI menggunakan Tkinter
root = tk.Tk()
root.geometry ("400x400")
root.resizable(False, False)
root.title("Input Nilai Siswa")

label_nama = tk.Label(root, text="Nama Siswa:")
label_nama.pack()
entry_nama = tk.Entry(root)
entry_nama.pack()

label_biologi = tk.Label(root, text="Nilai Biologi:")
label_biologi.pack()
entry_biologi = tk.Entry(root)
entry_biologi.pack()

label_fisika = tk.Label(root, text="Nilai Fisika:")
label_fisika.pack()
entry_fisika = tk.Entry(root)
entry_fisika.pack()

label_inggris = tk.Label(root, text="Nilai Inggris:")
label_inggris.pack()
entry_inggris = tk.Entry(root)
entry_inggris.pack()

button_submit = tk.Button(root, text="Submit", command=tambah_data)
button_submit.pack()

root.mainloop()
