_author_ = "amber buckley"

# description: write a program to calculate blue/green deploy time to production environments with count of applications
#
# declare real green deployTime
# declare real blue deployTime
# declare real total deployTime
# declare real Applications deployed

# module_main()
# declare variables
#   call lon_greenDeployTime()
#   call lon_blueDeployTime)
#   set lon_totalDeployTime = lon_greenDeployTime + lon_blueDeployTime
#   if lon_greenDeployTime < lon_blueDeployTime then
#       display "lon web1 was faster today!"
#   else:
#       display "lon web2 was faster today!"
#
#   elif lon_totalDeployTime < 3 hours then
#       display "nicely done!"
#   elif lon_totalDeloyTime > 3 hours then
#       display "That was a long deploy today!"
# display "today's deploy time was" lon_deploy_time
# end module

lon_greenDeployTime = 0.0
lon_blueDeployTime = 0.0
lon_totalDeployTime = 0.0
applications_deployed = 0.0

def lon_releaseTime():
    lon_greenDeployTime()
    lon_blueDeployTime()
    lon_totalDeployTime = lon_blueDeployTime + lon_greenDeployTime
#    applications_deployed = float(input("How many applications were deployed today?"))
    if lon_blueDeployTime > lon_greenDeployTime:
        print("Web2 took longer today than lon Web1, I wonder why?")
    elif lon_blueDeployTime < lon_greenDeployTime:
        print("Lon Web1 was faster than Web 2 today.")
    else:
        lon_greenDeployTime == lon_blueDeployTime
        print(" Each web server took the same amount of time today.")
print("The total deploy time to LON today was", lon_totalDeployTime + "with", applications_deployed, "released to LON")
lon_releaseTime()

def lon_greenDeployTime():
    lon_greenDeployTime = float(input("How long did it take to deploy to LON Web 1 today?"))
    print("It took ", lon_greenDeployTime + "to deploy to LON Web1")
    return lon_greenDeployTime

def lon_blueDeployTime():
    lon_blueDeployTime = float(input("How long did it take to deploy to LON Web 2 today?"))
    print("It took ", lon_blueDeployTime + "to deploy to LON Web2")
    return lon_blueDeployTime

lon_releaseTime()

#def applicationsDeployed():
#    applications_deployed = float(input("How many applications were released today?"))
#    print("There were", applications_deployed + "to production today.")
 #   return applications_deployed
