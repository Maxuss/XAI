from PyInstaller.utils.hooks import collect_data_files

#Instruct pyinstaller to collect data files from resources package.
datas = collect_data_files('resources')