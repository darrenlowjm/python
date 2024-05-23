#from package_testing import inner


if 0:
    #__init__.py in package_testing root folder
    # from .inner import inner_fn
    # from .inner_folder import inner_2_fn


    # this is ok
    import package_testing
    package_testing.inner_fn()
    package_testing.inner_2_fn()
    
if 0:
    from package_testing import *
    inner_fn()
    inner_2_fn()
