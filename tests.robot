*** Settings ***
| Library | Process

*** Test Cases ***
Addition
| | ${result}= | run process | python3 | calc.py | + | 2 | 2
  Log to console  2 + 2
  Should Be Equal As Strings  ${result.stdout}  4.0000000000

Subtraction
| | ${result}= | run process | python3 | calc.py | - | 10.5123213 | 6.5123213
  Log to console  10.5123213 - 6.5123213
  Should Be Equal As Strings  ${result.stdout}  4.0000000000

Multiplication
| | ${result}= | run process | python3 | calc.py | * | 1.00000 | 4.00000
  Log to console  1.00000 * 4.00000
  Should Be Equal As Strings  ${result.stdout}  4.0000000000  

Division
| | ${result}= | run process | python3 | calc.py | / | 8.8888 | 2
  Log to console  8.8888 / 2
  Should Be Equal As Strings  ${result.stdout}  4.4444000000

Division by zero
| | ${result}= | run process | python3 | calc.py | / | 4.44444 | 0
  Log to console  4.44444 / 0
  Should Be Equal As Strings  ${result.stdout}  Деление на ноль!  