package com.programsimulator

import org.jgrapht.graph.*;
import org.jgrapht.alg.connectivity.*;

class ProgramSimulator() {
    val programs = mutableListOf<String>()
    val translator = mutableListOf<Triple<String, String, String>>()
    val languages = mutableListOf<String>()
    val graph = DirectedPseudograph<String, DefaultEdge>(DefaultEdge::class.java)

    init {
        // Agrega el lenguaje LOCAL al grafo
        graph.addVertex("LOCAL")
    }

    fun run() {
        while (true) {
            print(">$ ")
            val command = readLine()!!.uppercase()
            val params = command.split(" ")
            
            when (params[0]) {
                "DEFINIR" -> {
                    if (params.size != 4 && params.size != 5) {
                        println("Error: número de parámetros incorrecto")
                        continue
                    }
                    define(params.subList(1, params.size))
                }
                "EJECUTABLE" -> {
                    if (params.size != 2) {
                        println("Error: número de parámetros incorrecto")
                        continue
                    }
                    execute(params.subList(1, params.size))
                }
                "SALIR" -> {
                    break
                }
                else -> {
                    println("Error: opción no válida")
                }
            }
        }
    }

    fun translator(base_language: String, source_language: String, target_language: String) {
        val inspec = ConnectivityInspector(graph)
        
        // Agrega los lenguajes al grafo (los duplicados no se agregan)
        graph.addVertex(base_language)
        graph.addVertex(source_language)
        graph.addVertex(target_language)

        // Si hay un camino entre el lenguaje base y LOCAL, agrega el arco de lenguaje
        // origen al lenguaje destino
        if (inspec.pathExists(base_language, "LOCAL")) {
            graph.addEdge(source_language, target_language)
            // Actualiza la lista de traductores
            update_translator_list()
        } else {
            // Agrega el traductor a la lista de traductores
            translator.add(Triple(base_language, source_language, target_language))
        }
        println("Se definió un traductor de '$source_language' hacia '$target_language', escrito en '$base_language'")
    }
    
    fun interpreter(base_language: String, language: String) {
        // Agregar los lenguajes al grafo (los duplicados no se agregan)
        graph.addVertex(base_language)
        graph.addVertex(language)

        // Agrega el arco de lenguaje a lenguaje base
        graph.addEdge(language, base_language)
        // Actualiza la lista de traductores
        update_translator_list()
        
        println("Se definió un intérprete para '$language', escrito en '$base_language'")
    }

    fun update_translator_list() {
        val inspec = ConnectivityInspector(graph)

        for (t in translator.size - 1 downTo 0) {
            // Verifica si hay un camino entre el lenguaje base y LOCAL
            if (inspec.pathExists(translator[t].first, "LOCAL")) {
                // Agrega el arco de lenguaje origen a lenguaje destino
                graph.addEdge(translator[t].second, translator[t].third)

                // Elimina el traductor de la lista de traductores
                translator.removeAt(t)
                update_translator_list()
                
            }
        }
    }

    fun define(listParam: List<String>) {
        val option = listParam[0].uppercase()

        when (option) {
            "PROGRAMA" -> {
                if (check_program_param(listParam.subList(1, listParam.size))) {
                    // Agrega el nombre del programa a la lista de programas
                    programs.add(listParam[1])
                    // Agrega el lenguaje del programa al grafo
                    graph.addVertex(listParam[2])
                    // Agrega el lenguaje del programa a la lista de lenguajes
                    languages.add(listParam[2])
                    
                    println("Se definió el programa '${listParam[1]}', ejecutable en '${listParam[2]}'")
                }
            }
            "TRADUCTOR" -> {
                if (check_translator_param(listParam.subList(1, listParam.size))) {
                    translator(listParam[1], listParam[2], listParam[3])
                }
            }
            "INTERPRETE" -> {
                if (check_interpreter_param(listParam)) {
                    interpreter(listParam[1], listParam[2])
                }
            }
            else -> {
                println("Error: opción no válida")
            }
        }
    }

    fun execute(param: List<String>) {

        if (param[0] !in programs) {
            println("Error: el programa '${param[0]}' no está definido")
            return
        }

        val language = languages[programs.indexOf(param[0])]
        val inspec = ConnectivityInspector(graph)
    
        // If hay un camino entre el lenguaje base y LOCAL, el programa es ejecutable
        if (inspec.pathExists(language, "LOCAL")) {
            println("Si, es posible ejecutar el programa '${param[0]}'")
        } else {
            println("No es posible ejecutar el programa '${param[0]}'")
        }
    }

    fun check_program_param(params: List<String>): Boolean {
        if (params.size != 2) {
            println("Error: número de parámetros incorrecto")
            return false
        }
        if (params[0] in programs) {
            println("Error: el programa '${params[0]}' ya está definido")
            return false
        }
        if (!isLettersOrDigits(params[1])) {
            println("Error: el nombre del lenguaje '${params[1]}' no es alfanumérico")
            return false
        }
        
        return true
    }

    fun check_translator_param(params: List<String>): Boolean {
        if (params.size != 3) {
            println("Error: número de parámetros incorrecto")
            return false
        }
        if (!isLettersOrDigits(params[0])) {
            println("Error: el nombre del lenguaje base '${params[0]}' no es alfanumérico")
            return false
        }
        if (!isLettersOrDigits(params[1])) {
            println("Error: el nombre del lenguaje origen '${params[1]}' no es alfanumérico")
            return false
        }
        if (!isLettersOrDigits(params[2])) {
            println("Error: el nombre del lenguaje destino '${params[2]}' no es alfanumérico")
            return false
        }

        return true
    }

    fun check_interpreter_param(params: List<String>): Boolean {
        if (params.size != 3) {
            println("Error: número de parámetros incorrecto")
            return false
        }
        if (!isLettersOrDigits(params[1])) {
            println("Error: el nombre del lenguahe base '${params[1]}' no es alfanumérico")
            return false
        }
        if (!isLettersOrDigits(params[2])) {
            println("Error: el nombre del lenguaje '${params[2]}' no es alfanumérico")
            return false
        }

        return true
    }

    
    fun isLettersOrDigits(chars: String): Boolean {
        for (c in chars) {
            if (c !in 'A'..'Z' && c !in 'a'..'z' && c !in '0'..'9') {
                return false
            }
        }
        return true
    }
}

fun main() {
    val p = ProgramSimulator()
    p.run()
}
