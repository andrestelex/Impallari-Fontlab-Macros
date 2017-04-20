#FLM: Center of Italic Glyph

# Description:
# Place a guideline in the center of the selected glyph
# Italic Version

# Credits:
# Pablo Impallari
# http://www.impallari.com
# Update: automatically get xHeight/2 and calculate shift

shift=0
from FL import *
import math

# Get current Glyphs
f = fl.font
g = fl.glyph

def rectCateto(angle, cat):
	angle = math.radians(angle)
	result = cat * (math.tan(angle))
	#result = round(result)
	return result

def getShift(angle):
	h = f.x_height[0]/2
	shift = rectCateto(angle, h)
	return shift

# Find Angle
angle = f.italic_angle
shift = -getShift(angle)

if angle <= -1 :
	angle = angle * -1


	
#Hardcoded Angle and Shift
#angle = 11.25
#shift = 45

# Clear Local Guidelines
gvguides = g.vguides
gvguides.clean()

# Find the center of the glyph
centro = g.width / 2

# Place Guideline
g.vguides.append(Guide(0-shift, angle))
g.vguides.append(Guide(centro-shift, angle))
g.vguides.append(Guide(g.width-shift, angle))
	
# Update font
fl.UpdateGlyph()


