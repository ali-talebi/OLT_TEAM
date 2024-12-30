"""
    Author : Amin Amani -Ali Talebi 
    
    Description : Connect to Test Link And Returned Total Test Case 
     
    Steps : 
    
        0 - install requirements : 
        
            setuptools                 66.1.1
            TestLink-API-Python-client 0.8.1
            wheel                      0.38.4
            
           
        1 - export  TESTLINK_API_PYTHON_SERVER_URL TESTLINK_API_PYTHON_DEVKEY 
        
            export TESTLINK_API_PYTHON_SERVER_URL=http://195.201.231.223:8080/lib/api/xmlrpc/v1/xmlrpc.php
            export TESTLINK_API_PYTHON_DEVKEY=2a40335f269615f7ebcef5af20141167

        2 - python Geter_TestCase.py -h show args for this file 
        
            positional arguments:
            server_api     server api url
            devk           key of user
            project        name of project
            TestPlaName    name of Test Plan
            TestSuiteName  Test Suite Name

            options:
            -h, --help     show this help message and exit
        
        3 - python Geter_TestCase.py http://195.201.231.223:8080/lib/api/xmlrpc/v1/xmlrpc.php 2a40335f269615f7ebcef5af20141167 OLT_SINA_Comp Sina_COM_TESTPLAN test_suite_1_olt_sin_com

        4 - Return Data IS a List of Dictionary  : 
        
            [{'id': '110', 'parent_id': '109', 'node_type_id': '3', 'node_order': '1000', 'node_table': 'testcases', 'name': 'TEST_FUNCTION_hello', 'external_id': 'olt_sina-1'}, {'id': '112', 'parent_id': '109', 'node_type_id': '3', 'node_order': '1001', 'node_table': 'testcases', 'name': 'TEST_FUNCTION_Bridge', 'external_id': 'olt_sina-2'}]


"""

import testlink
import argparse

def Total_Test_Case(project_name , test_plan_name , test_suite_name ) : 
    total_test_case_found = []
    total_project = client.getProjects()
    for iter_project in total_project : 
        if iter_project['name'] == project_name : 
            # print("Project : " , iter_project )
            total_test_plan = client.getProjectTestPlans(iter_project['id'])
            for iter_plan in total_test_plan : 
                if iter_plan['name'] == test_plan_name :
                    # print("Test Plan : " ,  iter_plan )
                    total_test_suite = client.getTestSuitesForTestPlan(iter_plan['id'])
                    # print("Total_Test Suite : " ,total_test_suite  )
                    for iter_test_suite in total_test_suite : 
                        # print("iter Test Suite ")
                        # print(iter_test_suite)
                        # print("iter_test_suite name " , iter_test_suite['name'])
                        total_test_cases = client.getTestCasesForTestSuite(testsuiteid = iter_test_suite['id'])
                        #print("Total Test Case " , total_test_cases )
                        for a in total_test_cases : 
                            print(a['name'])
                            total_test_case_found.append(a)
                            
                            
    return total_test_case_found 
                        

                            
                            
try :      
    
    parser = argparse.ArgumentParser()
    parser.add_argument('server_api' , help = 'server api url ')
    parser.add_argument('devk' , help = 'key of user')
    parser.add_argument('project' , help='name of project ' )
    parser.add_argument('TestPlaName' , help='name of Test Plan' )
    parser.add_argument('TestSuiteName' , help='Test Suite Name ')
    args = parser.parse_args()             
    if args :
        print(" ---- ** Total Test Case ** ---- ")
        TESTLINK_API_PYTHON_SERVER_URL=args.server_api
        TESTLINK_API_PYTHON_DEVKEY= args.devk  ## admin 
        client = testlink.TestLinkHelper().connect(testlink.TestlinkAPIClient)
        total_test_case = Total_Test_Case( args.project , args.TestPlaName , args.TestSuiteName ) 
        
        
except Exception as e : 
    print(e)
    
    
