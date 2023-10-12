/// Calcula la rotacion de [k] posiciones de la cadena [w]
String rotar(String w, int k) {
  if (k == 0 || w.isEmpty) {
    return w;
  }
  
  return rotar(w.substring(1) + w[0], k - 1);
}

void main() {
  print(rotar("hola", 0)); // hola
  print(rotar("hola", 1)); // olah
  print(rotar("hola", 2)); // laho 
  print(rotar("hola", 3)); // ahol
  print(rotar("hola", 4)); // hola
  print(rotar("hola", 5)); // olah
}