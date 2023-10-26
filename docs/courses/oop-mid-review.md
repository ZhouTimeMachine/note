# OOP Midterm Review

!!! info "PTA homework of ZJU *Object Oriented Programming*, 2022 Spring & Summer."

## Week1

**Q1.** （ ）不是面向对象程序设计的主要特征。

A. 封装

B. 继承

C. 多态

D. 结构

??? general "Answer"
	D。OOP 的主要特征为封装 (encapsulation)、继承 (inheritance)、多态 (polymorphism)

!!! info "第 1 课重要概念"

	回顾第 1 课讲述的几个重要概念：

	- **聚合 (cohesion)**，与**组合 (coupling)**类似，都相当于 Has-A 关系。两者的差异在于，设类 B has 类 A 的某个对象，那么如果是组合关系，B 消亡时 A 也会消亡；如果是聚合关系，B 消亡时 A 依然存在。一般地，组合是直接以另一个类的**对象**为成员，聚合是以另一个类的对象的**指针**为成员。
	- **继承 (inheritance)** 则是经典的 Is-A 关系。
	- **迭代器 (iterator)**：顾名思义，用来迭代
	- **重载 (override)**：**函数重载**，即同名函数，用不同参数区分，可以有不同类型的返回值，但是参数相同时不能仅靠返回值区分。另外还有**运算符重载**，相当于定义类的运算，方便一些吧。
	- **模板 (template)**：把不同的类型都能装进去。
	- **interface**，即**接口**或**端口**：我认为指的就是 `virtual` ，在顶层基类定义虚端口，在派生的子类中重定义实现**多态 (polymorphism)**。

**Q2.** `*ptr = new B(5); delete ptr;`

假设上述语句中，`new` 申请的内存空间首地址为 `Addr`, 存放`ptr` 指针变量值的内存空间首地址为 `PAddr`，则执行 `delete ptr` 语句后，`Addr`、`PAddr` 指向的内存区域均会被系统收回。(T/F)

??? general "Answer"
	F。只会收回 PAddr 的空间。
	
	delete 并不会递归释放空间，它的作用是非常直接的。

**Q3.** 用 `new` 关键字动态申请一个三维数组，则下列语句正确的是（）

A. `float *fp; fp = new float[10][25][10];`

B. `float (* fp)[25][10]; fp = new float[10][25][10];`

C. `float (* fp)[10]; fp = new float[10][25][10];`

D. `float *fp [25][10]; fp = new float[10][25][10];`

??? general "Answer"
	B。事实上涉及了C的知识。
	
  	A 定义的 p 是一个 float 指针，可以看作一维数组的隐式转化。
	
	B 定义的 fp 恰是三维数组对应的类型，
	
	对应 D 定义的 fp 是二维指针数组的类型。
	
	C 定义的是二维数组。

## Week2

**Q1.** `this` 指针是对象的非静态成员函数的隐含参数，其指向对象自己。(T/F)

??? general "Answer"
 	T。对象的静态成员函数是没有 this 指针的，不能通过对象调用，需要直接通过类调用。

**Q2.** Resolver `::` is used to:

A. Define a member function outside class declaration

B. Access a member of a namespace

C. Access a static member of a class

D. All of the others

??? general "Answer"
	D。ABC 都是 Resolver 的用途：
	
    1. 在类声明外部定义成员函数
	2. 获取 namespace 的成员
	3. 获取类的静态成员（变量或函数）
	
	总地来说就是表明从属关系吧。

**Q3.** 在面向对象的程序设计中，首先需要在问题域中识别出若干个（ ）

A. 函数

B. 类

C. 文件

D. 过程

??? general "Answer"
	B。OOP 思想。

## Week3

**Q1.** 给定以下类声明，哪个成员函数可能改变成员变量 `data`?

```cpp
class A {
public:
	void f1 (int d);
	void f2 (const int &d);
	void f3 (int d) const;
private:
	int data;
};
```

A. `f1`

B. `f2`

C. `f3`

D. `f1` 和 `f2`

??? general "Answer"
	D。
	
	f3 是 const 成员函数，不能修改类内的成员。
	
	f2 参数里的 const 表示的是参数d是常引用，不能通过d修改外面对应绑定的变量值，但是这并不影响f2修改类内成员data的权限。

