# coco-js

coco-js adds the CoffeeScript prototype alias operator `::` to JavaScript.

`npm install coco-js`

# Examples

```javascript
Array::slice.call("string")

/*
[
  's',
  't',
  'r',
  'i',
  'n',
  'g'
]
*/


var prop = 'slice';
Array::[prop].call("string")

/*
[
  's',
  't',
  'r',
  'i',
  'n',
  'g'
]
*/

var isString = function (obj) {
  return Object::toString.call(obj) === '[object String]'
}

isString('string') // true
isString([]) // false
```

## Tests

`make test`

## License

[MIT](https://github.com/benjreinhart/coco-js/blob/master/LICENSE.txt)
