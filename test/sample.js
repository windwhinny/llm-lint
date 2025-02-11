let a = 1;
[].map(b => a+b);
let doList = [];
class Circle{
    onMounted(){}
    makedName(b) {
        return <span>{b}</span>;
    }
    renderList() {
        var a = this.data;
        var l = a.map(b => {
            return this.makedName(b);
        });
        l = l.filter(Boolean);
        return l;
    }
    render() {
        return <div>this.renderList()</div>;
    }
}
var rect = new Circle();