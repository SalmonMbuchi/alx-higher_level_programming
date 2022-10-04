class Rectangle {
    constructor (w, h) {
        if (w <= 0 || h <= 0 || !w || !h) {
            const obj = {};
            return obj;
        }
        this.width = w;
        this.height = h;
    }
}
module.exports = Rectangle;