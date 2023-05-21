def SET_BIT(REG,BIT):
	Reg = int(REG)
	Bit = int(BIT)
	Reg |= (1<<Bit)
	return Reg
	
def CLR_BIT(REG,BIT):
	Reg = int(REG)
	Bit = int(BIT)
	Reg &= ~(1<<Bit)
	
def GET_BIT(REG,BIT):
	Reg = int(REG)
	Bit = int(BIT)	
	return Reg
	
def TOGGLE_BIT(REG,BIT):
	Reg = int(REG)
	Bit = int(BIT)
	Reg ^= (1<<Bit)
	return Reg

x = (TOGGLE_BIT(6,3))
print(bin(x))
print("New Num = ",x)