## Week4

**Q1.** 设有如下代码段:

```cpp
std::map<char *, int> m;
const int MAX_SIZE = 100;
int main() {
    char str[MAX_SIZE];
    for (int i = 0; i < 10; i++) {
        std::cin >> str;
        m[str] = i;
    }
    std::cout << m.size() << std::endl;
}
```

读入10个字符串，则输出的 m.size() 为

A. 0

B. 1

C. 10

??? general "Answer"
	B。
	
	注意到，尽管读了 10 个字符串，但都只是读进固定的 str。
	
	实际上前一次读入的信息都被后一次读入给覆盖了。每次的 `m[str]=i`，str 都是相同的 `char*`，相当于只是修改这个映射项的值，而没有增加新的映射项。
	
	所以 map 当中始终只有 1 个项，这个项的 `char*` 代表的字符串是最后一次输入的字符串，映射到的 value 为 9。

**Q2.** 下列关于STL的描述中，**错误**的是。

A. STL的内容从广义上讲分为容器、迭代器、算法三个主要部分

B. STL的一个基本理念就是将数据和操作分离

C. STL中的所有组件都由模板构成，其元素可以是任意类型

D. STL的容器、迭代器、算法是三个完全独立的部分，彼此也无任何联系

??? general "Answer"
	D。没有难度的一道题，单纯用于复习 STL 相关理论。

**Q3.** 下列创建 `vector` 容器对象的方法中，**错误**的是。

A. `vector<int> v(10);`

B. `vector<int> v(10, 1);`

C. `vector<int> v{10, 1};`

D. `vector<int> v = (10, 1);`

??? general "Answer"
	D。
	
	A 指创建含有 10 个 int 元素的 vector，可能会把每个 int 默认初始化为 0。
	
	B 指创建含有 10 个 int 元素的 vector，每个 int 都初始化为 1。
	
	C 则类似C语言的 int v[] = {10, 1} 的集合初始化。
	
	D 是不行的，顺道一提，v = 10 也是不行的，但是 v = {10, 1} 就和 C 是等价的。
	
	（据 floatshadow 说，v{10, 1} 在 98 标准下是不行的，或许选项 C 应该改成 v = {10, 1} 更好）

**Q4.** 下列选项中，哪一项不是迭代器。

A. 输入迭代器

B. 前向迭代器

C. 双向迭代器

D. 删除迭代器

??? general "Answer"
	D。其他三个都是有的。

!!! info "迭代器"

	回顾迭代器 (iterator)，类似于指针，有非 const (容器::iterator)和 const (容器::const_iterator)两种，const 只读，非const可以修改对应元素。迭代器一般用 `begin()` 和 `end()` 来迭代控制（ `vector` 重载了 `[]`，所以可以像数组一样迭代），都重载了 `++` 运算。

	一般的迭代器是正向的，有的容器还会提供反向迭代器 reverse_iterator，那就需要用 `rbegin()` 和 `rend()` 来迭代控制。

	迭代器可以分为以下五种：

	1. 输入迭代器：只读，只支持自增
	2. 输出迭代器：只写，只支持自增
	3. 前向迭代器：读写，只支持自增
	4. 双向迭代器：读写，可自增可自减
	5. 随机访问迭代器：读写，可以乱搞

	以**双向迭代器**为例介绍操作：

	1. 自增：重载了 `++`，可以进行 `p++`，`++p` 操作
	2. 自减：重载了 `--`，可以进行 `p--`，`--p`操作
	3. 比较是否相等：`p == p1`，`p != p1`（没有重载 `<`，`>` 之类）
	4. 读写：`*p`，写则 `*p=value`

	在**随机访问迭代器**中，不仅双向迭代器的所有操作都可以进行，而且还可以进行 `p += i` (`p = p + i`)，`p -= i`  (`p = p - i`)，`p[i]`，大于小于操作，以及指针相减也具有了意义（两个指针之间的元素数量）。

	给出常用容器上的迭代器类型：

	| 容器           | 容器上的迭代器类别 |
	| :------------- | ------------------ |
	| vector         | 随机访问           |
	| deque          | 随机访问           |
	| list           | 双向               |
	| set/multiset   | 双向               |
	| map/multimap   | 双向               |
	| stack/queue    | 不支持迭代器       |
	| priority_queue | 不支持迭代器       |

