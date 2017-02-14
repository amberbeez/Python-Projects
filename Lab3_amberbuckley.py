
_author_ = "amber buckley"

# description: write a program to calculate blue/green deploy time to production environments with count of applications
# declare real Web1 time
# declare real Web2 time
# declare real green deployTime
# declare real blue deployTime
# declare real total deployTime
# declare real Applications deployed

# module_main()
# declare variables
#   call lon_greenDeployTime
#   call lon_blueDeployTime
#   set lon_totalDeployTime = lon_greenDeployTime + lon_blueDeployTime
#   get number of applications deployed to LON
#   if lon_greenDeployTime > lon_blueDeployTime then
#       display "lon web1 took longer than web2 today"
#   if lon_greenDeployTime < lon_blueDeployTime then
#       display "Web1 was faster than Web2 today"
#   if lon_greenDeployTime == lon_blueDeploy time then
#       display "Each web server took the same amount of time today"
# display "Total DeployTime"
#   if totalDeployTime > 4 hours then
#       display "That was a long release today, let's look at why."
#           else: lon_totalDeployTime < 3 hours then
#       display "nicely done!"
# display "today's deploy total time with number of applications."
# end module

Web1Time = 0.0
Web2Time = 0.0
lon_greenDeployTime = 0.0
lon_blueDeployTime = 0.0
lon_totalDeployTime = 0.0
applications_deployed = 0.0

def lon_releaseTime():
    Web1Time = lon_greenDeployTime()
    Web2Time = lon_blueDeployTime()
    lon_totalDeployTime = Web1Time + Web2Time
    applications_deployed = float(input("How many applications were deployed today?"))
    if Web1Time > Web2Time:
        print("Web1 took longer today than lon Web2, I wonder why?")
    elif Web1Time < Web2Time:
        print("Lon Web1 was faster than Web 2 today.")
    else:
        Web2Time == Web1Time
        print(" Each web server took the same amount of time today.")
    print("LON release time was", lon_totalDeployTime, "hours.")
    if lon_totalDeployTime > 4:
        print("That was a long release today while deploying,", applications_deployed, "applications, let's find out why.")
    else:
        print("The total deploy time for LON was", lon_totalDeployTime , "hours, with", applications_deployed,
          "applications released to LON. Nice job Team!")



# get Web1 deploy time
def lon_greenDeployTime():
    lon_greenDeploytime = 0.0
    lon_greenDeployTime = float(input("How long did it take to deploy to LON Web 1 today?"))
    print("It took ", lon_greenDeployTime, "hours to deploy to LON Web1")
    return lon_greenDeployTime

# get Web2 deploy time
def lon_blueDeployTime():
    lon_blueDeploytime = 0.0
    lon_blueDeployTime = float(input("How long did it take to deploy to LON Web 2 today?"))
    print("It took ", lon_blueDeployTime , "hours to deploy to LON Web2")
    return lon_blueDeployTime

lon_releaseTime()

