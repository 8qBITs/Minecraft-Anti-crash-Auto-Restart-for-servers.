#!/bin/bash
 
JarFile = forge.jar
MaxMem = 12G

while true
do
   java -jar -Xms$MaxMem -Xmx$MaxMem -XX:+UseG1GC -XX:+UnlockExperimentalVMOptions -XX:MaxGCPauseMillis=100 -XX:+DisableExplicitGC -XX:TargetSurvivorRatio=90 -XX:G1NewSizePercent=50 -XX:G1MaxNewSizePercent=80 -XX:G1MixedGCLiveThresholdPercent=50 -XX:+AlwaysPreTouch $JarFile nogui
    echo "If you want to completely stop the server process now, press Ctrl+C before the time is up!"
    echo "CRASH Detected, Rebooting in:"
    for i in 5 4 3 2 1
    do
        echo "$i..."
        sleep 1
    done
    echo "Rebooting now!"
done