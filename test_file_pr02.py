import pytest 

class C():
	
	def f(self) : 
		return 1 

	def g(self) : 
		return 2 

@pytest.fixture(scope = "function" ) 
def my_fixure() : 

	isntance = C()
	return isntance 


def test_fun_f(my_fixure) : 
	
	assert my_fixure.f() == 1 

def test_fun_g(my_fixure) : 
	
	assert my_fixure.g() == 2 


print("-------------------------------------------------------------------------------")

@pytest.fixture(scope = 'function' ) 
def setup_teardown() : 
	print("In Fixture before yield" ) 
	yield 

	print("In Fixture after yield")

def test_fun_hello(setup_teardown) : 
	print("****")
	


@pytest.fixture(scope = "function")
def setup_f():
	print("Hello I am Start  Fixture F ")
	print("Hello I am End of Fixture F ")



def test_fun_p(setup_f) : 
	print(" I am Test Function P ")

print("-------------------------------------------------------------------------------")




@pytest.fixture(scope = 'function')
def olt_fixure() : 
	print("I am fixture olt ")

@pytest.mark.q
def test_fun_q(request , olt_fixure) : 
	name = request.config.getoption("--name")
	print(f"I am test in test Q , name recived {name}")


print("-------------------------------------------------------------------------------")











