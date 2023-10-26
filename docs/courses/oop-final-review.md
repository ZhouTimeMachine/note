# OOP Final Review

!!! info "PTA homework of ZJU *Object Oriented Programming*, 2022 Spring & Summer."

## Week9

**Q1.** 对象间赋值将调用拷贝构造函数。(T/F)

??? general "Answer"
	F。对象间赋值，如果是同类对象，有相关类型的赋值运算符重载的话优先调用重载的赋值运算符，否则会调用自动生成的 memberwise assignment，即自动的赋值运算。
	
	如果是不同类型的对象赋值，那么如果没有写相关类型的赋值运算符的重载的话，如果存在相关类型的构造函数，那么是会调用那个构造函数的。

**Q2.** 设类AA已定义，假设以下语句全部合法，哪些语句会触发调用拷贝构造函数（）。

```cpp
AA a, b; //1
AA c(10, 20); //2
AA d(c); //3
AA e = d; //4
```

A.2

B.3

C.4

D.3 和 4

??? general "Answer"
	D。1 是默认构造，2 是含参构造，
	
	3 是标准的复制构造，
	
	4 虽然看似有 =，其实也是复制构造。

**Q3.** 假设MyClass是一个类，则该类的拷贝初始化构造函数的声明语句为（）

A. `MyClass&(MyClass x);`

B. `MyClass(MyClass x);`

C. `MyClass(MyClass &x);`

D. `MyClass(MyClass *x);`

??? general "Answer"
	C。声明拷贝构造函数：A(const A & a) 或者 A(A & a)。
	
	虽然感觉加个 const 更好，但是没有 const 也行。

**Q4.** 下列关于异常类的说法中，错误的是。（）

A. 异常类由标准库提供，不可以自定义

B. C++的异常处理机制具有为抛出异常前构造的所有局部对象自动调用析构函数的能力

C. 若catch块采用异常类对象接收异常信息，则在抛出异常时将通过拷贝构造函数进行对象复制，异常处理完后才将两个异常对象进行析构，释放资源

D. 异常类对象抛出后，catch块会用类对象引用接收它以便执行相应的处理动作

??? general "Answer"
	A。可以自定义异常类。
	
	异常抛出，抛出位置构造的所有局部对象应该被释放。
	
	catch块可以用对象或者引用接受异常信息。
	
	其中使用对象接收异常对象是比较好的，因为可以将异常对象拷贝到 catch 块中，空间是确定的；
	
	而引用的话，可能异常对象就在某个被释放的栈空间中，不是很安全。

**Q5.** 下列哪一个说法是错误的?（）

A. 当用一个对象去初始化同类的另一个对象时,要调用拷贝构造函数

B. 如果某函数有一个参数是类A的对象,那么该函数被调用时,类A的拷贝构造函数将被调用

C. 如果函数的返回值是类A的对象时，则函数返回时，类A的拷贝构造函数将被调用

D. 拷贝构造函数必须自己编写

??? general "Answer"
	D。这道题本身没什么难度，但是作为复习比较适合。
	
	A、B、C 覆盖了课上讲到的拷贝构造函数被调用的三种情况。（尽管编译器可能会进行优化）

**Q6.** 假设A是一个类的名字,下面哪段程序不会用到A的拷贝构造函数？（）

A. A a1,a2; a1=a2;

B. void func( A a) { cout<<"good"<< endl; }

C. A func() { A tmp; return tmp;}

D. A a1; A a2(a1);

??? general "Answer"
	A。
	
	A 是赋值。
	
	B 的参数需要拷贝构造。
	
	C 是返回值需要拷贝构造。
	
	D 是最基本的拷贝构造。（以上都不考虑编译器优化）
	
	如果 A 写成 `A a1=a2;`，那么也是会用到拷贝构造函数的。

## Week10

**Q1.** 多数运算符可以重载，个别运算符不能重载，运算符重载是通过函数定义实现的。(T/F)

??? general "Answer"
	T。

!!! info "可以重载/不能重载的运算符"

	**可以重载**的运算符，有算术、赋值、比较、位运算、逻辑与或非、++/--等，比较特殊的有：

    - << 和 >>，或左移/右移，也可能是流插入/流提取
    - 逗号 , 也能重载
    - 指针中，-> 和 ->* 都能重载（虽然我并不太清楚 ->* 的重载的意义是什么……）
    - ()可以重载，在 minisql 中比较器就是重载了 () 
    - []也可以重载，像自定义数组类 Array 中就用到了 [] 的重载
    - new, new[], delete, delete[] 也能重载。

	**不能重载**的运算符有：

	- 成员相关的 . 和 .*
	- 宣誓主权的 ::
	- 三目运算符 ?:
	- sizeof 和 typeid（这两个竟然也算运算符）
	- 类型转换相关：static_cast, dynamic_cast, const_cast 和 reinterpret_cast

	只有**已有**的运算符能被重载。像 \*\* 就不能被重载，因为它被认为是"create"。

