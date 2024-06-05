<link rel="stylesheet" href="../../../css/counter.css" />

# Python Basics: Review

!!! info "Note of ZJU *Python Programming*, 2024 Spring & Summer."

## 基础输入理解

编程题常见的写法：同一行输入两个整数，以空格隔开，例如 `3 5`

```python
a, b = map(int, input().split())
```

需要了解每一步的作用。

### `input()`

读取一行输入，返回这行所有字符构成的**字符串**

```shell
>>> input()
3 5 7 8
'3 5 7 8'
```

### `input().split()`

将字符串按空格分割，返回一个**由多个子字符串构成的列表**。如果存在连续的空格，会当作一个空格进行分割

- `split()` 是从属于字符串类型的方法
- 格式 `string.split(separator, maxsplit)`
- `separator`：分隔符，默认为（可连续的）空格。注意，`split(" ")` 和 `split()` 是不同的，前者对于连续的空格会一个个进行分割，返回的列表长度会比较大
- `maxsplit`：分割次数，默认为 -1，即分割所有。如果指定，则分割 `num-1` 次，返回的列表长度最多为 `num`

```shell
>>> input().split()
3  5  7
['3', '5', '7']
>>> input().split(" ")
3  5  7
['3', '', '5', '', '7']
>>> input().split(":")
3::5::7
['3', '', '5', '', '7']
>>> input().split(maxsplit=0)
3 5 7 8
['3 5 7 8']
>>> input().split(maxsplit=-1)
3 5 7 8
['3', '5', '7', '8']
>>> input().split(maxsplit=1)
3 5 7 8
['3', '5 7 8']
```

### `map(int, input().split())`

将列表中的每个字符串转换为整数，返回一个**由多个整数构成的迭代器** 

- 注意返回的是一个 map 的迭代器，而不是一个列表
- 如果想要得到列表，需要使用 `list()` 函数，例如 `list(map(int, input().split()))`
- 注意，因为输入保证是整数才直接使用 `int`，如果有浮点数的可能性，需要使用 `float`。如果也不一定是 `float`，需要考虑直接继续字符串进行处理
- 如果已经知道有多少个参数，例如已经知道只有 2 个数，可以使用 `a, b = map(int, input().split())` 直接赋值，但是如果数量不对应会出现问题

```shell
>>> map(int, input().split())
3 5   7  8
<map object at 0x0000021D3D3A3D30>
>>> list(map(int, input().split()))
3 5   7  8
[3, 5, 7, 8]
>>> a, b, c, d = map(int, input().split())
3 5   7  8
>>> print(f"{a}-{b}-{c}-{d}")
3-5-7-8
>>> a, b, c, d, e = map(int, input().split())
3 5   7  8
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: not enough values to unpack (expected 5, got 4)
>>> a, b, c, d = map(int, input().split())
3.1 5.2   7.3  8.4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '3.1'
>>> a, b, c, d = map(int, input().split())
3.0 5.0   7.0  8.0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '3.0'
```

### `join`: `split` 的逆操作

在此同时引入 `join` 函数的使用方法。回顾 `s.split(sep)` 函数，是将 str 类型的 s 按照 str 类型的分隔符 sep 进行分割，得到一个 list 类型的分割结果，这个 list 的每个元素都是分割得到的字符串。即给定分隔符 sep 的情况下，split 输入一个长字符串，输出一个分割得到的字符串列表。

`join` 函数的使用方式为 `sep.join(lst)`，sep 同样是一个 str 类型的分隔符，lst 常常是一个字符串列表，最终得到一个拼接得到的长字符串，按列表中的字符串顺序，两两之间用 sep 拼接。即给定分隔符 sep 的情况下，join 输入一个字符串列表，输出一个拼接得到的长字符串。

```python
>>> lst = ["3", "5", "7", "8"]
>>> " ".join(lst)
3 5 7 8
```

