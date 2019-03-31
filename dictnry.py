

def dWrite(key, value):
	with open(__file__, 'r+') as f:
	    lines = f.read().split('\n')
	    
	    new_line =  "\nType[\"{}\"] =  \"{}\"".format(key, value)
	    f.write(new_line)






Type = {
"20 20 X 4" : "Angles", # inconsistency in data base with X and x 
"40 40 x 6" : "Angles",
"45 45 x 6" : "Angles",
"50 50 x 7" : "Angles",
"50 50 x 8" : "Angles",
"55 55 x 4" : "Angles",
"JB 200" : "Beams",
"LB 200" : "Beams",
"LB 225" : "Beams",
"LB 600" : "Beams",
"LB(P) 175" : "Beams",
"LB(P) 200" : "Beams",
"MB 200" : "Beams",
"MB 500" : "Beams",
"NPB 180x90x18.8" : "Beams",
"MC 350" : "Channels",
"MC 400" : "Channels",
"MCP 175" : "Channels",
"MCP 350" : "Channels",
"MCP 400" : "Channels",
"MCP 75" : "Channels"
}