**Q2.** 对每个可重载的运算符来讲，它既可以重载为友元函数，又可以重载为成员函数，还可以重载为非成员函数。(T/F)

??? general "Answer"
	F。运算符重载只能重载为友元函数或者成员函数。
	
	非友元函数的非成员函数是不能被重载的。

**Q3.** 对单目运算符重载为友元函数时，可以说明一个形参。而重载为成员函数时，不能显式说明形参。(T/F)

??? general "Answer"
	T。这里说明了重载为友元函数和成员函数的区别。
	
	双目运算符的重载，友元函数需要说明两个形参，成员函数只需要说明一个形参。

	三目运算符不能重载。
	
	然而，一般地，单目运算符应该重载为成员函数，双目运算符应该重载为友元函数。

!!! info "特别地， ()、[]、->、->\* ，以及 = 等赋值运算符都**必须**被重载为成员函数。"

**Q4.** 重载运算符可以保持原运算符的优先级和结合性不变。(T/F)

??? general "Answer"
	T。

**Q5.** 重载 `operator+` 时，返回值的类型应当与形参类型一致。比如以下程序中，`operator+` 的返回值类型有错：(T/F)

```cpp
class A {

int x;
public:

	A(int t=0): x(t) {     }

    int operator+(const A& a1){ return x+a1.x;  }
};
```

??? general "Answer"
	F。重载 operator+，返回值类型不一定要和形参类型一致。

**Q6.** 下列关于运算符重载的描述中，（）是正确的。

A. 运算符重载可以改变操作数的个数

B. 运算符重载可以改变优先级

C. 运算符重载可以改变结合性

D. 运算符重载不可以改变语法结构

??? general "Answer"
	D。不太清楚语法结构是什么意思，可能是指 A、B、C 都不能改？
	
	运算符重载还如原来的运算符一般，操作数个数、优先级、结合性都是不变的。

**Q7.** 下列关于运算符重载的表述中，正确的是（）。

A. C++已有的任何运算符都可以重载

B. 运算符函数的返回类型不能声明为基本数据类型

C. 在类型转换符函数的定义中不需要声明返回类型

D. 可以通过运算符重载来创建C++中原来没有的运算符

??? general "Answer"
	C。类型转换运算符重载，如 double 应声明为 `operator double() const;`，可见是不需要声明返回类型的。

**Q8.** 能用友元函数重载的运算符是（）。

A. +

B. =

C. []

D.->

??? general "Answer"
	A。BCD 都是被要求“必须”用成员函数重载的。
	
	另外，A 作为二元运算符也只是“应该”用友元函数重载。
	
	其他“必须”用成员函数重载的运算符是->*和()。

**Q9.** 下列哪一项说法是不正确的?()

A. 运算符重载的实质是函数重载

B. 运算符重载可以重载为普通函数,也成员可以重载为成员函数

C. 运算符被多次重载时,根据实参的类型决定调用哪个运算符重载函数

D. 运算符被多次重载时,根据函数类型决定调用哪个重载函数

??? general "Answer"
	D。C 对 D 错。
	
	B 严格来说，应该是“友元函数”而不是单纯的普通函数。
	
	如 A 所说，运算符重载实质是函数重载，函数重载是不能仅根据返回类型区分的，而是通过参数列表区分的。

**Q10.** 如何区分自增运算符重载的前置形式和后置形式？（）

A. 重载时，前置形式的函数名是 ++operator，后置形式的函数名是 operator ++

B. 后置形式比前置形式多一个 int 类型的参数

C. 无法区分，使用时不管前置形式还是后置形式，都调用相同的重载函数

D. 前置形式比后置形式多一个 int 类型的参数

??? general "Answer"
	B。前置形式为 operater++()，后置形式为 operator++(int)。

**Q11.** 下列运算符中，不可以重载的是（）。

A. new

B. ++

C. .*

D. []

??? general "Answer"
	C。比较容易考到的不能重载的运算符有
	
	- 成员相关的 . 和 .*
	- Resolver ::
	- 三目运算符 ?:
	- sizeof、typeid 和类型转换相关还没有见过

## Week11

**Q1.** 若重载为友元函数，函数定义格式如下：()

```c++
<类型>operator<运算符>（<参数列表>）
{
<函数体>
}
```

??? general "Answer"
	PTA 上答案为 F。网络解释是需要 friend。我觉得没有道理，本应该就是 T。记录此怪题。

## Week12

**Q1.** Given:

