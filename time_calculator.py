import re
HOUR = 60
HALF_DAY = HOUR * 12
DAY = HOUR * 24
WEEK_DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def classify_day(day):
  for i, d in enumerate(WEEK_DAYS):
    if d.lower() == day.lower():
      return i

def add_time(start, duration, day = ""):
  nums = re.findall(r'[0-9]+', start)
  amORpm = re.findall(r'[A-Z]+', start)[0]
  minutes = int(nums[0]) * HOUR + int(nums[1])
  if amORpm == "PM":
    minutes = minutes + HALF_DAY
  
  numsD = re.findall(r'[0-9]+', duration)
  minutesD = int(numsD[0]) * HOUR + int(numsD[1])

  minutesT = minutes + minutesD
  days = minutesT // DAY
  if(days == 0):
    daysLater = ""
  elif(days == 1):
    daysLater = " (next day)"
  else:
    daysLater= " ("+str(days)+" days later)"
  
  if(day != ""):
    dayI = classify_day(day)
    dayN = (dayI + days) % len(WEEK_DAYS)
    dayN = ", " + WEEK_DAYS[dayN]
  else:
    dayN = ""

  minutesN = minutesT % DAY
  if minutesN >= HALF_DAY:
    minutesN -= HALF_DAY
    amORpm = "PM"
  else:
    amORpm = "AM"

  hoursR = minutesN // HOUR
  minutesR = int(minutesN % HOUR)
  if(hoursR == 0):
    hoursR = 12

  hoursR = str(hoursR)

  if(minutesR < 10):
    minutesR = "0" + str(minutesR)
  else:
    minutesR = str(minutesR)

  timeN = hoursR + ":" + minutesR
  result = timeN + " " + amORpm + dayN + daysLater
  return result