> lst 也不一定就是字符串列表，如感兴趣详细可见官方文档：[str.join - Python 3.12.3 documentaion](https://docs.python.org/3/library/stdtypes.html#str.join)

!!! tip "易错点"
    `sep.join(lst)` 的 lst 要求是一个字符串列表，务必保证 lst 的每个元素都是字符串，例如 lst 的元素如果是数值类型，那么就会报错。

## 基础输出理解

### 最简单的方式

```python
print(a, b, c)
```

直接输出 `a`, `b`, `c` 三个量，并自动在两两之间添加空格，最后自动在末尾添加换行符 `\n`

### 了解 `print` 的参数

格式：`print(object(s), sep=separator, end=end, file=file, flush=flush)`

- `object(s)`：要打印的对象，可以是多个，用逗号隔开
- `sep`：分隔符，默认为一个空格，所以原始的 `print` 会自动在两两之间添加空格，可以将其改为 `""` 或者其他字符

```shell
>>> a, b, c = 12, 18.0, "Python"
>>> print(a, b, c)
12 18.0 Python
>>> print(a, b, c, sep="")
1218.0Python
>>> print(a, b, c, sep="!")
12!18.0!Python
```

- `end`：结束符，默认为换行符 `\n`，可以将其改为 `""`（从而不换行）或者其他字符

```shell
>>> for i in range(3)
...     print(a, b, c, sep="")
...
1218.0Python
1218.0Python
1218.0Python
>>> for i in range(3)
...     print(a, b, c, end="")
...
12 18.0 Python12 18.0 Python 1218.0 Python>>>
>>> for i in range(3)
...     print(a, b, c, end="$")
...
12 18.0 Python$12 18.0 Python$12 18.0 Python$
```

- `file`, `flush`：较少用，感兴趣可自主了解

### 格式化字符串 (Format String)

- 分为 3 种，分别是 `%` 格式化、`str.format()` 和 `f-string`
- `%` 是最原始的方法，`str.format()` 在 Python 2.5 之后出现，`f-string` 在 Python 3.6 之后出现
- 个人认为简洁性逐渐提升，推荐编程时选择 `str.format()` 和  `f-string` 这两种方式

```python
name, age, height = "Alice", 18, 160.0

# %
print("My name is %s. I'm %d years old, and I'm %.2f cm tall." % (name, age, height))

# format()
print("My name is {:s}. I'm {:d} years old, and I'm {:.2f} cm tall.".format(name, age, height))
print("My name is {}. I'm {} years old, and I'm {} cm tall.".format(name, age, height))

# f-string
print(f"My name is {name:s}. I'm {age:d} years old, and I'm {height:.2f} cm tall.")
print(f"My name is {name}. I'm {age} years old, and I'm {height} cm tall.")
```

需要注意的是，`format` 和 `f-string` 这两种方法在字符串中 `{}` 具有特殊含义，因此如果想要原样输出 `{` 或 `}`，需要使用 `{{` 或 `}}` 进行转义。同理，`%` 格式化方法中，想要输出 `%` 需要使用 `%%` 进行转义。

```python
print("{{}}".format())  # {}
print(f"{{}}")  # {}
print("%%" % ())  # %

print("%".format())
print(f"%")
print("{}" % ())
```

`format` 方法和 `f-string` 方法都有 `{X:Y}` 的形式，其中

- `f-string` 的 `X` 是需要输出的值，`Y` 是格式化控制符
- `format` 的 `X` 是需要输出的值的**索引**，`Y` 也是格式化控制符；`X` 也可以是一个标识符，但是需要在 `format` 方法中指定 `X` 的值
- 在不需要格式化控制符时，`:Y` 可以省略

```python
print("My name is {}. I'm {} years old, and I'm {} cm tall.".format(name, age, height))
# My name is Alice. I'm 18 years old, and I'm 160.0 cm tall.
print("My name is {2}. I'm {0} years old, and I'm {1} cm tall.".format(name, age, height))
# My name is 160.0. I'm Alice years old, and I'm 18 cm tall.
print("My name is {2:.2f}. I'm {0:s} years old, and I'm {1:d} cm tall.".format(name, age, height))
# My name is 160.00. I'm Alice years old, and I'm 18 cm tall.
print("My name is {n}. I'm {a} years old, and I'm {h} cm tall.".format(a=age, n=name, h=height))
# My name is Alice. I'm 18 years old, and I'm 160.0 cm tall.
```

格式化控制符可以控制左、右、居中对齐，以及宽度、精度等，具体可以参考官方文档：[Format Specification Mini-Language - Python 3.12.3 documentaion](https://docs.python.org/3/library/string.html#format-specification-mini-language)。需要注意的是，当控制的整体宽度大于实际宽度时，几种格式化字符串默认的左右对齐方式有所不同，展示如下：

```python
# %
print("My name is %9s. I'm %9d years old, and I'm %9.2f cm tall." % (name, age, height))
# My name is     Alice. I'm        18 years old, and I'm    160.00 cm tall.

# format()
print("My name is {:9s}. I'm {:9d} years old, and I'm {:9.2f} cm tall.".format(name, age, height))
# My name is Alice    . I'm        18 years old, and I'm    160.00 cm tall.

# f-string
print(f"My name is {name:9s}. I'm {age:9d} years old, and I'm {height:9.2f} cm tall.")
# My name is Alice    . I'm        18 years old, and I'm    160.00 cm tall.
```

可以看到，对于字符串类型，`%` 默认右对齐，`format` 和 `f-string` 方法默认左对齐；而对于 `int` 和 `float` 类型，三种方法都默认右对齐。推荐编程时不要直接利用这种默认对齐特性，不管你偏好使用哪种格式化字符串方法，建议使用格式控制符 `<` 或 `>`，或者使用 `str.ljust(width)` 或 `str.rjust(width)` 来进行对齐。

## 基础数据类型 (Data Type)

列举如下常见数据类型：

- 数值类型 (numeric type)
    - 整数 (integer): int
    - 浮点数 (floating point number): float
    - 复数: complex
- 布尔类型 (boolean type)
    - 布尔: bool
- 序列类型 (sequence type)
    - 字符串 (string): str
    - 列表: list
    - 元组: tuple 
- 映射类型 (mapping type)
    - 字典 (dictionary): dict
- 集合类型 (set type)
    - 集合: set

!!! tip "Remark"
    事实上还有很多内置的数据类型，详见官方文档 [Built-in Types - Python 3.12.3 Documentation](https://docs.python.org/3/library/stdtypes.html)。
    
    根据官方文档 [Numeric Types - int, float, complex - Python 3.12.3 Documentation](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)，布尔类型事实上是 int 类型的子类型 (subtype)，具有数值类型的一些特性。

### 可变 (mutable) 类型与不可变 (immutable) 类型

!!! info "可变和不可变"
    > 参考官方文档 [Built-in Types - Python 3.12.3 Documentation](https://docs.python.org/3/library/stdtypes.html) 和 [Data Model - Python 3.12.3 Documentation](https://docs.python.org/3/reference/datamodel.html)。

    值可以更改的对象 (object) 被称为可变 (mutable) 的，一旦创建值就不可更改的对象称为不可变 (immutable) 对象。
    
    对象的可变性由其类型 (type) 决定，因此有可变类型与不可变类型。

- **不可变**类型：int, float, complex, bool, str, tuple
- **可变**类型：list, set, dict

可以发现，int float complex bool 这种仅由一个或两个数值简单地构成的数值/布尔类型是不可变的。由任意多元构成的 str 和 tuple 也都不可变，这是需要特别注意的，特别是要对比它们和可变的 list, set, dict 的区别。

!!! tip "Remark"
    - 元组和列表都是序列类型，元组因为不可变使用限制更多，但是其操作所需资源开销更少
    - 对应地，我们认为集合和字典都是无序的，然而根据官方文档 [OrderedDict objects - Python 3.12.3 documentaion](https://docs.python.org/3/library/collections.html#ordereddict-objects)，Python3.7 之后字典开始保证按照插入顺序，因此可能会在实际编程中发现字典具有一些有序结构的特性，但实际上仍为无序结构
    - 字符串和列表在切片、拼接操作上表现类似，但是由于有可变与不可变的区别，因此不能像列表一样对特定的字符进行修改

### `int`, `float`, `complex`, `bool`

#### `int`

- `bin()`, `oct()`, `hex()` 分别能将 int 转换为对应的二进制/八进制/十六进制表示，返回 str 类型
- `int(value, base)`：将一个 str 按照 base 进制解释，转换为 int 类型后返回
    - `value`: 要求是 str 类型，要求能够按照 base 进制解释后转换为 int
    - `base`: 要求是 int 类型，实际上常常有数值限制，如要求 `2<=base<=36` 或 `base=0`

各进制的字面量表示：

- 十进制 (decimal): 6, -3
- 二进制 (binary): 0b101（前缀 0b 或 0B）
- 八进制 (octal): 0o10（前缀 0o 或 0O）
- 十六进制 (hexadecimal): 0x1A（前缀 0x 或 0X）

#### `float`

存在精度问题，会存在误差；绝对值非常大或非常小都可能会溢出

#### `complex`

创建一个复数：

```
a = 3 + 5j
a = 3 + 5J
a = complex(3, 5)
```

- `a.real` 和 `a.imag` 分别可以获得上面的复数的实部 (real component) 和虚部 (imaginary component)
- 注意实部和虚部的数据类型都是 `float`，所以在以上的例子中会有 `a.real=3.0`, `a.imag=5.0`

!!! tip "数值类型混合运算"
    `int`, `float`, `complex` 这三种数值类型之间的混合运算会自动进行类型转换，转换规则具体如下：

    - `int` 和 `float` 混合运算，`int` 会被转化为 `float`
    - `int` 和 `complex` 混合运算，`int` 会被转化为 `complex`
    - `float` 和 `complex` 混合运算，`float` 会被转化为 `complex`

    这是因为 `int` 是比 `float` 更“窄” (narrow) 的数据类型，`float` 是比 `complex` 更“窄”的数据类型，因此在混合运算时较“窄”的数据类型会先转换为较“宽”的数据类型，然后再进行运算。这在后面的[运算基础 - 基础数学运算符](#_8)中会有所体现。

    > 官方文档 [Numeric Types - int, float, complex - Python 3.12.3 documentation](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex) 的原文说明：Python fully supports mixed arithmetic: when a binary arithmetic operator has operands of different numeric types, the operand with the “narrower” type is widened to that of the other, where integer is narrower than floating point, which is narrower than complex. A comparison between numbers of different types behaves as though the exact values of those numbers were being compared.

#### `bool`

- 只能取 `True` 或者 `False` 两种值 **（首字母大写）**
- Python3 中，`bool` 是 `int` 的子类（即可认为 `bool` 是一种特殊的 `int`），`True` 和 `False` 对应的 `int` 中的值分别为 1 和 0
- 当 `int` 需要被强行解释为 `bool` 时，当且仅当这个 `int` 的值恰好等于 0 时才会被解释为 `False`，否则就会被解释为 `True`，例如

```python
if a:
  print("a is interpreted as True")
```

如果确定 `a` 是一个 `int`，则当 `a` 的值是 1, 32873, -1 等所有非零值时，这行 print 都会被执行。只有 `a` 的值为 0 时，这行 print 才不会被执行。

!!! tip "Remark"
    `bool` 是 `int` 的子类，所以其与数值类型混合运算时也可以参考前面的混合运算准则。 

## 基础运算

### 基础数学运算符

```python
a = 5 + 10       % a = 15
b = 100 - 5      % b = 95
c = 8 * 9        % c = 72
d1 = 10 / 4      % d1 = 2.5
d2 = 8 / 4       % d2 = 2.0
e1 = 10 // 4     % e1 = 2
e2 = 3.8 // 0.7  % e2 = 5.0
f1 = 9 % 4       % f1 = 1
f2 = 3.8 % 0.7   % f2 = 0.30000000000000004
g = 2 ** 3       % g = 8
```

注意以下几点并思考为什么：

- `d1`, `d2`, `e2`, `f2` 都是 float，`e1` 和 `f1` 都是 int
- `f2` 不严格为 0.3
- `2.1 - 2.0 == 0.1` 的返回值为 False

### 运算符优先级 (precedence) 与结合性

同一复杂表达式中，运算符按优先级自高到底进行计算，互相会发生冲突的同优先级运算符按照结合性顺序计算。根据官方文档：[Operator precedence - Python 3.12.3 documentaion](https://docs.python.org/3/reference/expressions.html#operator-precedence)，运算符优先级如下表所示：

| 运算符 | 描述 |
| :---: | :---: |
|(expressions...), [expressions...], {key: value...}, {expressions...} | 绑定/括号表达式, 列表, 字典, 集合 |
| x[index], x[index:index], x(arguments...), x.attribute | 下标, 切片, 函数调用, 属性引用 |
| await x | await 表达式（较少用） |
| ** | 幂运算 |
| +x, -x, ~x | 正, 负, 按位取反 |
| *, @, /, //, % | 乘, 矩阵乘, 除, 整除, 取余 |
| +, - | 加, 减 |
| <<, >> | 左移, 右移 |
| & | 按位与 |
| ^ | 按位异或 |
| \| | 按位或 |
| in, not in, is, is not, `<`, `<=`, `>`, `>=`, `!=`, `==` | 比较运算符，包括成员资格测试和身份测试 |
| not x | 布尔“非” |
| and | 布尔“与” |
| or | 布尔“或” |
| if – else | 条件表达式 |
| lambda | Lambda 表达式 |
| := | 海象运算符（较新的特性） |

关于结合性，除了**幂运算** (exponentiation) 和**条件表达式** (conditional expressions) 是**从右到左的结合性**之外，其他同级运算符都是从左到右的结合性。特别地，比较运算符在出现链接时会被特殊处理，例如 `a < b < c` 会被视为 `a < b and b < c` 进行计算，可以参考官方文档：[Comparisons - Python 3.12.3 documentaion](https://docs.python.org/3/reference/expressions.html#comparisons)。

### `math` 库常见运算

#### 如何使用 `math` 库

首先了解如何导入并使用 `math` 库中的函数或常数。以导入其中的向下取整函数 `floor` 和圆周率常数 `pi` 为例，一种方法是直接导入 `math`，这样就需要使用 `math.x` 来说明你想要调用的 `x` 是属于 `math` 这个库的。

```python
import math
print(f"floor(3.5) = {math.floor(3.5)}, pi = {math.pi}")
# floor(3.5) = 3, pi = 3.141592653589793
```

另一种方法是直接指明你需要 `math` 库中的哪几个函数/常数，这样调用它们时就不需要加前缀 `math.`

```python
from math import floor, pi
print(f"floor(3.5) = {floor(3.5)}, pi = {pi}")
# floor(3.5) = 3, pi = 3.141592653589793
```

但需要注意，这种指明的方式可能会造成“命名冲突”。比如说如果一个叫做 `fool` 的库里面也有一个和 `math.floor` 功能不同的 `floor` 的函数，然后你写下了

```python
from math import floor
from fool import floor
```

那么先导入的 `math` 库中的 `floor` 就会被 `fool` 库中的 `floor` 覆盖，如果你还下意识地认为 `floor` 是 `math` 库的 `floor` 就会出错。带库前缀去使用是一种解决方法，这里给出另外一种解决方法，即让 `fool` 库中的 `floor` 在这段代码中被重命名为 `floor2` 或其他名字：

```python
from math import floor
from fool import floor as floor2
```

如果你想使用 `math` 库中很多的函数/常量，然后你既苦于每次调用时都写前缀 `math.`，也不想在 `from math import` 后面如数家珍地把每个都写出来，那么你可以使用一种具有风险的导入方式，把 `math` 库中所有的函数/常量都导入进来：

```
from math import *
```

显而易见，导入了所有的函数/常量，将会导致和其他库“命名冲突”的概率大大增加，所以这种导入方式需要谨慎使用。

#### `math` 库常见函数/常量

并不依照考试列举，而只列举实际编程中较常用的

- `floor`: 向下取整
- `ceil`: 向上取整
- `abs`, `fabs`: 取绝对值，前者返回 `int`，后者返回 `float`
- `exp(x)`: 计算指数 $e^x$
- `log(x, n)`, `log10(x)`: 分别计算对数 $\log_nx$ 和 $\log_{10}x$，前者可以覆盖后者的功能
- `sqrt(x)`: 计算平方根 (square root) $\sqrt{x}$
- `sin`, `cos`, `tan`: 三角函数，**输入要求为弧度制**
- `radians`: 将一个角度值转换成弧度值（等价于乘上 $\frac{\pi}{180}$）
- `e`, `pi`: 自然底数 $e$ 和圆周率 $\pi$

其实都是英文的缩写，对照英文就会觉得取名还是比较自然的。

## 特殊语句

### 赋值 (assignment) 语句

**赋值语句是没有返回值的。**与 C 语言赋值后返回所赋的值不同，Python 中的赋值语句是没有返回值的，因此 `a = (b = c)` 这种语句在语法上就不被允许。

但特殊的，Python 特别允许连等式的存在，即 `a = b = c`。对于这种连等式，会先算出最右侧的表达式的值，然后从左到右依次赋值。对于这个例子，就是先计算出 `c` 的值，然后把这个值赋值给 `a`，然后再把这个值赋值给 `b`。

对于 `a1, b1, c1 = a2, b2, c2` 类型的赋值，则会先计算 a2, b2, c2 的值，然后以此赋值给 a1, b1, c1。

> 更多关于赋值语句的细节可以阅读官方文档：[Assignment statements - Python 3.12.3 documentaion](https://docs.python.org/3/reference/simple_stmts.html#assignment-statements)。

!!! tip "易错点"
    此处容易出错的点除了计算顺序之外，还有值传递和引用传递的问题。
    
    考虑 `a = b = []`，由于列表赋值是将其引用进行赋值，因此 `a` 和 `b` 得到的是同一个引用值，即这样会导致 `a` 和 `b` 是同一个列表，修改其中一个会导致另一个也改变。

### 循环语句中的 else 子句

> 参考官方文档：[break and continue Statements, and else Clauses on Loops - Python 3.12.3 documentaion](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)

for 循环和 while 循环都可以携带 else 子句，官方文档中对执行 else 子句的描述为：

> In a `for` loop, the else clause is executed after the loop reaches its final iteration.
>
> In a `while` loop, it’s executed after the loop’s condition becomes false.
>
> In either kind of loop, the `else` clause is **not** executed if the loop was terminated by a `break`.

翻译一下就是，当循环不被 `break` 打断、正常地因为停止条件结束（for 循环的最后一次迭代结束、while 循环的条件变成 False）的时候，就会执行 else 子句，反之就不会执行。

Else 子句常常用于节约 flag 的使用。如果不使用 else 子句，往往需要用一个 flag 来表示是否因为 `break` 而结束循环，然后在循环结束后判断这个 flag 是否为 True，而使用 else 子句则可以直接在循环正常结束后执行一些操作。

## 数据类型进阶

对于较为进阶的几种常见数据类型，前文已经提及：

- 字符串、元组、列表是序列类型
- 字符串和元组是不可变类型
- 列表、集合和字典是可变类型

而与序列类型对应地，我们认为集合与字典是无序类型，当然字典实际上已经在较新版本的 Python 中出现了一些有序的特性，前文已经说过，但是我们仍然认为它是无序的。

### 列表 (list)

常见的列表操作如下所示：

- `L.append(x)`：在列表 `L` 尾部追加一个新元素 `x`。几乎是最常用的列表操作。
- `L.extend(L2)`：将另一个列表 `L2` 扩充到列表 `L` 的后面。也可以使用**列表加法**，等价于 `L = L + L2`。
- `L.clear()`：移除列表 `L` 的所有元素
- `L.count(x)` 计算列表 `L` 中 `x` 出现的次数
- `L.copy()`：拷贝一份列表 `L`，拥有于 `L` 不同的内存空间，等价于 `L[:]`。
- `L.index(value[,start[,stop]])`：计算在指定范围内 `value` **第一次**出现的下标，如果有多个只会返回第一个元素的下标。这种写法的意思是，你可以采用如下三种方式调用这个函数：
    - `L.index(value)`：在整个列表中查找 `value` 的下标
    - `L.index(value, start)`：在从下标 `start` 开始到列表末尾的范围内查找 `value` 的下标
    - `L.index(value, start, stop)`：在从下标 `start` 开始到下标 `stop` 的范围内查找 `value` 的下标
- `L.insert(index, x)`：在下标 `index` 的位置插入 `x`
- `L.pop(index)`：返回并删除下标为 `index` 的元素，如果不输入 `index`，默认返回并删除最后一个元素
- `L.remove(value)`：删除值为 `value` 的**第一个**元素，如果有多个只会删除第一个
- `L.reverse()`：反转列表 `L`，等价于 `L = L[::-1]`
- `L.sort()`：对列表元素排序，有参数 `key` 和 `reverse`，分别表示排序的依据和是否逆序
    - `reverse` 默认为 `False`，表示升序排序
    - `key` 参数是很好用的一个参数，可以输入一个返回“依据”函数或者用于查找“依据”的列表

需要注意的是，`index` 和 `remove` 对于列表中存在多个匹配的元素时，会对第一个匹配的元素进行操作。

除了可以替代 `extend` 方法的列表加法之外，列表还可以进行一种数字乘法，即 `L * n`，表示将列表 `L` 重复 `n` 次。需要注意的是，对于一维列表会进行数值的拷贝，拷贝生成的数值之间不共享内存；对于高维的列表会进行引用的拷贝，拷贝生成的各个引用对应的内存空间是同一个。

```python
L = [1, 2, 3]
L1 = L * 3
# L1 = [1, 2, 3, 1, 2, 3, 1, 2, 3]
L1[0] = 4
# L1 = [4, 2, 3, 1, 2, 3, 1, 2, 3]
L2 = [L] * 3
# L2 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
L2[0][0] = 4
# L2 = [[4, 2, 3], [4, 2, 3], [4, 2, 3]]
```

### 集合 (set)

创建空集合往往只能用 `set()`，而不能用 `{}`，因为 `{}` 会被解释为创建空字典。

集合中的元素具有如下特性：

- 可哈希性：元素必须是不可变对象，从而可以被哈希
- 无序性：元素没有顺序，因此不能通过下标访问
- 唯一性：集合中的元素不会重复

集合的增删操作：

- `S.add(x)`：增加元素 `x` 到集合 `S` 中
- `S.discard(x)`：删除元素 `x`，如果 `x` 不在集合 `S` 中无效果
- `S.remove(x)`：删除元素 `x`，如果 `x` 不在集合 `S` 中会报错
- `S.clear()`：清空集合 `S`

类似于列表，集合可以用 `len(S)` 来获得集合的长度，用 `x (not) in S` 来判断 `x` 是否在集合 `S` 中，用 `max(S)` 和 `min(S)` 来获得集合中的最大值和最小值，用 `sum(S)` 来获得集合中所有元素的和。

> 不仅列表和集合，字典也都有这些操作，只是统计的是字典的键。

考虑到读者可能对数学中集合的一些术语不太熟悉，在此折叠了一些对集合（真）子集/超集、交集、并集、差集、对称差集这些术语的解释。

??? info "集合术语说明"
    - 对于集合 $A$ 和集合 $B$，如果 $A$ 中的所有元素都在 $B$ 中，那么 $A$ 是 $B$ 的**子集**，$B$ 是 $A$ 的**超集**
    - 如果 $A$ 是 $B$ 的子集，但不等于 $B$（也就是至少有 1 个 $B$ 中的元素不属于 $A$），那么 $A$ 是 $B$ 的**真子集**，$B$ 是 $A$ 的**真超集**
    - $A\cap B$: $A$ 和 $B$ 的**交集**，是一个新的集合，包含 $A$ 和 $B$ 中**共有**的元素
    - $A\cup B$: $A$ 和 $B$ 的**并集**，是一个新的集合，包含 $A$ 和 $B$ 中**所有**的元素
    - $A - B$: $A$ 和 $B$ 的**差集**，是一个新的集合，包含 $A$ 中**不在** $B$ 中的元素
    - $A$ 和 $B$ 的**对称差集**，是一个新的集合，包含 $A$ 和 $B$ 中**不共有**的元素，实际上是 $(A - B) \cup (B - A)$

因此与集合之间运算相关的方法有：

- `s1.issubset(s2)`：判断 `s1` 是否是 `s2` 的子集
- `s1.issuperset(s2)`：判断 `s1` 是否是 `s2` 的超集
- `s1.union(s2)`, `s1 | s2`：返回 `s1` 和 `s2` 的并集
- `s1.intersection(s2)`, `s1 & s2`：返回 `s1` 和 `s2` 的交集
- `s1.difference(s2)`, `s1 - s2`：返回 `s1` 和 `s2` 的差集
- `s1.symmetric_difference(s2)`, `s1 ^ s2`：返回 `s1` 和 `s2` 的对称差集

注意，集合的交集、并集、差集、对称差集都不会改变原集合的值，而是返回一个新的集合。

```python
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1.union(s2))
print(s1 | s2)
# {1, 2, 3, 4}
print(s1.intersection(s2))
print(s1 & s2)
# {2, 3}
print(s1.difference(s2))
print(s1 - s2)
# {1}
print(s1.symmetric_difference(s2))
print(s1 ^ s2)
# {1, 4}
```

以及关系运算符：

- `s1 == s2`：判断两个集合是否相等，以及 `s1 != s2`
- `s1 < s2`：判断 `s1` 是否是 `s2` 的真子集
- `s1 > s2`：判断 `s1` 是否是 `s2` 的真超集
- `s1 <= s2`：判断 `s1` 是否是 `s2` 的子集
- `s1 >= s2`：判断 `s1` 是否是 `s2` 的超集

### 字典 (dict)

字典的创建可以使用 `{}` 或者 `dict()`，删除有 `del`, `pop()`（用法类似 `list.pop`），清空有 `clear()`。

与集合相似地，字典的键必须可哈希（即必须是不可变对象），但是字典的值没有这种限制。

如果不加说明，直接使用 `len`, `max`, `min`, `sum`, `in` 这些操作，则默认对字典的键进行操作，而不是包含键和值的元组。字典自身常用的方法有：

- `D.keys()`：返回字典 `D` 的所有键
- `D.values()`：返回字典 `D` 的所有值
- `D.items()`：返回字典 `D` 的所有键值对，返回的是一个元组的列表
- `D.get(key[,default])`：返回字典 `D` 中键 `key` 对应的值，如果 `key` 不存在，返回 `default`，默认为 `None`
- `D.pop(key[,default])`：返回并删除字典 `D` 中键 `key` 对应的值，如果 `key` 不存在，返回 `default`，默认为 `None`

## 函数

### 函数参数 (parameter/argument)

> 更多内容可以参考官方文档：[More on Defining Functions - Python 3.12.3 documentation](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions)

在定义函数时，函数的参数在中文常称为“形参”，对应英文 parameter 或 formal parameter；而在实际传参时，函数的参数在中文常称为“实参”，对应英文的 argument 或 actual parameter。但是实际上这两个术语区分并不是非常清晰，下文中有的地方就直接称参数。

定义函数时，部分形参可以指定默认值，这些参数在实际调用函数时可以不传入，而使用默认值。这种参数就称为可选参数 (optional arguments)，可选参数必须放在必选参数 (mandatory argument) 的后面，否则会报错。

!!! warning "可选参数默认值的陷阱"
    可选参数的默认值只会被构造一次。如果默认值是一个可变对象，那么每次调用函数时，如果没有传入这个参数，那么这个参数会是同一个可变对象的引用，例如就会有
    ```python
    def f(a, L=[]):
        L.append(a)
        return L
    print(f(1))
    # [1]
    print(f(2))
    # [1, 2]
    ```

根据传参方式的不同，实参分为两种：位置参数 (positional argument) 和关键字参数 (keyword argument)。位置参数是指在调用函数时，按照函数定义的参数顺序传入的参数，而关键字参数是指在调用函数时，通过 `key=value` 的形式传入的参数。

```python
def f(a, b, c):
    return a + b + c

print(f(1, 2, 3))        # positional argument
print(f(a=1, b=2, c=3))  # keyword argument
print(f(1, c=3, b=2))    # mixed
```

当一个函数的最后一个形参的形式为 `**name` （`name` 可以替换成别的参数名称）时，它会接收一个**字典**，包含除与形式参数对应的参数之外的所有关键字参数，例如
```python
def f(a, c, **keywords):
    print(a)
    print(c)
    print(keywords)

f(1, b=2, c=3, d=4)
# 1
# 3
# {'b': 2, 'd': 4}
```

这可以与形式为 `*name` 的形参组合，该形式参数接收包含形式参数列表之外的位置参数的**元组**。注意，`*name` 必须出现在 `**name` 之前。组合使用时，有
```python
def f(a, c, *args, **keywords):
    print(a)
    print(c)
    print(args)
    print(keywords)

f(1, 5, 3, 4, b=5, d=6)
# 1
# 5
# (3, 4)
# {'b': 5, 'd': 6}
```

### 解包 (unpacking) 参数列表

> 参考官方文档 [Unpacking Argument Lists - Python 3.12.3 documentaion](https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists)

这种情况出现于，希望传递给函数的所有**位置参数**都已经在**列表、元组或者集合**之中，那么就可以利用 `*` 运算符解包出这些实参，然后传递给函数。

```python
>>> list(range(3, 6))
[3, 4, 5]
>>> args = [3, 6]
>>> list(range(*args))
[3, 4, 5]
```

如果希望以**关键字参数**的形式传递参数，那么可以使用 `**` 运算符解包出**字典**中的键值对。

```python
def f(a, b, c):
    return a + b + c

d = {'a': 1, 'b': 2, 'c': 3}
print(f(**d))
# 6
```

### Lambda 表达式

> 参考官方文档 [Lambda Expressions - Python 3.12.3 documentaion](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)

Lambda 表达式是创建匿名函数的一种方法，例如 `lambda a, b: a + b` 对应的函数即为
```python
def fun(a, b):
    return a + b
```

!!! example "Lambda 表达式的简单应用例子"
    此处的 Lambda 表达式的输入为一个元组，输出为这个元素的下标为 1 的元素，将其作为元组列表 `pairs` 的 `sort` 方法的 `key` 参数，以及就是以每个元组的第二个元素作为其排序的依据。
    ```python
    >>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
    >>> pairs.sort(key=lambda pair: pair[1])
    >>> pairs
    [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
    ```

    如果不使用 Lambda 表达式创建匿名函数，就需要显式地创建函数，即：
    ```python
    >>> def cmp(pair):
    ...     return pair[1]
    ...
    >>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
    >>> pairs.sort(key=cmp)
    >>> pairs
    [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
    ```

## 文件基础

### 文件操作流程

- 打开文件：`file = open(filename, mode)`
- 处理文件：
    - 读操作，例如 `file.read()`, `file.readline()`, `file.readlines()`
    - 写操作，例如 `file.write()`, `file.writelines()`
- 关闭文件：`file.close()`

### 文件打开模式

| 模式 | 含义 |
| :---: | :---: |
| `'r'` | 只读模式，文件必须存在 |
| `'w'` | 写入模式，文件不存在则创建，存在则覆盖 |
| `'x'` | 独占创建模式，文件不存在则创建，存在则报错 |
| `'a'` | 追加模式，文件不存在则创建，存在则追加 |
| `'b'` | 二进制模式，与其他模式结合使用，例如 `'rb'`, `'wb'` |
| `'t'` | 文本模式，与其他模式结合使用，例如 `'rt'`, `'wt'`（默认方式，如果不加 `t` 或者 `b` 默认为 `t`） |
| `'+'` | 读写模式，与 `r/w/x/a` 结合使用，例如 `'r+'`, `'w+'`，同时允许读和写 |