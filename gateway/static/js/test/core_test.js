describe("core game logic", function() {
    var object = {};

    beforeEach(function() {
        object.x = 0;
        object.y = 0;
    });

    it("will move object left when left key is pressed", function() {
        move(object, 37);
        expect(object.x).toBe(-5);
        expect(object.y).toBe(0);
    });

    it("will move object up when up key is pressed", function() {
        move(object, 38);
        expect(object.x).toBe(0);
        expect(object.y).toBe(-5);
    });

    it("will move object right when right key is pressed", function() {
        move(object, 39);
        expect(object.x).toBe(5);
        expect(object.y).toBe(0);
    });

    it("will move object down when down key is pressed", function() {
        move(object, 40);
        expect(object.x).toBe(0);
        expect(object.y).toBe(5);
    });

    it("will reset object to initial position", function() {
        reset(object);
        expect(object.x).toBe(100);
        expect(object.y).toBe(100);
    });
});
