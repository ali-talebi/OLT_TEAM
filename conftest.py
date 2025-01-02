




def pytest_addoption(parser) : 
	name = parser.addoption("--name" , default = "ali talebi" , action = 'store' , help = 'give name' ) 


