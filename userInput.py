import mysql.connector
import os
import uuid

cnx = mysql.connector.connect(user = 'a.schneider', password = '4u2change', database = 'dBAngelaSchneider', host = 'mysql.cs.rocky.edu')
cnx2 = mysql.connector.connect(user = 'a.schneider', password = '4u2change', database = 'dBAngelaSchneider', host = 'mysql.cs.rocky.edu')
cnx3 = mysql.connector.connect(user = 'a.schneider', password = '4u2change', database = 'dBAngelaSchneider', host = 'mysql.cs.rocky.edu')
cnx4 = mysql.connector.connect(user = 'a.schneider', password = '4u2change', database = 'dBAngelaSchneider', host = 'mysql.cs.rocky.edu')
cnx5 = mysql.connector.connect(user = 'a.schneider', password = '4u2change', database = 'dBAngelaSchneider', host = 'mysql.cs.rocky.edu')
cnx6 = mysql.connector.connect(user = 'a.schneider', password = '4u2change', database = 'dBAngelaSchneider', host = 'mysql.cs.rocky.edu')
cnx7 = mysql.connector.connect(user = 'a.schneider', password = '4u2change', database = 'dBAngelaSchneider', host = 'mysql.cs.rocky.edu')




cursor = cnx.cursor()
cursor2 = cnx2.cursor()
cursor3 = cnx3.cursor()
cursor4 = cnx4.cursor()
cursor5 = cnx5.cursor()
cursor6 = cnx6.cursor()
cursor7 = cnx7.cursor()



BUSINESS_NM = input("Enter your business's name. If you do not have a business name, enter None: ")
FIRST_NM = input("Enter your first name: ")
LAST_NM = input("Enter your last name: ")
STREET = input("Enter your street address: ")
CITY = input("Enter your city of residence: ")
STATE_PROV = input("Enter you state of residence: ")
POSTAL_CODE = input("Enter your zip code: ")
PHONE_NUMBER = input("Enter your phone number in this format xxx-xxx-xxxx: ")
EMAIL_ADDRESS = input("Enter your email address. If you do not have an email address, enter None: ")
UUID = uuid.uuid1()
UUID2 = uuid.uuid1()

print("Your information entered: ",  UUID, BUSINESS_NM, FIRST_NM, LAST_NM, STREET, CITY, STATE_PROV, POSTAL_CODE, PHONE_NUMBER, EMAIL_ADDRESS)


query = ("""INSERT INTO dBAngelaSchneider.UUIDS
        (UUID, LAST_ATTR_UPDT_ID, LAST_ATTR_UPDT_DT)
        VALUES('%s', 'Me', NOW())""" % (UUID))


query2 = ("""INSERT INTO dBAngelaSchneider.CUSTOMERS
        (UUID, CREATED_DT, LAST_ATTR_UPDT_ID, LAST_ATTR_UPDT_DT)
        VALUES('%s', NOW(), 'Me', NOW())""" % (UUID))

query3 = ("""INSERT INTO dBAngelaSchneider.NAMES
        (UUID, BUSINESS_NM, FIRST_NM, LAST_NM, LAST_ATTR_UPDT_ID, LAST_ATTR_UPDT_DT)
        VALUES('%s', '%s', '%s', '%s', 'Me', NOW())""" % (UUID, BUSINESS_NM, FIRST_NM, LAST_NM))

query4 = ("""INSERT INTO dBAngelaSchneider.ADDRESSES
        (UUID, STREET, CITY, STATE_PROV, POSTAL_CODE, LAST_ATTR_UPDT_ID, LAST_ATTR_UPDT_DT)
        VALUES('%s', '%s', '%s', '%s', '%s', 'Me', NOW())""" % (UUID, STREET, CITY, STATE_PROV, POSTAL_CODE))

query5 = ("""INSERT INTO dBAngelaSchneider.PHONE_NUMBERS
        (OWNER_UUID, PHONE_DESC_UUID, PHONE_NUMBER, LAST_ATTR_UPDT_ID, LAST_ATTR_UPDT_DT)
        VALUES('%s', '90E36D6F-688B-427C-AB8A-D4C20281656F', '%s', 'Me', NOW())""" % (UUID, PHONE_NUMBER))

query6 = ("""INSERT INTO dBAngelaSchneider.EMAILS
        (OWNER_UUID, UUID, EMAIL_ADDRESS, LAST_ATTR_UPDT_ID, LAST_ATTR_UPDT_DT)
        VALUES('%s', '%s', '%s', 'Me', NOW())""" % (UUID, UUID2, EMAIL_ADDRESS))



cursor.execute(query)
cnx.commit()
cursor2.execute(query2)
cnx2.commit()
cursor3.execute(query3)
cnx3.commit()
cursor4.execute(query4)
cnx4.commit()
cursor5.execute(query5)
cnx5.commit()
cursor6.execute(query6)
cnx6.commit()




cursor.close()
cnx.close()

cursor2.close()
cnx2.close()

cursor3.close()
cnx3.close()

cursor4.close()
cnx4.close()

cursor5.close()
cnx5.close()         

cursor6.close()
cnx6.close()

cursor7.close()
cnx7.close()