## Week5

**Q1.** 主程序调用内联函数（ `inline` ）时，不发生控制转移，无需保存和恢复环境变量等，因此，节省了系统开销。内联函数的声明以及最终的生效，是由程序员决定的。(T/F)

??? general "Answer"
	F。内联函数的生效是由编译器执行的。

**Q2.** 两个以上的函数，具有相同的函数名，且形参的个数或形参的类型不同，或返回的数据类型不同，则称之为函数的重载。(T/F)

??? general "Answer"
	F。不能仅根据返回值类型区分重载的函数。

**Q3.** 以下选项中，是正确的函数默认形参设置的是。

A. `int fun(int a,int b,int c);`

B. `int fun(int a,int b,int c=1);`

C. `int fun(int a,int b=1,int c);`

D. `int fun(int a=1,int b,int c);`

??? general "Answer"
	B。记录怪题一道，大概是因为 A 没有进行默认形参设置所以是错的吧……

## Week6

**Q1.** Order of initialization in the initial list is the order of their declaration in the list.(T/F)

??? general "Answer"
	F。应当是相关成员声明的顺序。

**Q2.** 类的组合关系可以用“Has-A”描述；类间的继承与派生关系可以用“Is-A”描述。(T/F)

??? general "Answer"
	T。当时第一次接触这种说法，在此记录。

**Q3.** 对于类之间的友元关系：

A. 如果类A是类B的友元，则B的成员函数可以访问A的私有成员

B. 如果类A是类B的友元，则B也是A的友元。

C. 如果类A是类B的友元，并且类B是类C的友元，则类A也是类C的友元。

D. 以上答案都不对。

??? general "Answer"
	D。

	A，写反了。
	
	B，如果只定义了单向的友元关系，那么不会是相互的。
	
	（我认为你是我的朋友，你却不认为，唉真是令人悲伤）
	
	C，友元关系不能继承、不能传递
	
	（朋友的子女不一定是朋友，朋友的朋友不一定是朋友）

!!! info "友元相关题外话"
	1. 友元关系不能继承包含两重意思：A 将 B 设为友元，C 是 A 的派生类，D 是 B 的派生类，则 B 不是 C  的友元，D 也不是 A 的友元。（长辈之间的单向朋友关系，子女均不可继承）

	2. 但是友元类的派生类，依然可以通过其基类接口去访问设置其基类为友元类的类的私有成员。（朋友的子女以子女的名义不一定是朋友，但是如果朋友的子女拿着它老爹的信物那也只能当朋友对待）

	3. 但是注意，如果派生类重载了基类的某个虚函数，那么这个被重载的虚函数在派生类中也无法访问设置其基类为友元类的私有成员。即使使用多态，这种重载也无法在编译时通过。（朋友的子女只有拿着它老爹的信物才会被当朋友对待，要是它改造了信物还是不认的）

**Q4.** 友元的作用是

A. 提高程序的运用效率

B. 加强类的封装性

C. 实现数据的隐藏性

D. 增加成员函数的种类

??? general "Answer"
	A。打破封装，走向 C-like。

**Q5.** 一个类的友元类中的成员函数都是这个类的友元函数 (T/F)

??? general "Answer"
    T。

**Q6.** Suppose a class is defined without any keywords such as public, private and protected, all members default to

A. public

B. protected

C. private

D. static

??? general "Answer"
	C。class 默认为 private，struct 默认为 public。

**Q7.** Who can access a private member of a class?

A. Only member functions of that class.

B. Only member functions of that class and friend functions or member functions of friend classes

C. Only member functions of that class and derived classes

D. None of the others

??? general "Answer"
	B。

**Q8.** 静态成员函数没有：

A. 返回值

B. this指针

C. 指针参数

D. 返回类型

??? general "Answer"
	B。静态成员函数不特别操作操作某个实例化的类对象，只能对静态成员变量进行操作，不需要有 this 指针。
	
	（生存域与全局函数相同，只是作用域被限制在类内）

**Q9.** For the code below:

