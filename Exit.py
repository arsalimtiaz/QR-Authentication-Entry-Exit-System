import sqlite3
import pyzbar.pyzbar as pyzbar
import cv2
import time

db_file = "Campus.db"

try:
    conn = sqlite3.connect(db_file)
except error as e:
    print(e)

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

USN = ''
print("Opened DB")

while True:

    cursor = conn.cursor()
    _, frame = cap.read()
    USN = ''

    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        cv2.putText(frame, str(obj.data), (50, 50), font, 2,
                    (255, 0, 0), 3)
        USN = obj.data.decode('utf-8')
        print(USN)
        cursor.execute("Select * from ID where USN = ?", (USN,))
        data = cursor.fetchall()

        if len(data) == 0:
            print("ENTRY DENIED")
            cv2.destroyAllWindows()
        else:
            ID = data[0][0]
            flag = data[0][1]
            # print(ID)
            # print(flag)
            if flag == 0:
                print("Exit Denied")
                cv2.destroyAllWindows()
            else:
                print("Please Exit")
                cursor.execute("UPDATE ID set Presence=0 where USN = ?", (USN,))
                conn.commit()
                time.sleep(5)

        cursor.close()
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break


conn.close()
