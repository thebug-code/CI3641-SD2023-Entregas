/// Calcula la transpuesta de la matriz cuadrada [A]
List<List<int>> transpuesta(List<List<int>> A) {
  for (var i = 0; i < A.length; i++) {
    for (var j = 0; j < A[0].length; j++) {
      A[i][j] = A[j][i];
    }
  }
  return A;
}

/// Multiplica las matrices [A] y [B]
List<List<int>> multiplicar(List<List<int>> A, List<List<int>> B) {
  var C = List.generate(A.length,
    (i) => List.filled(B[0].length, 0), growable: false);
 
  // Por cada fila de A
  for (var i = 0; i < A.length; i++) {
    // Por cada columna de B
    for (var j = 0; j < B[0].length; j++) {
      // Por cada fila de B
      for (var k = 0; k < B.length; k++) {
        C[i][j] += A[i][k] * B[k][j];
      }
    }
  }
  return C;
}


void main() {
  var a = [[2, 0, 1], [3, 0, 0], [5, 1, 1]];
  var aT = transpuesta(a);
  print(multiplicar(a, aT)); // [[38, 11, 18], [11, 10, 16], [18, 16, 27]]
}