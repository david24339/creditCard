Python 3.10.6 (v3.10.6:9c7b4bd164, Aug  1 2022, 17:13:48) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

============ RESTART: /Users/davidkabeya/Documents/Project credit.py ===========
------------------------------------
Welcome to the credit card checker
------------------------------------

Please input your credit card number:4003600000000014
Traceback (most recent call last):
  File "/Users/davidkabeya/Documents/Project credit.py", line 32, in <module>
    main()
  File "/Users/davidkabeya/Documents/Project credit.py", line 7, in main
    result=checkcard(cardNumber)
NameError: name 'checkcard' is not defined. Did you mean: 'checkCard'?

============ RESTART: /Users/davidkabeya/Documents/Project credit.py ===========
------------------------------------
Welcome to the credit card checker
------------------------------------

Please input your credit card number:4003600000000014
Traceback (most recent call last):
  File "/Users/davidkabeya/Documents/Project credit.py", line 32, in <module>
    main()
  File "/Users/davidkabeya/Documents/Project credit.py", line 7, in main
    result=checkCard(cardNumber)
UnboundLocalError: local variable 'checkCard' referenced before assignment

============ RESTART: /Users/davidkabeya/Documents/Project credit.py ===========
------------------------------------
Welcome to the credit card checker
------------------------------------

Please input your credit card number:4003600000000014
Traceback (most recent call last):
  File "/Users/davidkabeya/Documents/Project credit.py", line 33, in <module>
    main()
  File "/Users/davidkabeya/Documents/Project credit.py", line 27, in main
    result=checkCard(cardNumber)
  File "/Users/davidkabeya/Documents/Project credit.py", line 8, in checkCard
    for i in multipy2:
NameError: name 'multipy2' is not defined. Did you mean: 'multiply2'?

============ RESTART: /Users/davidkabeya/Documents/Project credit.py ===========
------------------------------------
Welcome to the credit card checker
------------------------------------

Please input your credit card number:4003600000000014
Traceback (most recent call last):
  File "/Users/davidkabeya/Documents/Project credit.py", line 33, in <module>
    main()
  File "/Users/davidkabeya/Documents/Project credit.py", line 27, in main
    result=checkCard(cardNumber)
  File "/Users/davidkabeya/Documents/Project credit.py", line 14, in checkCard
    counter3 += 2
UnboundLocalError: local variable 'counter3' referenced before assignment
