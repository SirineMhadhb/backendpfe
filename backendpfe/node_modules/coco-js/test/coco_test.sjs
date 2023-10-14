var expect = require('chai').expect;

describe('coco-js', function(){
  it('properly aliases the prototype with dot notation', function(){
    expect(Array::slice.call("string")).to.eql([
      's',
      't',
      'r',
      'i',
      'n',
      'g'
    ]);
  });

  it('properly aliases the prototype with bracket notation', function(){
    var prop = 'slice';
    expect(Array::[prop].call("string")).to.eql([
      's',
      't',
      'r',
      'i',
      'n',
      'g'
    ]);
  });

  it('works on any lhs value', function(){
    var isString = function (obj) {
      return Object::toString.call(obj) === '[object String]'
    }

    expect(isString("string")).to.be.true
    expect(isString([])).to.be.false
  });
});
