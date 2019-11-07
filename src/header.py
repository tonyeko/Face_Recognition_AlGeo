import tkinter.ttk as ttk

def header(self):
    text1 = r"""
  _______    ___       ______  _______                                                                     
 |   ____|  /   \     /      ||   ____|                                                                    
 |  |__    /  ^  \   |  ,----'|  |__                                                                       
 |   __|  /  /_\  \  |  |     |   __|                                                                      
 |  |    /  _____  \ |  `----.|  |____                                                                     
 |__|   /__/     \__\ \______||_______|                                                                    
                                                                                                         
 .______       _______   ______   ______     _______ .__   __.  __  .___________. __    ______   .__   __. 
 |   _  \     |   ____| /      | /  __  \   /  _____||  \ |  | |  | |           ||  |  /  __  \  |  \ |  | 
 |  |_)  |    |  |__   |  ,----'|  |  |  | |  |  __  |   \|  | |  | `---|  |----`|  | |  |  |  | |   \|  | 
 |      /     |   __|  |  |     |  |  |  | |  | |_ | |  . `  | |  |     |  |     |  | |  |  |  | |  . `  | 
 |  |\  \----.|  |____ |  `----.|  `--'  | |  |__| | |  |\   | |  |     |  |     |  | |  `--'  | |  |\   | 
 | _| `._____||_______| \______| \______/   \______| |__| \__| |__|     |__|     |__|  \______/  |__| \__| 
                                                                                                          
 
                                                                                                 By: UNITY
                                                                                  Tony Eko Yuwono 13518030
                                                                                   Tifany Angelia 13518067
                                                                           Rifaldy Aristya Kelana 13518082
    """


    style = ttk.Style()
    style.configure('Style.TButton', font='TkFixedFont')

    label = ttk.Label(self, text=text1, style='Style.TButton')

    label.grid(row = 0, column = 0, columnspan = 10, padx = 0, pady = 10)

def help_txt(self):
      help = r"""
    
  .----------------.  .-----------------. .----------------.  .----------------.  .----------------. 
  | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
  | | _____  _____ | || | ____  _____  | || |     _____    | || |  _________   | || |  ____  ____  | |
  | ||_   _||_   _|| || ||_   \|_   _| | || |    |_   _|   | || | |  _   _  |  | || | |_  _||_  _| | |
  | |  | |    | |  | || |  |   \ | |   | || |      | |     | || | |_/ | | \_|  | || |   \ \  / /   | |
  | |  | '    ' |  | || |  | |\ \| |   | || |      | |     | || |     | |      | || |    \ \/ /    | |
  | |   \ `--' /   | || | _| |_\   |_  | || |     _| |_    | || |    _| |_     | || |    _|  |_    | |
  | |    `.__.'    | || ||_____|\____| | || |    |_____|   | || |   |_____|    | || |   |______|   | |
  | |              | || |              | || |              | || |              | || |              | |
  | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 

    By: Kelompok UNITY
    Tony Eko Yuwono           13518030
    Tifany Angelia            13518067
    Rifaldy Aristya Kelana    13518082

    Cara menggunakan program ini:
    1. Masukkan nama file foto yang ingin diuji
          - Masukan dapat diinput secara manual 
          - Masukan dapat dipilih dengan menekan tombol "Browse File"
    2. Masukkan banyak foto termirip yang diinginkan
    3. Pilih metode yang diinginkan:
          - Cosine Similarity
          - Euclidean Distance
    4. Tekan Tombol "Run"
    """
      style = ttk.Style()
      style.configure('Style.TButton', font='TkFixedFont')

      label = ttk.Label(self, text=help, style='Style.TButton')

      label.grid(row = 2, column = 0, columnspan = 10, padx = 20, pady = 10)