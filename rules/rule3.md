# 实例名称要和类名相关

## 规则说明
类作为实例的所属，其名称表达的含义要一脉相承

## 错误案例
```js
class Person() {}
var dog = new Person(); // dog 不应该是Person的实例
```

## 正确案例
```js
class Person() {}
var jack = new Person();
```