```cpp
class A {
  static int i;
  //...
};
```
Which statement is **NOT** true?

A. All objects of `class A` reserve a space for `i`

B. All objects of `class A` share the space of `i`

C. `i` is a member variable of `class A`

D. `i` is allocated in global data space

??? general "Answer"
	A。静态成员变量由类的所有对象共享。本质上是全局变量（包括存储空间），只是被封装在类内。

## Week7

**Q1.** In C++, inheritance allows a derived class to directly access all of the functions and data of its base class. (T/F)

??? general "Answer"
	F。派生类只能直接访问基类的公共 (public) 和保护 (protected) 对象，私有 (private) 对象是无法直接访问的。

!!! info "对比 public, protected 和 private 三种继承方式"
	| 继承方式      | 基类public | 基类protected | 基类private |
	| :------------ | ---------- | ------------- | ----------- |
	| public继承    | public     | protected     | 不可访问    |
	| protected继承 | protected  | protected     | 不可访问    |
	| private继承   | private    | private       | 不可访问    |

**Q2.** One class can have more than one super classes.(T/F)

??? general "Answer"
	T。这题的意图应该在于，C++是有多重继承的。

**Q3.** 给出//1, //2, //3, //4, //5处产生的输出。

```cpp
#include <iostream>
#include <string>
using namespace std ;

class Testing
{
private:
    string words; 
    int number ;
public:
    Testing(const string & s = "Testing")
    {
        words = s ;
        number = words.length();
        if (words.compare("Testing")==0)
            cout << 1;
        else if (words.compare("Heap1")==0)
            cout << 2;
        else
            cout << 3;
    }
    ~Testing()
    {
        cout << 0;
    }
    void show() const
    {
        cout << number;
    }
};
int main()
{
    Testing *pc1 , *pc2;
    pc1 = new Testing ;          //1
    pc2 = new Testing("Heap1");  //2
    pc1->show();   //3
    delete pc1 ;   //4
    delete pc2 ;   //5
    return 0;
}
```

??? general "Answer"
	- //1: 1
	- //2: 2
	- //3: 7
	- //4: 0
	- //5: 0
	
	new 调用构造函数并分配空间。
	
	pc1 的构造没有给参数，将调用默认构造函数，这里定义的构造函数虽然有一个参数，但是存在默认参数值，因此与默认构造函数相容，会调用定义的构造函数。（因此编译器并不会再生成一个默认构造函数）
	
	因此构造时的参数为默认的 Testing，则 //1 处输出 1。据此，也就可知 //3 处输出 7。
	
	2 是有参数的构造，参数为 Heap1，构造时会输出 2，即 //2 的输出。
	
	//4，//5 处都是 delete，会调用析构函数并释放内存空间，因此都输出0。

**Q4.** 给出//1, //2, //3, //4处产生的输出。

```cpp
class A{
    int i;
public:
    A(int ii=0):i(ii) { cout << 1; }
    A(const A& a) {
        i = a.i;
        cout << 2;     
    }
    void print() const { cout << 3 << i; }
};

class B : public A {
    int i;
    A a;
public:
    B(int ii = 0) : i(ii) { cout << 4; }
    B(const B& b) {
        i = b.i;
        cout << 5;
    }
    void print() const {
        A::print();
        a.print();
        cout << 6 << i;    
    }
};

int main()
{
    B b(2);        //1
    b.print();    //2
    B c(b);        //3
    c.print();    //4
}
```

