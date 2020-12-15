# import MySQL connector
import mysql.connector

# connect to server
connection = mysql.connector.connect(user='root', password='XXXXXXXX', host='127.0.0.1', port='3308')
print('Connected to database.')
cursor = connection.cursor()

# Opdaterer virksomhed
cursor.callproc('stage_db.opret_virksomhed_1')
print('Stage_db virksomhed updated.')

# Opdaterer adresse
cursor.callproc('stage_db.opret_adresse_2')
print('Stage_db adresse updated.')

# Opdaterer teknologi
cursor.callproc('stage_db.opret_teknologi_3')
print('Stage_db teknologi updated.')

# Indsætter teknologi_Mobil
cursor.callproc('stage_db.insert_mobil_teknologi_4')
print('stage_db mobil data inserted.')

# Trimmer mobil data til en værdi
cursor.callproc('stage_db.trim_mobil_data_5')
print('stage_db mobil data trim executed.')

# Trimmer "" væk fra virksomhed
cursor.callproc('stage_db.trim_virksomhed_6')
print('stage_db virksomhed trimmet.')

# Sammensætter og flytter teknologi & adresse
cursor.callproc('stage_db.Teknologi_final_7')
print('stage_db teknologi table updated.')


# Kopier data fra Stage_db til datawarehouse viksomhed
cursor.callproc('datawarehouse.insert_virksomhed_1')
print('Data copied to Datawarehouse virksomhed.')

# Kopier data fra Stage_db til datawarehouse adresse
cursor.callproc('datawarehouse.insert_adressse_2')
print('Data copied to Datawarehouse adresse.')

# Kopier data fra Stage_db til datawarehouse teknologi
cursor.callproc('datawarehouse.insert_teknologi_3')
print('Data copied to Datawarehouse teknologi.')


#  commit & close connection
cursor.close()
connection.commit()
connection.close()
print('Disconnected from database.')
print('')
print(' _    ________  __________   ____________ ')
print('| |  / /  _/  |/  / ____/ | / /_  __/ __ \ ')
print('| | / // // /|_/ / __/ /  |/ / / / / / / /')
print('| |/ // // /  / / /___/ /|  / / / / /_/ / ')
print('|___/___/_/  /_/_____/_/ |_/ /_/  \____/  ')
print('')
