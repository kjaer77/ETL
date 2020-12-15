# import MySQL connector
import mysql.connector

# connect to server
connection = mysql.connector.connect(user='root', password='XXXXXXX', host='127.0.0.1', port='3308')
print('Connected to database.')
cursor = connection.cursor()

# Opdaterer adresse
#Sletter inholdet af datawarehouse.adress
query = ("TRUNCATE TABLE datawarehouse.adresse " )
cursor.execute(query)
#Disabler foreign key check
query = ("SET FOREIGN_KEY_CHECKS = 0")
cursor.execute(query)
#Bygger query her
query = (
        "INSERT INTO datawarehouse.adresse (the_key, vejNavn, husNr, postNr) "
        "SELECT the_key, vejnavn, husnr, postnr FROM vimento.cvr"
        )
cursor.execute(query)
print('Datawarehouse adress table updated.')



#Opdaterer koordinat
#Sletter inholdet af datawarehouse.adress
query1 = ("TRUNCATE TABLE datawarehouse.koordinat " )
cursor.execute(query1)
#Disabler foreign key check
query1 = ("SET FOREIGN_KEY_CHECKS = 0")
cursor.execute(query1)
#Bygger query her
query1 = (
        "INSERT INTO datawarehouse.koordinat (the_key, breddeGrad, laengdeGrad) "
        "SELECT the_key, latitude, longitude FROM vimento.cvr"
        )
cursor.execute(query1)
query1 = ("UPDATE datawarehouse.koordinat SET laengdeGrad = 0 WHERE laengdeGrad IS NULL")
cursor.execute(query1)
query1 = ("UPDATE datawarehouse.koordinat SET breddeGrad = 0 WHERE breddeGrad IS NULL")
cursor.execute(query1)
print('Datawarehouse koordinat table updated.')



#Opdaterer teknologi_dsl
query2 = ("TRUNCATE TABLE datawarehouse.teknologi " )
cursor.execute(query2)
#Bygger query her
query2 = (
        "INSERT INTO datawarehouse.teknologi (the_key, maxUp, maxDown, navn) "
        "SELECT cvr.the_key, down_dsl, up_dsl, 'dsl' FROM vimento.fixed_broadband "
        "INNER JOIN vimento.cvr ON fixed_broadband.adgangsadresseid = cvr.adgangsadresseid "
        )
cursor.execute(query2)
print('Datawarehouse teknologi dsl updated.')


#Opdaterer teknologi fiber
#Bygger query her
query3 = (
        "INSERT INTO datawarehouse.teknologi (the_key, maxUp, maxDown, navn) "
        "SELECT cvr.the_key, down_fiber, up_fiber, 'fiber' FROM vimento.fixed_broadband "
        "INNER JOIN vimento.cvr ON fixed_broadband.adgangsadresseid = cvr.adgangsadresseid "
        )
cursor.execute(query3)
print('Datawarehouse teknologi fiber updated.')



#Opdaterer teknologi kabel
#Bygger query her
query4 = (
        "INSERT INTO datawarehouse.teknologi (the_key, maxUp, maxDown, navn) "
        "SELECT cvr.the_key, down_kabel, up_kabel, 'kabel' FROM vimento.fixed_broadband "
        "INNER JOIN vimento.cvr ON fixed_broadband.adgangsadresseid = cvr.adgangsadresseid "
        )
cursor.execute(query4)
print('Datawarehouse teknologi kabel updated.')



#Opdaterer teknologi mobil
#Bygger query her
query5 = (
        "INSERT INTO datawarehouse.teknologi (the_key, mobilDown, navn) "
        "SELECT cvr.the_key, max_data, 'mobil' FROM vimento.mobile_tjek "
        "INNER JOIN vimento.cvr ON mobile_tjek.adgangsadresseid = cvr.adgangsadresseid "
        )
cursor.execute(query5)
print('Datawarehouse teknologi mobil updated.')



#Opdaterer virksomhed
#Bygger query her
query6 = ("TRUNCATE TABLE datawarehouse.virksomhed " )
cursor.execute(query6)
query6 = (
        "INSERT INTO datawarehouse.virksomhed (the_key, navn, branche, antalAnsatte) "
        "SELECT the_key, Firmanavn, 'branchebetegnelse_primær', ansatte FROM vimento.cvr "
        )
cursor.execute(query6)
print('Datawarehouse virksomhed updated.')

#  commit & close connection
cursor.close()
connection.commit()
connection.close()
print('Disconnected from database.')
