# 在大于 5 行的函数里，或者全局代码中，不要使用单字命名的变量。

## 错误案例
```js
var l = data.length;
b = l + a; 
```

## 正确案例
```js
data.map(d => d.length);
```