```cpp
void f(int i) { cout << "Func1" << endl; }
template<class T>
void f(T t) { cout << "Func2" << endl; }
main() {
    f(2);
}
```

The result is :

A. Func1

B. Func2

C. nothing

D. undetermined

??? general "Answer"
	A。在有多个函数和函数模板名字相同的情况下，编译器如下处理一条函数调用语句：
	
	1. 先找参数完全匹配的普通函数（非由模板实例化而得的函数）
	2. 再找参数完全匹配的模板函数
	3. 再找经过自动类型转换后能够匹配的普通函数
	4. 都找不到，则报错
	
	匹配模板函数时，不会进行自动类型转换。
	
	此处已存在参数完全匹配的普通函数，则不会再找模板函数，所以输出Func1。

**Q2.** 下列的模板说明中，正确的是()。

A. `template < typename T1, T2 >`

B. `template < class T1, T2 >`

C. `template < typename T1, typename T2 >`

D. `template ( typedef T1, typedef T2 )`

??? general "Answer"
	C。用 typename 和 class 都可以，但是不能缺或者其他的。

**Q3.** 关于类模板，描述错误的是()。

A. 一个普通基类不能派生类模板

B. 类模板可以从普通类派生，也可以从类模板派生

C. 根据建立对象时的实际数据类型，编译器把类模板实例化为模板类

D. 函数的类模板参数需生成模板类并通过构造函数实例化

??? general "Answer"
	A。B 反驳了 A。

	像minisql的B+树中，B+树基本数据页类就是普通基类，而其派生类中间结点页类、叶结点页类都是类模板。
	
	在这里的描述中，类模板指的是原始的带万能类型的模板，模板类是向类模板输入模板参数后实例化得到的类。

**Q4.** 下列有关模板的描述，错误的是\_\_\_\_。

A. 模板把数据类型作为一个设计参数，称为参数化程序设计

B. 使用时，模板参数与函数参数相同，是按位置而不是名称对应的

C. 模板参数表中可以有类型参数和非类型参数

D. 类模板与模板类是同一个概念

??? general "Answer"
	D。类模板 - 模板类 - 对象。

	模板参数表中的类型参数就是class或者typename所指明的万能类型，而非类型参数是直接在模板参数表中规定了类型的模板参数。

	比如模板参数表可以是<class T, int size>。

**Q5.** 模板函数的真正代码是在哪个时期产生的\_\_\_\_。

A. 源程序中声明函数时

B. 源程序中定义函数时

C. 源程序中调用函数时

D. 运行执行函数时

??? general "Answer"
	C。源程序调用函数模板，才会生成对应参数类型的模板函数的代码。

**Q6.** 类模板的使用实际上是将类模板实例化成一个\_\_\_\_。

A. 函数

B. 对象

C. 类

D. 抽象类

??? general "Answer"
	C。模板类本质就是一个类，模板类继续实例化可以得到对象。
	
	抽象类则是根据有无纯虚函数划分的。

**Q7.** 下列选项中，哪一项是类模板实例化的时期\_\_\_。

A. 在编译时期进行

B. 属于动态联编

C. 在运行时进行

D. 在连接时进行

??? general "Answer"
	A。类模板实例化为模板类是要产生相应的代码的，只能在编译阶段进行。

	动态联编就是动态绑定，与多态有关，与类模板实例化无关。

**Q8.** 下列关于 `pair<>` 类模板的描述中，错误的是。

A. `pair<>` 类模板定义头文件 `utility` 中

B. `pair<>` 类模板作用是将两个数据组成一个数据，两个数据可以是同一个类型也可以是不同的类型

C. 创建 `pair<>` 对象只能调用其构造函数

D. `pair<>` 类模拟提供了两个成员函数 `first` 与 `second` 来访问这的两个数据

??? general "Answer"
	C。创建 `pair<>` 对象还可以使用 `make_pair` 方法。

## Week13

**Q1.** If you are not interested in the contents of an exception object, the catch block parameter may be omitted. (T/F)

??? general "Answer"
	T。这里的意思应该是 catch(int) 这种。

	因为 catch() 是不允许的，catch(...) 又不太符合这里的意思。
	
	catch(int) 能够检测到抛出的int，但是又可以说没有参数。

**Q2.** 异常处理的 `catch{ }` 语句块必须紧跟 `try{ }` 语句块之后，这两个语句之间不能插入另外语句。(T/F)

??? general "Answer"
	T。

**Q3.** What is wrong in the following code?

```cpp
  vector<int> v;
  v[0] = 2.5;
```

A. The program has a compile error because there are no elements in the vector.

B. The program has a compile error because you cannot assign a double value to `v[0]`.

C. The program has a runtime error because there are no elements in the vector.

D. The program has a runtime error because you cannot assign a double value to `v[0]`.

