'''
Copyright (C) 2014 Jacques Lucke
mail@jlucke.com

Created by Jacques Lucke

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import bpy

def getSelectedObjects():
	return bpy.context.selected_objects
	
def newGroup(name):
	return bpy.data.groups.new(name)
	
def hasPrefix(name, prefix):
	return name[:len(prefix)] == prefix
	
def getActive():
	return bpy.context.scene.objects.active
	
def getGroupsWithPrefix(object, prefix):
	groups = []
	for group in object.users_group:
		if hasPrefix(group.name, prefix): groups.append(group)
	return groups