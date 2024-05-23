import re

def performInterpolation(cfg, originalStep, lineNum):
    '''Compute expressions embedded in test steps.'''

    '''In computer programming, string interpolation (or variable interpolation,
       variable substitution, or variable expansion) is the process of
       evaluating a string literal containing one or more placeholders,
       yielding a result in which the placeholders are replaced with their
       corresponding values.'''

    step = []
    unknownSignature = '?unknownVariableName?'
    anyInterpolationDone = False
    re_pattern = r'\$\w+\$'
    for originalArgument in originalStep:

        # If there are no '$variableName$' variables needing interpolation,
        # then just append the original argument to the test step and get next:

        argument = str(originalArgument)
        if argument.count('$') < 2:
            step.append(originalArgument)
            continue
        cfg.Log(argument)
        # Process expressions contained in test step argument(s):
        # First: Do variable substitution using dollar sign delimiters:
        
        ##if '(' in argument: #($Product_PODS$ && $Linear_Storage$
        ##    argument = argument.replace('(','')

        def evaluate_and_replace(matchobj):            
            anyInterpolationDone = True
            variableName = matchobj.group(0).replace('$', '')
            if variableName == 'loopCt':
                variableValue = cfg.LoopCt
            else:
                variableValue = cfg.varData.get(variableName, unknownSignature)
                if variableValue == unknownSignature: # Unknown variable name is being referenced!
                    cfg.Log('ERROR: Script step: {}, line {}: Unknown data variable "{}" referenced in test step expression: "{}"?'.format(stepCount, lineNum, variableName, originalArgument))
                    cfg.Log(argument)
                    LogOpcodeTime(cfg.opcodeTiming, step+[unknownSignature], time.time())
                    #return errorInfo.ERR_FAILED_VARIABLE_INTERPOLATION
                    
            cfg.Log(argument)
            return variableValue
            
        argument = re.sub(pattern, evaluate_and_replace, argument)
        if unknownSignature in argument:
            return errorInfo.ERR_FAILED_VARIABLE_INTERPOLATION
                  
        if argument.startswith('not ') or (' and ' in argument) or (' or ' in argument):
            computedValue = eval(argument)
            argument = str(computedValue)
 
        # Variable value insertion using equal sign to delimit the value:







        if '=' in argument:
            computedValue = 0 # Shuts off a pylint warning because dynamically created.
            anyInterpolationDone = True
            expression = 'computedValue = {}'.format(argument.split('=')[1])
            try: exec (expression)
            except Exception:
                cfg.Log('ERROR: Script step: {}, line {}: Original source:   "{}"'.format(stepCount, lineNum, originalStep))
                cfg.Log('ERROR: Script step: {}, line {}: Original argument: "{}"'.format(stepCount, lineNum, originalArgument))
                cfg.Log('ERROR: Script step: {}, line {}: Exception trying to compute expression: "{}"'.format(stepCount, lineNum, expression))
                raise
            if argument[0] == '=': argument = computedValue
            else:                  argument = argument.split('=')[0] + '=' + str(computedValue)

        cfg.Log('Computed: {} ==> {}'.format(originalArgument, argument)) # Debug printing.
        step.append(argument) # Append interpolated argument.
    if anyInterpolationDone:
        cfg.Log('Interpolated Test Step and Argument(s): {}'.format(step))
    return step