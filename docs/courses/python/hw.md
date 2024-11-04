<link rel="stylesheet" href="../../../css/counter.css" />

# Python Basics: PTA Problems

!!! info "PTA Problems of ZJU *Python Programming*, 2024 Spring & Summer."

## 基础知识

### 判断题

**Q1-1-7.** 在 Python 中，可以用 else 作为变量名。

??? general "Answer"
	F。Python 的保留字不能作为变量名，else 是保留字。通过如下方法可以看到所有 Python 的保留字：
    ```shell
    >>> import keyword
    >>> keyword.kwlist
    ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
    ```

**Q1-1-11.** 下面程序的输出是 5。
```python
print=3
print(5)
```

??? general "Answer"
    F。`print` 是 Python 的内置函数，但是在这里被赋值为 3，因此将被作为一个整数变量看待，而不是函数。
    
    因此会报错 `TypeError: 'int' object is not callable`。

**Q2-1-1.** 当输入是 `45,8` 时，下面程序的输出结果是 37。

```python
a, b = input().split(',')
b = int(b)
c = int('a', b)
print(c)
```

??? general "Answer"
    F。报错 `ValueError: invalid literal for int() with base 8: 'a'`，因为 'a' 在八进制下是没有意义的。
    
    需要了解 `int(value, base)` 函数中 `value` 和 `base` 的意义（见 [Review - int](review.md#int)），以及区分 `a` 和 `'a'` 的区别。

**Q2-1-2.** 表达式 `-2**2` 等于 4。

??? general "Answer"
    F。`**` 优先级高于 `-`。

**Q3-1-3.** 希望输入正整数 6 和 5，求和 6+66+666+6666+66666，下面程序正确吗？

```python
a=int(input())    
n=int(input())    
print(sum([int('a'*i) for i in range(1,n+1)]))
```

??? general "Answer"
    F。再次注意，'a' 是一个字符常量，而 a 是一个变量。a 和 'a' 一般没有关联。

**Q3-1-4.** 当输入是 10.0 时，下面程序的输出是 `f(10.0) = 0.1`。

```python
x=int(input())
if x==0:
    result=0
else:
    result=1/x
print('f({0:.1f}) = {1:.1f}'.format(x,result))
```

??? general "Answer"
    F。`x=int(input())` 会报错 `ValueError: invalid literal for int() with base 10: '10.0'`。

    注意 int 函数只能将字符串按整数进行解释，如果无法解释，将会报错。

**Q5-1-1-6.** 已知 x=3, 则执行 `x=7` 后，`id(x)` 的返回值与原来没有变化。

??? general "Answer"
    F。`id` 函数返回对象的内存地址，x=7 与原来的 x=3 不是同一个对象了，内存地址会发生变化。

**Q5-1-1-7.** `int("92",8)` 的值是 74。

??? general "Answer"
    F。根据 `int(value, base)` 函数中 `value` 和 `base` 的意义（见 [Review - int](review.md#int)），会把 "92" 试图按照八进制进行解释，但是 '9' 不是八进制的数字，因此会报错 `ValueError: invalid literal for int() with base 8: '92'`。

**Q6-1-16.** 表达式：`"34" in "1234"==True` 返回值是 `True`。

??? general "Answer"
    F。用到了比较运算符的链接。
    ```
    "34" in "1234"==True
    = "34" in "1234" and "1234"==True
    = True and False
    = False
    ```

**Q7-2-4.** `2 == 2.0` 的结果是 False。

??? general "Answer"
    F。比较作为 int 的 2 和 float 的 2.0 时，2 会先被转换为 float 2.0，然后进行比较，即
    ```python
    2 == 2.0 -> 2.0 == 2.0 -> True
    ```

    关于这种混合数值类型计算时的类型转换规则，可以参照 [Review - 数值类型混合运算](review.md#complex)。

**Q15-1-10.** 变量不需事先声明就可使用。

??? general "Answer"
    T。Python 是一种动态类型语言，变量的类型是在运行时确定的，不需要事先声明。

### 选择题（不一定单选）

**Q1-2-12.** 下面程序的输出是什么？

```python
a, b = 5, 9
print(a, b)
```

A. `59`

B. `5,9`

C. `5 9`（5 和 9 之间 1 个空格）

D. `5  9`（5 和 9 之间 2 个空格）

??? general "Answer"
    C。print 的 sep 参数默认为 `" "`。

**Q2-2-10.** 指出错误的说法。

A. 表示复数的语法是 real + imag j

B. 实部和虚部都是 int

C. 虚部必须后缀 j, 且必须是小写

D. 方法 conjugate 返回复数的共轭复数

??? general "Answer"
    BC。实部和虚部都是 float，虚部后缀可以是 j 或者 J。

**Q5-1-3-1:2:3:4.** 以下是合法标识符的是

A. `true`

B. `print`

C. `2age`

D. `_age`

??? general "Answer"
    ABD。
    
    A，Python 中的标识符是区分大小写的，`True` 是保留字，但 `true` 不是保留字，是合法标识符。
    
    B，`print` 是内置函数名，不是保留字，是合法标识符。

    C，标识符不能以数字开头。

    D，下划线开头的标识符是合法的。

    标识符由字母、数字、下划线组成，但不能以数字开头。

**Q15-2-1.** 下面哪些不是 Python 可以接受的变量名？

A. `abc`

B. `_23ac`

C. `23_ac`

D. `good-name`

??? general "Answer"
    CD。Python 变量名可以由字母、数字、下划线组成，但不能以数字开头。

**Q15-2-8.** 下面语句解释器将抛出什么错误信息？

```python
s = [1,2,3]
y = s[3]
```

A. NameError

B. IndexError

C. SyntaxError

D. TypeError

??? general "Answer"
    B。列表越界错误。

### 填空题

**Q2-1-3:4:5.** 计算以下表达式。

```
int(True)
bool([])
bin(12.5)
```

??? general "Answer"
    ```
    1
    False
    TypeError: 'float' object cannot be interpreted as an integer
    ```
    对于第一行，True 是 bool 类型，是 int 的 子类型，对应 int 的 1。

    对于第二行，空列表转 bool 为 False，非空列表转 bool 为 True。特别地，bool([[]]) 也为 True。

    对于第三行，`bin`, `oct`, `hex` 都要求输入为 int，详见 [Review - int](review.md#int)。

**Q2-2-7:11.** 给出以下程序的输出结果。

```python
print(chr(65))
print(ord('A'))
x = 'dog'
y = 6
print(x + y)
```

??? general "Answer"
    先输出 A 和 65。chr 将 ascii 码转化为字符，ord 把字符转化为 ascii 码。

    后报错 `TypeError: can only concatenate str (not "int") to str`。int 和 str 不能直接相加。

    特别地，如果 `print(x * y)`，将会输出 `dogdogdogdogdogdog`，即字符串乘法的结果。

**Q2-4-1:2:5:15.** 计算以下四行的输出。

```python
print(8 + 8//3 - True + False)
print(3**2**3)
print(int("20", 16), int("101",2))
print(--3)
```

??? general "Answer"
    ```
    9
    6561
    32 5
    3
    ```
    对于第一行，有
    ```
    8 + 8//3 - True + False = 8 + 2 - 1 + 0 = 9
    ```
    对于第二行，有
    ```
    3**2**3 = 3**8 = 6561
    ```
    对于第三行，按 16 进制和 2 进制解释字符串即可。

    对于第四行，两个负号相互抵消了效果，所以又回到了原始的 3。

    关于运算符优先级和结合性的内容可以去 [Review - 运算符优先级与结合性](review.md#precedence)查漏补缺。

**Q3-2-6:8:9.** 给出以下程序的输出结果

```python
print(0xA + 0xB)
print(1 + 2*3.14>0)
from math import sqrt
print(sqrt(4) * sqrt(9))
```

??? general "Answer"
    ```
    21
    True
    6.0
    ```
    对于第一行，`0xA` 和 `0xB` 分别是 10 和 11 的十六进制表示，相加为 21。

    对于第二行，先计算出大于号左侧为 7.42，然后和 0 比较，返回 True。注意运算顺序上大于号最后计算，最终返回值为 bool 类型。

    对于输出的第三行，`math` 库中的 `sqrt` 函数的返回值为 float 类型，两个 float 相乘还是 float，因此按照 float 输出为 6.0。

**Q3-4-4:7:12:17.** 给出以下程序的输出结果

```python
print(0 and 1 or not 2<True)
a, b, c, d = 3, 5, 6, True
print(not d or a>=0 and a+c>b+3)
print("Python" 'beginner')
print(43.5//2 - 20//4)
```

??? general "Answer"
    ```
    True
    True
    Pythonbeginner
    16.0
    ```
    关于运算符优先级和结合性的内容可以去 [Review - 运算符优先级与结合性](review.md#precedence)查漏补缺。

    对于第一行，计算顺序为
    ```python
    0 and 1 or not 2<True
    = 0 and 1 or not False
    = 0 and 1 or True
    = False or True
    = True
    ```

    对于第二行，计算顺序为
    ```python
    not d or a>=0 and a+c>b+3
    = not True or 3>=0 and 3+6>5+3
    = not True or True and True
    = False or True and True
    = False or True
    = True
    ```

    对于第三行，字符串拼接可以直接写在一起，不需要额外的 `+`；由于是拼接而不是作为两个参数输入 print，中间就没有空格。

    对于第四行，`20//4` 的结果是 int 5，但是 `43.5//2` 的结果是 float 21.0，所以最后结果为 float 类型。

**Q5-1-1-45.** 当输入为 `3 5` 时，分别给出如下两段程序的输出。

```python
m, n = int(input().split())
print(m+n)
```

```python
m, n = input().split()
print(m+n)
```

??? general "Answer"
    ```
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
    ```
    和
    ```
    35
    ```
    对于第一段程序，`int(input().split())` 会报错，因为 `int` 函数不能直接作用于 `input().split()` 所得到的字符串列表。

    对于第二段程序，`input().split()` 返回的是字符串列表 `['3', '5']`，所以 `m+n` 是字符串拼接，结果为 `35`。

**Q5-1-2-123.** 给出如下三段程序的输出（输入已经在注释中标出）：

```python
# 输入 123
a=input()
print(type(a))
```

```python
# 输入 123
a=int(input())
print(type(a))
```

```python
# 输入 12.3
a=int(input())
print(type(a))
```

??? general "Answer"
    ```
    <class 'str'>
    <class 'int'>
    ValueError: invalid literal for int() with base 10: '12.3'
    ```
    对于第一段程序，`input()` 返回的是字符串，所以 `type(a)` 是 `<class 'str'>`。

    对于第二段程序，`int(input())->int('123')->123` 返回 int 123，所以 `type(a)` 是 `<class 'int'>`。

    对于第三段程序，`int(input())=int('12.3')` 会报错，因为 `int` 函数不能直接作用于字符串 `'12.3'`。

**Q5-1-4-123.** 给出如下三段程序的输出：

```python
import math as m
print("{:08.2f}".format(m.pi))
```

```python
import math as m
print("{:.2f}".format(pi))
```

```python
from math import *
print("{:.2f}".format(math.pi))
```

??? general "Answer"
    ```
    00003.14
    NameError: name 'pi' is not defined
    NameError: name 'math' is not defined
    ```
    对于第一段程序，`m.pi` 是 `math` 库中的圆周率，`{:08.2f}` 表示总长度为 8，保留 2 位小数，不足的地方用 0 填充，所以输出为 `00003.14`。

    对于第二段程序，`pi` 没有被定义，会报错 `NameError: name 'pi' is not defined`。对于这种方式，需要 `from math import pi`。

    对于第三段程序，尽管 `from math import *` 导入了 `math` 库中的所有函数和常量，但没有导入 `math` 这一名字，因此使用 `math.pi` 会无法识别 `math`。

**Q5-2-2-123.** 给出以下程序的输出结果：

```python
print(type(1J))
print(type(1//2))
print(type(121 + 1.21))
```

??? general "Answer"
    ```
    <class 'complex'>
    <class 'int'>
    <class 'float'>
    ```
    对于第一行，`1J` 是复数（只有虚部的纯虚数），因此得到 complex。

    对于第二行，`1//2` 是两个 int 进行整除，所以还是返回 int。注意只要除数与被除数有一者是 float，结果就会变为 float。

    对于第三行，`121 + 1.21` 是 int 加 float，返回 float。只要有 float 参与运算，结果就会变为 float。

**Q5-2-5-1.** 以下程序的输出是？（字符 `a` 的 ASCII 码为 97）

```python
s = "abcdefg"
for i in s:
    if ord(i)%2:
        print(i,end='#')
```

??? general "Answer"
    `a#c#e#g#`。

    每隔两个字符输出一个字符，并且由于 print 的 end 从默认的 `'\n'` 改为了 `'#'`，每个字符后面都会跟着一个 #。

**Q5-4-1-1:2:3:6** 以下程序的输出是？

```python
print(True or False and False)
print(16-25>78/2 or "XYZ"!="xyz"and not (10-6>18/2))
print(((2>=2) or (2<2)) and 1<2>5)
print(False and 1 or not 2<False)
```

??? general "Answer"
    ```python
    True
    True
    False
    True
    ```
    对于第一行，有
    ```python
    True or False and False = True or False = True
    ```

    对于第二行，有
    ```python
    16-25>78/2 or "XYZ"!="xyz"and not (10-6>18/2)
    = -9>39 or "XYZ"!="xyz" and not 4>9
    = False or True and not False
    = False or True and True
    = Flase or True
    = True
    ```

    对于第三行，有
    ```python
    ((2>=2) or (2<2)) and 1<2>5
    = ((2>=2) or (2<2)) and (1<2 and 2>5)
    = (True or False) and (True and False)
    = True and False
    = False
    ```

    对于第四行，有
    ```python
    False and 1 or not 2<False
    = False and 1 or not False
    = False and 1 or True
    = False or True
    = True
    ```

**Q9-4-6:5.** 以下程序的输出是

```python
print(hex(16), bin(10))
print(int("20", 16), int("101",2))
```

??? general "Answer"
    ```
    0x10 0b1010
    32 5
    ```
    对于第一行，`hex` 和 `bin` 分别是将十进制 int 转化为十六进制和二进制表示的 str 的转换函数。

    对于第二行，按十六进制和二进制解释输入字符串，输出对应的十进制 int。

    可以参考 [Review - int](review.md#int)。

## 字符串

### 判断题

**Q6-1-5.** 可以通过 `[]` 来访问字符串的某个字符，也可以将它修改成其他字符。

??? general "Answer"
    F。可以通过下标访问，但是不能修改，因为字符串是不可变的。

**Q9-1-15.** 下面程序的输出结果为 `yes`。

```python
lst=["1","2","3","4","5"]
s1=""
for c in lst:
    s1=s1+c+" "
s2=" ".join(lst)
print("yes" if s1==s2 else "no")
```

??? general "Answer"
    F。
    
    `s1` 的每个数字后面都有一个空格，`s2` 仅在各数字之间存在空格，因此 `s1` 在末尾比 `s2` 多了一个空格，输出为 `no`。

    关于 join 可以回顾 [Review - join: split 的逆操作](review.md#join-split)。

**Q9-1-17\*.** `"12 "*3==" ".join([12, 12, 12])` 的输出是 `False`

??? general "Answer"
    F。`[12, 12, 12]` 是整数列表，输入给 `join` 会发生报错，无法得到正常输出。

    关于 join 可以回顾 [Review - join: split 的逆操作](review.md#join-split)。

### 选择题

**Q4-2-2.** 以下哪句打印出 `I\love\Python\test`？

A. `print("I\love\Python\test")`

B. `print("I\\love\\Python\\test")`

C. `print("I\"love\"Python\"txt")`

D. `print("I"\love"\Python"\txt")`

??? general "Answer"
    B。`\` 是转义字符，如果要输出 `\` 本身，需要使用 `\\`，所以 A 错 B 对。

    C 是转义输出 `"` 的方法，会输出 `I"love"Python.txt`。

    D 是错误的写法，会报错 `SyntaxError: unexpected character after line continuation character`。

**Q9-2-14.** 能打印输出 `I'm python.` 的语句是?

A. print('I'm python.')

B. print('I\'m python.')

C. print(r'I'm python.')

D. print('I"m python')

??? general "Answer"
    B。通过转义 `\` 使得 `'` 失去代码中划定字符串的功能，成为字符串的一部分被输出。

    A，三个 `'`，使得字符串字面量范围无法被清楚地划定，会报错。

    C，raw string 可以免于大部分特殊字符的转义 `\`，但在此处 `'` 是关键的划定字符串字面量范围的字符，因此在这里无法仅用 raw string 解决问题。

    D，会输出 `I"m python`，不符合要求。但是如果用 `print("I'm python")` 可以实现功能。

    关于 raw string 乃至字符串字面量的更多内容详见官方文档：[String and Bytes literals - Python 3.12.3 documentaion](https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals)

**Q4-2-12.** 下列说法错误的是：

A. 字符即长度为1的字符串

B. 字符串以\0标志字符串的结束

C. 既可以用单引号，也可以用双引号创建字符串

D. 在三引号字符串中可以包含换行回车等特殊字符

??? general "Answer"
    B。字符串以 `\0` 标志字符串的结束是 C 语言的特性，Python 中字符串以长度标志字符串的结束。

    三引号字符串是一种特殊的字符串，会保留其中字符串的格式，也就是会包含其中的换行、回车等特殊字符。

### 填空题

**Q3-1-1.** 以下程序的输出是：

```python
print("f-string{:5s}".format("123"))
print(f"format{'123':5s}")
print("percentage%5s"%("123"))
```

??? general "Answer"
    ```
    f-string123  
    format123  
    percentage  123
    ```
    f-string 和 format 输出字符串时，如果设定的宽度大于字符串的实际宽度，默认会在字符串右侧填充空格；而 % 这种格式化字符串，默认会在字符串左侧填充空格。详见 [Review - 格式化字符串](review.md#format-string)。

**Q4-4-1:8.** 下面程序的输出是：

```python
print('67'*3)
print("{:>08s}".format(bin(31)[2:]))
```

??? general "Answer"
    ```
    676767
    00011111
    ```
    对于第一行，字符串乘法 `'67'*3` 是将字符串 `'67'` 重复 3 次，即 `'676767'`。

    对于第二行，
    
    - `bin(31)` 是将 int 类型的 31 转换为其二进制表示的字符串 `'0b11111'`
    - `[2:]` 去掉了前缀 `0b`，得到字符串切片 `'11111'`
    - 然后 `{:>08s}` 控制格式为靠右对齐，总长度为 8，不足的地方用 `0` 填充（即在左侧填充），所以输出的字符串为 `'00011111'`

**Q5-2-1-2.** 下面程序的输出是：

```python
a = 1
b = 2
c = 3
a, b, c = c, a, b
print("{1:2d}{2:2d}{0:2d}".format(a, b, c))
```

??? general "Answer"
    ` 1 2 3`（1、2、3 前面都有 1 个空格）。经历 `a, b, c = c, a, b` 后，a=3, b=1, c=2；

    `"{1:2d}{2:2d}{0:2d}".format(a, b, c)` 表示输出的顺序为 b, c, a，且各自占 2 个字符的宽度，不足宽度的部分（默认）在左侧填充空格。

**Q6-1-15.** 给出以下程序的输出，输入为 ` c d e a`，每个字母前面都有一个空格，`a` 后面无空格。

```python
a = input().split(" ")
for i in a.sort():    
    print(i, end=" ")
```

??? general "Answer"
    ```
    TypeError: 'NoneType' object is not iterable
    ```
    `a.sort()` 是没有返回值的一个语句，因此 `for i in a.sort()` 是不合法的。`a.sort()` 会直接对 `a` 进行排序。

**Q6-1-15+.** 给出以下程序的输出，输入为 ` c d e a`，每个字母前面都有一个空格，`a` 后面无空格。

```python
a = input().split(" ")
a.sort()
for i in a:    
    print(i, end=" ")
```

??? general "Answer"
    ```
     a c d e 
    ```
    注意输出一共有 5 个空格，而且最后没有换行。
    
    `a = input().split()` 后，有 `a = ['', 'c', 'd', 'e', 'a']`。

    `a.sort()` 排序后，有 `a = ['', 'a', 'c', 'd', 'e']`。因此最后会得到这样的输出。

**Q6-4-2:9:12.** 给出以下程序的输出。

```python
print(len('3//11//2018'.split('/')))
print("programming".find("r",2))
print("aABC".isalpha())
s = "aabcab"
print(s.title())
print(s)
print(s.count('ab'))
```

??? general "Answer"
    ```python
    5
    4
    True
    Aabcab
    aabcab
    2
    ```
    对于第一行，`'3//11//2018'.split('/') = ['3', '', '11', '', '2018']`，列表长度为 5。

    对于第二行，找到第 2 个 "r" 的位置，即下标为 4。

    对于第三行，判断 "aABC" 是否每个字符都是英文字母，所以为 True。

    对于第四行和第五行输出，`s.title()` 是返回一个 s 中首字母变成大写之后的字符串，但并不改变 s 本身（字符串不可变）。

    对于第六行输出，统计 s 中子串 'ab' 的数量，那就是 2。

**Q9-2-30.** 输入：`12#11##10`，程序输出为？

```python
a=input().split('#')
print("{0:}:{2:}:{1:}".format(len(a), a[-1], a[0]))
```

??? general "Answer"
    ```python
    4:12:10
    ```
    输入后，得到的 `a=['12', '11', '', '10']`。从而有 `len(a)=4, a[-1]='10', a[0]='12'`。

    0, 2, 1 对应的分别为 `len(a), a[0], a[-1]`，因此最后结果为 `4:12:10`。

**Q9-4-13.** 以下程序的输出为

```python
a=34
b=23
print("{first}-{second}={0}".format(34-23,first=a,second=b))
```

??? general "Answer"
    ```
    34-23=11
    ```
    `"{first}-{second}={0}".format(34-23,first=a,second=b)` 中的 `0` 对应的是 `34-23`，`first` 对应的是 `a`，`second` 对应的是 `b`。注意这种 format 的用法比较少见但确实是合法的，可见 [Review - 格式化字符串](review.md#format-string)。

**Q15-2-10.** 下面代码的输出结果是

```python
a=666666
b="T"
print("{0:{2}^{1}}\n{0:{2}>{1}}\n{0:{2}<{1}}".format(a,20,b))
```

??? general "Answer"
    ```
    TTTTTTT666666TTTTTTTT
    TTTTTTTTTTTTTTT666666
    666666TTTTTTTTTTTTTTT
    ```
    相当于
    ```python
    print("{0:{1}^{2}}".format(666666, "T", 20))
    print("{0:{1}>{2}}".format(666666, "T", 20))
    print("{0:{1}<{2}}".format(666666, "T", 20))
    ```
    
    每行输出的总宽度都是 20，三行格式分别为居中、右对齐、左对齐，输出内容是 666666，用 "T" 字符填充空缺部分。

**Q15-4-2.** 输入 `dbc` 时，以下程序的输出是

```python
my_str = input()
index_int = 0
result_str = ''
while index_int < (len(my_str) - 1): 
    if my_str[index_int] > my_str[index_int + 1]:
        result_str = result_str + my_str[index_int]
    else:
        result_str = result_str * 2
    index_int += 1 
print(result_str)
```

??? general "Answer"
    `dd`。
    
    `len(my_str) - 1 = 2`，所以只会进行 `index_int` 为 0 和 1 的两次循环。

    `index_int = 0` 时，`my_str[0] > my_str[1]`，所以 `result_str` 乘 2，变为 `dd`。

**Q15-4-12.** 以下程序统计字符串中各字符出现次数。

```python
mstr = "Hello world, I am using Python to program, it is very easy to implement."
mlist = list(mstr)
___(1)___
___(2)___
    if mdict.get(e,-1)==-1:
        mdict[e]=1
    else:
        mdict[e]+=1
for key,value in ___(3)___:
    print (key,value)
```

填空，可在下面 9 个选项中选择。

```
A）mdict.values()    B) mdict.items()   C) mdict.keys()
D) mdict = {}        E)mdict = []       F) mdict = ()
G)for key in mlist:  H)for e in mlist:  I) for value in mstr：
```

??? general "Answer"
    DHB。

    - 可以看出 `mdict` 是一个字典，所以应该用 `mdict = {}` 来初始化
    - `for e in mlist:` 遍历字符串中的每个字符，需要有 `e`，否则循环中的 `e` 没有意义了
    - `mdict.items()` 可以遍历字典中的键值对，不能只有键或只有值

## 程序结构

### 判断题

**Q3-1-2.** z 已被赋值，则 `x=(y=z+1)` 是错误语句。

??? general "Answer"
    T。Python 的赋值语句是没有返回值的，不允许这种写法，在编译时直接会被认为是非法语句。

    而 `x=y=z+1` 是合法的，这是因为 Python 特别规定了这种连等的赋值语句，将会首先计算最右侧的表达式，将其计算结果赋值给左边的每一个对象。

    关于赋值语句的更多内容可以参考 [Review - 赋值语句](review.md#assignment)。

**Q8-1-2.** 带有 `else` 子句的循环如果因为执行了 `break` 语句而退出的话，会执行 `else` 子句的代码。

??? general "Answer"
    F。`else` 子句只有在循环正常结束时才会执行，如果是因为 `break` 语句退出的，`else` 子句不会执行。

**Q8-1-6.** 以下程序的输出是 `3`。

```python
lst=[34,6,7,0,0,0,9]
n=0
for i in lst:
    if i==0:
        lst.remove(i)
        n+=1
print(n)
```

??? general "Answer"
    F。
    
    在遍历列表时，不要对列表进行增删操作，容易会导致遍历出错。这里发生的事情大概为：

    - 前一轮循环，取出 lst 中的前 3 个元素，不是 0，继续。
    - 第四轮循环，取出 lst 中的第 4 个元素 0（下标为 3），删除这个元素，lst 变为 `[34, 6, 7, 0, 0, 9]`。
    - 第五轮循环，取出 lst 中的第 5 个元素 0（下标为 4），删除这个元素，lst 变为 `[34, 6, 7, 0, 9]`。
    - 此时发现 lst 的长度已经是 5 了，没有第 6 个元素，因此不再继续。

    所以最后 `n` 的值就是 2。

**Q9-1-17.** 下面程序的输出是 `[3, 2, 3, 4, 5]`。

```python
x = [1, 2, 3, 4, 5]
i = 0
i = x[i] = 3
print(x)
```

??? general "Answer"
    F。`i = x[i] = 3` 是一个连等赋值语句，先将 3 赋值给 `i`，再将 3 赋值给 `x[i]`，因此输出应当为
    ```
    [1, 2, 3, 3, 5]
    ```

    具体细节可以参照 [Review - 赋值语句](review.md#assignment)。

### 选择题

**Q5-2-3-2.** 输入整数 x，当 x 不为 0 时输出 1/x 的值，否则输出 0。以下代码段正确的是：

A. 
```python
x=int(input())
if x=0:
    y=0
else:
    y=1/x
print(y)
```

B.
```python
x=int(input())
if x!=0
    y=1/x
else
    y=0
print(y)
```

C.
```python
x=int(input())
if x:
    y=1/x
else:
    y=0
print(y)
```

D.
```python
x=int(input())
if x==0
    y=0
else
    y=1/x
print(y)
```

??? general "Answer"
    C。由于 int 类型的 x 被强制处理为 bool，仅当 x 为 0 的时候会被认为是 True，非零即为 False。因此，`if x` 和 `if x != 0` 是等价的。

    A，`if x=0` 应该为 `if x==0`。

    B，`if x!=0` 后面漏了一个冒号。D 同样也是漏了冒号。

**Q5-2-4-1.** 以下哪段代码可以实现对数列 $-1/2+2/3-3/4+4/5-5/6$ 的求和？

A. `sum([i-1/i if i%2==1 else 1-i/i for i in range(2,7)])`

B. `sum([for i in range(2,6) (i-1)/i if i%2 else (1-i)/i ])`

C. `sum([(i-1)/i if i%2 else (1-i)/i for i in range(2,7)])`

D. `sum([(i-1)/i if i%2 else (1-i)/i for i in range(7)])`

??? general "Answer"
    C。对于列表推导式，应将其展开解读。

    B 首先应该排除，这是不合法的列表推导式写法，应当将列表中元素的形式放在最前面。

    A 应当解读为：
    ```python
    lst = []
    for i in range(2, 7):
        if i%2==1:
            lst.append(i-1/i)
        else:
            lst.append(1-i/i)
    sum(lst)
    ```
    其中 `i-1/i=i-(1/i)`，`1-i/i=1-1.0=0.0`，完全不符合题目要求的数列形式。

    C 应当解读为：
    ```python
    lst = []
    for i in range(2, 7):
        if i%2:
            lst.append((i-1)/i)
        else:
            lst.append((1-i)/i)
    sum(lst)
    ```
    可以看出是符合题目要求的。

    D 的解读与 C 类似，只是 `range` 的起点不同，第一项会计算 `(1-0)/0`，发生除零错误。

**Q8-2-5.** 下面哪个语句不能完成 1 到 10 的累加功能，total 初值为 0。

A. `for i in range(10,0):total+=i`

B. `for i in range(1,11):total+=i`

C. `for i in range(10,0,-1):total+=i`

D. `for i in (10,9,8,7,6,5,4,3,2,1):total+=i`

??? general "Answer"
    A。步长默认为正步长 1，初始就有 `10<0`，于是没能进入循环。

    B 是正确的，`range(1, 11)` 会生成 1 到 10 的整数序列。

    C 是正确的，`range(10, 0, -1)` 会生成 10 到 1 的整数序列。

    D 是正确的，`for i in (10,9,8,7,6,5,4,3,2,1)` 会遍历元组中的元素。

**Q8-2-7.** 下面程序输入 1 时，输出是什么？

```python
num=int(input())
a=num-1
while a>1:
   if num % a == 0:
        print("不是素数")
        break
   a=a-1
else:
   print("是素数")
```

A. 不是素数

B. 是素数

C. 没有输出

D. 出现异常

??? general "Answer"
    B。当输入 1 时，`a` 的初始值为 0，不会进入 `while` 循环，直接输出 `是素数`。

### 填空题

**Q7-2-6:3:4.** 以下三段程序的输出为

```python
s, a, b = 0, 1, 2
if a > 0:
    s = s + 1
elif b > 0:
    s = s + 1
print(s)
```

??? general "Answer"
    `1`。由于 `a` 大于 0，所以第一个条件满足，执行完毕后直接跳出，不会执行 `elif` 语句。

```python
# Input 82
score = eval(input("Input score:"))
if score >= 60:  
    grade = "D"
elif score >= 70:  
    grade = "C"
elif score >= 80:  
    grade = "B"
elif score >= 90:
    grade = "A"
print("Grade {}".format(grade))
```

??? general "Answer"
    `Grade D`。
    
    由于 `score` 为 82，满足第一个条件，因此 `grade` 直接被赋值为 `D`，不会再执行后面的 elif。

```python
for s in "PythonNCRE":
    if s == "N":
        break
    print(s, end="")
```

??? general "Answer"
    `Python`。遇到 `s == "N"` 时，执行 `break` 语句，直接跳出循环。

**Q7-4-1:4.** 以下三段程序的输出为

```python
for s in "PythonNCRE":
    while s == "N":
        break
    print(s, end="")
```

??? general "Answer"
    `PythonNCRE`。
    
    当 s 为 "N" 时，会进入 while 循环，然后 `break` 表示离开最近的一层循环（也就是 `while` 循环），然后继续 print，继续执行 for 循环。
    
    当 s 不是 "N" 时，不进入 while 循环。因此实际上就是打印了整个 "PythonNCRE"。

```python
for i in range(1,5):
    j=0
    while j<i:
       print(j,end=" ")
       j+=1
    print()
```

??? general "Answer"
    ```
    0 
    0 1 
    0 1 2 
    0 1 2 3 
    ```
    对于第一行，`i=1`，`j=0`，`j<i`，输出 `0`。

    对于第二行，`i=2`，`j=0`，`j<i`，输出 `0 1`。

    对于第三行，`i=3`，`j=0`，`j<i`，输出 `0 1 2`。

    对于第四行，`i=4`，`j=0`，`j<i`，输出 `0 1 2 3`。

```python
a = [1, 2, 3, 4, [5, 6], [7, 8, 9]]
s = 0
for row in a:
    if type(row)==list:
        for elem in row:
            s += elem
    else:
        s+=row
print(s)
```

??? general "Answer"
    `45`。对于列表中的每个元素，如果是列表，则将列表中的元素相加，否则直接加到 s 上。

    该程序仅针对最多嵌套一层的列表进行求和，而且假定各基础元素都是数值类型可以互相相加。


**Q8-2-3.** 下面程序中语句 `print(i*j)` 的执行次数为

```python
for i in  range(5):
    for j in range(2,5):
        print(i*j)
```

??? general "Answer"
    15 次。外层循环 5 次，内层循环 3 次，总共 `5*3=15` 次。

**Q9-4-16:24:27.** 以下 3 段程序的输出为

```python
l3=[i+j for i in range(1,6) for j in range(1,6)]
print(sum(l3))
```

??? general "Answer"
    `150`。可以按如下计算

    $$
    =\sum_{i=1}^{5}\sum_{j=1}^{5}(i+j)
    =\sum_{i=1}^{5}\sum_{j=1}^{5}i + \sum_{i=1}^{5}\sum_{j=1}^{5}j
    =5\sum_{i=1}^{5}i + 5\sum_{j=1}^{5}j
    =10\sum_{i=1}^{5}i
    =10\times 15
    =150
    $$

```python
t=1
t,a=2,t+1
print(a)
```

??? general "Answer"
    `2`。
    
    对于第二行代码，首先算出等号右侧的 2 和 `t+1=2`。随后按顺序赋值，先将 2 赋值给 t，再将算好的 t+1 的值，也就是 2 赋值给 a。

    关于赋值语句的计算顺序，可以参考 [Review - 赋值语句](review.md#assignment)。

```python
lst=[2,3,5,6,8,9,10]
n=0
for i in lst[:]:
    if i%3!=1:
        lst.remove(i)
        n+=1
print(n)
```

??? general "Answer"
    `6`。
    
    尽管我们说，“对于列表的遍历，不要在遍历的过程中对列表进行增删操作，会导致遍历出错”，但是这里的 `lst[:]` 是复制了一份原列表，被遍历的是复制的列表、被删除的是原列表，因此不会出错。

    在遍历的过程中，删除了所有模 3 不为 1 的 6 个元素。

**Q15-4-14.** 输入一个十进制正整数，将它对应的二进制数的各位反序，形成新的十进制数输出。如有多组答案可选，则选答案字符序在先的那组答案。

如：13-->1101-->1011-->11
如：10-->1010-->0101-->5

```python
x = eval(input())
y = 0
while(___(1)___):   
    t=x%2
    ___(2)___    
    ___(3)___    
print(y)
```

在下面 9 个答案中选择。

```
A) x              B) x or y      C) not x 
D) y = y*10 + t   E) y *= 2 + t  F) y = y//2 
G) x= x //10      H) x= x // 2   I) y = y*2 + t
```

??? general "Answer"
    AHI。

    其思想是，一开始的 `t=x%2` 是二进制最低位，反向后是二进制最高位。逐渐将 `x//2`，可以得到原来的数中更高维的二进制数位，然后反向后的数位逐渐变低。累加，使用 `*2+t` 的方法，对应二进制相邻数位之间的关系。

**Q15-4-15.** 10 进制转 16 进制。

```python
decimal = eval(input("Enter an integer: "))
hexString = ""
value = ___(1)___
while value != 0:
    single = value % 16
    if single == 15: 
        hexString = "F" + hexString
    elif single == 14:
        hexString = "E" + hexString
    elif single == 13:
        hexString = "D" + hexString
    elif single == 12:
        hexString = "C" + hexString
    elif single == 11:
        hexString = "B" + hexString
    elif single == 10:
        hexString = "A" + hexString
    else:
        hexString = ___(2)___+ hexString
    value = ___(3)___
print(str(decimal) + "'s hex representation is " + hexString)
```

在下面 9 个答案中选择。

```
A) single       B) decimal        C) hexString
D) value / 16   E) value // 16    F) value % 16
G) str(single)  H) str(hexSting)  I) singles
```

??? general "Answer"
    BGE。

    - `value` 会逐渐变化，所以不能直接使用原来的 `decimal`，因为在最后还需要输出 `decimal`
    - 模仿前面的，其实就是 single 对应的字符
    - `value` 逐渐除以 16，获得十六进制的下一位

## 列表与元组

### 判断题

**Q6-1-23** `[4,5]*3` 的结果是 `[[4,5],[4,5],[4,5]]`。

??? general "Answer"
    F。其结果为 `[4, 5, 4, 5, 4, 5]`，每个元素的内存都是独立的。

    而 `[[4,5]]*3` 的结果是 `[[4, 5], [4, 5], [4, 5]]`，但是这个二维列表（矩阵）中的每个一维列表共享内存，即该矩阵的每一行都是同一行。例如会有：

    ```python
    a = [[4,5]]*3
    # a = [[4, 5], [4, 5], [4, 5]]
    a[1][1] = 2
    # a = [[4, 2], [4, 2], [4, 2]]
    ```

    可以参考 [Review - 列表](review.md#list)。

**Q9-1-22.** `[1,2,[3]]+[4,5]` 的结果是 `[1,2,3,4,5]`。

??? general "Answer"
    F。其结果为 `[1, 2, [3], 4, 5]`，两个列表直接相加，会将第二个列表整体加到第一个列表的末尾。

**Q6-1-14** 以下程序的运行结果是运行错误。

```python
lst=[12, -5, -22, -10, -26, 35, 0, 49, 3, -21]
print(lst[100])
```

??? general "Answer"
    T。列表越界错误。

**Q9-1-1.** 字符串、列表、元组都是序列类型。

??? general "Answer"
    T。参考 [Review - 数据类型](review.md#data-type)。

**Q9-1-2.** 列表可以用 `find()` 函数来搜索数据是否在列表中。

??? general "Answer"
    F。`find()` 是字符串的方法，用于查找子串的位置，列表没有这个方法。

**Q9-1-3.** 字符串对象和元组对象是不可变对象，列表对象为可变对象。

??? general "Answer"
    T。参考 [Review - 可变类型与不可变类型](review.md#mutable-immutable)。

### 选择题

**Q9-2-15.** 如果 `list1 = [1, 2, 3, 4, 5, 4, 3, 2, 1]`，那么以下哪个是 `list1[:-1]`？

A. `0`

B. `[1, 2, 3, 4, 5, 4, 3, 2, 1]`

C. `[1, 2, 3, 4, 5, 4, 3, 2]`

D. `[0, 1, 2, 3, 4, 3, 2, 1, 0]`

??? general "Answer"
    C。舍去最后一个元素后的列表，注意是 `list1[:-1]` 而不是 `list1[::-1]`。

**Q15-2-12.** 下面程序的运行结果是什么？

```python
b=[1,2,3]
b[2]=b
s = 0
for row in b:
    if type(row)==list:
        for elem in row:
            s += elem
    else:
        s+=row
print(s)
```

A. 9

B. 10

C. 8

D. 其他

??? general "Answer"
    D。报错在第 4 行：`TypeError: unsupported operand type(s) for +=: 'int' and 'list'`。
    
    这是一个循环引用的例子，`b[2]` 指向了 `b` 这个列表，是一种特殊的用法，这种用法本身并不会报错。

    实际执行中，`row` 取 1 和 2 不会发生问题；接下来 `row` 取 `b[2]` 也就是 `b`，也不会发生问题。

    接下来由于 b 是 list 类型，就会执行 `for elem in b`。`elem` 取 1 和 2 也不会发生问题，但是接下来 `elem` 还是会取到 `b`，此时的 `s` 是 int 类型，但是 `b` 是 list 类型，会试图将 `s` 与 `b` 相加，于是会报错。

### 填空题

**Q6-2-1:3.** 给出如下三个表达式的结果：

```python
max((3, 5, 1, 7, 4))
max([3, 5, 1, 7, 4])
max("35174")
list("abcd")
```

??? general "Answer"
    ```python
    7
    7
    "7"
    ['a', 'b', 'c', 'd']
    ```

**Q6-4-3:14.** 给出以下两段程序的输出。

```python
lst = [3,4,5,6,5,4,3]
lst.remove(3)
print(lst[0])
```

??? general "Answer"
    ```python
    4
    ```
    原来在 0 号位的 3 被 remove 了，后面的元素依次补上，因此 0 号位变成了 4。

```python
a=[1,2,3,4]
b=a
print(id(a)==id(b))
c=a.copy()
print(id(a)==id(c))
d=a[:]
print(id(a)==id(d))
```

??? general "Answer"
    ```python
    True
    False
    False
    ```
    对于第一行输出，直接赋值 `b=a` 是一个引用赋值，b 和 a 对应的内存空间是相同的。

    对于第二行输出，`copy` 会将整个一维列表进行拷贝，内存空间会不一样。

    对于第三行输出，切片操作会进行类似 `copy` 的操作，而不是引用赋值。

    可以参考 [Review - 列表](review.md#list)。

**Q7-4-7:8:9:10.** 给出以下四段程序的输出。

```python
n = 3
m = 4
a = [0] * n
for i in range(n):
    a[i] = [0] * m
    print(a)
a[2][2] = 7
print(a)
```

??? general "Answer"
    ```
    [[0, 0, 0, 0], 0, 0]
    [[0, 0, 0, 0], [0, 0, 0, 0], 0]
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 7, 0]]
    ```
    可以看出，这是在构造一个 3 行 4 列的矩阵。

    首先把 `a` 构造为 `[0, 0, 0]`，每个 0 都是一行的占位符。随后循环为 `a` 补上每一行，每行都是长度为 m 的全零列表。利用了一维列表的乘法。由此前三行输出就很自然了。

    对于最后一行输出，修改 `a[2][2]` 为 7 并不会影响其他元素，因为 `a` 的每一行都是单独构造 `[0] * m` 后赋值的，没有共享内存空间。

```python
row=[0]*3
data=[row,row,row]
data[2][2]=7
print(data[0][2])
```

??? general "Answer"
    `7`。
    
    `data` 中的每一行都是同一个 `row`，所以修改 `data[0][2]` 实际上是在修改 `row[2]`，于是 `data` 的每一行都改变了。（每一行都是同一行）

```python
data=[[0]*3] *3
data[2][2]=7
print(data[0][2])
```

??? general "Answer"
    `7`。
    
    用这种方式构造出来的 `data` 矩阵的每一行也都是同一行。一维列表的乘法是拷贝值后拼接，二维列表的乘法就是拷贝引用后拼接了。

```python
data=[]
for i in range(3):
    data.append([0]*3)
data[2][2]=7
print(data[0][2])
```

??? general "Answer"
    `0`。
    
    这种方式构造的 `data` 矩阵的每一行都是独立构造的 `[0]*3`，因此修改 `data[2][2]` 不会影响其他元素。

> 对于列表的困惑，可以参考 [Review - 列表](review.md#list)。

**Q9-1-5:6:7:8:9:10:11:12.** 给出以下程序的输出。

```python
lst=[12, -5, -22, -10, -26, 35, 0, 49, 3, -21]
print(lst[::-1])
print(lst[::2])
print(lst[::])
print(lst[3:8:2])
print(lst[1::2])
print(lst[0:100])
print(lst[100])
```

??? general "Answer"
    ```python
    [-21, 3, 49, 0, 35, -26, -10, -22, -5, 12]
    [12, -22, -26, 0, 3]
    [12, -5, -22, -10, -26, 35, 0, 49, 3, -21]
    [-10, 35, 49]
    [-5, -10, 35, 49, -21]
    [12, -5, -22, -10, -26, 35, 0, 49, 3, -21]
    IndexError: list index out of range
    ```

    列表切片 `[start:stop:step]` 的意义是从 `start` 开始，到 `stop` 结束，每隔步长 `step` 取一个元素，与 `range` 是类似的。

    `step` 默认为 1，`start` 默认为 0，`stop` 默认为列表的长度。值得注意的是，`stop` 可以取大于列表的长度，会被自动截断。

**Q15-4-6.** 给出如下两段程序的输出。

```python
list1=[1,43]
list2=list1
list1[0]=22
print(list2[0])
```

??? general "Answer"
    `22`
    
    列表直接赋值给另一个变量是引用赋值，因此`list1` 和 `list2` 都指向同一个列表，修改 `list1` 的元素也会影响 `list2`。

```python
d1=[1,5,7]
d2=d1.copy()
d1[0]=6
print(d1[0]+d2[0])
```

??? general "Answer"
    `7`

    发生了列表的拷贝，`d1` 和 `d2` 是两个不同的列表，`d1[0]=6` 不会影响 `d2`，因此输出是 `6+1=7`。

## 排序与矩阵计算

### 判断题

**Q8-1-5.** 下列程序在输入 `36` 时输出为 `10`。

```python
a=[3,5,7,11,13,16,21,24,28,32,36,40,46]
x = int(input())
found = -1
left = 0                      #第一个元素下标
right = len(a)-1              #最后一个元素下标
while left<right:
    mid = (left + right) // 2
    if a[mid] > x:
        right = mid - 1
    elif a[mid] < x:
        left = mid + 1
    else:                     # a[mid]==x
        found = mid
        break
print(found)
```

??? general "Answer"
    F。这个二分查找是有问题的，`while` 的条件应该改为 `left <= right`。对于 `36` 这一输入，最后会进入 `left == right`，然后直接退出循环（本应先令 `found = mid` 的），使 found 保持 -1。

### 填空题

**Q9-4-25.** 给出以下程序的输出。

```python
mat=[[i*3+j+1 for j in range(3)] for i in range(5)]
mattrans=[[row[col] for row in mat] for col in range(3)]
print(mattrans[1][3])
```

??? general "Answer"
    `11`。
    
    `mat` 是一个 5 行 3 列的矩阵，即
    ```
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9],
     [10, 11, 12],
     [13, 14, 15]]
    ```

    构造 `mat` 的语句可以展开解读为
    ```python
    mat = []
    for i in range(5):
        row = []
        for j in range(3):
            row.append(i*3+j+1)
        mat.append(row)
    ```

    同理，`mattrans` 的构造可以解读为
    ```python
    mattrans = []
    for col in range(3):
        rowtrans = []
        for row in mat:
            rowtrans.append(row[col])
        mattrans.append(rowtrans)
    ```
    
    可以看出，`mattrans` 逐渐将 `mat` 的第 0, 1, ... 列加入到第 0, 1, ... 行，因此是 `mat` 的转置矩阵。
    
    因此，`mattrans[1][3]` 就是 `mat[3][1]`，即 `11`。

**Q13-4-12.** 给出如下程序的输出

```python
def ins_sort_rec(seq, i):
    if i == 0: return
    ins_sort_rec(seq, i - 1)
    j = i
    while j > 0 and seq[j - 1] > seq[j]: 
        seq[j - 1], seq[j] = seq[j], seq[j - 1] 
        j -= 1

seq = [3,-6,79,45,8,12,6,8]
ins_sort_rec(seq, len(seq)-1)
print(seq[5])
```

??? general "Answer"
    `12`
    
    这个程序实现了框架像插入排序、实现像冒泡排序的一种排序算法的递归版本，`ins_sort_rec` 函数的作用是将 `seq` 中前 `i` 个元素排序。因此 `ins_sort_rec(seq, len(seq)-1)` 就是对 `seq` 进行排序。
    
    其逻辑为，如果 `i==0` 说明无需排序，否则就首先先将前 `i-1` 个元素进行排序。此时，前 `i-1` 个元素已经是有序的，只需让第 `i` 个元素插入到前 `i-1` 个元素中，使得前 `i` 个元素有序，接下来的 `while` 循环就是将第 `i` 个元素插入到前 `i-1` 个元素中的过程。

    由于排序后 `seq` 的第 5 个元素是 12，因此输出就是 12。

**Q14-4-14.** 请填空如下程序，实现冒泡排序。

```python
def bubble(List):
    for j in range(________,0,-1):
        for i in range(0,j):
            if List[i]>List[i+1]:List[i],List[i+1]=List[i+1],List[i]
    return List

testlist = [49, 38, 65, 97, 76, 13, 27, 49] 
print( bubble(testlist))
```

??? general "Answer"
    `len(List)-1`

    冒泡排序的基本思想是，每次比较相邻的两个元素，如果顺序不对就交换。第一轮比较后，最大的元素就会被交换到最后一个位置；第二轮比较后，第二大的元素就会被交换到倒数第二个位置；以此类推，第 `j` 轮比较后，第 `j` 大的元素就会被交换到倒数第 `j` 个位置。

**Q14-4-15.** 请填空如下程序，实现选择排序。

```python
def selSort(nums):
    n = len(nums)
    for bottom in range(n-1):
        mi = bottom
        for i in range(_________, n):
            if nums[i] < nums[mi]:
                 mi = i
        nums[bottom], nums[mi] = nums[mi], nums[bottom] 
    return nums
                
numbers = [49, 38, 65, 97, 76, 13, 27, 49]
print(selSort(numbers))
```

??? general "Answer"
    `bottom` 或 `bottom+1` 或 `mi` 或 `mi+1`

    选择排序的基本思想是，每次从未排序的元素中选择最小的元素，放到已排序的元素的末尾。第 `bottom` 轮比较后，最小的元素就会被放到第 `bottom` 个位置。

**Q15-4-1.** 执行下列语句后 `v` 的显示结果是什么?

```python
values = [[3, 4, 5, 1], [33, 6, 1, 2]]

v = values[0][0]
for row in range(0, len(values)):
    for column in range(0, len(values[row])):
        if v < values[row][column]:
            v = values[row][column]
print(v)
```

??? general "Answer"
    `33`

    这段程序的作用是找出二维列表 `values` 中的最大值。首先将 `v` 初始化为 `values[0][0]`，然后遍历整个二维列表，如果发现更大的值就更新 `v`。最终 `v` 的值就是整个二维列表的最大值。

**Q15-4-13.** 下面程序随机生成 10 个整数，将它们从大到小排序后输出。

```python
from random import * 

def sort1(___(1)___):
    for k in range(n-1):
        index = k
        for i in ___(2)___:
            if a[i] > a[index]:
                index = i 
        a[k], a[index] = a[index], a[k]

c = []
for i in range(10):
    b = randint(1, 10000)
    c.append(b)
___(3)___
print(c)   
```

在下面 9 个选项中选择。

```
A）range(k, n)  B) range(k+1, n-1)  C) a, n-1
D) a, n         E) sort1(c)         F) sort1(c[], 10) 
G) a[]          H) range(k+1, n)    I) sort1(c, 10)
```

??? general "Answer"
    D, A 或 H, I。

    其实就是实现选择排序。
    - 作为函数的形参列表，只有 D 是合法的
    - A 和 H 都对，其实就是找到 k 之后的最小值，包含不包含 k 都对，当然包含 k 的话会多一次比较
    - F 中 `c[]` 是不合法写法，E 中少输入了一个参数，I 是正确的方法

## 集合与字典

### 判断题

**Q11-1-1.** 集合的元素可以是任意数据类型。

??? general "Answer"
    F。集合的元素具有可哈希性，必须是不可变类型。

**Q11-1-1+.** 字典的值可以是任意数据类型。

??? general "Answer"
    T。字典的值可以是任意数据类型，包括列表、元组、集合、字典等。

**Q11-1-1++** 字典的键可以是任意数据类型。

??? general "Answer"
    F。类似于集合的元素，字典的键也必须是不可变类型。

**Q11-1-2.** `len(set([0,4,5,6,0,7,8]))` 的结果是 `7`。

??? general "Answer"
    F。集合中的元素具有唯一性，因此列表转换为集合后，只有 `[0, 4, 5, 6, 7, 8]` 这 6 个元素。

**Q11-1-3.** `a={}`, `type(a)` 结果是 `<class 'set'>`。

??? general "Answer"
    F。`{}` 默认是空字典，`type(a)` 的结果是 `<class 'dict'>`。如果希望创建空集合，应该使用 `set()`。

**Q11-1-5.** 列表可以作为字典的键。

??? general "Answer"
    F。列表是可变类型，不能作为字典的键。

**Q11-1-13.** 下面程序的输出是 `5`。

```python
set2={num for num in range(1,15) if num%3==0}
print(len(set2))
```

??? general "Answer"
    F。

    `set2` 是一个集合，包含了 1 到 15 中所有能被 3 整除的数，即 `{3, 6, 9, 12}`，因此输出应该是 4。

### 选择题

**Q11-2-3.** 对于两个集合 `s1` 和 `s2`，`s1 < s2` 的意思是？

A. `s1` 的大小小于 `s2` 的大小

B. `s1` 的元素比 `s2` 的小

C. `s1` 是 `s2` 的真子集

D. `s2` 是 `s1` 的真子集

??? general "Answer"
    C。

**Q11-2-4.** 对于集合 `s`，以下哪个操作是不存在的？

A. `len(s)`

B. `s.append(1)`

C. `max(s)`

D. `s - {1}`

??? general "Answer"
    B。`append` 是列表的方法，不是集合的方法。

    `len(s)` 是求集合中元素的个数，`max(s)` 是求集合中元素的最大值，`s - {1}` 是从集合中删除元素 1。

**Q11-2-5.** 对于正确的表达式 `a[2]`，`a` 不可能是以下哪个类型？

A. 集合

B. 列表

C. 元组

D. 字典

??? general "Answer"
    A。集合具有无序性，不支持索引操作。

    对于列表和元组，`a[2]` 是获取索引为 2 的元素；对于字典，`a[2]` 是获取键为 2 的值。

**Q11-2-7.** 你可以使用什么方法从字典中删除元素？

A. `remove`

B. `rease`

C. `delete`

D. `del`

??? general "Answer"
    D。`remove` 是列表和集合删除元素的方法。

**Q11-2-8.** 返回集合中元素个数的函数是

A. `size()`

B. `len()`

C. `elements()`

D. `count()`

??? general "Answer"
    B。

**Q15-2-6** 下面定义字典的语句哪个是正确的？

A. `momthdays = dict(Jan=31, Feb=28, Mar=31, Apr=30)`

B. `momthdays = dict("Jan"=31, "Feb"=28, "Mar"=31, "Apr"=30)`

C. `momthdays = {Jan:31, Feb:28, Mar:31, Apr:30}`

D. `momthdays = {Jan=31, Feb=28, Mar=31, Apr=30}`

??? general "Answer"
    A。

    除了 A 之外，与 CD 类似的正确的定义方式为
    ```python
    momthdays = {"Jan":31, "Feb":28, "Mar":31, "Apr":30}
    ```

### 填空题

**Q12-4-1:2:3:4:5.** 给出以下五段程序的输出。

```python
squares = {x:x*x  for x in range(20)}
print(squares[12])
```

??? general "Answer"
    `144`。构造了一个字典，键为 0 到 19，值为键的平方，因此查询得到 12 的平方。

```python
text="four score and 7 years"
lenwords={s:len(s) for s in text.split()}
print(lenwords["score"])
```

??? general "Answer"
    `5`。
    
    `text.split()` 会将字符串按空格分割为字符串列表，得到
    ```
    ['four', 'score', 'and', '7', 'years']
    ```
    
    然后构造子字符串（单词）到其长度的映射，键为单词，值为单词的长度
    ```
    {'four': 4, 'score': 5, 'and': 3, '7': 1, 'years': 5}
    ```

    因此 `lenwords["score"]` 就是 5。

```python
dic1 = {"姓名": "xiaoming", "年龄": 27} 
dic2 = {"性别": "male","年龄": 30} 
dic3 = {k:v for d in [dic1, dic2] for k,v in d.items()} 
print(dic3["年龄"])
```

??? general "Answer"
    `30`。
    
    `d.items()` 是字典的键值对视图，`for k,v in d.items()` 就是遍历字典的键值对。`[dic1, dic2]` 是一个列表，遍历列表中的字典，将字典的键值对加入到新字典中，后面的键值对会覆盖前面的。相当于
    ```python
    dic3 = {}
    for d in [dic1, dic2]:
        for k, v in d.items():
            dic3[k] = v
    ```

```python
cells=dict(values=[[100, 90, 80, 90], [95, 85, 75, 95]])
print(cells["values"][1][2])
```

??? general "Answer"
    `75`。
    
    `cells` 是一个字典，只有 `values` 这一个键，其值是一个二维列表（2 行 4 列的矩阵）。因此 `cells["values"][1][2]` 就是取出这个矩阵第 2 行第 3 列的元素。

```python
myth=[{'label': color, 'value': color} for color in ['blue', 'red', 'yellow']]
print(myth[1]["label"])
```

??? general "Answer"
    `'red'`。
    
    将构造 `myth` 的过程展开：
    ```python
    myth = []
    for color in ['blue', 'red', 'yellow']:
        myth.append({'label': color, 'value': color})
    ```

    因此构造得到的 `myth` 为
    ```
    [{'label': 'blue', 'value': 'blue'},
     {'label': 'red', 'value': 'red'},
     {'label': 'yellow', 'value': 'yellow'}]
    ```

    所以 `myth[1]["label"]` 就是第 2 个字典的 `label` 值，即 `'red'`。

**Q15-4-8.** 给出如下程序的输出。

```python
print(len(set([1,2,1,2,3])))
```

??? general "Answer"
    `3`。集合的元素具有唯一性，因此只剩下 `[1, 2, 3]` 这 3 个元素。

## 函数

### 判断题

**Q13-1-1.** 函数也是对象，下面程序可以正常运行吗？

```python
def func():
    print("11",end=" ")
    
print(id(func),type(func),func)
```

??? general "Answer"
    T。
    
    - 函数也是对象，所以打印 `func` 是合法的
    - 并且函数具有内存地址和类型，所以 `id(func)` 和 `type(func)` 也是合法的

### 选择题

**Q13-2-2.** 在 Python 中，对于函数定义代码的理解，正确的理解是

A. 必须存在形参

B. 必须存在 `return` 语句

C. 形参和 `return` 语句都是可有可无的

D. 形参和 `return` 语句要么都存在，要么都不存在

??? general "Answer"
    C。

    函数可以没有形参，也没有 `return` 语句。如果没有形参，函数就不需要传入参数；如果没有 `return` 语句，函数就没有返回值。

**Q13-2-5.** 函数可以改变哪种数据类型的实参？

A. int

B. string

C. list

D. float

??? general "Answer"
    C。函数可以改变列表等可变对象的实参。

**Q13-2-3.** 在一个函数中如局部变量和全局变量同名，则：

A. 局部变量屏蔽全局变量

B. 全局变量屏蔽局部变量

C. 全局变量和局部变量都不可用

D. 程序错误

??? general "Answer"
    A。即在函数中，同名变量优先指代局部变量。

### 填空题

**Q13-2-7.** 下面程序的运行结果是什么？

```python
def fun(x1, x2, x4, **x3):
    print(x1, x2, x3, x4)
   
fun(x1=1, x2=22, x5=333, x4=4444)
```

??? general "Answer"
    ```
    1 22 {'x5': 333} 4444
    ```
    本题考查 `**name` 形式的形参的作用，`**name` 会将多余的关键字参数收集到字典 name 中。此处的关键字传参中，`x1`, `x2`, `x4` 已经有专门的形参接收，从而 `x5` 会被收集到 `x3` 中。

**Q13-4-1:8:9:10.** 给出以下四段程序的输出

```python
def scope():
    n, m = 4, 5
    print(m, n, end=' ')
n, t = 5, 8
scope()
print(n, t)
```

??? general "Answer"
    ```
    5 4 5 8
    ```
    局部变量屏蔽全局变量，因此修改函数内局部的 n 不会修改全局的 n。

```python
l=[1]
def scope1():
    l.append(6)    
    print(*l)
scope1()
```

??? general "Answer"
    `1 6`。
    
    此处未构造局部变量，因此函数向外部寻找 `l`，并最后找到全局变量 `l` 进行使用，所以到 print 时的 `l` 就是 `[1, 6]`。

    `*l` 意为对列表 `l` 进行解包 (unpack) 后获得 print 函数的参数列表，即让 1 和 6 称为 print 的参数，实际上相当于调用了 `print(1, 6)`。

    关于函数的解包参数列表，可以参考 [Review - 解包参数列表](review.md#unpacking)。

```python
a=10
def func():
    global a
    a=20
    print(a,end=' ')
func()
print(a)
```

??? general "Answer"
    `20 20`。
    
    `global` 关键字用于声明全局变量，即声称函数内的 `a` 就是全局变量 `a`，因此在函数内部修改 `a` 就是修改全局的 `a`。

```python
b, c=2, 4
def g_func(d):
    global a
    a=d*c
g_func(b)
print(a)
```

??? general "Answer"
    `8`。
    
    相比于上一段程序，这里的函数实现了对全局变量 `a` 的创建。

**Q15-2-15.** 给出如下程序的输出

```python
b, c = 2, 4
def g_func():
    b = 1
    b = b * c
    d = b
    print(b, d, end='  ')
g_func()
print(b, c)
```

??? general "Answer"
    `4 4  2 4`

    `g_func` 中的局部的 `b` 屏蔽了全局的 `b`，而不存在局部的 `c`，因此 `g_func` 中的 `c` 是全局的 `c`。
    
    因此 `g_func` 中的 `b` 是 `1*c=4`，`d=b`，所以输出是 `4 4`；回到全局，全局的 `b` 由于被局部屏蔽而没有被修改，而 `c` 还是 4，所以输出是 `2 4`。

**Q13-4-3:6.** 给出如下两段程序的输出

```python
lst=[(1,"one"),(2,"two"),(3,"three"),(4,"four")]
lst.sort(key=lambda x:x[1])
print(lst[3][1][2])
```

??? general "Answer"
    ```
    o
    ```
    此处的 Lambda 表达式的输入是列表的每个元组元素，输出是元组的下标为 1 的元素。因此，将以元组第二个元素 - 字符串为排序依据，对 `lst` 进行排序，得到
    ```
    [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
    ```

    此处注意，字符串排序规则是首先根据第一个字符的 ascii 码，如果相同则再看第二个字符，以此类推。如果前 n 个字符都相同，一个字符串没有第 n+1 个字符，另一个存在第 n+1 个字符，那么认为长度就是 n 的字符串更小（相当于第 n+1 个字符的 ascii 码为 0）。

    关于 Lambda 表达式的简单例子，可以参考 [Review - Lambda 表达式](review.md#lambda)。

```python
f = lambda p:p+5
t = lambda p:p*3
x=7
x=f(x)
x=t(x)
x=f(x)
print(x)
```

??? general "Answer"
    `41`

    根据 Lambda 表达式，`f` 的作用是输入 `p`，返回 `p+5`；`t` 的作用是输入 `p`，返回 `p*3`。

    因此最终的 `x` 就是 `((x+5)*3) + 5`，即 `41`。

**Q13-4-5.** 给出如下程序的输出

```python
def func1():
    print("11",end=" ")
    
def func2():
    print("22",end=" ")

def func3():
    print("33",end=" ")

funclist=[func1,func2,func3]
for func in funclist:
    func()
```

??? general "Answer"
    `11 22 33 `
    
    在 Python 中，函数是对象，可以像其他数据对象一样使用。`funclist` 中存储了三个函数，遍历 `funclist`，依次调用三个函数。

## 递归与动态规划

### 填空题

**Q13-4-4.** 给出如下程序的输出

```python
def perm(choice,selected=[]):
    if len(choice)==1:
        print("".join(selected+choice))
    else:
        for i in range(len(choice)):
            t=choice[i]
            choice.remove(t)
            selected.append(t)
            perm(choice,selected)
            choice.insert(i,t)
            selected.pop()

first=["1","2","3"]
perm(first,selected=[])
```

??? general "Answer"
    ```
    123
    132
    213
    231
    312
    321
    ```
    这个程序的作用是按照字符顺序输出 1, 2, 3 的全排列，使用了递归函数树形搜索。

    `choice` 表示可选的排列项，`selected` 表示前几位已经选择了的项。每次 `perm` 执行时，会遍历 `choice` 中的每个元素，即遍历每种可能的下一步的选择，然后把这一项从 `choice` 中去除，加入到 `selected`。为了对下一种可能的选择进行尝试时，不被上一步的尝试影响，需要 `insert` 和 `pop` 这两行恢复上一步尝试产生的影响（把加入到 `selected` 的元素从 `selected` 删掉，重新加回到 `choice`）

    从顺序上，初始的 `choice` 中的顺序就是 1, 2, 3，因此遍历时的顺序也就是这样的字符顺序，所以输出全排列的顺序也就是字符顺序。

    为了方便理解，给出 `perm` 函数的部分调用顺序：
    ```
    perm(["1", "2", "3"], [])
    perm(["2", "3"], ["1"])    # in perm(["1", "2", "3"], [])
    perm(["3"], ["1", "2"])    # in perm(["2", "3"], ["1"])
    print("123")               # in perm(["3"], ["1", "2"])
    perm(["2"], ["1", "3"])    # in perm(["2", "3"], ["1"])
    print("132")               # in perm(["2"], ["1", "3"])
    perm(["1", "3"], ["2"])    # in perm(["1", "2", "3"], [])
    ...
    ```

**Q13-4-7.** 给出如下程序的输出

```python
def factorial(n):
    match n:
        case 0 | 1:
            return 1
        case _:
            return n * factorial(n - 1)
print(factorial(5))
```

??? general "Answer"
    `120`。
    
    `match` 语句是 Python 3.10 新引入的模式匹配语法，`case 0 | 1:` 表示匹配 0 或 1，`case _:` 表示匹配其他情况。因此可以理解为
    ```python
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)
    ```

    所以这个函数在计算 $n!$，于是结果就是 $5!$。 

    更多关于 `match` 语句的内容，可以参考官方文档 [match Statements - Python 3.12.3 documentaion](https://docs.python.org/3/tutorial/controlflow.html#match-statements)。

**Q13-4-11.** 给出如下程序的输出

```python
import math
def factors(x):
    y=int(math.sqrt(x))
    for i in range(2, y+1):
        if x%i ==0:
            factors(x//i)
            break
        else:
            print(x,end=' ')
        return
factors(38)
```

??? general "Answer"
    `19`
    
    这个递归程序实际上 `i` 只能取到 2，一轮循环之后要么通过 `break` 退出循环结束函数，要么通过 `return` 结束函数。

    因此对于 `factors(n)`，
    
    - 如果 `n` 不是 2 的倍数，那就会输出 `n`，然后结束函数
    - 如果 `n` 是 2 的倍数，那就会执行 `factors(n//2)`，再判定 `n//2` 是不是 2 的倍数
    - 以此类推，直到执行 `factors(n//(2 ** k))`，使得 `n//(2 ** k)` 不是 2 的倍数，而且 `factors(n//(2 ** (k-1)))` 是 2 的倍数时，就会输出 `n//(2**k)`，然后返回。由于前面每次调用的后面都紧跟着 `break`，因此都既不会再 `print` 也不会再调用，最后一层层返回结束函数

    于是递归函数 `factors(38)` 的执行过程可以展开为
    ```
    factors(38)
    factors(19)
    print(19)
    return to factors(38)
    break
    return to main
    ```

**Q15-2-11.** 给出如下程序的输出

```python
import math
def factors(x):
    y=int(math.sqrt(x))
    for i in range(2, y+1):
        if x%i == 0:
            print(i, end=' ');
            factors(x//i)
            break
        else:
            print(x, end=' ')
    return
factors(18)
```

??? general "Answer"
    `2 9 3`
    
    类似上题进行分析。递归函数 `factors(18)` 的执行过程可以展开为
    ```python
    factors(18)
    print(2)          # i = 2, y = 4
    factors(9)
    print(9)          # i = 2, y = 3
    print(3)          # i = 3, y = 3
    factors(3)
    # y = 1, return to factors(9) directly
    break and return  # from factors(9) to factors(18)
    break and return  # from factors(18) to main
    ```

**Q13-4-13.** 给出如下程序的输出

```python
def basic_lis(seq):
    l=[1]*len(seq)
    for cur ,val in enumerate(seq):           #enumerate 返回元素的"索引和值"
        for pre in range(cur):
            if seq[pre]<val:
                l[cur]=max(l[cur],1+l[pre])
    return max(l)

L=[49, 64, 17, 100, 86, 66, 78, 68, 87, 96, 19, 99, 35]
print(basic_lis(L))
```

??? general "Answer"
    `7`
    
    这个程序实现了最长递增子序列 (Longest Increasing Subsequence, LIS) 问题的动态规划算法。`l` 是一个列表，`l[i]` 表示以 `seq[i]` 结尾的最长递增子序列的长度。

    算法的基本思想是，对于每个元素 `seq[cur]`，`l[cur]` 的基本值是 1，对于所有比 `cur` 小的 `pre`，如果 `seq[pre] < seq[cur]`，那么到 `pre` 为止的递增子序列就可以在后面接上一个 `seq[cur]`，于是出现新的递增子序列长度 `1+l[pre]`。遍历之前的元素 `seq[pre]`，找到最大的满足 `seq[pre] < seq[cur]` 的 `1+l[pre]`，就是 `l[cur]` 的值。

    对于输入 `L`，最长递增子序列是 `[49, 64, 66, 68, 87, 96, 99]`，长度为 7。

**Q15-4-5.** 下面程序用动态规划法快速计算斐波那契数，在下划线处填上正确的表达式。

```python
def fastFib(n, memo = {}):
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        ____________= result
        return result

print(fastFib(20))
```

??? general "Answer"
    `memo[n]`

    这个递归程序的思想就是存储中间结果。计算 `fib(n)`，利用递归首先需要计算 `fib(n-1)`，此时它会需要算出 `fib(n-2)` 和 `fib(n-3)`，但是算完 `fib(n-1)` 之后还需要去算 `fib(n-2)`，实际上已经算过它了。

    因此，为了避免重复计算，第一次算出 `fib(n-2)` 的时候就将它存进 `memo`，这样第二次再遇到就可以直接查字典 `memo` 获得 `fib(n-2)` 的值。

    具体而言，用能否查找成功判断是否是第一次计算。如果在字典中能查到，就说明已经被算过了，直接使用查找到的数值；如果发生 KeyError，就说明还没被算过，需要先把它算出来。

## 文件

### 选择题

**Q15-2-3.** 下面哪种方法读文件 `input.txt` 是正确的

A. `in_file = open('input.txt', 'w')`

B. `in_file = open('input.txt', r)`

C. `in_file = open('input.txt', 'r')`

D. 都不正确

??? general "Answer"
    C。

    A 是写文件，B 的 `'r'` 缺少引号，mode 要求输入一个字符串。

### 填空题

**Q15-4-11.** 文件 `populationdata.txt` 是部分国家的人口数据。每行一个国家人口数据。统计人口数中以"1"/"2"/"3"/"4"/"5"/"6"/"7"/"8"/"9"开头的百分比数，输出样例如下所示：
```
[(1, 27.586206896551722), (2, 19.396551724137932), (3, 12.931034482758621), (4, 9.482758620689655),
(5, 7.327586206896552), (6, 9.051724137931034), (7, 5.603448275862069), (8, 5.172413793103448),
(9, 3.4482758620689653)]
```

这表示 "1" 开头的百分比数为 `27.586206896551722`，"2"开头的百分比数为 '19.396551724137932'，以此类推。请填写下面程序中的空格，使得程序能够正确统计人口数据。

```python
populationfile=open('populationdata.txt',_(1)_)
digit_counts={d:0 for d in "123456789"} 
total=0
for line in _(2)_：
     line=line.strip()     
     if line and _(3)_:    
         first_digit=line[0]    
         digit_counts[first_digit]+=1        
         total+=1   
percents=sorted([(int(digit),count*100/total)  for digit,count in digit_counts.items()])
print( percents)
```

在下面 9 个可选项中选择。

```
A) digit_counts       B) 'w'                C) digit_count
D) line[1].isalpha()  E) line[0].isalnum()  F) 'a'
G) line[0].isdigit()  H) 'r'                I) populationfile
```

??? general "Answer"
    HIG。

    - 只用读取数据，所以 `r` 就可以了，`a` 和 `w` 都不具有读的功能
    - 要从文件中读每一行，只能使用 `populationfile`
    - 只接收数字开头，字符开头不合法，因此应当使用 `isdigit()` 方法

