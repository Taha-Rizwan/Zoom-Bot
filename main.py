import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime

def sign_in(meetingid, pswd):
  subprocess.call('C:/Users/hp/AppData/Roaming/Zoom/bin/Zoom.exe')
  
  time.sleep(20)

  join = pyautogui.locateCenterOnScreen('join.png')
  pyautogui.moveTo(join)
  pyautogui.click()
  time.sleep(10)
  # meeting_id_btn = pyautogui.locateCenterOnScreen('idman.png')
  # pyautogui.moveTo(meeting_id_btn)
  # pyautogui.click()
  pyautogui.write(meetingid)

  join_btn = pyautogui.locateCenterOnScreen('jointheting.png')
  pyautogui.moveTo(join_btn)
  pyautogui.click()
  time.sleep(10)

  pyautogui.write(pswd)
  join_meeting = pyautogui.locateCenterOnScreen('joinmeeting.png')
  pyautogui.click()
 
df = pd.read_csv('timings.csv')
while True: 
  now = datetime.now().strftime("%H:%M")
  if now in str(df['timings']):

    row = df.loc[df['timings'] == now]
    m_id = str(row.iloc[0,1])
    m_pswd = str(row.iloc[0,2])

    sign_in(m_id, m_pswd)
    time.sleep(40)
    print('signed in')