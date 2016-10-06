var matrix = [
  ['z','b','c','d'], 
  ['t','b','c','d'], 
  ['a','b','c','d'], 
  ['y','b','c','d']
];
var testWord = 'ztb';
var boggle = function(matrix, targetWord){
  lib = {};
  var traverse = function(xCoor, yCoor, word){
    console.log(lib);
    if (lib[xCoor + '_' + yCoor]){
      return false;
    } else if (word === targetWord){
      return true;
    } else if (word.length > targetWord.length){
      return false;
    } else if (xCoor < 0 || yCoor < 0 || xCoor >= matrix[0].length || yCoor >= matrix.length){
      return false;
    }
    lib[xCoor + '_' + yCoor] = true;
    var north = traverse(xCoor, yCoor-1, word + matrix[yCoor][xCoor]);
    var east = traverse(xCoor+1, yCoor, word + matrix[yCoor][xCoor]);
    var south = traverse(xCoor, yCoor+1, word + matrix[yCoor][xCoor]);
    var west = traverse(xCoor-1, yCoor, word + matrix[yCoor][xCoor]);
    var northeast = traverse(xCoor+1, yCoor-1, word + matrix[yCoor][xCoor]);
    var northwest = traverse(xCoor-1, yCoor-1, word + matrix[yCoor][xCoor]);
    var southeast = traverse(xCoor+1, yCoor+1, word + matrix[yCoor][xCoor]);
    var southwest = traverse(xCoor-1, yCoor+1, word + matrix[yCoor][xCoor]);
    delete lib[xCoor + '_' + yCoor];
    return north || east || south || west || northeast || northwest || southeast || southwest;
  };
  for (y = 0; y < matrix.length; y++){
    for (x = 0; x < matrix[0].length; x++){
      if (traverse(x, y, '')){
        return true;
      }
    }
  }
  return false;
};
console.log(boggle(matrix, testWord));