??? general "Answer"
	C。程序出错的原因在于 v 是空的，但是却要强行对其中第一个元素赋值，导致 runtime error。
	
	2.5 原本数据类型为 double，但是可以自动类型转换为 int，如果有空间的话，v[0] 将会被赋值为 2，B、D 错误。
	
	编译阶段无法发现“给 vetcor 中不存在的元素赋值”的这种错误，因此不是 compile error，A 错误。

**Q4.** The function `what()` is defined in \_\_.

A. `exception`

B. `runtime_error`

C. `overflow_error`

D. `bad_exception`

??? general "Answer"
	A。what() 用来查 error 信息的，当然是在 exception 中了。

**Q5.** Which of the following statements are true?

A. A custom exception class is just like a regular class.

B. A custom exception class must always be derived from `class exception`.

C. A custom exception class must always be derived from a derived class of `class exception`.

D. A custom exception class must always be derived from `class runtime_error`.

??? general "Answer"
	A。可以将任何东西抛出为异常，那么自定义异常类当然就像一个普通类了。

**Q6.** Suppose `Exception2` is derived from `Exception1`. Analyze the following code.

```cpp
try {

statement1;

statement2;

statement3;
}

catch (Exception1 ex1)
{
}

catch (Exception2 ex2)
{
}
```

A. If an exception of the `Exeception2` type occurs, this exception is caught by the first catch block.

B. If an exception of the `Exeception2` type occurs, this exception is caught by the second catch block.

C. The program has a compile error because these two catch blocks are in wrong order.

D. The program has a runtime error because these two catch blocks are in wrong order.

??? general "Answer"
	A。糟糕的代码。

	catch 的顺序中，由于 is-A 关系，基类在前就会导致直接被基类给 catch 了。
	
	不过编译还是会通过的，不过应该会给warning。

**Q7.** Suppose that statement2 throws an exception of type Exception2 in the following statement:

```cpp
try {

statement1;

statement2;

statement3;
}

catch (Exception1 ex1)
{
}

catch (Exception2 ex2)
{
}

catch (Exception3 ex3)
{
statement4;
throw;
}

statement5;
```

A. statement2

B. statement3

C. statement4

D. statement5

??? general "Answer"
	D。猜想问题是：（原题没给问题）statement2 执行完后，下一条被执行的语句是什么？
	
	Exception2 在 statement2 被抛出，语句块后面的 statement3 被抛弃不再执行，而 Exception2 很快被 catch，但是什么都没有做。
	
	出了 try-catch，执行 statement5，也就是 statement2 下一条语句。

**Q8.** Suppose that statement2 throws an exception of type Exception2 in the following statement:

```cpp
try {

statement1;

statement2;

statement3;
}

catch (Exception1 ex1)
{
}

catch (Exception2 ex2)
{
}

catch (Exception3 ex3)
{
statement4;
throw;
}

statement5;
```

A. statement2

B. statement3

C. statement4

D. statement5

??? general "Answer"
	C。与上一题有所不同的是，Exception3 的 catch 块中是有语句的，因此会继续执行 statement4。
	
	这里有趣的是 throw;
	
	即重抛异常，一般表示这里无法处理该异常，需要将其抛至更上层进行处理。

**Q9.** 下列关于异常的描述中，错误的是（）。

A. 编译错属于异常，可以抛出

B. 运行错属于异常

C. 硬件故障也可当异常抛出

D. 只要是编程者认为是异常的都可当异常抛出

??? general "Answer"
	A。编译阶段是无法抛出异常的，所以编译错误不可以当作异常抛出。

**Q10.** 下列关于重抛异常的描述中，错误的是。()

A. 处理不了的异常，可以通过在 `catch` 结构中调用 `throw` 重新抛出异常，将当前异常传递到外部的 `try-catch` 结构中

B. 重抛异常时只能从 `catch` 语句块或从 `catch` 块中的调用函数中完成

C. 重抛的异常可以被同一个 `catch` 语句捕捉

D. 可以单独使用 `throw` 关键字完成异常重抛

??? general "Answer"
	C。抛到更外层了，只能被更外层的 catch 捕捉。

**Q11.** 下列关于断言的描述中，错误的是。()

A. 断言是调试程序的一种手段

B. 若断言情况发生，一般会终止程序

C. 在 C++ 中，宏 `assert()` 用来在调试阶段实现断言

D. 断言在程序调试与发布版本中都可以使用断言

??? general "Answer"
	D。仅在调试 (debug) 版本中存在断言，发布 (release) 版本中的断言会被去掉。

**Q12.** C++处理异常的机制是由（）3部分组成。

A. 编辑、编译和运行

B. 检查、抛出和捕获

C. 编辑、编译和捕获

D. 检查、抛出和运行

??? general "Answer"
	B。