??? general "Answer"
	- //1: 114
	- //2: 303062
	- //3: 115
	- //4: 303062
	
	//1 处，调用普通含参构造函数构造 b。
	
	- 在 b 的该构造函数中没有初始化基类 A，因此基类 A 默认构造，i 初始化为 0，输出 1
	- 接着是 b 的成员变量的初始化，先是 b.i 通过初始化列表初始化为 2，然后是 b.A 调用构造函数，因为没有初始化列表指定，因此也是默认构造，b.A.i 初始化为 0，输出 1
	- 最后是 b 的构造函数的剩余部分，输出 4
	
	//2 处，调用 B 类的 print()。
	
	- 首先是基类 A 的 print，输出 3 和基类 A 的 i（之前已经确认它是 0）
	- 然后是 b 的成员 A，也是输出 3 和 0
	- 最后是输出 6 和 b.i，b.i 是 2
	
	//3 处，调用拷贝构造函数构造 c。
	
	- 可以看到，这个拷贝构造是盗版的，实际上只拷贝了 c.i=b.i，c 的基类 A 和 c.A 都是默认构造，不过由于 b 的基类和 b.A 也是这么构造的，导致最终 b 和 c 确实是一样的
	- 不过在这一步的输出并不一样，尽管两个 A 的输出依然都是 1，但是由于调用的 B 类构造函数是拷贝构造，因此最后输出的是5
	
	//4 处，由于 c 最后和 b 是一样的，那么 c.print() 的结果和 b.print() 的结果也就是一样的。

!!! info "const 的对象和成员函数"
	这里有趣的是，非 const 的对象调用了 const 的成员函数。

	这是因为 const 的成员函数实际上是让 this 指针是 const 的，由于一个非 const 的指针是可以传参给一个 const 的指针的，因此可以这么做。

	相反地，const 的指针不能传参给非 const 的指针，因此 const 的对象不能调用非 const 的成员函数。

## Week8

**Q1.** 虚函数是用 `virtual` 关键字说明的成员函数。(T/F)

??? general "Answer"
	T。virtual 只能修饰类的成员函数。

**Q2.** 将构造函数说明为纯虚函数是没有意义的。(T/F)

??? general "Answer"
	T。构造函数不能是虚函数，这个时候 vtable 都还没有建立。
	
	析构函数需要是虚函数。

**Q3.** 抽象类是指一些没有说明对象的类。(T/F)

??? general "Answer"
	F。抽象类是含有纯虚函数的类。

**Q4.** 动态绑定是在运行时选定调用的成员函数的。(T/F)

??? general "Answer"
	T。不同于静态绑定，静态绑定是在编译时就确定了的。

**Q5.** 因为静态成员函数不能是虚函数，所以它们不能实现多态。(T/F)

??? general "Answer"
	T。静态成员函数是没有 this 指针的，而虚函数需要 this 指针找到 vptr，所以静态成员函数不能是虚函数。

**Q6.** 在多继承中，派生类的构造函数需要依次调用其基类的构造函数，调用顺序取决于定义派生类时所指定的各基类的顺序。

??? general "Answer"
    T。

**Q7.** 虚函数具有继承性。(T/F)

??? general "Answer"
	T。指某个类的某个函数被声明为虚函数之后，它的所有直接或间接基类中的同名函数，即使前面不加 virtual 关键字，也会被认为是虚函数。

	(但是 wk 建议还是该加 virtual 的都加 virtual，减少向父类查找是否 virtual 的开销)

**Q8.** 如果一个类的函数全部都是纯虚函数，则这个类不能有自己类的实现（包括引用和指针），只能通过派生类继承实现。(T/F)

??? general "Answer"
	F。含有一个纯虚函数的类就是抽象类了。
	
	抽象类不能有自己类的实现，但是可以有引用和指针。

**Q9.** Given:

```cpp
class A {
    A() {};
    virtual f() {};
    int i;
};
```
which statement is NOT true:

A. i is private

B. f() is an inline function

C. i is a member of class A

D. sizeof(A) == sizeof(int)

??? general "Answer"
	D。
	
	默认private，A正确。
	
	默认inline，B正确。
	
	D，A还要包括vptr的空间，因此不正确。

**Q10.** 以下说法正确的是？

A. 在虚函数中不能使用this指针

B. 在构造函数中调用虚函数，不是动态联编

C. 抽象类的成员函数都是纯虚函数

D. 构造函数和析构函数都不能是虚函数

??? general "Answer"
	B。在构造函数中调用虚函数是静态绑定，不是动态联编（动态绑定）。
	
	A，虚函数的动态绑定需要通过 this 指针找到 vptr，需要使用 this 指针，当然也可以在虚函数中使用。
	
	（反而是没有this指针的静态成员函数不能是虚函数）
	
	C，抽象类只要包含纯虚函数就行，不需要全部都是纯虚函数。
	
	D，构造函数不能是虚函数，析构函数最好是虚函数。