# sets translate and rotate fields of rig controllers to zero
# usage: 
#   using the script with any number of objects selected will reset their translate and rotate values to zero
#   if nothing is selected, it will reset the values of all objects with '_CTRL' in their name
# WARNING: this should work on any object, so if used on an object whose transforms have not or cannot be set to zero, it will move them from their default position!

import maya.cmds as cmds

# create a list of all selected
controllerList = cmds.ls(selection = True) 


if len(controllerList) > 0:
    pass
    #print(controllerList)
else:
    controllerList = cmds.ls('*_CTRL')
    #print(controllerList)
#print(cmds.getAttr('R_Leg_CTRL.translateX'))
for i in controllerList:
    tx = i + '.translateX'
    ty = i + '.translateY'
    tz = i + '.translateZ'
    rx = i + '.rotateX'
    ry = i + '.rotateY'
    rz = i + '.rotateZ'
    cmds.setAttr(tx, 0)
    cmds.setAttr(ty, 0)
    cmds.setAttr(tz, 0)
    cmds.setAttr(rx, 0)
    cmds.setAttr(ry, 0)
    cmds.setAttr(rz, 0)
    print(i + ' ' + str(cmds.getAttr(attr)))