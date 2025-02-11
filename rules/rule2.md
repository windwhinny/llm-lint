# 应该有且只有方法和函数应以动词开头

## 规则说明
函数的命名需要体现内部工作，应该以不包含时态的动词开头。
值变量以动词命名，则会容易让人误解为是一个匿名函数。

以下函数的命名可以不遵守此规则：
- 回调函数
- 生命周期函数
- 框架级别函数
- getter/setter 

## 错误案例
```js
// 以名词开头，看不明白什么有什么功能
function option() {}

// 时态不对
function updatedTime() {}
```

## 正确案例
```js
function selectOption() {}
function updateTime() {}

class App {
    // 因为是 getter 函数，不需要遵守此规则
    get name() { }
    // 因为是生命周期函数，所以不需要遵守此规则
    componentDidMount() {}
    // 因为是点击事件回调函数，不需要遵守此规则
    onModalClick() { }
}
```