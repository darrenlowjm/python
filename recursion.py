tests = \
[
    ['test-block', 'Single_PSU', '$Single_PSU$',
        ['var-set', 'Health_State', 'Degraded'],
        ['var-set', 'Health_Component', 'Power Supply'],
        ['var-set', 'Health_Reason', '=None'],
    ],
    ['test-block', 'Double_PSU', '$Double_PSU$',
        ['var-set', 'Health_State', 'OK'],
        ['var-set', 'Health_Component', '=None'],
        ['var-set', 'Health_Reason', '=None'],
    ],
    ['test-block', 'Check_Health', '$Check_Health$',
        ['print', 'Checking system health'],
        ['assert-system-health', '$Health_State$', '$Health_Component$', '$Health_Reason$']
    ]
]

def search_tests_list(tests_list):
    found_opcodes = set()
    for item in tests_list:
        if item[0] == 'test-block':
            found_opcodes.add('test-block')
            for opcode in item:
                if isinstance(opcode, list):
                    found_opcodes.add(opcode[0])
                    
    print(found_opcodes)


search_tests_list(tests)