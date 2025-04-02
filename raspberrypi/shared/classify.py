bean_classification1 = 'dark-purple'
bean_classification2 = 'white'

if bean_classification1 == 'dark-purple' and not bean_classification2 in ('dark-purple', 'white'):
    if bean_classification2 == 'white':
        print('Trinotario')
elif bean_classification2 == 'white':
    print('criollo')
elif bean_classification2 == 'dark-purple':
    print('Forastero')
else:
    print('Unknown cacao been.')